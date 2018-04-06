from django.shortcuts import render, redirect

from info.models import LandingTab, Question
from info.forms import QuestionForm
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
    question_form = QuestionForm(request.POST)
    tabs = LandingTab.objects.actual().select_related('content')
    questions = Question.objects.answered().filter(theme='credit')
    context = {
        'questions': questions,
        'question_form': question_form,
        'tabs': tabs
        }
    return render(request, 'main/landing.html', context)


def credit_page(request):
    tabs = LandingTab.objects.actual().select_related('content')
    return render(request, 'main/credit_page.html', {'tabs': tabs})