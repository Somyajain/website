from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render,redirect,render_to_response
from app.models import Recent_events,Teacher
from app.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.core.mail import send_mail



#erp_page,contact_page,register_page,events_page,projects_page,results_page

def home_page(request):
    t = get_template('index.html')
    html = t.render(Context())
    return HttpResponse(html)

def events_page(request):
   
    events = Recent_events.objects.all().order_by('-date')
    
    
    return render_to_response("events.html", {"events": events})
def overview_page(request):
    t = get_template('overview.html')
    html = t.render(Context())
    return HttpResponse(html)
def mission_page(request):
    t = get_template('mission.html')
    html = t.render(Context())
    return HttpResponse(html)
def vision_page(request):
    t = get_template('vision.html')
    html = t.render(Context())
    return HttpResponse(html)
def gallery_page(request):
    t = get_template('gallery.html')
    html = t.render(Context())
    return HttpResponse(html)
def family_page(request):
    teacher = Teacher.objects.all().order_by('-date')
    return render_to_response("family.html", {"teacher": teacher})
    
def admissions_page(request):
    t = get_template('admissions.html')
    html = t.render(Context())
    return HttpResponse(html)

def contact_page(request):

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['somyajain131@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
    return render(request, "contact.html", {'form': form})






'''
def erp_page(request):
    t = get_template('base.html')
    html = t.render(Context())
    return HttpResponse(html)

def family_page(request):
    t = get_template('navbar.html')
    html = t.render(Context())
    return HttpResponse(html)

def admissions_page(request):
    t = get_template('main.html')
    html = t.render(Context())
    return HttpResponse(html)
'''
