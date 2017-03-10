import operator
from .models import Word, Dictionary, Item
import re, math
from nltk import FreqDist, WordNetLemmatizer
from nltk.corpus import stopwords


def create_dictionary(string, item):

    # leave only ASCII A-Za-z0-9:
    string = re.sub(r'[\W_]+', ' ', string)
    my_stopwords = stopwords.words('english')
    word_list = string.lower().split()
    wnl = WordNetLemmatizer()
    filtered_word_list = []
    for word in word_list:  # iterate over word_list
        if word not in my_stopwords:
            filtered_word_list.append(wnl.lemmatize(word))  # insert word from word_list if it is a stopword

    item.count_of_terms = len(filtered_word_list)
    item.save()
    fdist = FreqDist(filtered_word_list)
    for word in filtered_word_list:
        if len(word) > 1:
            new_word = Word.objects.get_or_create(word=word)[0]
            dictionary = Dictionary.objects.get_or_create(word=new_word, item=item, count=fdist[word])[0]
            dictionary.save()


        # for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        #     print(key, value)


def analyze_dictionary():

    all_words = Word.objects.all()
    count_of_items = Item.objects.count()
    for word in all_words:
        df = Dictionary.objects.filter(word__word=word).count()
        if df:
            word.idf = math.log2(count_of_items / df)
            word.save()
    for dict in Dictionary.objects.all():
        tf = dict.count / dict.item.count_of_terms
        dict.weight = dict.word.idf * tf
        dict.save()


def clean_database():
    Word.objects.all().delete()
    Dictionary.objects.all().delete()
    Item.objects.all().delete()
