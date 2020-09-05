from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.db.models import Q
from .models import Task, Product, Order, Budget, Token
from .forms import TaskForm, ProductForm, OrderForm, BudgetForm
from django.views.generic import ListView, DetailView
import requests
import vk
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

@login_required
def index(request):
	if request.method == 'POST':
		form = BudgetForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = 'Что-то пошло не так..'

	budget = Budget.objects.all()

	budget_sum = 0

	for item in budget:
		budget_sum += item.earn

	form = BudgetForm()
	context = {
		'form': form,
		'budget': budget,
		'budget_sum': budget_sum,
	}


	return render(request, 'main/index.html', context)

@login_required
def about(LoginRequiredMixin, request):
    return render(request, 'main/about.html')

@login_required
def create(request):
	error = ''
	if request.method == 'POST':
		form = TaskForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = 'Что-то пошло не так..'

	budget = Budget.objects.all()

	form = TaskForm()
	context = {
		'form': form,
		'error': error,
		'budget': budget,
	}
	return render(request, 'main/create.html', context)

@login_required
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

@login_required
def product_list(request):
	products = Product.objects.all()
	return render(request, 'main/product_list.html', {'name': 'Список товаров', 'products': products})

class search_product_list(LoginRequiredMixin, ListView):
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

class search_add_product(LoginRequiredMixin, ListView):
	model = Product
	template_name = 'main/search_add_product.html'
	def get_queryset(self):
		query = self.request.GET.get('q')
		print (query)
		a = query
		print (a)
		object_list = Product.objects.filter(Q(product_name__icontains=a) | Q(product_id__icontains=a) | Q(product_size__icontains=a))
		print (object_list)
		return object_list

@login_required
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


class order_list(LoginRequiredMixin, ListView):
	model = Order
	template_name = 'main/order_list.html'

class order_page(LoginRequiredMixin, DetailView):
	model = Order
	template_name = 'main/order_page.html'

@login_required
def add_product_count(request):

	add_product_count = request.POST["add_product_count"]
	a = bool(add_product_count)

	if a == False:
		add_product_count = 1
		print ('Сколько нужно добавить?')
		print (add_product_count)
		print ('')

		product_id = request.POST['product_id']

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
		url = '/product/' + product_id
		print (url)
		return HttpResponseRedirect(url)

	if a == True:
		print ('Сколько нужно добавить?')
		print (add_product_count)
		print ('')

		product_id = request.POST['product_id']

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
		url = '/product/' + product_id
		print (url)
		return HttpResponseRedirect(url)

@login_required
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

		product_id = request.POST['product_id']

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
		url = '/product/' + product_id
		print (url)
		return HttpResponseRedirect(url)

	if a == True:
		print ('Сколько нужно добавить?')
		print (add_product_count)
		print ('')

		product_id = request.POST['product_id']

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
		url = '/product/' + product_id
		print (url)
		return HttpResponseRedirect(url)

@login_required
def delete_product(request):

	product_id = request.POST["product_id"]
	a = product_id
	print ('PRODUCT_ID:\n', product_id)

	product = Product.objects.get(product_id=a)
	product_count = product.product_count
	print (product)
	product.delete()
	return redirect('add_product')

@login_required
def edit_product(request):
	product_id = request.POST['product_id']
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
	url = '/product/' + product_id
	print (url)
	return HttpResponseRedirect(url)

@login_required
def change_order_status(request):
	product = Product.objects.get(product_id=1)
	product_image = product.product_image
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

	return redirect ('order_list')

