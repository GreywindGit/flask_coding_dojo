from flask import Flask, render_template, redirect
import helper
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello :)"


@app.route('/request-counter', methods=['GET'])
def get_counter():
    counter['GET'] += 1
    return redirect('/')


@app.route('/request-counter', methods=['POST'])
def post_counter():
    counter['POST'] += 1
    return redirect('/')


@app.route('/request-counter', methods=['PUT'])
def put_counter():
    counter['PUT'] += 1
    return redirect('/')


@app.route('/request-counter', methods=['DELETE'])
def del_counter():
    counter['DELETE'] += 1
    return redirect('/')


@app.route('/statistics')
def statistics():
    stats = helper.get_stats('request_counts.txt')
    return render_template('statistics.html', stats=stats)

if __name__ == "__main__":
    app.run(debug=True)