import operator

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'prova':'Inserisci il testo'})

def viva(request):
    return HttpResponse('<h1>Viva la figa!</h1>')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordcollection = {}
    for i in wordlist:
        if i not in wordcollection.keys():
            wordcollection[i] = 1
        else:
            wordcollection[i] += 1

    wordcollection = sorted(wordcollection.items(), key=operator.itemgetter(1), reverse=True)
    return  render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist), 'list':wordcollection})
