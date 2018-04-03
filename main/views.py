from django.shortcuts import render, redirect

from info.models import LandingTab, Question
from users.forms import ContactVerificationForm

# def landing(request):
#     if request.user.is_authenticated():
#         # We need this redirect while we have no landing.
#         return redirect('transfer')
#     tabs = LandingTab.objects.actual().select_related('content')
#     questions = Question.objects.answered()
#     return render(request, 'main/landing.html', {'tabs': tabs,
#                                                  'questions': questions})

def landing(request):
    return render(request, 'main/landing.html', {})


def credit_page(request):
    return render(request, 'main/credit_page.html', {})