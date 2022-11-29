from django.shortcuts import render,redirect,HttpResponse
from .models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('inbox')
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password')
        if " " in full_name:
            first_name = full_name.split(' ')[0]
            last_name = full_name.split(' ')[1]
        else:
            first_name = full_name
            last_name = ""
        user = User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email)
        user.set_password(password)
        user.username_edit = True
        user.save()
        
        user = authenticate(
            username=email,
            password=password,
        )
        if user is not None:
            login(request, user)
            return redirect('inbox')
    return render(request, 'accounts/register.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('inbox')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(
            username=email,
            password=password,
        )
        print(user)
        if user is not None:
            login(request,user)
            return redirect('inbox')
        else:
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

# @login_required(login_url='/login/')
def logoutPage(request):
    logout(request)
    return HttpResponse("Logout")

def profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.id)
        if user.username_edit:
            if request.method == 'POST':
                username = request.POST.get('username')
                if request.FILES:
                    image = request.FILES['image']
                else:
                    image = None
                user.username = username
                user.image = image
                user.username_edit = False
                user.save()
                return redirect('inbox')
            return render(request, 'accounts/profile.html',{"user":user})
        else:
            return redirect('inbox')            
    else:
        return redirect('login')