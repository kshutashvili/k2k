from django.shortcuts import render, get_object_or_404

from info.models import Flatpage


def flatpage(request, slug):
    page = get_object_or_404(Flatpage, slug=slug, is_draft=False)
    return render(request, 'info/flatpage.html', {'page': page})
