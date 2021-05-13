from django.db import models
from home.models import Feature

# Create your models here.

class Tutorials(models.Model):

    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    tutorial_number = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=200)
    description = models.CharField(default="Tutorial Description", max_length=500)
    url = models.URLField(max_length=500, default='https://www.youtube.com/watch?v=OmKbGOARXao')
    # file = models.FileField(upload_to='home/tutorials/uploads', max_length=254, null=True)

    class Meta:
        verbose_name = 'Tutorials'

    def __str__(self):
        return self.name