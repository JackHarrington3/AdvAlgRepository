from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from hangman.models import Game

#made thisGame a global variable so it can be useed in getGallows()
global thisGame

#def thisWillBeTheIndexPage(request):
    #return HttpResponse(template.render(context, request))

def leaderboard(request):
    template = 
    return HttpResponse
    
def getGallows(n):
    global thisGame
    if(n==0):
        return      """<br>|=====<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                     |<br>
                     |<br>
                     |<br>
                     |<br>
                     |_______
                     """
    if(n==1):
        return      """<br>|=====<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O<br>
                     |<br>
                     |<br>
                     |<br>
                     |_______
                     """
    if(n==2):
        return      """<br>|=====<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                     |<br>
                     |<br>
                     |_______
                     """
    if(n==3):
        return      """<br>|=====<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--|<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
                     |<br>
                     |_______
                     """
    if(n==4):
        return      """<br>|=====<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--|--<br>
                     |<br>
                     |<br>
                     |_______
                     """
    if(n==5):
        return      """<br>|=====<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--|--<br>
                     |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/<br>
                     |<br>
                     |_______
                     """
    if(n>=6):
        return "<H1>YOU LOST! THE WORD WAS " + thisGame.origWord.upper() + "</H1>"
    
            

def newGame():
    import urllib.request
    url="https://www.randomword.com/noun"

    newWrongGuesses = 0
    newWord = ""
    newWordBlanks = ""


    page = urllib.request.Request(url, headers={'User-Agent': 'Hangman/1.0'})

    html = urllib.request.urlopen(page).read()
    data = html.decode('ISO-8859-1')

    dataLoc = data.find('<div id="random_word">')
    data = data[dataLoc+22:]
    dataLoc = data.find("<")
    data = data[:dataLoc]

    newWord = data

    for i in range(len(newWord)):
        newWordBlanks = newWordBlanks + "_ "

    #need to insert the game data into the table; obtain
    #  the game id so we can store it on the user's computer
    #  as a cookie
    newGame = Game(wrongGuesses = newWrongGuesses,
        word = newWord,
        wordBlanks = newWordBlanks,
        origWord = newWord,
        prevGuesses = "")
    newGame.save()
    newGameId = newGame.id;
    return newGameId
    
#At the start of a game, the game row has to be
#initialized with a new game (new word, new wordBlanks,
# wrongGuesses set to 0)

#urls.py directs players to start when accessing the root
def start(request):
    global thisGame
    curKeyFound = False
    gameID = 0
    for k, v in request.COOKIES.items():
        if (k == 'HangmanGID'):
            curKeyFound = True
            gameID = int(v)
                        
    if (not curKeyFound):
        newGameId = newGame()

        #response = HttpResponse("check for a new game with id " + str(newGameId))
        #TODO: create HttpResponse that doesn't require the user to see it
        #think redirects - HttpResponseRedirect
        response = HttpResponseRedirect("/hangman/game")
        response.set_cookie('HangmanGID', str(newGameId))
        return response
    else:
        thisGame = Game.objects.get(pk=gameID)
        wrongguesses = thisGame.wrongGuesses
        wordblank = thisGame.wordBlanks
        if (wordblank.find("_") < 0 or wrongguesses > 5):
            response = HttpResponseRedirect("/hangman/game")
            response.delete_cookie('HangmanGID')
            gameID = 0
            return response

    
    #I moved the content of game() here so that the game runs
    #on just one page (/hangman/game). That way, we can have
    #an index page welcoming the player or something.
    gameID = request.COOKIES["HangmanGID"]
    print("This is where index function is called with gameID=" + str(gameID))
    thisGame = Game.objects.get(pk=gameID)
    word = thisGame.word
    prevguesses = thisGame.prevGuesses
    print("DEBUG:the word is " + thisGame.word)
    wrongguesses = thisGame.wrongGuesses
    wordblank = thisGame.wordBlanks
    prevguesses = thisGame.prevGuesses
    gameStatus = "P"
    if ("letter" not in request.POST):
        let=""
    else:
        let = request.POST["letter"]
        if (len(let) == 1):
            prevguesses = prevguesses + " " + let
    if(word.find(let) < 0 and len(let) == 1):
        wrongguesses += 1
        
    else:
        while(word.find(let) >= 0 and len(let) == 1):
            wordblank = wordblank[:2*word.find(let)] + let + " " + wordblank[2*word.find(let)+2:]
            word = word[:word.find(let)] + "-" + word[word.find(let)+1:]

    if(wordblank.find("_") < 0):
        gallows = "<H1> CONGRATULATIONS, THE WORD WAS " + thisGame.origWord.upper() +"!</H1>"
        gameStatus = "D"
        #Add code that will erase current game id cookie, or we could
        #possibly ask the user if they'd like to play again with
        #a submit action included
        #This happens in start() now

        
    else:
        #moved gallows into a function
        gallows = getGallows(wrongguesses)
    if (wrongguesses >=6):
        gameStatus = "D"

    #set the values in the Game table row matching the gameID
    thisGame.word = word
    thisGame.wrongGuesses = wrongguesses
    thisGame.wordBlanks = wordblank
    thisGame.prevGuesses = prevguesses
    thisGame.save()

    template = loader.get_template("hangman/game.html")
    context = {
        "letter":let,"gallows":gallows,"wordblank": wordblank,
        "prevguesses":prevguesses, "gameStatus":gameStatus
    }
    return HttpResponse(template.render(context, request))

    