def order_need_buy(request):
	order_content = request.POST.getlist('order_content')
	print ('ПОЛУЧИЛИ ДАННЫЕ В ТАКОМ ВИДЕ: \n',order_content)
	print (' ')
	order_content_ = []
	for item in order_content:
		content = item.split(" ")
		print (content)
		for el in content:
			order_content_.append(el)
			print ('ДАННЫЕ ПОСЛЕ ПЕРЕРАБОТКИ: ',order_content_)

	order_content = order_content_
	print ('ОКОНЧАТЕЛЬНЫЙ ОРДЕР КОНТЕНТ: ', order_content)

	need_buy = []
	in_stock = []

	for el in order_content:
		print (el)
		product = Product.objects.get(product_id=el)
		product_count = int(product.product_count)
		if product_count == 0:
			need_buy.append(product)
		elif product_count > 0:
			in_stock.append(product)

	print (need_buy)
	print (' ')
	print (' ')
	print (' ')
	print (in_stock)

	context = {
		"need_buy": need_buy,
		'in_stock': in_stock,
	}

	return render(request, 'main/order_need_buy.html', context)


class filter_order_status(LoginRequiredMixin, ListView):
	model = Order
	template_name = 'main/filter_order_status.html'
	def get_queryset(self):
		queryset = Order.objects.filter(order_status__in=self.request.GET.getlist("qq"))
		return queryset

class product_page(LoginRequiredMixin, DetailView):
	model = Product
	template_name = 'main/product_page.html'

class add_product(LoginRequiredMixin, ListView):
	model = Product
	template_name = 'main/add_product.html'



@login_required
def vkgetcode(request):
	client_id = 7574810
	client_secret = '3gi802fi8D7nB7sgC2m9'
	version = 5.122
	group_id = 197063065
	if request.get_host() == '127.0.0.1:8000':
		redirect_uri = 'http://127.0.0.1:8000/vkgettoken'
	elif request.get_host() == 'shopofsocks.ru':
		redirect_uri = 'http://shopofsocks.ru/vkgettoken'
	scopes = 'market,photos'

	auth_url = 'https://oauth.vk.com/authorize' + '?' + 'client_id=' + str(client_id) + '&display=page&redirect_uri=' + redirect_uri + '&scope=' + scopes + '&response_type=code&v=' + str(version)
	return redirect(auth_url)

@login_required
def vkgettoken(request):
	code = request.GET.get('code')
	print ('КОДДД', code)
	client_id = 7574810
	client_secret = '3gi802fi8D7nB7sgC2m9'
	version = 5.122
	group_id = 197063065
	print (request.get_host())
	if request.get_host() == '127.0.0.1:8000':
		redirect_uri = 'http://127.0.0.1:8000/vkgettoken'
	elif request.get_host() == 'shopofsocks.ru':
		redirect_uri = 'http://shopofsocks.ru/vkgettoken'
	scopes = 'market,photos'
	get_access_token = requests.get('https://oauth.vk.com/access_token',
							params = {
								'client_id': client_id,
								'client_secret': client_secret,
								'redirect_uri': redirect_uri,
								'v': version,
								'code': code,
							}
							)

	new_access_token = get_access_token.json()['access_token']
	print (new_access_token)

	token_object = Token.objects.get(pk=1)
	access_token = token_object.access_token
	print ('СТАРЫЙ ТОКЕН: ', access_token)

	token_object.access_token = new_access_token

	token_object.save()

	return redirect('home')

