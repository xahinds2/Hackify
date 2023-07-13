from django.shortcuts import render
from create.models import Hackathon


def show(request):
    context = {
        'hackathons': Hackathon.objects.all().values()
    }
    return render(request, 'hackathons.html', context)
