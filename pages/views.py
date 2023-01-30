from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def home(request):
  return render(request,"index.html")

def lotus(request):
  return render(request,"details_lotus.html")

def horus(request):
  return render(request,"details_horus.html")

def goldn(request):
  return render(request,"details_goldn.html")

def book(request):
  
  if request.method=="POST":
    form=ReservationForm(request.POST)
    
    if form.is_valid():
      form.save()
      return redirect("home")
    else:
      print(form.errors)
      return redirect("book")
  
  return render(request,"book_form.html")

@login_required(login_url="login")
def dashboard(request):
  reservations=Reservation.objects.filter(status="pending")
  context={
    "reservations":reservations,
  }
  
  return render(request,"dashboard.html",context)


def logoutPage(request):
    logout(request)
    return redirect("login")


def loginPage(request):
    
    if request.user.is_authenticated==False:
        
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
            
        return render(request,"login.html")
    
    else:
        return redirect("dashboard")


def approveReserv(request,pk):
  
  res=Reservation.objects.get(id=pk)
  
  res.status="approved"
  
  res.save()
  
  return redirect("dashboard")


def delReserv(request,pk):
  
  res=Reservation.objects.get(id=pk)
  res.delete()
  return redirect("dashboard")

