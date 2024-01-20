import re
import requests
from datetime import datetime

from django.shortcuts import render

from vacancy.service import *
from vacancy.api import ApiHeadHunter


def home_page(request):
    return render(request, 'HomePage.html',
                  {'navigation': get_navigation_data(), 'context': get_main_page_data()})


def demand_page(request):
    return render(request, 'Demend.html', {'navigation': get_navigation_data(), 'context': get_demand_page_data()})


def geography_page(request):
    return render(request, 'Geography.html',
                  {'navigation': get_navigation_data(), 'context': get_geography_page_data()})


def skills_page(request):
    return render(request, 'Skills.html', {'navigation': get_navigation_data(), 'context': get_skills_page_data()})


def last_vacancy_page(request):
    last_vacancies = get_last_vacancy_page_data()
    for vacancy in last_vacancies:
        name_vacancy_to_parse = vacancy.name_vacancy_to_parse
    hh = ApiHeadHunter(name_vacancy_to_parse)
    vacs = hh.get_data_vacancies('2023-12-20', 10)

    context = {'vacs': vacs, 'last_vacancies': last_vacancies, 'navigation': get_navigation_data()}

    return render(request, 'LastVacancy.html', context)
