from django.urls import path

from .views import *


urlpatterns = [
    path('', home_page, name='home'),
    path('demend/', demand_page, name='demend'),
    path('geography/', geography_page, name='geography'),
    path('skills/', skills_page, name='skills'),
    path('lastVacancy/', last_vacancy_page, name='lastVacancy'),
]