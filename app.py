from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

@app.route('/test', methods=['GET'])
def hellotest():
   return "Hello World"
   
if __name__ == '__main__':
    app.run()
