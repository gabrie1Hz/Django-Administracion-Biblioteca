from django.shortcuts import render,HttpResponse ,redirect
from django.contrib.auth.decorators import login_required
from library.models import books, category ,issuedbooks
from datetime import datetime ,timedelta
from django.utils.timesince import timesince
from django.db.models import Q ,Count
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.http import JsonResponse

User = get_user_model()
# Create your views here.

@login_required
def dashboard(request):

	librarybooks = books.objects.order_by('quantity')[:5]
	books_p_category = books.objects.values('category').annotate(count=Count('category')).order_by('count')[:5]

		


	context = {
		'today' : datetime.today(),
		'due_date' : issuedbooks.objects.filter(userid_id = request.user.id),	
		'librarybooks':librarybooks,
		'bpc':books_p_category
	

	}
	return render(request, 'main/dashboard.html',context)
	




class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 23, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response
