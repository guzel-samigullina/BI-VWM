from .models import Item, Word
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from .scraper import trade_spider
from .search import search


def index(request):
    words_for_search = request.POST.get('query', '')
    all_items = search(words_for_search) or Item.objects.all()
    # all_words = Word.objects.all()
    all_words = []
    return render(request, 'index.html', {'all_items': all_items, 'words_for_search': words_for_search, 'all_words': all_words})


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'detail.html', {'item': item})


def results_of_search(request, word):
    return render(request, 'index.html', {'word': word})


def crawler(request):
    trade_spider(1)
    return index(request)


class DetailView(generic.DetailView):
    model = Item
    template_name = 'detail.html'


class ItemCreate(CreateView):
    model = Item
    fields = ['title', 'url', 'image', 'price']



