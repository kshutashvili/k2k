from django.shortcuts import render, get_object_or_404

from info.models import Flatpage


def flatpage(request, slug):
    kwargs = {'slug': slug}
    if not (request.user.is_authenticated()
            and request.user.has_perm('info.change_flatpage')):
        kwargs['is_draft'] = False
    page = get_object_or_404(Flatpage, **kwargs)
    return render(request, 'info/flatpage.html', {'page': page})
