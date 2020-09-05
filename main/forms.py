from .models import Task, Product, Order, Budget
from django.forms import ModelForm, TextInput, Textarea, ImageField, ClearableFileInput, Select


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название',
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание',
            }),
        }
        
class ProductForm(ModelForm):
    class Meta:
        model = Product 
        fields = ["product_id", "product_name", "product_price", "product_size", "product_image"]
        widgets = {
            "product_id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер товара'
            }),
            "product_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название товара'
            }),
            "product_price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите закупочную цену'
            }),
            "product_size": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите размер'
            }),
        }

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["order_id", "order_status", "order_name", "order_address", "order_contain"]
        widgets = {
            "order_id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер заказа', 
            }),
            "order_status": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Статус заказа', 
            }),
            "order_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО покупателя', 
            }),
            "order_address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес покупателя',
            }),
            "order_contain": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите содержание заказа',
            }),
        }

class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ["budget_name", "earn", "budget_tag"]
        widgets = {
            "budget_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'На что?',
            }),
            "earn": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сколько?',
            }),
            "budget_tag": Select(attrs={
                'class': 'custom-select',
            }),
            }