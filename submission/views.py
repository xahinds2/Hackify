from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from hackathon.models import Hackathon
from submission.models import DataSubmission


@login_required
def submit_data(request, hack_id):

    if request.method == 'POST':
        name = request.POST.get('name')
        summ = request.POST.get('summ')
        link = request.POST.get('link')
        file = request.POST.get('file')
        image = request.POST.get('image')
        hack = Hackathon.objects.filter(pk=hack_id).first()

        if DataSubmission.objects.filter(owner=request.user, hack=hack):
            return render(request, 'submit_data.html')

        if link:
            DataSubmission.objects.create(name=name, summ=summ, link=link, owner=request.user, hack=hack)
        elif image:
            DataSubmission.objects.create(name=name, summ=summ, image=image, owner=request.user, hack=hack)
        elif file:
            DataSubmission.objects.create(name=name, summ=summ, file=file, owner=request.user, hack=hack)

    return render(request, 'submit_data.html')


def view_submissions(request):
    submissions = DataSubmission.objects.all().values()
    print(submissions)
    return render(request, 'view_submissions.html', {'submissions': submissions})
