from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

import snippets.views as views

urlpatterns = [
    path('', views.SnippetList.as_view()), #as view bo to nie def
    path('<int:pk>', views.SnippetDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)