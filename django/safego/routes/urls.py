from django.contrib import admin
from django.urls import path,re_path,include
from django.urls import path
from routes import views, search

urlpatterns = [
    path('riskIndex/', views.risk_index().post),
    re_path(r"^search_advise/$", search.search_advise, name="search_advise"),
    re_path(r"^search_risk/$", search.search_risk, name="search_risk"),
]