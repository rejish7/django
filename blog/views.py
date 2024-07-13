from django.shortcuts import render

from django.http import HttpResponse

# def index(request):
#     return render(request,"index.html")

# def user(request):
#     return render(request,"user.html")

# def news(request):
#     return render(request,"news.html")

def  gallery(request):
    return render(request,"gallery.html")

# def faq(request):
#     return render(request,"faq.html")

# def travel(request):
#     return render(request,"travel.html")