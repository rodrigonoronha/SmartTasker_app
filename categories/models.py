from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50,)
    description = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
