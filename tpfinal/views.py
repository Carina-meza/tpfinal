from django.shortcuts import render



def PRINCIPAL (request):
	return render (request, 'homemedio.html')

def Segunda (request):
	return render (request, 'segunda.html')

def Pant (request):
	return render (request, 'pantallita.html')

