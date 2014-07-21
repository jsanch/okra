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
    return render_template('new_tab.html')

@app.route('/tab')
def tab_view():
    resp = make_response(render_template('tab.html'))
    resp.set_cookie('user_id', 'poo')
    return resp

@app.route('/start')
def start():
    return render_template('index.html')

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

# CREATE TAB
@app.route('/create_tab', methods=['POST', 'GET'])
def create_tab():
    db = get_db_connection("okra") #get conncection
    # tabs = db.tabs #get tabs collection
    tabs = get_db_collection('tabs')
    # invites = db.invites #get invites collection

    if request.method == 'POST':
        #Get JSON
        data = request.get_json(True)

        #Get wanted data
        tab_title = data['title']
        tab_group = data['group'] #array of user ids
        tab_items = data['items']
        tab_subtotal = data['subtotal']
        tab_total = data['total']
        tab_tip = data['tip']
        tab_tax = data['tax']
        tab_paid_users = data['paid_users']
        tab_paid = data['paid']

        # prepare data for db 
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
        #insert to db 
        tab_id = tabs.insert(tab)
        print str(tab_id)
        # create invites from group.
        create_invites(tab_group, tab_id)

        # return msg
        print 'Inserted tab with tab_id: ' + str(tabs.find_one({"_id":tab_id})['_id'])
        return '{ "_id":' + str(tabs.find_one({"_id":tab_id})['_id']) + '}'
    else:
        return 'error'

# UPDATE TAB
@app.route('/update_tab', methods=['POST', 'GET'])
def update_tab():
    '''Updates tab with JSON sent by client '''
    db = get_db_connection("okra") #get conncection
    # tabs = db.tabs #get tabs collection
    tabs = get_db_collection('tabs')
    # invites = db.invites #get invites collection

    if request.method == 'POST':
        #Get JSON
        data = request.get_json(True)

        #Get wanted data
        tab_title = data['title']
        tab_group = data['group'] #array of user ids
        tab_items = data['items']
        tab_subtotal = data['subtotal']
        tab_total = data['total']
        tab_tip = data['tip']
        tab_tax = data['tax']
        tab_paid_users = data['paid_users']
        tab_paid = data['paid']

        # prepare data for db 
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
        #get desired  tab
        tab_id = request.args.get('tab_id', '')
        le_tab = tabs.find_one( { "_id" : ObjectId(tab_id) } )

        return "NOT IMPLEMENTED YET"
    else:
        return "not a post req"



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
    ''' add user to  items in a tab '''
    #get db collection
    tabs = get_db_collection('tabs')
    
    #get args
    tab_id = request.form['tab_id']
    user_id = request.form['user_id']
    item_id = request.form['item_id']

    #get tab 
    le_tab = tabs.find_one( { "_id" : ObjectId(tab_id) } )


    if (le_tab == None):
        return 'Fail'
    else:
        le_tab['items'][str(item_id)]['assigned_to'].append(user_id)
        print le_tab['items'][str(item_id)]['assigned_to']
        tabs.save(le_tab)
        return "True"

# REMOVE USER 
# NEEDS: tab_id, user_id, item_id
@app.route('/remove_user_from_item', methods=['POST'])
def remove_user_to_item():
    ''' remove user of items in a tab '''
    #get db collection
    tabs = get_db_collection('tabs')
    
    #get args
    tab_id = request.form['tab_id']
    user_id = request.form['user_id']
    item_id = request.form['item_id']

    #get tab 
    le_tab = tabs.find_one( { "_id" : ObjectId(tab_id) } )


    if (le_tab == None):
        return 'Fail'
    else:
        le_tab['items'][str(item_id)]['assigned_to'].remove(user_id)
        print le_tab['items'][str(item_id)]['assigned_to']
        tabs.save(le_tab)
        return "True"




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

        return json.dumps({'user_id': user_mongo_id})

