from django.urls import path
from .views import index, form_view, second_form_view, page_view
from .models import PageModel

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('form/', form_view, name='form'),
    path('second_form/', second_form_view, name='second_form')
]


pages = PageModel.objects.all()
# print(pages[0].title)

for page in pages:
    print(page.title)
    urlpatterns.append(
        path(page.url, page_view, name=page.title),

    )