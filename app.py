from flask import Flask ,render_template,jsonify #inside module import Class named Flask
from flask_pymongo import PyMongo

#to use template insid ethe app.py we make useof render_template

app = Flask(__name__) # createing object of the class / putting the class object into variable app
 # __name__ referes to how this particular script was invoked. Since __name__ is invoked at app.py it refers to __manin__
app.config['MONGO_URI'] = 'mongodb://admin:password@my_mongodb_container:27017/my_database'
mongo = PyMongo(app)

 # any website you access is via url hence we need to create a route
 # now we need to tell the flask when certain url is requested what we should return
 
 # @ here is called the decorator in python - often used in libraries to provide some advance functionalities.
 
 #CREATE A PYTHON LIST - JOBS
JOBS=[
    {
         'id':1,
         'title':'SEO Analyst',
         'location':'Cyberpark,Kozhikode',
         'description':"Conduct keyword research to identify opportunities for improving search engine rankings Analyze website traffic and search engine rankings to identify trends and opportunities for improvement Assist in developing and implementing on-page and off-page SEO strategies to increase organic traffic and improve search engine rankings Work closely with the content team to create high-quality, SEO-friendly content Collaborate with the web development team to ensure that website code is optimized for search engines and provides a great user experience Stay up-to-date with the latest trends and best practices in SEO and search engine marketing Produce regular reports on SEO performance and provide recommendations for... improvement "
     },
     {
         'id':2,
         'title':'Data Analyst',
         'location':'Cyberpark,Kozhikode',
         'description':"Conduct keyword research to identify opportunities for improving search engine rankings Analyze website traffic and search engine rankings to identify trends and opportunities for improvement Assist in developing and implementing on-page and off-page SEO strategies to increase organic traffic and improve search engine rankings Work closely with the content team to create high-quality, SEO-friendly content Collaborate with the web development team to ensure that website code is optimized for search engines and provides a great user experience Stay up-to-date with the latest trends and best practices in SEO and search engine marketing Produce regular reports on SEO performance and provide recommendations for... improvement "
     },
     {
         'id':3,
         'title':'Data Engineer',
         'location':'Remote',
         'description':"Conduct keyword research to identify opportunities for improving search engine rankings Analyze website traffic and search engine rankings to identify trends and opportunities for improvement Assist in developing and implementing on-page and off-page SEO strategies to increase organic traffic and improve search engine rankings Work closely with the content team to create high-quality, SEO-friendly content Collaborate with the web development team to ensure that website code is optimized for search engines and provides a great user experience Stay up-to-date with the latest trends and best practices in SEO and search engine marketing Produce regular reports on SEO performance and provide recommendations for... improvement "
     },
    {
         'id':4,
         'title':'Frontend Engineer',
         'location':'Cyberpark,Kozhikode',
         'description':"Conduct keyword research to identify opportunities for improving search engine rankings Analyze website traffic and search engine rankings to identify trends and opportunities for improvement Assist in developing and implementing on-page and off-page SEO strategies to increase organic traffic and improve search engine rankings Work closely with the content team to create high-quality, SEO-friendly content Collaborate with the web development team to ensure that website code is optimized for search engines and provides a great user experience Stay up-to-date with the latest trends and best practices in SEO and search engine marketing Produce regular reports on SEO performance and provide recommendations for... improvement "
     },
    {
         'id':5,
         'title':'Backend Engineer',
         'location':'Cyberpark,Kozhikode',
         'description':"Conduct keyword research to identify opportunities for improving search engine rankings Analyze website traffic and search engine rankings to identify trends and opportunities for improvement Assist in developing and implementing on-page and off-page SEO strategies to increase organic traffic and improve search engine rankings Work closely with the content team to create high-quality, SEO-friendly content Collaborate with the web development team to ensure that website code is optimized for search engines and provides a great user experience Stay up-to-date with the latest trends and best practices in SEO and search engine marketing Produce regular reports on SEO performance and provide recommendations for... improvement "
     },
 ]
 
@app.route('/') # registering the route which is the part of the url
def home():
    return render_template('home.html',jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

@app.route('/apply')
def apply():
    return render_template('form.html')
