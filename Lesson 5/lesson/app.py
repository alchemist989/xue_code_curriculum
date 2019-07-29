from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return render_template('home_example.html')



volunteer_posting = [
  {
    'organization': 'Have a Heart',
    'author': 'Joseph', 
    'description': 'Donate Blood today!'
  },
  {
    'organization': 'Homeless Shelter',
    'author': 'Grace',
    'description': 'Help out at the local homeless shelter'
  }
]

title = "My Volunteering Match"

@app.route('/post')
def post():
  return render_template('post.html', posts=volunteer_posting, title=title)

@app.route('/sandbox')
def sandbox():
  return render_template('sandbox.html')

if __name__ =="__main__":
  app.run(debug=True,port=5000)
              