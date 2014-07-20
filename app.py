import os
from flask import Flask, request, redirect, render_template, url_for, jsonify, send_from_directory, session
from werkzeug.utils import secure_filename
from pymongo import MongoClient
from threading import Thread
import json
from bson import Binary, Code
from bson.json_util import dumps
from charge import *
from constants import CONSUMER_ID, CONSUMER_SECRET, APP_SECRET
import requests
import scan.okraparser

app = Flask(__name__, static_url_path = '')

app.secret_key = APP_SECRET

########################## VIEWS #######################################

#landing page
@app.route('/')
def landing():
   return render_template('landing_page/landing_page.html')

@app.route('/new_tab')
def new_tab_view():
    return render_template('new_tab_view/index.html')


################################ DB ####################################


def get_db_connection(db):
    client = MongoClient()
    return client[db]
def get_db_collection(collection):
    return get_db_connection('okra').okra[collection]

########################################################################


#############################   TAB      #########################

# CREATE TAB
@app.route('/create_tab', methods=['POST', 'GET'])
def create_tab():
    db = get_db_connection("okra") #get conncection
    # tabs = db.tabs #get tabs collection
    tabs = get_db_collection('tabs')
    # invites = db.invites #get invites collection

    if request.method == 'POST':
        #MUST VALIDATE
        tab_group = request.form['group']
        tab_items = dumps(request.form['items']) #convert to json

        tab_subtotal = request.form['subtotal']
        tab_total = request.form['total']
        tab_tip = request.form['tip']
        tab_tax = request.form['tax']


        #prepare for db entry
        tab = {
                'title' : request.form['title'],
                'group' : request.form['group'], #array of user ids
                'items' : tab_items,
                'subtotal' : request.form['subtotal'],
                'total' : request.form['total'],
                'tip' : request.form['tip'],
                'tax' : request.form['tax']
                }
        tabs_id = tabs.insert(tab)


        # create invites from group.
        create_invites(tab_group, tab_id)
        print 'items = ' + tabs.find_one({"_id":tabs_id})['items']

        return 'inserted tab with tab_id: ' + tabs.find_one({"_id":tabs_id})['id']
    else:
        return "not a post request"

# GET TAB
@app.route('/get_tab', methods=['GET'])
def get_tab():
    tabs = get_db_collection('tabs')
    tab_id = request.args.get('tab_id', '')
    le_tab = tabs.find_one({"_id" : tab_id})
    json = json.dumps(le_tab)
    return json

# UPDATE TAB ITEMS
@app.route('/update_tab_items', methods=['POST'])
def update_tab_items():
    ''' updates items in a tab '''
    tabs = get_db_collection('tabs')
    tab_id = request.form['tab_id']
    le_tab = tabs.find_one({"id" : tab_id})
    if (le_tab == None):
        return 'Tab not found'
    else:
        print   le_tab['items'][1]
        return 'jello'

# UPDATE TAB BILL
@app.route('/update_tab_bill', methods=['POST'])
def update_tab_bill(bill_json):
    '''Updates tab to add each bill items description and value'''
    db = get_db_connection("okra")   #get conncection
    tabs = get_db_collection('tabs')#get tabs collection

    tab_id = request.args.get('tab_id', '')
    le_tab = tabs.find_one({"id" : tab_id})

    #whatever stevens json collection is called
    bill_json = get_db_collection('bill_json')

    #Insert bill items to tab
    le_tab['items_prices'] = bill_json['tab_items']
    le_tab['total'] = bill_json['tab_meta']

    tabs.insert(le_tab)


########################################################################
=======
>>>>>>> 5112a34733697429d484063ceb5dfb9b90432d21



##################################################################
############################## USERS   ###########################
##################################################################
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
    user = users_collection.find_one({"_id":user_id}))
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

########################################################################

##############################    ITEMS   #############################
#ASSIGN ITEM
@app.route('/assign_item')
def assign_item(tab_id, item_id, user_id):
    ''' gets the list of friends with their ids and names for a given user id '''
    tabs = get_db_collection('tabs')
    tab_id = request.form['tab_id']
    le_tab = tabs.find_one({"id" : tab_id})
    
    le_tab['items'][2].append(user_id)
    tabs.insert(le_tab)

#UNASSIGN ITEM
@app.route('/unassign_item')
def unassign_item(tab_id, item_id, user_id):
    ''' gets the list of friends with their ids and names for a given user id '''
    tabs = get_db_collection('tabs')
    tab_id = request.form['tab_id']
    le_tab = tabs.find_one({"id" : tab_id})
    
    le_tab['items'][2].append(user_id)
    number_of_users = len(le_tab['items'][2])
    remove_location = -1
    i=0
    for i in range(0, number_of_users):
        if (le_tab['items'][2][i] == user_id):
            remove_location = i
            break
    if (remove_location > 0):
        le_tab['items'][2].pop(remove_location)      

    tabs.insert(le_tab)    

############################## INVITE shit  ############################

def create_invites(group, tab_id): #used by create tab to invite users that are added.
    invites = get_db_collection('invites')
    print "Creating invites for " +  group
    users = eval(group)
    for user_id in users:
        print str(user_id) + " " + tab_id
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


############################# UPLAOD IMAGE #############################
# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'images/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/img-upload')
def img_upload():
    return render_template('img-upload.html')

# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
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
        parsed_tabs = scan.okraparser.full_scan(filename)
        print parsed_tabs
        okratabs = get_db_collection("tabs")   #get conncection

        insert_tabs = {}
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

        # okratabs = db.tabs
        tab_id = okratabs.insert(insert_tabs)

        # tab_id = db.
        # return str(insert_tabs)
        return str({'tab_id' : tab_id})
        # return redirect(url_for('uploaded_file',
                                # filename=filename))



# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

########################################################################


############################## VENMO ###################################

### init
@app.route('/venmo_login')
def index():
    if session.get('venmo_token'):
        # return 'Your Venmo token is %s' % session.get('venmo_token')
        # venmo_token  = session.get('venmo_token')
        # charge_or_pay('charge',venmo_token,8576009129, 0.01,'')
      return 'Jaime charged'
    else:
      return redirect('https://api.venmo.com/v1/oauth/authorize?client_id=%s&scope=make_payments,access_profile&response_type=code' % CONSUMER_ID)


#### Charge
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


    # phone_number = request.args.get('phone_number', '')
    # print phone_number
    # user