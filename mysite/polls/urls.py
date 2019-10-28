from django.urls import path
from . import views
app_name = "polls"
urlpatterns = [
    #path("", views.index, name="index"),
    path("", views.index2, name="index2"),
    #zmienne w nawiasach ostrych
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: pools/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: pools/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote")
]