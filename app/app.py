import os
import requests
import operator
import re
import json
from sqlalchemy.sql import text
from flask import Flask, render_template, request, jsonify, session, redirect, flash, jsonify
from flask_sqlalchemy import SQLAlchemy 
from collections import Counter
from os import getenv
import time
from utils.help_functions import HelpFunctions
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = getenv('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///erikstandard"
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
        #print("Tässä on user", user)
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
    #flash('Olet kirjautunut ulos.')
    return 'Olet kirjautunut ulos.'

@app.route('/translating', methods=['POST'])
def translating():
    file = request.files.get('file')
    if file:
        video_content = file.read()
        audioclip = HelpFunctions.irroita_aani(video_content)
        transcribed_text = HelpFunctions.whisper_f(audioclip)
        
        # Tallenna transkriptio väliaikaisesti (esim. sessioon)
        # mahdollisesti tietokantaan
        session['transcribed_text'] = transcribed_text
        
        return jsonify({'status': 'done'})

    return jsonify({'status': 'error'})

@app.route('/info')
def info():
    return "Tässä informaatiota käännöksen toiminnasta" 

@app.route('/account')
def account():
    return "Tässä on käyttäjän informaatiot" 

@app.route('/help')
def help():
    return "Tässä sulle apuva" 

@app.route('/text-ready')
def text_ready():
    transcribed_text = session.get('transcribed_text', '')
    return render_template('text_data.html', text=transcribed_text)


@app.route('/texteditor', methods=['GET', 'POST'])
def texteditor():
    return "tämä on tekstin tarkastelluun tarkoitettu sivu" 



