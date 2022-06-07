import imaplib
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/api/hotmail')
def hotmail():
	# create an IMAP4 class with SSL 
	imap = imaplib.IMAP4_SSL("imap-mail.outlook.com")
	# authenticate
	try:
  		imap.login(request.args.get("login"), request.args.get("passwd"))
  		return '{"status": "success"}'
	except:
		return '{"status": "failed"}'
