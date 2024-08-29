from django.shortcuts import render
from .models import User


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.get(username=username)

        if user:
            if user.password == password:
                if user.is_ldap_user:
                    # input LDAP authentication
                    pass
                else:
                    # authentication code here
                    pass
            else:
                return render(request, 'login.html', {'error': 'invalid password'})
        else:
            return render(request, 'login.html', {'error': 'User not found'})

    return render(request, 'login.html')


def change_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')

        user = User.objects.get(username=username)

        if user:
            if user.password == old_password:
                user.password = new_password
                user.save()
                return render(request, 'change_password.html', {'message': 'Password changed successfully'})
            else:
                return render(request, 'change_password.html', {'error': 'Invalid password'})
        else:
            return render(request, 'change_password.html', {'error': 'User not found'})
    return render(request, 'change_password.html')
