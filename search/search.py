from .models import Dictionary, Word


def search(string):
    items, dicts, words = [], [], []
    if not string:
        return items
    words = string.lower().split()

    dicts = Word.objects.get(word=string.lower()).dictionary_set.all()
    for dictionary in dicts:
        print(dictionary.item)
        items.append(dictionary.item)
    return items




