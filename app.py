import os
from flask import Flask, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename




app = Flask(__name__)

@app.route('/')
def index():
    return 'HELLO'

tab = [

        'invitation_id' : 1,
        'user_id' : 2,
        'tab_id' : 5,
        'tab_name': 'Wagamama'

]

@app.route('/ajax/polltab')
def get_polltab():
    return jsonify( { 'tab': tab } )

############################# UPLAOD IMAGE #############################
UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
########################################################################

####################### VENMO ##########################################



########################################################################

@app.route('/')
def index():
    if session.get('venmo_token'):
        return 'Your Venmo token is %s' % session.get('venmo_token')
    else:
        return redirect('https://api.venmo.com/v1/oauth/authorize?client_id=%s&scope=make_payments,access_profile&response_type=code' % CONSUMER_ID)




if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')
