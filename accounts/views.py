from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
def login(request):
   if request.method=='POST':
      username=request.POST['username']
      Password=request.POST['password']
      user=auth.authenticate(username=username,password=Password)
      if user is not None:
         auth.login(request,user)
         return redirect("/")
      else:
         messages.info(request,'invalid credentials')
         return redirect("login")   

   else:
      return render(request,'login.html')


   

def register(request):
   if request.method=='POST':
      first_name=request.POST['first_name']
      last_name=request.POST['last_name']
      username=request.POST['username']
      email=request.POST['email']
      Password1=request.POST['password1']
      Password2=request.POST['password2']
      if Password1==Password2:
         if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('register')
         else:
            user=User.objects.create_user(username=username,password=Password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            print("user created")
            return redirect("login")
      else:
         messages.info(request,"Password not matching")
         return redirect('register')
      return redirect('/')
   else:
      return render(request,'register.html')

def logout(request):
   auth.logout(request)
   return redirect('/')