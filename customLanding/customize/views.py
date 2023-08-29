from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import json
from .models import DisplayModel, HeaderModel, TextModel, ImageModel, LinkModel, ButtonModel, CardModel, FormModel, \
    IconModel


def index(request):
    data = {}

    # first display
    displays = DisplayModel.objects.all()

    for display in displays:

        headers = HeaderModel.objects.filter(display=display)
        images = ImageModel.objects.filter(display=display)
        texts = TextModel.objects.filter(display=display)
        links = LinkModel.objects.filter(display=display)
        buttons = ButtonModel.objects.filter(display=display)
        cards = CardModel.objects.all()
        icons = IconModel.objects.all()
        data[f'Display_{display.id}'] = {
            'headers': {},
            'texts': {},
            'images': {},
            'links': {},
            'buttons': {},
            'icons': []
        }
        data['icons'] = [icon for icon in icons]
        data['cards'] = [card.to_dict() for card in cards]
        for header in headers:
            data[f'Display_{display.id}']['headers'][header.name.replace(' ', '_')] = header.text
        for text in texts:
            data[f'Display_{display.id}']['texts'][text.name.replace(' ', '_')] = text.text
        for image in images:
            data[f'Display_{display.id}']['images'][image.name.replace(' ', '_')] = image.to_dict()
        for link in links:
            data[f'Display_{display.id}']['links'][link.name.replace(' ', '_')] = link
        for button in buttons:
            data[f'Display_{display.id}']['buttons'][button.name.replace(' ', '_')] = button
        # if icons:
        #     for icon in icons:
        #         data[f'Display_{display.id}']['icons'].append(icon)
        # for card in cards:
        #     data['cards'][card.name.replace(' ', '_')] = card
    # print(data)

    return render(request, 'base.html', context=data)


def form_view(request):

    if request.method == 'POST':
        byte_string = request.body
        json_string = byte_string.decode('utf-8')
        parsed_dict = json.loads(json_string)

        mail_to_send = FormModel.objects.get(name='Форма заявки 1')
        print(send_mail(subject='Форма пользователя', message=f"{parsed_dict['name']} - {parsed_dict['email']}",
                        recipient_list=[mail_to_send.mail_to], from_email='userform1@yandex.ru'))
    return HttpResponse({'hello': 1})
