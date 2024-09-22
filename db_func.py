from models import db,UserTabel,UserChat,datetime
from packagee import unic,my_hash

def add_user(email:str,password:str,name:str,):
    print("Start add user 1")
    x = UserTabel(
        code = unic(),
        email = email,
        password = my_hash(password),
        name = name,
        )
    print("Start add user2")
    db.session.add(x)
    db.session.commit()
    print("add user OK")
    return x.code

def delete_user(code,email:str,password:str):
    try:
        user = db.get_or_404(UserTabel,code)
        if user == None:
            pass
        if user.password != my_hash(password):
            return 'user is not valid in database'
        elif user.password == my_hash(password):
            pass
        if user.email != email:
            return "I can't removing your email"
        if user.email == email:
            print('Email is OK')
            db.session.delete(user)
            db.session.commit()
            print('Delete done')
            return ('حساب شما حذف شد')
    except Exception:
        return 'Error: what is that?'
        
def update_user(code,email:str,password:str,newemail:str,newpass:str):
    try:
        user = db.get_or_404(UserTabel,code)
        if user == None:
            pass
        if user.password != my_hash(password):
            return 'user is not valid in database'
        elif user.password == my_hash(password):
            pass
        if user.email != email:
            return "I can't find your email"
        if user.email == email:
            pass
        user.email = newemail
        user.password = my_hash(newpass)
        user.date = datetime.now()
        db.session.add(user)
        db.session.commit()
        print('Updating your Email !')
        return f'you are new account: ({user.email})'
    except Exception:
        return 'Error: what is that?'
    
def confirm_by_code(code:str,password:str):
    try:
        user = db.get_or_404(UserTabel,code)
    except:
        return 'user in not valid in database'
    if user.password == my_hash(password):
        return user
    else:
        pass
    return 'user in not valid in database'
    
    
def confirm_by_email(email:str,password:str):
    users = db.session.execute(db.select(UserTabel)).scalars().all()
    selected = None
    for i in users:
        if i.email == email and i.password == my_hash(password):
            selected = i
            return selected
    return 'user in not valid in database'

def user_post(code,name,chat,tag):
    try:
        x = UserChat(
            code = code,
            name = name,
            chat = chat,
            tag = tag,
            )
        db.session.add(x)
        db.session.commit()
        print('post added to DataBase')
        return True
    except:
        return 'Post not added to DB'
    
def reload(chats:list):
    print('in Function:',chats,end='\n \n')
    y = chats[::-1]
    return y

def confirm_by_code_withnot_hash(code:str,password:str):
    try:
        user = db.get_or_404(UserTabel,code)
    except:
        return 'user in not valid in database'
    if user.password == password:
        return user
    else:
        pass
    return 'user in not valid in database'

def search_tag(word:str):
    users = db.session.execute(db.select(UserChat)).scalars().all()
    kalam = []
    for i in users:
        if word in i.tag:
            kalam.append(i)
        else:
            pass
    kalam = reload(kalam)
    return kalam


def search_chat(chat):
    users = db.session.execute(db.select(UserChat)).scalars().all()
    var = []
    for i in users:
        if chat in i.chat:
            var.append(i)
        else:
            pass
    kalam = reload(var)
    return kalam

def search_code(code:int):
    code = int(code)
    users = db.session.execute(db.select(UserChat)).scalars().all()
    var = []
    for i in users:
        if code == i.code:
            var.append(i)
        else:
            pass
    kalam = reload(var)
    return kalam
