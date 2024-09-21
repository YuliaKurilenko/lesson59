from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from task1.forms import UserRegister
from django.http import HttpResponse

def menu_page(request):
    return render(request,'menu.html')


def shop_page(request):
    # clothes = ['Футбоки', 'Джинсы', 'Кроссовки ', 'Кофты']
    # context = {
    #     'clothes': clothes
    # }
    # return render(request, 'shop_page.html', context)
    list_games = Game.objects.all()
    context = {'list_games': list_games}
    return render(request, 'shop_page.html', context)

def bin_page(request):
    cont = 'Продолжить покупки'
    done = 'Оформить заказ'
    context = {
        'cont': cont,
        'done': done,

    }
    return render(request, 'bin_page.html', context)


def buyers_list():
    result = []
    all_buyers = Buyer.objects.all()
    for buyer in all_buyers:
        result.append(buyer.name)
    return result


def check_errors(username, password, repeat_password, age):
    result = None
    if password != repeat_password:
        result = 'Пароли не совпадают!'
    elif int(age) < 18:
        result = 'Вам должно быть не меньше 18 лет!'
    elif username in buyers_list():
        result = 'Пользователь уже существует!'
    return result


def sign_up_by_html(request):
    representation = 'HTML'
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        error = check_errors(username, password, repeat_password, age)
        if not error:
            Buyer.objects.create(name=username, balance='0.00', age=age)
            return HttpResponse(f'<center><h2 style=color:Green>Приветствуем, {username}!</h2></center>')
    info = {'representation': representation, 'error': error}
    return render(request, 'registration_page.html', info)



def sign_up_by_django(request):
    representation = 'Django'
    error = None
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            error = check_errors(username, password, repeat_password, age)
            if not error:
                Buyer.objects.create(name=username, balance='0.00', age=age)
                return HttpResponse(f'<center><h2 style=color:Green>Приветствуем, {username}!</h2></center>')
    else:
        form = UserRegister()
    info = {'representation': representation, 'error': error, 'form': form}
    return render(request, 'registration_page.html', info)