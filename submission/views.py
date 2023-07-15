from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from hackathon.models import Hackathon
from submission.models import DataSubmission


@login_required
def submit_data(request, hack_id):

    hack = Hackathon.objects.filter(pk=hack_id).first()
    sub_typ = hack.sub_typ

    if request.method == 'POST':
        name = request.POST.get('name')
        summ = request.POST.get('summ')
        data = request.POST.get(sub_typ)

        if sub_typ == 'link':
            DataSubmission.objects.create(name=name, summ=summ, link=data, owner=request.user, hack=hack)
        elif sub_typ == 'img':
            DataSubmission.objects.create(name=name, summ=summ, image=data, owner=request.user, hack=hack)
        elif sub_typ == 'file':
            DataSubmission.objects.create(name=name, summ=summ, file=data, owner=request.user, hack=hack)

        return redirect('view_submissions')

    return render(request, 'submit_data.html', {'sub_typ': sub_typ})


@login_required
def view_submissions(request):

    submissions = DataSubmission.objects.all().values()
    for i in range(len(submissions)):
        submissions[i]['hack_name'] = Hackathon.objects.get(pk=submissions[i]['hack_id']).title

    return render(request, 'view_submissions.html', {'submissions': submissions})