#dummy game() function
#it doesn't do anything - it's just here b/c views requires there to be a game() function
def index(request):
    template = loader.get_template("hangman/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

#when accessed, check if the cookie with a game id exists
#if it does, then check if the game is still running
#if the game is still running, continue where the player left off
#if the game is completed, start a new game (new game_id)
##def game(request):
##    global thisGame
##
##    gameID = request.COOKIES["HangmanGID"]
##    print("This is where index function is called with gameID=" + str(gameID))
##    thisGame = Game.objects.get(pk=gameID)
##    word = thisGame.word
##    prevguesses = thisGame.prevGuesses
##    print("DEBUG:the word is " + thisGame.word)
##    wrongguesses = thisGame.wrongGuesses
##    wordblank = thisGame.wordBlanks
##    prevguesses = thisGame.prevGuesses
##    gameStatus = "P"
##    if ("letter" not in request.POST):
##        let=""
##    else:
##        let = request.POST["letter"]
##        if (len(let) == 1):
##            prevguesses = prevguesses + " " + let
##    if(word.find(let) < 0 and len(let) == 1):
##        wrongguesses += 1
##        
##    else:
##        while(word.find(let) >= 0 and len(let) == 1):
##            wordblank = wordblank[:2*word.find(let)] + let + " " + wordblank[2*word.find(let)+2:]
##            word = word[:word.find(let)] + "-" + word[word.find(let)+1:]
##
##    if(wordblank.find("_") < 0):
##        gallows = "<H1> CONGRATULATIONS, THE WORD WAS " + thisGame.origWord.upper() +"!</H1>"
##        gameStatus = "D"
##        #Add code that will erase current game id cookie, or we could
##        #possibly ask the user if they'd like to play again with
##        #a submit action included
##        #This happens in start() now
##
##        
##    else:
##        #moved gallows into a function
##        gallows = getGallows(wrongguesses)
##    if (wrongguesses >=6):
##        gameStatus = "D"
##
##    #set the values in the Game table row matching the gameID
##    thisGame.word = word
##    thisGame.wrongGuesses = wrongguesses
##    thisGame.wordBlanks = wordblank
##    thisGame.prevGuesses = prevguesses
##    thisGame.save()
##
##    template = loader.get_template("hangman/index.html")
##    context = {
##        "letter":let,"gallows":gallows,"wordblank": wordblank,
##        "prevguesses":prevguesses, "gameStatus":gameStatus
##    }
##    return HttpResponse(template.render(context, request))
    

