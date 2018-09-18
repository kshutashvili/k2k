from django.shortcuts import render

from info.models import (
    LandingTab, Question, MainBlock, FooterMenuBlock1Credit,
    FooterMenuBlock2Credit, FooterMenuBlock3Credit, Privileges)
from info.forms import QuestionForm


def landing(request):
    question_form = QuestionForm(request.POST)
    tabs = LandingTab.objects.actual().select_related('content')
    main_block = MainBlock.objects.filter(page='credit')
    questions = Question.objects.answered().filter(theme='credit')
    fmenu1 = FooterMenuBlock1Credit.objects.actual().select_related('content')
    fmenu2 = FooterMenuBlock2Credit.objects.actual().select_related('content')
    fmenu3 = FooterMenuBlock3Credit.objects.actual().select_related('content')
    privileges = Privileges.objects.filter(page='credit', draft=False)
    context = {
        'questions': questions,
        'question_form': question_form,
        'tabs': tabs,
        'main_block': main_block,
        'footer_menu1': fmenu1,
        'footer_menu2': fmenu2,
        'footer_menu3': fmenu3,
        'privileges': privileges
    }
    return render(request, 'main/landing.html', context)


def credit_page(request):
    tabs = LandingTab.objects.actual().select_related('content')
    fmenu1 = FooterMenuBlock1Credit.objects.actual().select_related('content')
    fmenu2 = FooterMenuBlock2Credit.objects.actual().select_related('content')
    fmenu3 = FooterMenuBlock3Credit.objects.actual().select_related('content')
    context = {
        'tabs': tabs,
        'footer_menu1': fmenu1,
        'footer_menu2': fmenu2,
        'footer_menu3': fmenu3
    }
    return render(request, 'main/credit_page.html', context)
