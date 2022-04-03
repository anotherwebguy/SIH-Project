from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect
import pyrebase
from django.contrib import auth as _auth
from datetime import datetime
from django.shortcuts import redirect
from web3 import Web3
import json
from django.http import JsonResponse
import pyqrcode
import collections
from pyqrcode import QRCode
# Create your views here.

config = {
    'apiKey': "AIzaSyCxwXqN_3rokuLqVsDCa9UsfRbVblHpj7o",
    'authDomain': "sih-project-b6cc5.firebaseapp.com",
    'projectId': "sih-project-b6cc5",
    'storageBucket': "sih-project-b6cc5.appspot.com",
    'messagingSenderId': "187249171665",
    'databaseURL': 'https://sih-project-b6cc5-default-rtdb.firebaseio.com/',
    'appId': "1:187249171665:web:237a2a6e9dae33996539f0"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

def welcome(request):
    return render(request,'main/welcome.html')

def index(request):
    return render(request,'main/home.html')

def register(request):
    return render(request,'main/signup.html')

def signin(request):
    return render(request,'main/login.html')

def signup(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    username = request.POST.get('username')
    role = request.POST.get('role')
    address = request.POST.get('address')

    try:
        user = auth.create_user_with_email_and_password(email, password)
    except:
        message="Unable to create account"
        return render(request,'main/signup.html')
    
    print(user)
    data = {"name":username,"email":email,"address":address,"role":role,"uid":user['localId']}
    db.child('users').child(user['localId']).set(data,user['idToken'])
    return render(request,'main/login.html')

def home(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    role = request.POST.get('role')

    try:
        user = auth.sign_in_with_email_and_password(email, password)
    except:
        message="Invalid credentials"
        return render(request,'main/login.html',{"message":message})

    print(user)
    details = db.child('users').child(user['localId']).get().val()
    frole = details['role']

    if frole == role:
        session_id = user['idToken']
        request.session['uid']=str(session_id)
        return render(request,'main/home.html')
    else:
        message="Invalid credentials"
        return render(request,'main/login.html',{"message":message})
    

def logout(request):
    _auth.logout(request)
    try:
        del request.session['uid']
    except:
        pass
    return render(request,'main/login.html')