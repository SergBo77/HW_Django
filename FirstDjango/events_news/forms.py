from .models import events_news
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class New_eventForm(ModelForm):
	class Meta:
		model = events_news
		fields = ['title', 'short_description', 'text', 'pub_date']
		widgets = {
			'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
			'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
			'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание новости'}),
			'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'})
		}