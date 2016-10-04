from django.shortcuts import render, redirect

from info.models import LandingTab, Question


def landing(request):
    if request.user.is_authenticated():
        # We need this redirect while we have no landing.
        return redirect('transfer')
    tabs = LandingTab.objects.actual().select_related('content')
    questions = Question.objects.answered()
    return render(request, 'main/landing.html', {'tabs': tabs,
                                                 'questions': questions})
