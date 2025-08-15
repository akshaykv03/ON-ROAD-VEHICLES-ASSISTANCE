from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Customer,Mechanic,Bookings,SOS,Fire,Feedback
from django.contrib.auth import authenticate
from django.db.models import Q

# Create your views here.
def index(request):
  return render(request,"index.html")

def custReg(request):
  msg=''
  if request.POST:
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    address=request.POST['address']
    password=request.POST['password']
    try:
      user=User.objects.create_user(username=email,password=password,is_active=1)
      user.save()

      cust=Customer.objects.create(name=name,email=email,phone=phone,address=address,user=user)
      cust.save()
      msg="Registration Successfull..."
      return render(request,"custReg.html",{"msg":msg})
    except:  
      msg="Username already registered... "
      return render(request,"custReg.html",{"msg":msg})
  else:
    return render(request,"custReg.html",{"msg":msg})

def mechReg(request):
  msg=''
  if request.POST:
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    address=request.POST['address']
    password=request.POST['password']
    lat=request.POST['l1']
    lon=request.POST['l2']
    try:
      user=User.objects.create_user(username=email,password=password,is_active=0,is_staff=1)
      user.save()

      cust=Mechanic.objects.create(name=name,email=email,phone=phone,address=address,lat=lat,lon=lon,user=user)
      cust.save()
      msg="Registration Successfull..."
      return render(request,"mechReg.html",{"msg":msg})
    except:  
      msg="Username already registered... "
      return render(request,"mechReg.html",{"msg":msg})
  else:
    return render(request,"mechReg.html",{"msg":msg})
  

def login(request):
  msg=''
  if request.POST:
    email=request.POST['email']
    password=request.POST['password']
    user=authenticate(username=email,password=password)
    if user is not None:
      if user.is_superuser:
        return redirect("/adminHome")
      elif user.is_staff:
        data=Mechanic.objects.get(email=email)
        request.session['id']=data.id
        return redirect("/mechHome")
      elif user.username == "ambulance":
        return redirect("/ambulanceHome")
      elif user.username == "fire_fighter":
        return redirect("/fireFighterHome")
      else:
        data=Customer.objects.get(email=email)
        request.session['id']=data.id
        return redirect("/custHome")
    else:
      msg="Invalid username or password.."    
      return render(request,"login.html",{"msg":msg})
  else:
    return render(request,"login.html")  
  





def adminHome(request):
  return render(request,"adminHome.html")


def adminCust(request):
  data=Customer.objects.all()
  return render(request,"adminCust.html",{"data":data})


def adminMech(request):
  data=Mechanic.objects.all()
  return render(request,"adminMech.html",{"data":data})


def adminBookings(request):
  bok=Bookings.objects.all().order_by("-id")
  return render(request,"adminBookings.html",{"bok":bok})

def adminAmbulance(request):
  amb=SOS.objects.all().order_by("-id")
  return render(request,"adminAmbulance.html",{"amb":amb})

def adminFire(request):
  fire=Fire.objects.all().order_by("-id")
  return render(request,"adminFire.html",{"fire":fire})


def adminApproveMech(requset):
  id=requset.GET['id']
  status=requset.GET['status']
  data=User.objects.get(id=id)
  data.is_active=status
  data.save()
  return redirect("/adminMech")


def adminApproveCust(requset):
  id=requset.GET['id']
  status=requset.GET['status']
  data=User.objects.get(id=id)
  data.is_active=status
  data.save()
  return redirect("/adminCust")

def adminReport(request):
  data=Bookings.objects.filter().order_by("-id")
  return render(request,"adminReport.html",{"data":data})

def adminFeedback(request):
  feed=Feedback.objects.filter().order_by("-id")
  return render(request,"adminFeedback.html",{"feed":feed})





def custHome(request):
  
  return render(request,"custHome.html")

def custFindMech(request):
  uid=request.session['id']
  cust=Customer.objects.get(id=uid)

  data=''
  bokid=''

  if request.POST:
    lat=request.POST['lat']
    lon=request.POST['lon']
    if Bookings.objects.filter(customer__id=uid,status="Pending").exists():
      bok=Bookings.objects.get(customer__id=uid,status="Pending")
      bok.lat=lat
      bok.lon=lon
    else:
      bok=Bookings.objects.create(customer = cust, lat = lat , lon = lon )  
      bok.save()
    bokid = bok.id
    l11 = str(float(lat) + 0.05)
    l12 = str(float(lat)-0.05)
    l21 = str(float(lon)+0.05)
    l22 = str(float(lon)-0.05)
    data = Mechanic.objects.filter(
        (Q(lon__gte=l22, lat__gte=l12) | Q(lon__lte=l21, lat__lte=l11)) & Q(user__is_active=1)).order_by("-id")
    
  return render(request,"custFindMech.html",{"data":data,"bokid":bokid})





