from django.urls import path
from . import views
    
from .views import base_view   # <=== 通常會掛掉都是這個地方忘了再引用一次。

urlpatterns = [
    path('', base_view, name='base'),   # <=== 當網址都沒有的時候，執行[views.py]的[base_view]函式。
]