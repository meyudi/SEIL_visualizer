from flask import Flask, request, Response, jsonify
#from flaskext.mysql import MySQL
from datetime import datetime

#mysql = MySQL()
app = Flask(__name__)

'''
DB = ""
HOST=""
USER =""
PASSWORD=""

app.config['MYSQL_DATABASE_USER'] = USER
app.config['MYSQL_DATABASE_PASSWORD'] = PASSWORD
app.config['MYSQL_DATABASE_DB'] = DB
app.config['MYSQL_DATABASE_HOST'] = HOST

mysql.init_app(app)

con = mysql.connect()
cur = con.cursor()

'''




'''
	pick the name count from the tagging_app API
	
'''







'''
	get the last T minutes temperature, a sample every minute
'''
@app.route('/last_T_temperature', methods = ['POST','GET'])
def get_last_T_temperature():
	if request.method == 'GET':

		'''
			T is passed as a parameter stored in get request field 'period'
		'''
		period = request.args.get('period')


		cb = request.args.get('callback')

		'''
			Try passing data as json data {'period':X,'values':[,,,,,,]}
		'''
		#update this string with appropriate format
		resp = "%s('%s')" %(cb, name)

		return Response(resp, mimetype='application/javascript')

	elif request.method == 'POST':
		return 'post request not supported'




'''
	get the recent temperature
'''
@app.route('/recent_temperature' , methods = ['POST','GET'])
def get_current_temperature():
	if request.method == 'GET':

		'''
			get temperature which is average over past two minutes
		'''

		cb = request.args.get('callback')

		#update this string with appropriate format
		resp = "%s('%s')" %(cb, name)

		return Response(resp, mimetype='application/javascript')

	elif request.method == 'POST':
		return 'post request not supported'



@app.route('/')
def index():
	info_str = "v1.0<br>" + "These are only GET APIs"

	return info_str




if __name__ == '__main__':
	app.run('0.0.0.0',port=7001, debug=True)