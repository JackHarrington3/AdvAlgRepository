from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import urllib.request

url = "https://randomword.com/noun"
page = urllib.request.Request(url, headers={'User-Agent': 'Hangman/1.0'})

html = urllib.request.urlopen(page).read()
data = html.decode('ISO-8859-1')

dataLoc = data.find('<div id="random_word">')
data = data[dataLoc+22:]
dataLoc = data.find("<")
data = data[:dataLoc]

global wrongguesses
global wordblank

wrongguesses = 0
count = 0


word = data
wordcopy = data
wordblank = ""

for i in range(len(word)):
    wordblank = wordblank + "_ "


def start(request):
    global wrongguesses
    global word
    global wordblank
    global wordcopy
    
    page = urllib.request.Request(url, headers={'User-Agent': 'Hangman/1.0'})

    html = urllib.request.urlopen(page).read()
    data = html.decode('ISO-8859-1')

    dataLoc = data.find('<div id="random_word">')
    data = data[dataLoc+22:]
    dataLoc = data.find("<")
    data = data[:dataLoc]

    wrongguesses = 0


    word = data
    wordcopy = data
    wordblank = ""

    for i in range(len(word)):
        wordblank = wordblank + "_ "

    let = ""

    template = loader.get_template("hangman/start.html")
    context = {
        "letter":let
    }

    return HttpResponse(template.render(context, request))


def index(request):
    global wrongguesses
    global word
    global wordblank
    global wordcopy
    
    let = request.POST["letter"]

    if(word.find(let) < 0 and len(let) == 1):
        wrongguesses += 1
        
    else:
        while(word.find(let) >= 0 and len(let) == 1):
            wordblank = wordblank[:2*word.find(let)] + let + " " + wordblank[2*word.find(let)+2:]
            word = word[:word.find(let)] + "-" + word[word.find(let)+1:]

    if(wordblank.find("_") < 0):
        gallows = "<H1> CONGRATULATIONS, THE WORD WAS " + wordcopy.upper() +"!</H1>"
        wrongguesses = 0;
        page = urllib.request.Request(url, headers={'User-Agent': 'Hangman/1.0'})
        html = urllib.request.urlopen(page).read()
        data = html.decode('ISO-8859-1')

        dataLoc = data.find('<div id="random_word">')
        data = data[dataLoc+22:]
        dataLoc = data.find("<")
        data = data[:dataLoc]
        word = data
        wordcopy = data
        wordblank = ""

        for i in range(len(word)):
            wordblank = wordblank + "_ "

        
    elif(wrongguesses == 0):
        gallows = """<br>|=====<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                     |<br>
                     |<br>
                     |<br>
                     |<br>
                     |_______
                     """
    elif(wrongguesses ==1):
        gallows = """<br>|=====<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O<br>
                     |<br>
                     |<br>
                     |<br>
                     |_______
                     """
    elif(wrongguesses == 2):
        gallows = """<br>|=====<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                     |<br>
                     |<br>
                     |_______
                     """
    elif(wrongguesses ==3):
        gallows = """<br>|=====<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--|<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
                     |<br>
                     |_______
                     """
    elif(wrongguesses ==4):
        gallows = """<br>|=====<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--|--<br>
                     |<br>
                     |<br>
                     |_______
                     """
    elif(wrongguesses ==5):
        gallows = """<br>|=====<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--|--<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<br>
                     |<br>
                     |_______
                     """
    elif(wrongguesses == 6):
        gallows = "<H1>YOU LOST! THE WORD WAS " + wordcopy.upper() + "</H1>"
        wrongguesses = 0;
        page = urllib.request.Request(url, headers={'User-Agent': 'Hangman/1.0'})
        html = urllib.request.urlopen(page).read()
        data = html.decode('ISO-8859-1')

        dataLoc = data.find('<div id="random_word">')
        data = data[dataLoc+22:]
        dataLoc = data.find("<")
        data = data[:dataLoc]
        word = data
        wordcopy = data
        wordblank = ""

        for i in range(len(word)):
            wordblank = wordblank + "_ "
        

        
    template = loader.get_template("hangman/index.html")
    context = {
        "letter":let,"gallows":gallows,"wordblank": wordblank
    }

    return HttpResponse(template.render(context, request))
    




    
    #global MJ
    #MJ += 1

  #  gallows = "|=======<br>|&#160;&#160;|"

   # return HttpResponse(str(MJ) + " " + '<br><br><label for="fname">Guess a Letter:</label><input type="text" id="fname" name="fname"><br><br><br><br>'+gallows)
#return HttpResponse('<form action="/action_page.php"> <label for="fname">First name:</label><input type="text" id="fname" name="fname"><br><br><label for="lname">Last name:</label><input type="text" id="lname" name="lname"><br><br><input type="submit" value="Submit"></form>')
    
