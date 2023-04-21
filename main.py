import requests


def chek_ru_letter(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(text.lower())


def show_weather(places):
    for place in places:
        if chek_ru_letter(place):
            payload = {'nqTM': '', 'lang': 'ru'}
        else:
            payload = {'nTqu': '', 'lang': 'en'}
        url = 'http://wttr.in/{}'.format(place)
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


def main():
    places = ['London', 'SVO', 'Череповец']
    show_weather(places)


if __name__ == '__main__':
    main()
