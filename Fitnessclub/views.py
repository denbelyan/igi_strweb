import calendar

from dateutil.tz import tzlocal
from django.shortcuts import render, redirect
from .models import Employee, Service, Card, Schedule, Hall, WorkVakansiya, feedback, promocodes
from .forms import LoginForm, SignupForm, CardForm, ClientForm, Hallform, feedbackForm
from django.contrib.auth import login
import requests
import logging
from django.utils import timezone
import plotly.express as px
from datetime import timezone, datetime, timedelta
import pytz
from tzlocal import get_localzone



def current_date_view(request):
    tz = get_localzone()
    local_time = datetime.now(tz)
    now_time = datetime.now(tz)
    utc_time = datetime.now(tz = pytz.timezone('UTC'))
    text_cal = calendar.month(local_time.year, local_time.month)
    context = {
        'user_timezone': tz,
        'current_date_formated': now_time.strftime("%m-%d-%Y %H: %M: %S %Z"),
        'calendar_text': text_cal, 'utc_time': utc_time.strftime("%m-%d-%Y %H: %M: %S %Z"),
    }
    return render(request, 'calendar.html', context)

def plot_view(request):
    data = [
        {'label': '20.05.2024', 'value': '10'},
        {'label': '21.05.2024', 'value': '15'},
        {'label': '22.05.2024', 'value': '25'},
        {'label': '23.05.2024', 'value': '45'}
    ]
    fig = px.pie(data, values='value', names='label')
    plot_div = fig.to_html()
    context = {'plot_div': plot_div}
    return render(request, 'plot.html', context)

def plot_clients_view(request):
    data = [
        {'label': '20.05.2024', 'value': 'clients.FirstLogIn("20:05:2024'},
        {'label': '21.05.2024', 'value': 'clients.FirstLogIn("21:05:2024'},
        {'label': '22.05.2024', 'value': 'clients.FirstLogIn("22:05:2024'},
        {'label': '23.05.2024', 'value': 'clients.FirstLogIn("23:05:2024'}
    ]
    fig = px.pie(data, values='value', names='label')
    plot_div_clients = fig.to_html()
    context = {'plot_div_clients': plot_div_clients}
    return render(request, 'plot.html', context)


def home(request):

    logging.info("BACK TO HOME PAGE")
    return render(request, 'home.html')



def about_us(request):
    logging.debug("auto_generated_info")
    response = requests.get('https://api.chucknorris.io/jokes/random').json()
    context = {'response': response}
    return render(request, 'about_us.html', context)


# view

def privacy_policy(request):
    return render(request, 'privacy_policy.html')
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


def employees_info(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    return render(request, 'employees_info.html', {'employee': employee})


def hall_list(request):
    halls = Hall.objects.all()
    return render(request, 'halls_list.html', {'halls': halls})


def hall_add(request):
    if request.method == 'POST':
        form = Hallform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Hallform()

    context = {'form': form}
    return render(request, 'halls_add.html', context)


def card_list(request):
    cards = Card.objects.all()
    return render(request, 'card_list.html', {'cards': cards})


def service_list(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'service_list.html', context)


# detail
def card_detail(request, card_id):
    card = Card.objects.get(pk=card_id)
    return render(request, 'card_detail.html', {'card': card})


# signup
def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context, )


# crud operations
def create_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CardForm()

    context = {'form': form}
    return render(request, 'create_card.html', context)


def update_card(request, card_id):
    card = Card.objects.get(id=card_id)
    halls = Hall.objects.all()
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('card_detail', package_id=card_id)
    else:
        form = CardForm(instance=card)

    context = {'form': form, 'card': card, 'halls': halls}
    return render(request, 'update_card.html', context)

def delete_card(request, card_id):
    card = Card.objects.get(id=card_id)
    if request.method == 'POST':
        card.delete()
        return redirect('home')

    return redirect('card_list')


# order
def create_service(request, card_id):
    card = Card.objects.get(id=card_id)

    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client = client_form.save()
            service = Service.objects.create(client=client, package=card)
            return redirect('card_detail', package_id=card_id)
    else:
        client_form = ClientForm()

    context = {'client_form': client_form, 'card': card}
    return render(request, 'create_service.html', context)


def service_detail(request, service_id):
    service = Service.objects.get(id=service_id)
    context = {'service': service}
    return render(request, 'service_detail.html', context)

def NewsView(request):
    return render(request, template_name = 'news.html')

def NewsReadView(request):
    return render(request, template_name='news_read.html')

def news_read1(request):
    return render(request, template_name='news1.html')

def news_read2(request):
    return render(request, template_name='news2.html')

def faq_view(request):
    return render(request, template_name='FAQ.html')


def WorkView(request):
    works = WorkVakansiya.objects.all()
    context = {'work': works}
    return render(request, 'Work.html', context)

def feedback_view(request):
    feedbacks = feedback.objects.all()
    return render(request, 'feedback.html', {'feedback': feedbacks})

def feedback_add_view(request):
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = feedbackForm()

    context = {'feedbackForm': form}
    return render(request, 'feedback_add.html', context)

def promocode_view(request):
    promocode = promocodes.objects.all()
    context = {'prom': promocode}
    return render(request, 'Promocodes.html', context)

def mediaview(request):
    return render(request, 'home.html')