"""askme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from question import views
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('top', views.top, name='top'),
    path('new', views.new, name='new'),
    path('tag/<int:id>', views.tag, name='tag'),
    path('question/<int:id>/', views.question, name='question'),
    path('question/<int:id>/', views.new_answer, name='new_answer'),
    path('ask/', views.ask, name='ask'),
    path('login/', views.signin, name='login'),
    path('registration/', views.registration, name='registration'),   
    path('signout/', views.signout, name='signout'),   
    path('user/<int:id>/', views.profile, name='user'),  
    path('user/edit/', views.edit, name='edit'),  
    path('user/questions/<int:id>/', views.user_questions, name='user_questions'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += staticfiles_urlpatterns()