def custDesc(request):
  uid=request.session['id']

  bid=request.GET['id']
  bokid=request.GET['bokid']
  # review=request.GET['review']
  msg=''
  bok=Bookings.objects.get(id=bokid)
  mech=Mechanic.objects.get(id=bid)
  bok.mechanic=mech
  # bok.review=review
  bok.save()
  # return redirect("/custBookings")

  if request.POST:
    msg="Booking Successfull.."
    desc=request.POST['desc']
    bok.desc=desc
    bok.save()
    # return redirect("/custBookings",{"msg":msg})
  return render(request,"custDesc.html",{"msg":msg})

def custBookings(request):
  uid=request.session['id']
  # msg=''
  # if msg in request.GET:
    # msg="Booking Successfull.."
  feedbacks=Feedback.objects.filter(booking__customer__id=uid).order_by("-id")
  data=Bookings.objects.filter(customer__id=uid).order_by("-id")
  
  return render(request,"custBookings.html",{"data":data})


def custAddReview(request):
  uid=request.session['id']
  bid=request.GET['bid']
  bok=Bookings.objects.get(id=bid)
  msg=''
  
  if request.POST:
    feedback=request.POST['feedback']
    feed=Feedback.objects.create(feedback=feedback,booking=bok)
    feed.save()
    bok.review=1
    bok.save()
    return redirect("/custBookings")

  return render(request,"custAddReview.html")



def custMakePayment(request):
  id=request.GET['id']
  bok=Bookings.objects.get(id=id)
  rate=bok.rate
  
  if request.POST:
    status="Payment Completed"
    bok.status=status
    bok.save()
    return redirect("/custBookings")
  
  return render(request,"custMakePayment.html",{"rate":rate})


def custEmergency(request):
  id=request.session['id']
  amb=SOS.objects.filter(customer__id=id).order_by("-id")
  fire=Fire.objects.filter(customer__id=id).order_by("-id")
  return render(request,"custEmergency.html",{"amb":amb,"fire":fire})


def custAmbulanceMsg(request):
  id=request.session['id']
  cust=Customer.objects.get(id=id)
  msg=''
  if request.POST:
    lat=request.POST['lat']
    lon=request.POST['lon']
    desc=request.POST['desc']
    data=SOS.objects.create(lat=lat,lon=lon,msg=desc,customer=cust)
    data.save()
    msg="Message sent successfully.."
  return render(request,"custAmbulanceMsg.html",{"msg":msg})


def custFireMsg(request):
  id=request.session['id']
  cust=Customer.objects.get(id=id)
  msg=''
  if request.POST:
    lat=request.POST['lat']
    lon=request.POST['lon']
    desc=request.POST['desc']
    data=Fire.objects.create(lat=lat,lon=lon,msg=desc,customer=cust)
    data.save()
    msg="Message sent successfully.."
  return render(request,"custFireMsg.html",{"msg":msg})


def mechHome(request):
  return render(request,"mechHome.html")



def mechViewReq(request):
  id=request.session['id']

  bok=Bookings.objects.filter(mechanic__id=id,status="Pending")

  return render(request,"mechViewReq.html",{"bok":bok})


def mechApproveReq(request):
  id=request.GET['id']
  status=request.GET['status']
  bok=Bookings.objects.get(id=id)
  if status == "Approved":
    bok.status="Approved"
    bok.save()
    return redirect("/mechViewBok")
  else:
    bok.status="Rejected"
    bok.save()
    return render(request,"mechApproveReq.html")


  

def mechViewBok(request):
  id=request.session['id']
  bok=Bookings.objects.filter(Q(mechanic__id=id) & Q(status="Approved") | Q(status="Completed") | Q(status="Payment_Pending") |Q(status="Payment Completed") ).order_by("-id")
  return render(request,"mechViewBok.html",{"bok":bok})


def mechCompleted(request):
  id=request.GET['id']
  status=request.GET['status']
  bok=Bookings.objects.get(id=id)
  if status == "Completed":
    bok.status=status
    bok.save()
    return redirect("/mechViewBok")
  elif status == "Payment_Pending":
    bok.status=status
    bok.save()
    return redirect(f"/mechAddPay?id={id}")  
    
  

def mechAddPay(request):
  id=request.GET['id']
  bok=Bookings.objects.get(id=id)
  if request.POST:
   rate=request.POST['rate']
  #  desc=request.POST['desc']
   bok.rate=rate
  #  bok.desc=desc
   bok.save()
   return redirect("/mechViewBok")
  return render(request,"mechAddPay.html")





def ambulanceHome(request):
 return render(request,"ambulanceHome.html")

def ambulanceNotification(request):
  sos=SOS.objects.all().order_by("-id")
  return render(request,"ambulanceNotification.html",{"sos":sos})







def fireFighterHome(request):
 
 return render(request,"fireFighterHome.html")


def fireNotification(request):
  fire=Fire.objects.all().order_by("-id")
  return render(request,"fireNotification.html",{"fire":fire})

