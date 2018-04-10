from django.shortcuts import render, redirect

from info.models import (
    LandingTab, Question, MainBlock, FooterMenuBlock1Credit,
    FooterMenuBlock2Credit, FooterMenuBlock3Credit)
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
    main_block = MainBlock.objects.filter(page='credit')
    questions = Question.objects.answered().filter(theme='credit')
    footer_menu1 = FooterMenuBlock1Credit.objects.actual().select_related('content')
    footer_menu2 = FooterMenuBlock2Credit.objects.actual().select_related('content')
    footer_menu3 = FooterMenuBlock3Credit.objects.actual().select_related('content')
    context = {
        'questions': questions,
        'question_form': question_form,
        'tabs': tabs,
        'main_block': main_block,
        'footer_menu1': footer_menu1,
        'footer_menu2': footer_menu2,
        'footer_menu3': footer_menu2
        }
    return render(request, 'main/landing.html', context)


def credit_page(request):
    tabs = LandingTab.objects.actual().select_related('content')
    footer_menu1 = FooterMenuBlock1Credit.objects.actual().select_related('content')
    footer_menu2 = FooterMenuBlock2Credit.objects.actual().select_related('content')
    footer_menu3 = FooterMenuBlock3Credit.objects.actual().select_related('content')
    context = {
        'tabs': tabs,
        'footer_menu1': footer_menu1,
        'footer_menu2': footer_menu2,
        'footer_menu3': footer_menu2
        }
    return render(request, 'main/credit_page.html', context)