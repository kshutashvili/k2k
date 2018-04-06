from django.shortcuts import render, get_object_or_404, redirect

from info.models import Flatpage
from info.forms import QuestionForm


def flatpage(request, slug):
    kwargs = {'slug': slug}
    if not (request.user.is_authenticated()
            and request.user.has_perm('info.change_flatpage')):
        kwargs['is_draft'] = False
    page = get_object_or_404(Flatpage, **kwargs)
    return render(request, 'info/flatpage.html', {'page': page})


def ask_question(request):
    form = QuestionForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('landing')
    context = {'question_form': form}
    return render(request, 'info/question_form.html', context)


