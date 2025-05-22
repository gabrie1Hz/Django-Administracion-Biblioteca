from rest_framework.serializers import ModelSerializer
from library.models import books ,author ,category



class booksserializer(ModelSerializer):
	class Meta:
		model = books
		#fields = ['id','title']
		fields = '__all__'

class authorslzr(ModelSerializer):
	class Meta:
		model = author
		fields = '__all__'


class categoryslzr(ModelSerializer):
	class Meta:
		model = category
		fields = '__all__'