from django.http import HttpResponse
from django.shortcuts import redirect

def about(request):
    return HttpResponse('Django func descriptions')

def home(request):
    return HttpResponse('Homepage')

def create_post(request):
    return HttpResponse('Creating new article')

def topics(request):
    return HttpResponse('Topics list')

def topic_subscribe(request, topic):
    return HttpResponse(f'Subscribe to the {topic = }')

def topic_unsubscribe(request, topic):
    return HttpResponse(f'Unsubscribe to the {topic = }')

def show_article(request, article):
    return HttpResponse(f'Here {article = }')

def article_comment(request, article):
    return HttpResponse(f'Here comment to {article = }')

def article_update(request, article):
    return HttpResponse(f'Updating {article = }')

def article_delete(request, article):
    return HttpResponse(f'Deleting {article = }')

def profile(request, username: str):
    return HttpResponse(f'Hello {username}')

def set_password(request):
    return HttpResponse('Updating password')

def set_userdata(request):
    return HttpResponse('Updating userdata')

def deactivate_profile(request):
    return HttpResponse('Deactivating profile')

def register_new_profile(request):
    return HttpResponse('Profile registration')

def user_login(request):
    return HttpResponse('User login')

def user_logout(request):
    return redirect('home')

def posts_archive(request, year, month):
    return HttpResponse(f'archive {year =}, {month = }')