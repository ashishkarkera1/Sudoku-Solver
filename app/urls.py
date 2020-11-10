from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index),
    url(r'^sudokusolver$',views.SudokuSolver),
    url(r'^algorithm$',views.Algorithm),
    url(r'^about$',views.About),
    url(r'^testing$',views.testing),
]