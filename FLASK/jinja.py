from flask import redirect,url_for
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("getresult.html") 


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    subject = request.form["subject"]
    message = request.form["message"]

    print("name : ",name)
    print("email : ",email)
    print("subject : ",subject)
    print("message : ",message)

    return render_template("index1.html")

#variable rule
@app.route('/succes/<int:score>')
def succes(score):
    res=''
    if score>=50:
        res='Passed'
    else:
        res='Failed'

    return render_template('index2.html',result=res)


#dinamic url(calling anther url)
@app.route('/getresult',methods=['POST'])
def getresult():
    name=request.form['name']
    subject1=request.form['subject1']
    subject2=request.form['subject2']
    subject3=request.form['subject3']
    subject4=request.form['subject4']
    result=float(subject1+subject2+subject3+subject4)/4
    return redirect(url_for('succes',score=result))
    
if __name__ == "__main__":
    app.run(debug=True)



