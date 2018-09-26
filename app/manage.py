
#-*-coding: euc-kr -*-

from flask import Flask, jsonify, request
from Menu import menu
import src

app = Flask(__name__)

@app.route('/')
def temp() :
	return 'god yungoon ������'

@app.route('/keyboard')
def keyboard() :
	return jsonify(src.mealTimeKeyB)

@app.route('/message', methods = ['POST'])
def message() :
	data = request.get_json()
	content = data['content']

	resp = dict()
	if content in src.mealTime:
		resp['message'] = {'text' : menu.getMeal(content)}
		resp['keyboard'] = src.mealTimeKeyB
	return jsonify(resp)

if __name__ == '__main__' :
	app.debug = True
	app.run(host = '0.0.0.0', port = 1526)