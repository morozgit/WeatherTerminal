import requests


def ru_letter(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(text.lower())


def show_weather(places):
    for place in places:
        if ru_letter(place):
            url = 'http://wttr.in/{}?nqTmM&lang=ru'.format(place)
        else:
            url = 'http://wttr.in/{}?nTqu&lang=en'.format(place)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)


def main():
    places = ['London', 'SVO', 'Череповец']
    show_weather(places)


if __name__ == '__main__':
    main()
