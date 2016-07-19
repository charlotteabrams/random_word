from django.shortcuts import render, redirect
from random import randint
#CONTROLLER
# Create your views here.
def index(request):
	return render(request, "wordgenerate/index.html")

def generate(request): 
	if "counter" in request.session:
		request.session['counter'] +=1
	else:
		request.session['counter'] = 1

	word = ""
	letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9",]
	for x in range(0,14):
		letter = letters[(randint(0,35))]
		word += str(letter)
	words = {
		"random_word": word
	}
	return render(request, 'wordgenerate/index.html', words)





