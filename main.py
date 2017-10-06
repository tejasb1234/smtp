from flask import Flask ,render_template,request
import socket
app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template("main.html")


@app.route('/fetch_ip',methods = ['POST', 'GET'])
def fetch_ip():
	if request.method=="POST":
		str=request.form['web_add']
		while True:
			try:
				ip_add=socket.gethostbyname(str)
				return port_check(ip_add)
			except socket.gaierror:
				return render_template("error.html")

def port_check(ip_address):
	import subprocess,os,nmap
	ip_str=str(ip_address)
	nm=nmap.PortScanner()
	real_check=nm.scan(ip_address,'22-443')
	if 25 in real_check['scan'][ip_str]['tcp']:
		if real_check['scan'][ip_str]['tcp'][25]['state']=='open':
			return render_template("exploity.html",ip_value=ip_address)
		else:
			return render_template("exploitn.html")
	else:
		return render_template("exploitn.html")


@app.route('/smtp_detail',methods=['POST','GET'])
def smtp_detail():
	return render_template("smtp_detail.html")


@app.route('/smtp_exploit',methods=['POST','GET'])
def smtp_exploit():
	if request.method=="POST":
		import smtplib
		import email
		msg=email.message.Message()
		mail_from=request.form['Sender']
		msg["From"]=mail_from
		mail_to=request.form['Recipient']
		msg["To"]=mail_to
		mail_subj=request.form['Subject']
		msg["Subject"]=mail_subj
		mail_body=request.form['message']
		msg["body"]=mail_body
		mail_ser=request.form['Server']
		server=smtplib.SMTP(mail_ser, 25)
		server.starttls()
		server.ehlo_or_helo_if_needed()
		try:
			failed=server.sendmail(mail_from, mail_to, msg.as_string())
			server.close()
			return render_template("Success.html")
		except Exception as e:
			return render_template("Failure.html")
			




if __name__ == '__main__':
	app.run(debug=True)