@login_required
def add_product_vk(request):
	end = '"photo":"4de5b8f0b3x","sizes":[],"sizes2":[["max","5d4ad2505889b301475723ad3197fb2319c506d354cc70d7e5c521ee","8699078778338907580",1440,1440],["a","f98803ab36efd6937d64616d3f2cd83cca2c33b1677d50d3137f0c36","-2445330089933293795",800,800],["b","db462598e9fd32b911e68944bdb7de5e39adb53187dcd60c927036dc","5981226008241475202",400,400],["c","784fb9e174f7d0fe14bcbae26eb11f388ea6e3da0a2f7e588d920739","2596944398728374318",300,300],["d","f6fe524fc1c8e6bdbb47d6caa69851bce6c2ddd473924a136316a409","8891666904311755021",200,200],["e","39aec961cade0eb6c0bf1a3aad8a8ed3bf017802bf461c5e98f528c1","7938689004032980611",150,150],["f","b7a06ce2db54436d04080323618f31ba8a9a56c3b05bc61f1dc6c8bd","-5021090960027821844",100,100],["g","8422c08dfd93751c56f550a25ec6a48ed55cb063854cc41370894e48","-2252590944185552705",50,50],["o","5d4ad2505889b301475723ad3197fb2319c506d354cc70d7e5c521ee","8699078778338907580",1440,1440]'
	start = '"photo":"c0eefcc716x","sizes":[],"sizes2":[["max","5d4ad2505889b301475723ad3197fb2319c506d354cc70d7e5c521ee","8699078778338907580",1440,1440],["a","f98803ab36efd6937d64616d3f2cd83cca2c33b1677d50d3137f0c36","-2445330089933293795",800,800],["b","db462598e9fd32b911e68944bdb7de5e39adb53187dcd60c927036dc","5981226008241475202",400,400'
	print (len(end))
	print (len(start))
	code = request.GET.get('code')
	print ('КОДДД', code)
	product_size = request.POST['product_size']
	product_pk = request.POST['product_pk']
	product_id = request.POST['product_id']
	product_image = request.POST['product_image']
	product_count = request.POST['product_count']
	product_name = request.POST['product_name']
	album_ids_ = request.POST.getlist("qq")
	album_ids = ', '.join(album_ids_)
	product_size_index = product_size[0]
	if product_size == '36-44.':
		pass
	elif product_size == '38-42.':
		pass
	else:
		if product_size_index == '3':
			album_ids = album_ids + ', 7'
		elif product_size_index == '4':
			album_ids = album_ids + ', 8'


	if product_size == 'One size.':
		product_description = 'Товар №' + product_id + '.' + '''
Универсальный размер.''' + '''

Состав:
80% Хлопок
17% Полиамид
3% Эластан'''
	else:
		product_description = 'Товар №' + product_id + '.' + '''
Размер: ''' + product_size + '''

Состав:
80% Хлопок 
17% Полиамид
3% Эластан'''

	token_object = Token.objects.get(pk=1)
	access_token = token_object.access_token
	client_id = 7574810
	client_secret = '3gi802fi8D7nB7sgC2m9'
	version = 5.122
	group_id = 197063065
	redirect_uri = 'http://127.0.0.1:8000/change_order_status'
	scopes = 'market,photos'
	if request.get_host() == '127.0.0.1:8000':
		files = {
		'file': open('media/' + product_image, 'rb')
		}
	elif request.get_host() == 'shopofsocks.ru':
		files = {
			'file': open('/home/users/j/j1100207/projects/demo/shop_of_socks/media/' + product_image, 'rb')
		}

	auth_url = 'https://oauth.vk.com/authorize' + '?' + 'client_id=' + str(client_id) + '&display=page&redirect_uri=' + redirect_uri + '&scope=' + scopes + '&response_type=code&v=' + str(version)

	getuploadserver = requests.post('https://api.vk.com/method/photos.getMarketUploadServer',
							params = {
								'group_id': group_id,
								'main_photo': 1,
								'access_token': access_token,
								'v': version,
								'crop_width': 2048,
							}
							)

	upload_server = getuploadserver.json()['response']['upload_url']
	uploadphoto = requests.post(upload_server, files=files)
	server = int(uploadphoto.json()['server'])
	photo= uploadphoto.json()['photo']
	hash_ = uploadphoto.json()['hash']
	crop_data = uploadphoto.json()['crop_data']
	crop_hash = uploadphoto.json()['crop_hash']


	params={
			'group_id': group_id,
			'photo': photo,
			'hash': hash_,
			'crop_data': crop_data,
			'crop_hash': crop_hash,
			'server': server,	
			'access_token': access_token,
			'v': version,
			}

	savephoto = requests.post('https://api.vk.com/method/photos.saveMarketPhoto', data=params)
	photo = savephoto.json()['response']
	for row in photo:
		photo_id = int(row.get('id'))

	response = requests.get('https://api.vk.com/method/market.add',
						params = {
							'name': product_name,
							'description': product_description,
							'category_id': 5,
							'price': 150.0,
							'access_token': access_token,
							'owner_id': -group_id,
							'v': version,
							'main_photo_id': photo_id,
							'photo_id': photo_id,
							'deleted': 0,
						})

	item_id = response.json()['response']['market_item_id']

	addAlbum = requests.get('https://api.vk.com/method/market.addToAlbum',
							params = {
								'owner_id': -group_id,
								'access_token': access_token,
								'v': version,
								'item_id': item_id,
								'album_ids': album_ids,
							})

	data = addAlbum.json()

	url = '/product/' + product_id
	return HttpResponseRedirect(url)

