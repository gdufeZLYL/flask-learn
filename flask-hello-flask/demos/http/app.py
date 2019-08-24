from flask import Flask, request

app = Flask(__name__)

'''
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return '<h1>Hello, Flask<h1>'
'''

@app.route('/hello', methods=['GET'])
def hello():
    # 获取查询参数name的值
    name = request.args.get('name', 'Flask')
    # 插入到返回值中
    return '<h1>Hello, %s!<h1>' % name

@app.route('/goback/<int:year>')
def go_back(year):
    return '<p>Welcome to %d! </p>' % (2018 - year)

@app.route('/colors/<any(blue, white, red):color>')
def three_colors(color):
    return '<p>Love is patient and kind. Love is ' \
           'not jealous or boastful or proud or rude.</p>'

