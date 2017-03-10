from django.db import models
from django.core.urlresolvers import reverse


class Item(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=500)
    image = models.CharField(max_length=1000)
    description = models.CharField(max_length=5000)
    price = models.IntegerField()
    count_of_terms = models.IntegerField(default=0)
    size = models.FloatField(default=10)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('search:detail', kwargs={'pk': self.pk})


class Word(models.Model):
    word = models.CharField(max_length=25)
    idf = models.FloatField(default=0)  # inverse document frequency

    def __str__(self):
        return self.word


class Dictionary(models.Model):
    count = models.IntegerField(default=0)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    weight = models.FloatField(default=0)

    def __str__(self):
        return str(self.item.title) + ' ' + str(self.word.word)

    class Meta:
        ordering = ['-weight', 'word']