@login_required
def edit_product_vk(request):
	product_size = request.POST['product_size']
	product_pk = request.POST['product_pk']
	product_id = request.POST['product_id']
	product_image = request.POST['product_image']
	product_count = request.POST['product_count']
	if product_size == 'One size.':
		product_description = 'Товар №' + product_id + '.' + '''
Универсальный размер.''' + '''

Состав:
80% Хлопок
17% Полиамид
3% Эластан'''
	else:
		product_description = 'Товар №' + product_id + '.' + '''
Размер: ''' + product_size + '''

Состав:
80% Хлопок 
17% Полиамид
3% Эластан'''
	if request.get_host() == '127.0.0.1:8000':
		files = {
		'file': open('media/' + product_image, 'rb')
		}
	elif request.get_host() == 'shopofsocks.ru':
		files = {
			'file': open('/home/users/j/j1100207/projects/demo/shop_of_socks/media/' + product_image, 'rb')
		}

	token_object = Token.objects.get(pk=1)
	access_token = token_object.access_token
	client_id = 7574810
	version = 5.122
	group_id = 197063065
	if int(product_id) > 200:
		offset = 0
	else: 
		offset = 200

	getuploadserver = requests.post('https://api.vk.com/method/photos.getMarketUploadServer',
							params = {
								'group_id': group_id,
								'main_photo': 1,
								'access_token': access_token,
								'v': version,
								'crop_width': 2048,
							}
							)

	upload_server = getuploadserver.json()['response']['upload_url']
	uploadphoto = requests.post(upload_server, files=files)
	server = int(uploadphoto.json()['server'])
	photo= uploadphoto.json()['photo']
	hash_ = uploadphoto.json()['hash']
	crop_data = uploadphoto.json()['crop_data']
	crop_hash = uploadphoto.json()['crop_hash']


	params={
			'group_id': group_id,
			'photo': photo,
			'hash': hash_,
			'crop_data': crop_data,
			'crop_hash': crop_hash,
			'server': server,	
			'access_token': access_token,
			'v': version,
			}

	savephoto = requests.post('https://api.vk.com/method/photos.saveMarketPhoto', data=params)
	photo = savephoto.json()['response']
	for row in photo:
		photo_id = int(row.get('id'))

	market_get = requests.get('https://api.vk.com/method/market.get',
						params = {
							'access_token': access_token,
							'owner_id': -group_id,
							'v': version,
							'offset': offset,
							'count': 200,
						})



	data = market_get.json()['response']['items']
	item_id = ''

	for item in data:
		items = item.get('id')
		description = item.get('description')

		if len(product_id) == 1:
			product_id_ = product_id + '.'
			product_id_vk = description[7:9]
		elif len(product_id) == 2:
			product_id_ = product_id + '.'
			product_id_vk = description[7:10]
		else:
			product_id_ = product_id
			product_id_vk = description[7:10]
			print (product_id_vk)

		if product_id_ == product_id_vk:
			item_id = items
			break

	print ('item: \n',item_id)

	market_edit = requests.get('https://api.vk.com/method/market.edit',
						params = {
							'access_token': access_token,
							'owner_id': -group_id,
							'v': version,
							'item_id': item_id,
							'description': product_description,
							'main_photo_id': photo_id,

						})

	response = market_edit.json()
	print (response)

	product_id = request.POST['product_id']
	url = '/product/' + product_id
	return HttpResponseRedirect(url)

@login_required
def budget(request):
	pass

@login_required
def change_budget_tag(request):
	pass