#GET USER
@app.route('/get_user')
def get_user():
     # gets a user_id and returns json info of user
    users_collection = get_db_collection('users')
    user_id = request.args.get('user_id')
    user = users_collection.find_one({"_id":user_id})
    return json.dumps(user)

#GET FRIENDS
@app.route('/get_friends')
def get_friends():
     # gets the list of friends with their ids and names for a given user id 
    users_collection = get_db_collection('users')
    user_id = request.args.get('user_id')
    user = users_collection.find_one({'_id':user_id})
    friend_ids = user['friends']
    friends = {}
    for friend_id in friend_ids:
        friends[friend_id] = users_collection.find_one({'_id':friend_id})
    return friends



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

#poll invite
@app.route('/poll_for_invite')
def poll_for_invite():
    '''Returns tab_id if the passed user_id has an invite '''
    #get db collection
    invites = get_db_collection('invites')
    #get param
    req_user_id = request.args.get('user_id', '')
    print "requested user id : " +  req_user_id
    inv = invites.find_one({'user_id':req_user_id})
    print inv
    if ( inv == None ):
        return 'null'
    else:
        return inv['tab_id']

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
    # try:
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
        insert_tabs['title'] = ''
        insert_tabs['total'] = float(parsed_tabs['meta']['total'])
        insert_tabs['subtotal'] = float(parsed_tabs['meta']['subtotal'])
        insert_tabs['tax'] = float(parsed_tabs['meta']['tax'])
        insert_tabs['tip'] = float(0)

        insert_tabs['group'] = {}
        insert_tabs['items'] = {}
        insert_tabs['paid_users'] = []
        insert_tabs['paid'] = False

        index_id = 0
        for parsed_item in parsed_tabs['items']:
            insert_tabs['items'][str(index_id)] = parsed_item
            index_id += 1

        print insert_tabs

        #INSERT TAB
        tab_id = okratabs.insert(insert_tabs)
        print 'SUCCESS'
        print 'SUCCESS'
        print 'SUCCESS'
        print 'SUCCESS'
        print 'SUCCESS'
        print 'SUCCESS'
        print 'SUCCESS'
        return str({'tab_id' : tab_id})
    # except Exception:
    #     return 'fail'




###############################################################################
################################## VENMO  #####################################
###############################################################################

### INIT 
@app.route('/venmo_login')
def venmo_login():
    if session.get('venmo_token'):
        # return 'Your Venmo token is %s' % session.get('venmo_token')
        # venmo_token  = session.get('venmo_token')
        # charge_or_pay('charge',venmo_token,8576009129, 0.01,'')
      return 'Jaime charged'
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
      le_user = tabs.find_one({"id" : user_id})
      if (user_id != ""):
        charge_or_pay('pay', user.token, master.phone, master.amt, user.note)


# def add_venmo_user(phone_number,display_name, token):


###### OAuth

@app.route('/oauth-authorized')
def oauth_authorized():
    db = get_db_connection("okra")   #get conncection
    users = get_db_collection('users')

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

    session['venmo_token'] = access_token
    session['venmo_username'] = user['username']
    session['first_name'] = user['first_name']
    session['last_name'] = user['last_name']
    session['profile_picture_url'] = user['profile_picture_url']

    users.insert( {
                    "first_name" : session['first_name'],
                    "second_name": session['last_name'],
                    "name" : session['first_name'] + ' ' + session['last_name'],
                    "friends" : ["user_id","user_id"],
                    "phone": "",
                    "token": session['venmo_token'],
                    "pic_url": session['profile_picture_url']
                  }
        )
    
    response = make_response(redirect('/'))
    response.set_cookie('user_id',value="session['venmo_username']")
    response.set_cookie('first_name',value="session['first_name']")
    response.set_cookie('last_name',value="session['last_name']")
    response.set_cookie('profile_picture_url',value="session['profile_picture_url']")

    #return  'fuck you %s' % session['venmo_token']
    # return 'You were signed in as %s' % session['venmo_token']
    return response
    

###############################################################################
################################## FLASK  #########################



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
