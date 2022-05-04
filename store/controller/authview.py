from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User

from store.forms import CustomUserForm
from store.models import Customer


def register(request):
    form = CustomUserForm()

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()

            customer, created = Customer.objects.get_or_create(
                email=request.POST.get('email'),
            )
            customer.name = request.POST.get('name')
            customer.save()


            messages.success(request, "Correco Registro..!! Iniciar Sesión para continuar")
            return redirect('/login')

    context = {'form': form}
    return render(request, "store/auth/register.html", context)


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect('/')

    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or Password")
                return redirect('/login')
        return render(request, "store/auth/login.html")


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Succesfully")
    return redirect('/')