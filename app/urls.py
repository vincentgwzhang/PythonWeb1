from django.urls import path
from .views import index, index2, Message, HTMLIndex

urlpatterns = [
    path('', index2),
    path('index/<str:name>/<int:age>', index),
    path('message/', Message.as_view()),
    path('html', HTMLIndex.as_view())
]
