from django.shortcuts import render, HttpResponse,redirect
from .forms import UserForm
from .models import User
from django.contrib import messages

def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']#getting raw password
            user = form.save(commit=False) #commit assigns data to user and ready to be saved.
            user.set_password(password) #setting hashed password
            user.role = User.CUSTOMER
            user.save()
            messages.success(request,"Succesfully Registered !")
            return redirect('registerUser')
    else:
        form = UserForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/registerUser.html',context)

