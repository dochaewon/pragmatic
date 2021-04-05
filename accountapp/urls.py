from django.urls import path

from accountapp.views import hello_world

app_name = 'accountapp'

#accountapp:hello_world 요러케 해주는거 있움

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
]
