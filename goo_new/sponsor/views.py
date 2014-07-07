from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import AuthKey, Sponsor
from .forms import LoginForm
from .helpers import check_password


def payment(request):

    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "10.00",
        "item_name": "Goo.IM Sponsor Account",
        "notify_url": "https://www.goo.im" + reverse('paypal-ipn'),
        "return_url": "https://www.goo.im/confirmation",
        "cancel_return": "https://www.goo.im/sponsorcancel",
    } 
	
    # Create Form Instance
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render_to_response("sponsor_payment.html", context)

def signup(request):

    if request.method == "GET":
        if 'token' in request.GET:
            token = request.GET.get('token')

            try:
                auth_key = AuthKey.objects.get(token=token)
            except:
                messages.error(request, 'Auth Key Not Valid')
                return HttpResponseRedirect(request.path)

            request.session['auth_key'] = auth_key		
            return HttpResponseRedirect('complete_sponsor_signup')
		
def complete_signup(request):

    if request.method == "GET":
        if not 'auth_key' in request.session:
            messages.error(request, 'Did not receive auth key.  Please check that cookies are enabled and re-enter your auth key.')
            return HttpResponseRedirect('start_sponsor_signup')
        else:
            auth_key = request.session['auth_key']
            form = SignupForm({'auth_key': auth_key})
			

def login_view(request):

    if request.method == "GET":
        if 'sponsor' in request.session:
            return render(request, "sponsor/alreadyloggedin.html")

        form = LoginForm
        d = {"form": form}
        return render(request, "sponsor/login.html", d)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                sponsor = Sponsor.objects.get(username=username)
            except Sponsor.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'Username or Password not recognized.', extra_tags="danger")
                return HttpResponseRedirect(request.path)

            salt = sponsor.salt

            if sponsor.migrated:
                pw_correct = check_password(username, password, salt)
            else:
                pw_correct = check_password(username, password,  old=True)

          
            if pw_correct:
                request.session['sponsor'] = username
                return redirect('index')

            messages.add_message(request, messages.ERROR, 'Username or Password not recognized.', extra_tags="danger")
            return HttpResponseRedirect(request.path)

def logout_view(request):
    
    if 'sponsor' in request.session:
        del request.session['sponsor']

    return redirect('index')
