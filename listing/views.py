from create.models import Hackathon
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from users.models import Cart


def hackathons(request):

    context = {
        'hackathons': Hackathon.objects.all().values()
    }
    return render(request, 'hackathons.html', context)


@login_required
def register_hack(request, hack_id):
    hackathon = get_object_or_404(Hackathon, pk=hack_id)
    cart, created = Cart.objects.get_or_create(user=request.user, hackathon=hackathon)
    if not created:
        cart.save()
    return redirect('hackathons')


@login_required
def cart_view(request):
    cart = Cart.objects.filter(user=request.user)

    hacks = []
    for v in cart:
        hack = Hackathon.objects.filter(id=v.hackathon_id).first()
        hacks.append(hack)

    return render(request, 'registered_hacks.html', {'hackathons': hacks})
