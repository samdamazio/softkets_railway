from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

User = get_user_model()


@login_required
def profile_view(request, username=None, *args, **kwargs):
    user = request.user

    #<app_label>.view_<model_name>
    #<app_label>.add_<model_name>
    #<app_label>.change_<model_name>
    #<app_label>.delete_<model_name>
    
    # print(user.has_perm("auth.view_user"))
    # print(user.has_perm("visits.view_pagevisit"))

    # profile_user_obj = User.objects.get(username=username)
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = profile_user_obj == user
    return HttpResponse(f"Hello there {username} - {profile_user_obj.id} - {user.id} - {is_me}")