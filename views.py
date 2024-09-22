from flask import (render_template,request,redirect,url_for)
from db_func import (add_user,delete_user,update_user,confirm_by_code,confirm_by_email,user_post,
                     confirm_by_code_withnot_hash,search_code,search_chat,search_tag,reload)
from models import (db,UserTabel,UserChat)
from packagee import (my_hash)

def inapp():
  return render_template('inapp.html')

def singup():
    try:
        if request.method == "POST":
            email = request.form['email']
            password = request.form['password']
            name = request.form['name']
            
            if email == '': # پارامتر های ایمیل
                report = "لطفا ایمیل درست را وارد کنید"
                return render_template("singup.html",report=report)
            else:
                pass
            gmail = '@gmail.com'
            yahoo = '@yahoo.com'
            if gmail in email or yahoo in email:
                pass
            else:
                report = '@Gmail.com, @Yahoo.com' + 'ایمیل هایی مورد تایید'
                return render_template("singup.html",report=report)
            # پایان پارامترهای ایمیل
            
            password = str(password)
            if password == "" or len(password) < 5: # پارامتر های گذرواژه 
                report = "گذرواژه قوی تری وارد کنید"
                return render_template("singup.html",report=report)
            # پایان پارامتر های گذرواژه
            
            report = "شما ثبت نام شدید"
            shenaseh = add_user(email,password,name)
            return render_template("singup.html",report=report,sh=shenaseh)
        
    except:
        report = 'این ایمیل قبلا ثبت شده است'
        shenaseh = "شناسه دریافت نکردید"
        return render_template("singup.html",report=report,sh=shenaseh)
        
    return render_template("singup.html")

def delete_email():
    try:
        if request.method == "POST":
            code = request.form['code']
            email = request.form['email']
            password = request.form['password']
            
            if code == '':
                report = 'لطفا شناسه را خالی وارد نکنید'
                return render_template("delet_email.html",report=report)
            if email == "":
                report = 'لطفا ایمیل را خالی وارد نکنید'
                return render_template("delet_email.html",report=report)
            if password == "":
                report = 'لطفا رمز عبور خود را وارد کنید'
                return render_template("delet_email.html",report=report)
            
            report = delete_user(code,email,password)
            return render_template("delet_email.html",report=report)
    except:
        report = 'خطای رخ داده است یا اطلاعات وارد شده غلط است , مجددا تلاش کنید'
        return render_template("delet_email.html",report=report)
        
    return render_template("delet_email.html")

def change_account():
    try:
        if request.method == "POST":
            code = request.form['code']
            email = request.form['email']
            password = request.form['password']
            new_email = request.form['new_email']
            newpass = request.form['newpass']
            print(code,email,password)
            if code == '' or email == "" or password == "":
                report = 'لطفا اطلاعات قبلی خود را درست وارد کنید'
                return render_template("updateuser.html",report=report)
            # پارامتر های آپدیت
            if new_email == "":
                report = 'ایمیل جدید را وارد کنید'
                return render_template("updateuser.html",report=report)
            gmail = 'gmail'
            yahoo = 'yahoo'
            if gmail in new_email or yahoo in new_email:
                pass
            else:
                report = ' @Gmail.com, @Yahoo.com ' + ' ایمیل هایی مورد تایید '
                return render_template("updateuser.html",report=report)
            
            if newpass == "" or len(newpass) < 5:
                report = "گذرواژه قوی تر انتخاب کنید"
                return render_template("updateuser.html",report=report)
            else:
                pass
            # پایان پارامترها
            report =  update_user(code,email,password,new_email,newpass)
            return render_template("updateuser.html",report=report)
           
    except:
        report = 'خطای رخ داده است یا اطلاعات وارد شده غلط است , مجددا تلاش کنید'
        return render_template("updateuser.html",report=report)
    
    return render_template("updateuser.html")

def Login():
    return render_template("login.html",report=None)

def Login_code():
    try:
        if request.method == "POST":
            code = request.form['code']
            password = request.form['password']
            if code == "":
                report = 'لطفا شناسه خود را وارد کنید'
                return render_template("login.html",report=report)
            if password == "":
                report = 'گذرواژه اشتباه است'
                return render_template("login.html",report=report)
            user = confirm_by_code(code,password)
            if user.password == my_hash(password):
                print(user)
                dbchat = search_code(user.code)
                return render_template('inapp.html',inuser=user,dbchat=dbchat)
    except:
        report = 'خطای رخ داده است یا اطلاعات وارد شده غلط است , مجددا تلاش کنید'
        return render_template("Login.html",report=report)
    return redirect('/Login')
        
def Login_email():
    try:
        if request.method == "POST":
            email = request.form['email']
            password = request.form['password']
            user = confirm_by_email(email,password)
            print(user)
            if user.password == my_hash(password):
                print(user)
                dbchat = search_code(user.code)
                print(dbchat)
                return render_template('inapp.html',inuser=user,dbchat=dbchat)
    except Exception:
        report = 'خطای رخ داده است یا اطلاعات وارد شده غلط است , مجددا تلاش کنید'
        return render_template("Login.html",report=report)
    return redirect('/Login')

def sabt_post():
    try:
        try:
            code = request.form['code'] # ثابت
            password = request.form['password'] # ثابت
            user = confirm_by_code_withnot_hash(code,password)
            chat = request.form['chat'] # متغیر
            tag = request.form['tag']   # متغیر
            if chat == "" or len(chat) < 28 or tag == "":
                    report = 'یک تگ حداقل بنویسید و لطفا طول حروف را بیشتر از 30 تا و کمتر از 259 تا وارد کنید و پر کردن کادر الزامی است'
                    dbchat = search_code(user.code)
                    return render_template('inapp.html',inuser=user,dbchat=dbchat,report=report)
            user_post(code, user.name, chat, tag)
            dbchat = search_code(user.code)
            print(dbchat)
            return render_template('inapp.html',inuser=user,dbchat=dbchat,report=None)
        except:
            return "<h1><a href='/Login'>بابت بروز خطا شرمنده ایم</a></h1>"
    except:
        dbchat = search_code(user.code)
        report = 'کلام تکراری ثبت نمی شود'
        return render_template('inapp.html',inuser=user,dbchat=dbchat)

def new_kalam():
    chats = db.session.execute(db.select(UserChat)).scalars().all()
    kalam = reload(chats)
    return render_template("new.html",kalam=kalam)

