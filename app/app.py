from sqlalchemy.sql import text
from flask import Flask, render_template, request, jsonify, session, redirect, flash, jsonify
from flask_sqlalchemy import SQLAlchemy 
from collections import Counter
from os import getenv
import time
from datetime import datetime
from werkzeug.datastructures import FileStorage
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename


from app.utils.help_functions import HelpFunctions

app = Flask(__name__)
app.secret_key = getenv('SECRET_KEY')

#For local
#app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")

#For deployment
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL").replace("://", "ql://", 1)

db = SQLAlchemy(app)

@app.route('/')
def index():
    # Tarkistaa, onko käyttäjänimi tallennettu ses
    if 'username' in session:
        # Käyttäjä on kirjautunut sisään
        return render_template('upload.html')
    else:
        # Käyttäjä ei ole kirjautunut sisään
        return redirect('/login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        #ei saa olla SQL injektion
        password = request.form.get('password')
        #ei saa olla SQL injektion
        confirm_password = request.form.get('confirm_password')
        purpose = request.form.get('purpose')

        if password != confirm_password:
            return 'Salasanat eivät täsmää.'

        # Tarkista, onko käyttäjänimi jo käytössä
        existing_user = db.session.execute(text('SELECT * FROM userinfo WHERE username = :username'), {'username': username}).fetchone()
        if existing_user:
            #flash('Käyttäjänimi on jo käytössä.')
            return 'Käyttäjänimi on jo käytössä.'

        # Luo uusi käyttäjä
        hashed_password = generate_password_hash(password)
        db.session.execute(text('INSERT INTO userinfo (username, password, purpose) VALUES (:username, :password, :purpose)'),
                           {'username': username, 'password': hashed_password, 'purpose': purpose})
        db.session.commit()
        return 'Pääsit kirjautumaan sisään'

    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        #EI saa olla SQL inj
        password = request.form.get('password')
        ##EI saa olla SQL inj
        result = db.session.execute(text('SELECT * FROM userinfo WHERE username = :username'), {'username': username})
        user = result.fetchone()
       
        if user is not None:
            if check_password_hash(user[2], password):
                session['username'] = username
                return render_template('upload.html')
            else:
                return 'Väärä salasana.'
        else:
            return 'Väärä käyttäjätunnus tai salasana.'

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

@app.route('/translating', methods=['POST'])
def translating():
    file = request.files.get('file')
    if file:
        if file.content_type == 'video/mp4':
            filename = secure_filename(file.filename) ###
        else: 
            return "Tiedosto ei ole mp4 muodossa"
        video_content = file.read()
        audioclip = HelpFunctions.irroita_aani(video_content)

        transcribed_text = HelpFunctions.whisper_f(audioclip, trans_model= request.form['size'])

        session['transcribed_text'] = transcribed_text
        db.session.execute(text('INSERT INTO content (user_id, text, date_posted, video_name) VALUES (:user_id, :text, :date_posted, :video_name)'), 
                           {'user_id': session.get('username'), 'text': session['transcribed_text'], 'date_posted': datetime.now(), 'video_name':filename})
        db.session.commit()
        
        
        result = db.session.execute(text('SELECT purpose FROM userinfo WHERE username = :username'), {'username': session.get('username')}).fetchone()
        purpose = result[0]
        db.session.execute(text('INSERT INTO data (data_posted, purpose, lenght) VALUES (:data_posted, :purpose, :lenght)'), 
                           {'data_posted': datetime.now(), 'purpose': purpose, 'lenght': file.content_length })
        db.session.commit()
        return jsonify({'status': 'done'})

    return jsonify({'status': 'error'})

@app.route('/info')
def info():
    if 'username' in session:
        # Käyttäjä on kirjautunut sisään
        return render_template('info.html')
    else:
        # Käyttäjä ei ole kirjautunut sisään
        return redirect('/login')

@app.route('/account')
def account():
    if 'username' in session:
        # Käyttäjä on kirjautunut sisään
        return render_template('account.html')
    else:
        # Käyttäjä ei ole kirjautunut sisään
        return redirect('/login') 

@app.route('/help')
def help():
    if 'username' in session:
        # Käyttäjä on kirjautunut sisään
        return render_template('help.html')
    else:
        # Käyttäjä ei ole kirjautunut sisään
        return redirect('/login') 

@app.route('/text-ready')
def text_ready():
    if 'username' in session:
        transcribed_text = session.get('transcribed_text', '')
        return render_template('text_data.html', text=transcribed_text)
    else:
        # Käyttäjä ei ole kirjautunut sisään
        return redirect('/login')
    
@app.route('/textdata', methods=['GET', 'POST'])
def texteditor():
    if 'username' in session:
        user_texts = db.session.execute(text('SELECT video_name, date_posted, text FROM content WHERE user_id = :username'), {'username': session.get('username')}).fetchall()

        user_data = {}
        for video_name, date_posted, text_content in user_texts:
            user_data[video_name] = [date_posted, text_content]

        print(user_data)

        return render_template('previous_texts.html')
    else:
        return redirect('/login')



