from hackathon.models import Hackathon
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from home.models import Cart
from submission.models import DataSubmission


def create(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        bg_img = request.FILES['bg_img']
        hack_img = request.FILES['hack_img']
        sub_typ = request.POST.get('sub_typ')
        start = request.POST.get('start')
        end = request.POST.get('end')
        reward = request.POST.get('reward')
        prize = request.POST.get('prize')

        Hackathon.objects.create(title=title, desc=desc, sub_typ=sub_typ,
                                 start=start, end=end, reward=reward, prize=prize)

        with open('static/'+title+'_bg_img.jpg', 'wb') as destination:
            for chunk in bg_img.chunks():
                destination.write(chunk)

        with open('static/'+title+'_hack_img.jpg', 'wb') as destination:
            for chunk in hack_img.chunks():
                destination.write(chunk)

        return redirect('hackathons')

    return render(request, 'create.html')


def hackathons(request):

    hacks = []
    query = Hackathon.objects.all()

    for hack in query:
        if not Cart.objects.filter(user=request.user, hackathon=hack):
            hacks.append(hack)

    return render(request, 'hackathons.html', {'hackathons': hacks})


@login_required
def register_hack(request, hack_id):
    hackathon = get_object_or_404(Hackathon, pk=hack_id)
    cart, created = Cart.objects.get_or_create(user=request.user, hackathon=hackathon)
    if not created:
        cart.save()
    return redirect('hackathons')


@login_required
def my_hackathons(request):
    cart = Cart.objects.filter(user=request.user)

    hacks = []
    for v in cart:
        hack = Hackathon.objects.filter(id=v.hackathon_id).first()
        if DataSubmission.objects.filter(owner=request.user, hack=hack):
            hack.sub_typ = ''
        hacks.append(hack)

    return render(request, 'registered_hacks.html', {'hackathons': hacks})
