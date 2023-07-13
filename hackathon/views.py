from hackathon.models import Hackathon
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from home.models import Cart


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

        with open('create/static/'+title+'_bg_img.jpg', 'wb') as destination:
            for chunk in bg_img.chunks():
                destination.write(chunk)

        with open('create/static/'+title+'_hack_img.jpg', 'wb') as destination:
            for chunk in hack_img.chunks():
                destination.write(chunk)

        return redirect('hackathons')

    return render(request, 'create.html')


def hackathons(request):

    context = {
        'hackathons': Hackathon.objects.all().values()
    }
    return render(request, 'hackathons.html', context)


@login_required(login_url='login/')
def register_hack(request, hack_id):
    hackathon = get_object_or_404(Hackathon, pk=hack_id)
    cart, created = Cart.objects.get_or_create(user=request.user, hackathon=hackathon)
    if not created:
        cart.save()
    return redirect('hackathons')


@login_required(login_url='login/')
def cart_view(request):
    cart = Cart.objects.filter(user=request.user)

    hacks = []
    for v in cart:
        hack = Hackathon.objects.filter(id=v.hackathon_id).first()
        hacks.append(hack)

    return render(request, 'registered_hacks.html', {'hackathons': hacks})
