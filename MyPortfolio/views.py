from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


def count(request):
    #takes the input from the counter page an take an input marked "fulltext"
    answer = request.GET['fulltext']
    #this splits the input from recieved from the list from every space
    word_list = answer.split()

    #creates an empty the list
    worddictionary = {}
    #this cycles through the words and increments and splits each word
    for word in word_list:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    #this sorts the list and sorts it according to the 2nd operator(number of words) and sorts from highest to least amount of times its shown
    sorted_words = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'answer': answer, 'count': len(word_list), 'sorted_words': sorted_words})


def movetocounter(request):
    response = request.GET
    return request(request, 'home.html')