from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print(f'{name} {email} {message}')
    return render(request, 'catalog/index.html')


def contact(request):
    return render(request, 'catalog/contacts.html')


def trevor(request):
    return render(request, 'catalog/newtab/trevor.html')


def base(request):
    return render(request, 'catalog/newtab/base.html')


def artur(request):
    return render(request, 'catalog/newtab/artur.html')


def artur_two(request):
    return render(request, 'catalog/newtab/artur_two.html')