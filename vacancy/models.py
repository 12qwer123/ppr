from django.db import models


class Navigation(models.Model):
    title = models.TextField(blank=False, verbose_name='Заголовок вакансии', max_length=25)
    logo_field = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='Логотип')
    first_menu = models.TextField(blank=False, verbose_name='Первый пункт меню', max_length=25)
    second_menu = models.TextField(blank=False, verbose_name='Второй пункт меню', max_length=25)
    third_menu = models.TextField(blank=False, verbose_name='Третий пункт меню', max_length=25)
    fourth_menu = models.TextField(blank=False, verbose_name='Четвертый пункт меню', max_length=25)
    fifth_menu = models.TextField(blank=False, verbose_name='Пятый пункт меню', max_length=25)
    author = models.TextField(blank=False, verbose_name='Автор', max_length=50)


class MainPage(models.Model):
    content = models.TextField(blank=True, verbose_name='Описание профессии')
    photo = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='Фото')


class Demand(models.Model):
    graph_salary_level = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='График уровень зарплат по годам')
    graph_num_vacancy = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='График количество вакансий по годам')
    table = models.TextField(blank=False, verbose_name='Таблица')

class Geography(models.Model):
    graph_salary_level_by_city = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='График уровень зарплат по городам')
    graph_vacancy_fraction_by_city = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='График доля вакансий по городам')
    table = models.TextField(blank=False, verbose_name='Таблица')

class Skills(models.Model):
    table_name = models.TextField(blank=False, verbose_name='Название таблицы', max_length=30)
    table = models.TextField(blank=False, verbose_name='Таблица')
    graph_skills = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='График по скиллам')

class LastVacancyModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    name_vacancy_to_parse = models.TextField(blank=False, verbose_name='Вакансия для парсинга', max_length=15)
