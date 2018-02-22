from django.db import models

# Create your models here.
class Link(models.Model):
    version = models.CharField(max_length=15)
    game_title = models.CharField(max_length=30)
    release_date = models.CharField(max_length=15)
    linked_text = models.CharField(max_length=500)

    def __str__(self):
        return self.version + " - " + self.game_title