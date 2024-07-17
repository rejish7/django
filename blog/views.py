from django.shortcuts import render,redirect

from django.http import HttpResponse
from .model import User
from django.contrib import messages



def user(request):
    if request.method=="POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        address = request.POST.get("Address")
        age = request.POST.get("Age")
        gender = request.POST.get("Gender")
        country = request.POST.get("Country")
        User.objects.create(Name=name,Email=email,Address=address,Age=age,Gender=gender,Country=country)
        messages.success(request,'Data inserted successfully')
        return redirect("/")
    else:
        data={'userdata':User.objects.all(),}
    return render(request,"user.html",data)

def delete (request,id):
    User.objects.get(id=id).delete()
    return redirect("/")


def edit(request,id):
    if request.method=="POST":
        obj=User.objects.get(id=id)
        obj.name = request.POST.get("Name")
        obj.email = request.POST.get("Email")
        obj.address = request.POST.get("Address")
        obj.age = request.POST.get("Age")
        obj.gender = request.POST.get("Gender")
        obj.country = request.POST.get("Country")
        return redirect("/")
    else:
        data={'userdata':User.objects.get(id=id),
        }
        return render(request,"edit.html",data)



