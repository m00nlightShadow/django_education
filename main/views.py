from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'main/post/list.html')


def about(request):
    return render(request, 'main/post/about.html')


def create_post(request):
    return render(request, 'main/post/create_post.html')


def topics(request):
    return render(request, 'main/topic_list/topics.html')


def topic_subscribe(request, topic):
    return render(request, 'main/topic_list/topic_subscribe.html')


def topic_unsubscribe(request, topic):
    return render(request, 'main/topic_list/topic_unsubscribe.html')


def show_article(request, article):
    return render(request, 'main/post/detail.html')


def article_comment(request, article):
    return render(request, 'main/post/add_comments.html')


def article_update(request, article):
    return render(request, 'main/topic_list/article_update.html')


def article_delete(request, article):
    return render(request, 'main/topic_list/article_delete.html')


def profile(request, username: str):
    return render(request, 'main/user_templates/profile.html')


def set_password(request):
    return render(request, 'main/user_templates/set_user_password.html')


def set_userdata(request):
    return render(request, 'main/user_templates/set_userdata.html')


def delete_account(request):
    return render(request, 'main/user_templates/delete_account.html')


def register_new_profile(request):
    return render(request, 'main/user_templates/register.html')


def user_login(request):
    return render(request, 'main/user_templates/login.html')


def user_logout(request):
    return render(request, 'main/base.html')


def posts_archive(request, year, month):
    return HttpResponse(f'archive {year =}, {month = }')
