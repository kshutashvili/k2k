from collections import defaultdict

from info.models import Contact


def contacts(request):
    items = defaultdict(list)
    for c in Contact.objects.actual():
        items[c.type].append(c)
    return {'contacts': items}
