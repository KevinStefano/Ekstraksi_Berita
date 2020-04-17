from django.shortcuts import render
import requests

def button(req):
    return render(req,'web.html')

def output(req):
    data = req.get("https://www.google.com/")
    print(data.text)
    data = data.text
    return  render(req,'web.html', {'data':data})