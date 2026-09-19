from flask import Flask

'''
app=Flask()---> instace of flask class and it our msgi(web server gateway interface)
this will create a server in our local system
'''

app = Flask(__name__) 
@app.route('/')
def check():
    return 'welcome to flask journey.Go with fucking fearless'

@app.route('/home')
def home():
    return 


if __name__=='__main__':
    app.run(debug=True) #debug help to reload web page auto automatically when we save changes in the code
    








