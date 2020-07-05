from django.contrib import admin
from django.urls import path,re_path,include
from safego import search
urlpatterns=[
   path('search-form/', search.search_form),
   re_path(r"^search_advise/$", search.search_advise, name="search_advise"),
    re_path(r"^search_risk/$", search.search_risk, name="search_risk"),

]