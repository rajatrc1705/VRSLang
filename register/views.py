from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout 


def register_request(request):
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration Successful')
            return redirect('/login')
        query_dict = request.POST
        password1 = query_dict['password1']
        password2 = query_dict['password2']
        language = query_dict['language']
        if language == '':
            messages.error(request, 'Fill in a preferred language')
        elif len(password1) < 8:
            messages.error(request, 'Password length should be more than 8')
        elif password1.isdecimal():
            messages.error(request, 'Password Should not be entirely numeric')
        else:            
            messages.error(request, "Password is Too Common OR Password is Too similar to Username")
    form = NewUserForm
    return render(request, 'mysite/register.html', {'form': form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, template_name="mysite/login.html", context={'form':form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('/login')