import os
from flask import Flask, request, redirect, render_template, url_for, jsonify, send_from_directory, session, make_response
from werkzeug.utils import secure_filename
from pymongo import MongoClient
from threading import Thread
import json
from bson import Binary, Code
from bson.json_util import dumps
from bson.objectid import ObjectId
from charge import *
from constants import CONSUMER_ID, CONSUMER_SECRET, APP_SECRET
import requests
import scan.okraparser

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

mongo_encoder = JSONEncoder()

app = Flask(__name__)
app.jinja_env.autoescape = False
app.secret_key = APP_SECRET

###############################################################################
################################   VIEWS      #################################
###############################################################################

#landing page
@app.route('/')
def index():
    return render_template('landing_page/landing_page.html')

@app.route('/new_tab')
def new_tab_view():
    if session.get('user_id'):
        return render_template('new_tab.html')
    else:
        return redirect('/login')

@app.route('/tab')
def tab_view():
    if session.get('user_id'):
        resp = make_response(render_template('tab.html'))
        return resp
    else:
        return redirect('/login')

    resp = make_response(render_template('tab.html'))
    return resp

@app.route('/img-upload')
def img_upload():
    return render_template('img-upload.html')


###############################################################################
################################     DB      ##################################
###############################################################################


def get_db_connection(db):
    client = MongoClient()
    return client[db]

def get_db_collection(collection):
    return get_db_connection('okra')[collection]


###############################################################################
###############################     TAB      ##################################
###############################################################################

@app.route('/make_payment', methods=['POST'])
def make_payment():
    print 'MAKE PAYMENTS'
    user_id = session['user_id']
    tab_id = session['tab_id']
    print 'stage 1'
    tabs = get_db_collection('tabs')
    le_tab = tabs.find_one( { "_id" : ObjectId(tab_id) } )
    le_tab['paid_users'].append(user_id)
    print 'stage 2'

    tip_and_tax = float(le_tab['tax']) + float(le_tab['tip'])

    for item in le_tab['items']:
        if user_id in item['assigned_to']:
            le_tab['paid'] += float(item[price])

    print 'stage 3'
    tabs.save(le_tab)
    return 'success'

# GET TAB
@app.route('/get_tab', methods=['GET'])
def get_tab():
    tabs = get_db_collection('tabs')
    tab_id = request.args.get('tab_id', '')
    le_tab = tabs.find_one( { "_id" : ObjectId(tab_id) } )
    if (le_tab == None):
        return 'Tab not found'
    else: 
        #Get wanted data
        tab_title = le_tab['title']
        tab_group = le_tab['group'] #array of user ids
        tab_items = le_tab['items']
        tab_subtotal = le_tab['subtotal']
        tab_total = le_tab['total']
        tab_tip = le_tab['tip']
        tab_tax = le_tab['tax']
        tab_paid_users = le_tab['paid_users']
        tab_paid = le_tab['paid']

        tab = {
            "title" : tab_title,
            "group" : tab_group,
            "items" : tab_items,
            "subtotal" : tab_subtotal,
            "total" : tab_total,
            "tip" : tab_tip,
            "tax" : tab_tax,
            "paid_users" : tab_paid_users,
            "paid" : tab_paid,    
        }

        return  jsonify(tab)

###############################################################################
################################## ITEMS  #####################################
###############################################################################

# ADD USER TO TAB'S ITEMS
# NEEDS: tab_id, user_id, item_id
@app.route('/add_user_to_item', methods=['POST'])
def add_user_to_item():
    print ''' add user to  items in a tab '''
    #get db collection
    tabs = get_db_collection('tabs')
    
    print 'stage 1'

    #get args
    tab_id = request.form['tab_id']
    # print 'a', tab_id
    print tab_id

    user_id = request.form['user_id']
    print user_id
    # print 'b'
    item_id = request.form['item_id']
    print item_id

    print 'stage 2'

    #get tab 
    le_tab = tabs.find_one( { "_id" : ObjectId(tab_id) } )
    print str(le_tab)

    print 'stage 3'

    if (le_tab == None):
        print 'fail'
        return 'fail'
    else:
        if not 'assigned_to' in le_tab['items'][str(item_id)]:
            le_tab['items'][str(item_id)]['assigned_to'] = []
        if not user_id in le_tab['items'][str(item_id)]['assigned_to']:
            le_tab['items'][str(item_id)]['assigned_to'].append(user_id)
        else:
            return 'already'
        print le_tab['items'][str(item_id)]['assigned_to']
        tabs.save(le_tab)
        print 'add_user_to_item success'
        return "success"

