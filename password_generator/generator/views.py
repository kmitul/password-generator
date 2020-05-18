from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    pwd = ''
    gen_string = list('qwertyuiopasdfghjklzxcvbnm')

    length = int(request.GET.get('length'))

    if request.GET.get('specialchar'):
        gen_string.extend(list('@#$%^&*~?/!'))
    if request.GET.get('numbers'):
        gen_string.extend(list('1234567890'))
    if request.GET.get('uppercase'):
        gen_string.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    for _ in range(length):
        pwd+= random.choice(gen_string)

    mydict = {'password':pwd}

    return render(request, 'generator/password.html', mydict)
