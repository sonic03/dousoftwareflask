from flask import Flask,render_template,redirect,url_for,request,flash
from wtforms import StringField,TextAreaField,Form
from flask_mail import Mail,Message




class ContactForm(Form):
    email=StringField("Mail adresiniz")
    detay=TextAreaField("Detaylı bilgi")



app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'reklamvereneleman@gmail.com'
app.config['MAIL_PASSWORD'] = '147852963Dark'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = "reklamvereneleman@gmail.com"
app.config['SECRET_KEY'] = "denemedenemedımdımdım"

mail = Mail(app)




@app.route("/",methods=["GET","POST"])
def index():
    form=ContactForm(request.form)
    if request.method=="POST":
        try:
        
    
            email=form.email.data
            detay=form.detay.data
        
            msg=Message("DouSoftware Mesajı",
            sender="reklamvereneleman@gmail.com",
            recipients=["gozluklubukalemun@gmail.com"])

            msg.body=email+" "+"tarafından gelen mesaj\n"+" "+detay
            mail.send(msg)
            flash("Gönderme Başarılı","succes")
            return redirect(url_for("index",form=form))
        except Exception as e:
            return(str(e))
        
    else:
        return render_template("index.html",form=form)




    














if __name__=="__main__":
    app.run(debug=True)