# REMOVE USER 
# NEEDS: tab_id, user_id, item_id
@app.route('/remove_user_from_item', methods=['POST'])
def remove_user_to_item():
    ''' remove user of items in a tab '''
    #get db collection
    tabs = get_db_collection('tabs')
    
    print 'stage 1'
    #get args
    tab_id = request.form['tab_id']
    user_id = request.form['user_id']
    item_id = request.form['item_id']

    print 'stage 2'
    #get tab 
    le_tab = tabs.find_one( { "_id" : ObjectId(tab_id) } )

    print 'stage 3'
    if (le_tab == None):
        return 'fail'
    else:
        if not 'assigned_to' in le_tab['items'][str(item_id)]:
            le_tab['items'][str(item_id)]['assigned_to'] = []
        if user_id in le_tab['items'][str(item_id)]['assigned_to']:
            le_tab['items'][str(item_id)]['assigned_to'].remove(user_id)
        else:
            return 'already'
        print le_tab['items'][str(item_id)]['assigned_to']
        tabs.save(le_tab)
        return "success"


###############################################################################
################################## USERS  #####################################
###############################################################################

@app.route('/add_user' , methods=['POST', 'GET'])
def add_user():
    users = get_db_collection('users')
    if request.method == 'POST':
        user_phone = request.form['phone']
        user_name = request.form['name']
        user_friends = request.form['friends'] #list

        user = {
                'phone' : user_phone,
                'name' : user_name,
                'friends' : user_friends
        }
        user_mongo_id = users.insert(user)

        return JSONEncoder.encode(mongo_encoder, {'user_id': user_mongo_id})

#GET USER
@app.route('/get_user')
def get_user():
     # gets a user_id and returns json info of user
    users_collection = get_db_collection('users')
    user_id = request.args.get('user_id')
    user = users_collection.find_one({"_id":ObjectId(user_id)})
    return JSONEncoder.encode(mongo_encoder, user)

#GET FRIENDS
@app.route('/get_friends')
def get_friends():
     # gets the list of friends with their ids and names for a given user id 
    users_collection = get_db_collection('users')
    print 'stage 1'
    user_id = request.args.get('user_id')
    user = users_collection.find_one({'_id':ObjectId(user_id)})
    print 'stage 2'
    friend_ids = user['friends']
    friends = {}
    print 'stage 3'
    for friend_id in friend_ids:
        friends[friend_id] = users_collection.find_one({'_id':ObjectId(friend_id)})
    print 'stage 4'

    print friends
    return JSONEncoder.encode(mongo_encoder, friends)


###############################################################################
################################ INVITES  #####################################
###############################################################################

def create_invites(group, tab_id): #used by create tab to invite users that are added.
    invites = get_db_collection('invites')
    print group
    # print "Creating invites for " +  str(group)
    for user_id in group:
        print str(user_id) + " " + str(tab_id)
        invite = { 'user_id': user_id, 'tab_id' : tab_id }
        invite_id = invites.insert(invite)

@app.route('/create_invite', methods=['POST'])
def create_invite_route():
    inv_user_id = request.form['user_id']
    create_invites([inv_user_id], session['tab_id'])
    return 'success'

@app.route('/create_invites',  methods=['POST'])
def create_invites_route():
    print "asdkjfhakgjha"
    inv_group = request.values.getlist('group[]')
    print inv_group
    create_invites(inv_group, session['tab_id'])
    return 'success'

#poll invite
@app.route('/poll_for_invite')
def poll_for_invite():
    '''Returns tab_id if the passed user_id has an invite '''
    #get db collection
    invites = get_db_collection('invites')
    #get param
    req_user_id = request.args.get('user_id', '')
    print "requested user id : " +  req_user_id
    invite = invites.find_one({'user_id':req_user_id})
    print invite
    if ( invite == None ):
        return 'null'
    else:
        return invite['tab_id']

