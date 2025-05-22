# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from library.models import books ,author ,category
from .serializers import booksserializer ,authorslzr ,categoryslzr


@api_view(['GET'])
def getroutes(request):
	routes =[

	'GET/API',
	'uzapi/books/',
	'uzapi/author/',
	'uzapi/category/',

	]
	return Response(routes)

@api_view(['GET'])
def getbooks(request):
	allbooks = books.objects.all()
	serializedbooks = booksserializer(allbooks,many=True)
	return Response(serializedbooks.data)

@api_view(['GET'])
def getbook(request,pk):
	book = books.objects.get(id=pk)
	serializedbook = booksserializer(book,many=False)
	return Response(serializedbook.data)

@api_view(['GET'])
def getauthor(request):
	authors = author.objects.all()
	serializedauthor = authorslzr(authors,many=True)
	return Response(serializedauthor.data)


@api_view(['GET'])
def getcategory(request):
	allcategory = category.objects.all()
	serializedcategory = categoryslzr(allcategory,many=True)
	return Response(serializedcategory.data)
	