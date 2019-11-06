from flask import Flask, render_template, request, send_from_directory
import matplotlib.pyplot as plt
import math

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('main.html')


@app.route('/result', methods=['POST'])
def result():
	question_type, question_string = request.form.get('type'), request.form.get('string')
	#  Call main function of the module which calculates the answer
	#answer = call_func(question_string, question_type)
	x = list(range(1, 100))
	y = [math.cos(val) for val in x]
	plt.plot(x, y)

	plt.savefig('static/file.png')

	answer = f'The web-page sent the string {question_string} and the type {question_type}'
	return render_template('result.html', answer=answer)

@app.route('/path:<path>')
def static_file(path):
	return send_from_directory('static', path)

if '__main__' == __name__:
	app.run()