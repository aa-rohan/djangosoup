from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time
import requests
import bs4


def home(request):
    names = ['Aarohan', 'Rachana', 'Shreejit']
    d = {
        'names': names
    }
    return render(request, 'index.html', d)
    # return HttpResponse('Greetings. Welcome to the time machine.')


def today(request):
    date = datetime.date.today()
    return HttpResponse("Today's date is: {}".format(date))


def timestamp(request):
    ts = time.time()
    return HttpResponse("Timestamp: {}".format(ts))


def mathematicians(request):
    page = requests.get('https://fabpedigree.com/james/mathmen.htm')

    soup = bs4.BeautifulSoup(page.content, 'html.parser')

    names = soup.select('li a')
    list = []
    for name in names:
        if name.string is None:
            for x in soup.select('a small'):
                list.append(x.string)
        else:
            list.append(name.string)
    names_dict = {'names': list}
    return render(request, 'math.html', names_dict)
