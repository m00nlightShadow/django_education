from django.urls import path, register_converter
from .views import (
    home,
    about,
    create_post,
    topics,
    topic_subscribe,
    topic_unsubscribe,
    profile,
    set_password,
    set_userdata,
    delete_account,
    register_new_profile,
    user_login,
    user_logout,
    posts_archive,
    show_article,
    article_comment,
    article_update,
    article_delete,
    )
from . import converters


register_converter(converters.FourDigitYearConverter, 'year4')
register_converter(converters.MonthConverter, 'month2')

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about_page'),
    path('create/', create_post, name='create_post'),
    path('topics/', topics, name='topics'),
    path('topics/<topic>/subscribe/', topic_subscribe, name='topic_subscribe'),
    path('topics/<topic>/unsubscribe/', topic_unsubscribe, name='topic_unsubscribe'),
    path('profile/<str:username>/', profile, name='profile_data'),
    path('set-password/', set_password, name='set_password'),
    path('set-userdata/', set_userdata, name='set_userdata'),
    path('deactivate/', delete_account, name='delete_account'),
    path('register/', register_new_profile, name='register_new_profile'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('archive/<year4:year>/<month2:month>/', posts_archive),
    path('<article>/', show_article, name='show_article'),
    path('<article>/comment/', article_comment, name='article_comment'),
    path('<article>/update/', article_update, name='article_update'),
    path('<article>/delete/', article_delete, name='article_delete'),
]
