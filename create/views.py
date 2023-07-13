from django.shortcuts import render, redirect
from create.models import Hackathon


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
