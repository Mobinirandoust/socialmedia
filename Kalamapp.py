from flask import (Flask,redirect,render_template,request)
from models import (db,UserTabel,UserChat)
from views import (singup,delete_email,change_account,Login,Login_code,Login_email,sabt_post,new_kalam)
from db_func import (update_user,delete_user,add_user,confirm_by_code,confirm_by_email,user_post,reload,search_tag
                    ,search_code,search_chat,confirm_by_code_withnot_hash)
from random import (choice)
from packagee import (trans_my_hash,my_hash)    

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"


db.init_app(app)

with app.app_context():
    db.create_all()
    # users = db.session.execute(db.select(UserTabel)).scalars().all()
    # print(users)
    # users = db.session.execute(db.select(UserChat)).scalars().all()
    # s = reload(users)
    # s = user_post(52668,'سعید ایران دوست',"آرزو دوست دارم",'آرزو')
    # s = confirm_by_email('sima@gmail.co','123')
    # s = confirm_by_code(324000,'123')
    # s = delete_user(155610,'mobin1234567@com.ir','123')
    # add_user('simaaaaaaaa@com.ir','123',"سیما ایران دوست")
    # s = update_user(324000,'hashtag@gmail.co','123','sima@gmail.co','123')
    # s = search_tag('کلام')
    # s = search_chat('دانشجو')
    # s = search_code('383040')
    # print(s)
    pass

app.add_url_rule("/","index",view_func=singup,methods=["post","get"])
app.add_url_rule("/delete_email","Delete Email",view_func=delete_email,methods=["post","get"])
app.add_url_rule("/change_account","Change Account",view_func=change_account,methods=["post","get"])
app.add_url_rule("/Login","Login",view_func=Login,methods=["post","get"])
app.add_url_rule("/Login/email","Login email",view_func=Login_email,methods=["post","get"])
app.add_url_rule("/Login/code","Login code",view_func=Login_code,methods=["post","get"])
app.add_url_rule("/Login/sabt_post/","Sabt Post",view_func=sabt_post,methods=["post","get"])
app.add_url_rule("/new/kalam"," Kalam's ",view_func=new_kalam,methods=["get",'post'])


@app.route('/<name>')
def exp(name):
    return redirect('/')

@app.route('/home/<code>/')
def hmoe_code(code):
    chats = search_code(code)
    return render_template("new.html",kalam=chats)

@app.route('/delete/kalam/',methods=["get",'post'])
def del_kalam():
    try:
        code = request.form['code'] # ثابت
        password = request.form['password'] # ثابت
        id = request.form['ID'] # ثابت
        user = confirm_by_code_withnot_hash(code,password)
        if type(user) == type(""):
            return "کاربر مورد نظر پیدا نشد"
        else:
            req = db.get_or_404(UserChat,id)
            db.session.delete(req)
            db.session.commit()
            dbchat = search_code(user.code)
            return render_template('inapp.html',inuser=user,dbchat=dbchat)
    except:
        return 'موفق نبودیم شرمنده ایم'

@app.route('/search/s/',methods=['get','post'])
def search():
    try:
        s = request.form['sabt']
        s = f'{s}'
        print(s)
        sib = search_chat(s)
        return render_template('sch.html',msg=sib)
    except:
        return render_template('sch.html',msg=None)

