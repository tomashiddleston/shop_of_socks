from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import Task, Product, Order
from .forms import TaskForm, ProductForm, OrderForm
from django.views.generic import ListView, DetailView


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
	error = ''
	if request.method == 'POST':
		form = TaskForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = 'Что-то пошло не так..'


	form = TaskForm()
	context = {
		'form': form,
		'error': error,
	}
	return render(request, 'main/create.html', context)

def product(request):
	error = ''
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = 'Что-то пошло не так..'

	form = ProductForm()
	context = {
		'form': form,
		'error': error,
	}
	return render(request, 'main/product.html', context)

def product_list(request):
	products = Product.objects.all()
	return render(request, 'main/product_list.html', {'name': 'Список товаров', 'products': products})

class search_product_list(ListView):
	model = Product
	template_name = 'main/search_product_list.html'
	def get_queryset(self):
		query = self.request.GET.get('q')
		print (query)
		a = query
		print (a)
		object_list = Product.objects.filter(Q(product_name__icontains=a) | Q(product_id__icontains=a))
		print (object_list)
		return object_list

class search_add_product(ListView):
	model = Product
	template_name = 'main/search_add_product.html'
	def get_queryset(self):
		query = self.request.GET.get('q')
		print (query)
		a = query
		print (a)
		object_list = Product.objects.filter(Q(product_name__icontains=a) | Q(product_id__icontains=a))
		print (object_list)
		return object_list

def order(request):
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = 'Что-то пошло не так..'

	orderform = OrderForm()
	context = {
		'title': 'Создание заказа',
		'orderform': orderform,
	}
	return render(request, 'main/order.html', context)

class order_list(ListView):
	model = Order
	template_name = 'main/order_list.html'

class order_page(DetailView):
	model = Order
	template_name = 'main/order_page.html'

def add_product_count(request):

	add_product_count = request.POST["add_product_count"]
	a = bool(add_product_count)

	if a == False:
		add_product_count = 1
		print ('Сколько нужно добавить?')
		print (add_product_count)
		print ('')

		product_count = request.POST["product_count"]
		print ('Доступность сейчас:')
		print (product_count)
		print ('')

		product_pk = request.POST["product_pk"]
		a = product_pk
		print ('PRODUCT_ID:\n', product_pk)

		product = Product.objects.get(pk=a)
		product_count = product.product_count
		print (product_count)

		a = int(product.product_count)
		b = int(add_product_count)

		c = a + b

		product.product_count = c
		product.save()

		print ('PRODUCT COUNT: ', c)
		product_pk = request.POST["product_pk"]
		url = '/product/' + product_pk
		print (url)
		return HttpResponseRedirect(url)

	if a == True:
		print ('Сколько нужно добавить?')
		print (add_product_count)
		print ('')

		product_count = request.POST["product_count"]
		print ('Доступность сейчас:')
		print (product_count)
		print ('')

		product_pk = request.POST["product_pk"]
		a = product_pk
		print ('PRODUCT_ID:\n', product_pk)

		product = Product.objects.get(pk=a)
		product_count = product.product_count
		print (product_count)

		a = int(product.product_count)
		b = int(add_product_count)

		c = a + b

		product.product_count = c
		product.save()

		print ('PRODUCT COUNT: ', c)
		product_pk = request.POST["product_pk"]
		url = '/product/' + product_pk
		print (url)
		return HttpResponseRedirect(url)

def add_product_count_page(request):

	add_product_count = request.POST["add_product_count"]
	a = bool(add_product_count)

	if a == False:
		add_product_count = 1
		print ('Сколько нужно добавить?')
		print (add_product_count)
		print ('')

		product_count = request.POST["product_count"]
		print ('Доступность сейчас:')
		print (product_count)
		print ('')

		product_pk = request.POST["product_pk"]
		a = product_pk
		print ('PRODUCT_ID:\n', product_pk)

		product = Product.objects.get(pk=a)
		product_count = product.product_count
		print (product_count)

		a = int(product.product_count)
		b = int(add_product_count)

		c = a + b

		product.product_count = c
		product.save()

		print ('PRODUCT COUNT: ', c)
		product_pk = request.POST["product_pk"]
		url = '/product/' + product_pk
		print (url)
		return HttpResponseRedirect(url)

	if a == True:
		print ('Сколько нужно добавить?')
		print (add_product_count)
		print ('')

		product_count = request.POST["product_count"]
		print ('Доступность сейчас:')
		print (product_count)
		print ('')

		product_pk = request.POST["product_pk"]
		a = product_pk
		print ('PRODUCT_ID:\n', product_pk)

		product = Product.objects.get(pk=a)
		product_count = product.product_count
		print (product_count)

		a = int(product.product_count)
		b = int(add_product_count)

		c = a + b

		product.product_count = c
		product.save()

		print ('PRODUCT COUNT: ', c)
		product_pk = request.POST["product_pk"]
		url = '/product/' + product_pk
		print (url)
		return HttpResponseRedirect(url)

def delete_product(request):

	product_id = request.POST["product_id"]
	a = product_id
	print ('PRODUCT_ID:\n', product_id)

	product = Product.objects.get(product_id=a)
	product_count = product.product_count
	print (product)
	product.delete()
	return redirect('add_product')


def edit_product(request):
	product_pk = request.POST["product_pk"]
	a = product_pk
	print ('PRODUCT_ID:\n', product_pk)

	product = Product.objects.get(pk=a)
	product_image = product.product_image
	print (product_image)

	c = request.FILES["product_image"]
	product.product_image = c
	product.save()

	print ('PRODUCT COUNT: ', c)
	product_pk = request.POST["product_pk"]
	url = '/product/' + product_pk
	print (url)
	return HttpResponseRedirect(url)

def change_order_status(request):
	order_pk = request.POST["order_pk"]
	new_order_status = request.POST["order_status"]

	print ('Номер заказа:\n', order_pk)
	print ('Новый статус заказа:\n', new_order_status)

	a = order_pk
	order = Order.objects.get(pk=a)
	order_status = order.order_status
	print ('Текущий статус заказа:\n', order_status)

	order.order_status = new_order_status
	order.save()

	return redirect('order_list')

class filter_order_status(ListView):
	model = Order
	template_name = 'main/filter_order_status.html'
	def get_queryset(self):
		queryset = Order.objects.filter(order_status__in=self.request.GET.getlist("qq"))
		return queryset

class product_page(DetailView):
	model = Product
	template_name = 'main/product_page.html'

class add_product(ListView):
	model = Product
	template_name = 'main/add_product.html'

# def order_list(request):
# 	if request.method == 'POST':
# 		form = OrderForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('home')
# 		else:
# 			error = 'Что-то пошло не так..'

# 	form = OrderForm()
# 	context = {
# 		'title': 'Создание заказа',
# 		'form': form,
# 	}
# 	return render(request, 'main/order_list.html', context)








