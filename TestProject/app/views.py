from django.shortcuts import render
from app.models import User


def show_user(request, user):
    return render(request,
                  "info_users.html",
                  context={'user': User.objects.get(first_name=user),})


def main_page(request):
    context = {'user_list': User.objects.all()}

    return render(request,'main_page.html',context)
