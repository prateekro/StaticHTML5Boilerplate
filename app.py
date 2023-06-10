app = Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')
