from create.models import Hackathon
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from users.models import Cart
from django.urls import reverse


def hackathons(request):

    if request.method == 'GET':
        hack_id = request.POST
        url = reverse('register_hack') + '?hack_id='
        # return redirect(url)

    context = {
        'hackathons': Hackathon.objects.all().values()
    }
    return render(request, 'hackathons.html', context)


def register_hack(request, hack_id):
    hackathon = get_object_or_404(Hackathon, pk=hack_id)
    # cart, created = Cart.objects.get_or_create(user=request.user, hackathon=hackathon)
    print(request.user)
    # if not created:
    #     cart.save()
    return redirect('hackathons')
