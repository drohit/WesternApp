from django.shortcuts import render, render_to_response
from django.template import RequestContext
from Person.forms import RegistrationForm
from django.contrib.auth.models import User
from Person.models import Person
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def logout_request(request):
	logout(request)
	return HttpResponseRedirect('/')
def homepage(request):
	return render(request, "index.html")

def intro(request):
	return render(request, "index2.html")	

def residence_choice(request):
	residencename = Residence.objects.all()
	rname =	request.POST.get('dropdown1')
	if request.method == 'GET':
		form = ResidenceForm()

def signup(request):
	if request.method == 'POST': #User giving us data
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user_email = form.cleaned_data['email']
			user = User.objects.create_user(first_name=form.cleaned_data['name'],
											username=user_email,
											email=user_email,
											password=form.cleaned_data['password']
				)
			user.save()

			person = Person(user=user,
							name=form.cleaned_data['name'],
							email=user_email,
				)
			person.save()
			return HttpResponseRedirect('/home')


	form = RegistrationForm()
	return render_to_response("signup.html", {'form': form}, context_instance=RequestContext(request))



