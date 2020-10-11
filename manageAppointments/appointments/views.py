from django.shortcuts import render, redirect  
from appointments.forms import AppointForm  
from appointments.models import Appointments
from . import forms
from django.core.mail import send_mail


#function request form
def appform(request):  
    if request.method == "POST":  
        form = AppointForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = AppointForm()  
    return render(request,'app_form.html',{'form':form}) 

#function to display the dashboard
def show(request):  
    appointments = Appointments.objects.all()  
    return render(request,'dashboard.html',{'appointments':appointments}) 

#function to edit record
def edit(request, id):  
    appointment = Appointments.objects.get(id=id)  
    return render(request,'edit.html',{'appointment':appointment})  

#function  to update record
def update(request, id):  
    appointment = Appointments.objects.get(id=id)   
    form = AppointForm(request.POST, instance = appointment)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'appointment':appointment}) 

#function to delete record
def destroy(request, id):  
    appointment = Appointments.objects.get(id=id)  
    appointment.delete()  
    return redirect("/show")  

#function to call calender
def calender(request):
    return render(request, 'calender.html')

#function to watch the full report

def fullreport(request , id):
     appointment = Appointments.objects.get(id=id)  
     return render(request,'report.html',{'appointment':appointment})

#function to analyse full records
def fullrecords(request, id):
    appointments = Appointments.objects.all()  
    return render(request,'fullrecords.html',{'appointments':appointments})
    
#function to send emails
def sendmail(request, id):
    appointment = Appointments.objects.get(id=id)
    #send email
    send_mail(
    'About the appointment',
    'Dear Sir/Madam,Here is the summary of your appointment.  Venue' + appointment.Ap_Venue + 'Purpose' + appointment.Ap_Purpose + 'Extra Notes' + appointment.Ap_Notes,
    'shashibandarass@gmail.com',
    [appointment.Ap_Cus_email],
    fail_silently=False,
    )
    return render(request,'fullrecords.html')
    