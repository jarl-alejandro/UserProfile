from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from .forms import UserCreationForm, EmailAuthenticationForm

class IndexView(TemplateView):
	template_name = "index.html"

class AppView(TemplateView):
	template_name = "app.html"

	@method_decorator(login_required(login_url = "/login/"))
	def dispatch(self, request, *args, **kwargs):
	    return super(AppView, self).dispatch(request, *args, **kwargs)


def log_out(request):
	logout(request)
	return redirect("/")

def log_in(request):
	if request.method == "POST":
		form = EmailAuthenticationForm(request.POST)
		if form.is_valid():
			login(request, form.get_user())

		if request.user.is_authenticated():
			return redirect("/app/")
	else:
		form = EmailAuthenticationForm()
	return render(request, "login.html", { "form":form })

def registrate(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			email = request.POST["email"]
			password = request.POST["password1"]

			user = authenticate(email=email, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect("/app/")
				else:
					return HttpResponse("Usuario inactivo")
			else:
				return HttpResponse("Usuario incorrecto")
	else:
		form = UserCreationForm()
	return render(request, "registrate.html", { "form":form })