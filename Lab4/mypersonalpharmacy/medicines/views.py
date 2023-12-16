from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic import TemplateView

from .models import *
from .forms import *

import random
import requests
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


class Certificate(TemplateView):
    template_name = 'medicines/certificate.html'


class Lab3js(TemplateView):
    template_name = 'medicines/lab3js.html'


class Lab2css(TemplateView):
    template_name = 'medicines/lab2css.html'


class Task9(TemplateView):
    template_name = 'medicines/task9.html'


class Task10_1(TemplateView):
    template_name = 'medicines/task10_1.html'


class Task10_2(TemplateView):
    template_name = 'medicines/task10_2.html'


class Task11(TemplateView):
    template_name = 'medicines/task11.html'


class Employees(ListView):
    model = Employee
    template_name = 'medicines/employees.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Employee.objects.all()


class Coupons(ListView):
    model = Coupon
    template_name = 'medicines/coupons.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Coupon.objects.all()


class FAQs(ListView):
    model = FAQ
    template_name = 'medicines/faqs.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return FAQ.objects.all()


class Vacancies(ListView):
    model = Vacancy
    template_name = 'medicines/vacancies.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Vacancy.objects.all()


class SxNews(TemplateView):
    template_name = 'medicines/sx_news.html'


class InNews(TemplateView):
    template_name = 'medicines/in_news.html'


class PrivacyPolicy(TemplateView):
    template_name = 'medicines/privacy_policy.html'


class Newsv(ListView):
    model = News
    template_name = 'medicines/news.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return News.objects.all()


class Company(TemplateView):
    template_name = 'medicines/company.html'


class Main(ListView):
    model = News
    template_name = 'medicines/main.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return News.objects.all()


class MedList(ListView):
    model = Medication
    template_name = 'medicines/med_list.html'
    context_object_name = 'posts'
    ordering = ('title',)


class Pharmacies(ListView):
    model = Department
    template_name = 'medicines/pharms.html'
    context_object_name = 'posts'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class NoAvailable(ListView):
    model = Sale
    template_name = 'medicines/no_avail.html'
    context_object_name = 'posts'
    ordering = ('medication', )


def home(request):
    return render(request, "medicines/home.html")


def test(request):
    response = requests.get('https://cat-fact.herokuapp.com/facts')
    facts = response.json()

    random_fact = None
    if facts:
        random_fact = random.choice(facts)
        if 'source' not in random_fact:
            random_fact['source'] = 'Unknown'
    data = {
        'title': 'Домашняя страница',
        'random_fact': random_fact,
    }
    return render(request, 'medicines/test.html', data)


def about(request):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    image_url = response.json()['message']
    context = {
        'title': 'Мы Вас любим',
        'image_url': image_url,
    }
    return render(request, 'medicines/about.html', context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Мы не нашли страницу, которую вы искали :( </h1><p>Попробуйте перепроверить поисковый запрос.</p>")


def bying(request, bying_id):
    purchase = Medication.objects.get(pk=bying_id)
    promocode = Promocode.objects.order_by('title')

    return render(request, 'medicines/bying.html', {'title': 'Покупка', 'purchase': purchase, 'promocode': promocode})


def thanks(request, thanks_id):
    posts = Sale.objects.order_by('medication')
    purchase = Medication.objects.get(pk=thanks_id)
    saled = Sale.objects.all()
    if purchase.quantity == 0:
        purchase.is_available = False
        return render(request, 'medicines/no_avail.html', {'posts': posts, 'title': 'Не куплено'})
    for el in saled:
        if el.medication == purchase:
            el.quantity += 1
            purchase.quantity -= 1
            if purchase.quantity == 0:
                purchase.is_available = False
            el.save()
            purchase.save()
    return render(request, 'medicines/thanks.html', {'posts': posts, 'title': 'Куплено'})


class FeedBackForm(CreateView):
    form_class = FeedBackForm
    template_name = 'medicines/feedback_form.html'
    success_url = reverse_lazy('feedback_view')
    login_url = reverse_lazy('register')
    raise_exception = True

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class FeedBackView(ListView):
    model = FeedBack
    template_name = 'medicines/feedback_view.html'

    def get_queryset(self):
        return FeedBack.objects.all()