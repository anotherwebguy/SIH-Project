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
from django.views.decorators.cache import cache_control
from pyqrcode import QRCode
# Create your views here.

config = {
    'apiKey': "AIzaSyD7M-q1iWhGNNfbubsLqk5c6JkPcpsncWk",
    'authDomain': "test-27aa1.firebaseapp.com",
    'projectId': "test-27aa1",
    'storageBucket': "test-27aa1.appspot.com",
    'messagingSenderId': "719972795548",
    'databaseURL': 'https://test-27aa1-default-rtdb.firebaseio.com',
    'appId': "1:719972795548:web:ef9f14894c265919b89959"
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
    public_key = request.POST.get('address')
    role = request.POST.get('role')
    name = request.POST.get('username')

    try:
        user = auth.create_user_with_email_and_password(email,password)
        print(user['idToken'])
        uid = user['localId']
        print(uid)
        data = {
            "name": name,
            "email": email,
            "address": public_key,
            "role": role,
        }
        result = db.child("user").child(role).child(uid).set(data)
        print(result)
    except:
        return redirect('register')
    return render(request,'main/login.html')


def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    role = request.POST.get('role')
    
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        user_details = db.child('user').child(role).get()
        check = False
        for u in user_details:
             if u.key() == user['localId'] and u.val()['role'] == role:
                 check = True
                 break
        request.session['uid'] = user['localId']
    except:
        return render(request,'main/login.html',{"message":"Invalid credentials"})
    return redirect('index')

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return redirect('welcome')