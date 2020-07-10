from django.contrib import admin
from django.urls import path,re_path,include
from safego import search
urlpatterns=[
   path('search-form/', search.search_form),
   re_path(r"^search_advise/$", search.search_advise, name="search_advise"),
    re_path(r"^search_risk/$", search.search_risk, name="search_risk"),
    path('search_by_map/',search.search_by_map,name="search_by_map"),
    path('go_back/',search.go_back,name='go_back'),
    path('search_simple/',search.search_simple,name='search_simple'),
    path('search_detail/', search.search_detail, name='search_detail'),
    path('',search.search_form)

]