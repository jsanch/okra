import os

def charge_or_pay(payment_type, token, phone, amount, note):
	if (payment_type != 'charge' or payment_type != 'pay'):
		payment_type = 'charge'

	if (note == ""):
		note = 'OkraPayment'

	if (token == ""):
		token = 'mTx8m3RhPX59bty5etDaVTD8CxYq6BNG'

	if (payment_type == "charge"):
		amount = -amount

	url = 'curl https://api.venmo.com/v1/payments -d access_token=' + token + ' -d phone="' + str(phone) + '" -d amount=' + str(amount) + ' -d note=' + note

	os.system(url)

	#os.system('curl https://api.venmo.com/v1/payments -d access_token=mTx8m3RhPX59bty5etDaVTD8CxYq6BNG -d phone="8576009129" -d amount=-0.01 -d note="Okra."')