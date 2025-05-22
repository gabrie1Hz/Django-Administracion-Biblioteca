from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,FormView,UpdateView
from django.views.generic.edit import CreateView
from .models import books,author,category
from .forms import AddBookForm 
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
#from django.utils.translation import ugettext_lazy as _

# Create your views here.
<a href="{% url 'returnbook' mybooks.id %}">Returned</a>
def  hardcopybooks(request):
	return render(request,'library/hardcopybooks.html')


class booksView(ListView):
	model = books
	template_name = 'library/books.html'
	context_object_name = 'all_books'


def addbooks(request):
	if request.method == 'POST':
	 form = AddBookForm(request.POST)
	 if form.is_valid():
	 	form.save()
	 	messages.success(request, f'Book successfully added')
	 	return redirect('addbooks')
	else:
		form = AddBookForm()
	return render(request,'library/addbooks.html',{'my_form':form})


class add_category(SuccessMessageMixin, CreateView ):
	model = category
	fields =['category_name']
	#template_name = "library/addcategory.html"
	success_url = reverse_lazy('Viewcategory')
	
	


class ListCategoryView(ListView):
	model = category
	template_name = "library/category.html"
	paginate_by = 5
	context_object_name = 'category'
	success_message = "Category Successfully Added"


class UpdateCategoryView(UpdateView):
	model = category
	fields = ['category_name']

	#def test_func(self):
	#	post = self.get_object()
        




@login_required
def test(request , categoryid):
	categoryid = categoryid
	books_cat = books.objects.filter(category = categoryid)

	data = { books_cat : books_cat }
	return render(request,'library/hardcopybooks.html',data)

'''email = User.objects.filter(email = request.user.email)
				name = "Kudakwashe"
				message = "test message night"
				send_mail(str(name) + '' +str(email),message, EMAIL_HOST_USER, ['kudam775@gmail.com'], fail_silently = False)

				'''
				'''{% if today %}
{{ today|timeuntil:due_date }} ago<br/>
{{ due_date }}
{% endif %}'''


<td scope="row">
        {% if useracc %}
      {{ acc.issudate|timeuntil:acc.due_date }} 
      {% endif %}
    </td>

     <form class="form-inline my-4 my-lg-2" method="Post"  action=" {% url 'searched-books' %}" >
     {% csrf_token %}
      <input class="form-control mr-sm-2" name="searchedbook" required="required" type="text" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    
    </form>

    {{  mybooks.booksid.title}}
    <!--
<script>

    var config = {
      type: 'pie',
      data: {
        datasets: [{
          data: {{ data|safe }},
          backgroundColor: ['#696969', '#808080', '#A9A9A9', '#C0C0C0', '#D3D3D3'],
          label: 'quantity'
        }],
        labels: {{ labels|safe }}
        },
      options: {
        responsive: true
      }
    };

    window.onload = function() {
      var ctx = document.getElementById('pie-chart').getContext('2d');
      window.myPie = new Chart(ctx, config);
    };

  </script>-->