###############################################################################
################################## OCR  #####################################
###############################################################################
#
# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'images/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    try:
        # Get the name of the uploaded file
        file = request.files['file']
        # Check if the file is one of the allowed types/extensions
        if file and allowed_file(file.filename):
            # Make the filename safe, remove unsupported chars
            filename = secure_filename(file.filename)
            # Move the file form the temporal folder to
            # the upload folder we setup
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Redirect the user to the uploaded_file route, which
            # will basicaly show on the browser the uploaded file
            
            # OCR PARSING
            parsed_tabs = scan.okraparser.full_scan(filename)
            print parsed_tabs
           
            #  CREATE NEW TAB WITH RECEIPT INFO
            okratabs = get_db_collection("tabs")   #get conncection
            insert_tabs = {}
            insert_tabs['title'] = session['first_name'] + '\'s tab'
            insert_tabs['total'] = float(parsed_tabs['meta']['total'])
            insert_tabs['subtotal'] = float(parsed_tabs['meta']['subtotal'])
            insert_tabs['tax'] = float(parsed_tabs['meta']['tax'])
            insert_tabs['tip'] = float(0)
            if 'user_id' in session:
                insert_tabs['master_user_id'] = session['user_id']
            else:
                insert_tabs['master_user_id'] = None
            insert_tabs['group'] = []
            insert_tabs['items'] = {}
            insert_tabs['paid_users'] = []
            insert_tabs['paid'] = False

            index_id = 0
            for parsed_item in parsed_tabs['items']:
                insert_tabs['items'][str(index_id)] = parsed_item
                insert_tabs['items'][str(index_id)]['assigned_to'] = []
                index_id += 1

            print insert_tabs

            #INSERT TAB
            tab_id = okratabs.insert(insert_tabs)
            print 'SUCCESS'
            session['tab_id'] = str(tab_id)
            return jsonify({'tab_id' : str(tab_id)})
        return 'fail'
    except Exception as e:
        print e
        return 'fail'




###############################################################################
################################## VENMO  #####################################
###############################################################################

@app.route('/venmo_login')
def venmo_login():
    return redirect('/login')

### INIT 
@app.route('/login')
def login():
    if session.get('venmo_token'):
        # return 'Your Venmo token is %s' % session.get('venmo_token')
        # venmo_token  = session.get('venmo_token')
        # charge_or_pay('charge',venmo_token,8576009129, 0.01,'')
      return redirect('/tab')
    else:
      return redirect('https://api.venmo.com/v1/oauth/authorize?client_id=%s&scope=make_payments,access_profile&response_type=code' % CONSUMER_ID)


#### CHARGE
@app.route('/master_charge')
def master_charge(master):
  if session.get('venmo_token'):
    db = get_db_connection("okra") #get conncection
    users = db.users #get tabs collection

    for user in users:
      user_id = request.args.get('user_id', '')
      le_user = tabs.find_one({"_id" : ObjectId(user_id)})
      if (user_id != ""):
        charge_or_pay('pay', user.token, master.phone, master.amt, user.note)


# def add_venmo_user(phone_number,display_name, token):


###### OAuth

@app.route('/oauth-authorized')
def oauth_authorized():
    db = get_db_connection("okra")   #get conncection
    users = get_db_collection('users')

    print 'stage 1'

    AUTHORIZATION_CODE = request.args.get('code')
    data = {
        "client_id":CONSUMER_ID,
        "client_secret":CONSUMER_SECRET,
        "code":AUTHORIZATION_CODE
        }
    url = "https://api.venmo.com/v1/oauth/access_token"
    response = requests.post(url, data)
    response_dict = response.json()
    access_token = response_dict.get('access_token')
    user = response_dict.get('user')

    print 'stage 2'

    session['venmo_token'] = access_token
    session['venmo_username'] = user['username']
    session['first_name'] = user['first_name']
    session['last_name'] = user['last_name']
    session['profile_picture_url'] = user['profile_picture_url']

    print user
    possible_new_user = {
            "first_name" : session['first_name'],
            "second_name": session['last_name'],
            "name" : session['first_name'] + ' ' + session['last_name'],
            "friends" : [],
            "phone": user['phone'],
            "username": user['username'],
            "token": session['venmo_token'],
            "pic_url": session['profile_picture_url']}

    if not users.find({"username": user['username']}):
        users.update({"username": user['username']}, possible_new_user, True)
    # user_id = users.insert( {
    #                 "first_name" : session['first_name'],
    #                 "second_name": session['last_name'],
    #                 "name" : session['first_name'] + ' ' + session['last_name'],
    #                 "friends" : ["user_id","user_id"],
    #                 "phone": session['phone'],
    #                 "token": session['venmo_token'],
    #                 "pic_url": session['profile_picture_url']
    #               }
    #     )

    user = users.find_one({"username": user['username']})
    # print possible_new_user
    # print user_id
    print user
    user_id = user['_id']
    print user_id

    session['user_id'] = str(user_id)
    print 'stage 3'

    response = make_response(redirect('/tab'))
    response.set_cookie('user_id',str(session['user_id']))
    response.set_cookie('first_name',str(session['first_name']))
    response.set_cookie('last_name',str(session['last_name']))
    response.set_cookie('profile_picture_url',session['profile_picture_url'])

    return response
    

###############################################################################
################################## FLASK ######################################
###############################################################################


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
############################################### ################################
################################# DEL
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
################################# DEL
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
################################# DEL