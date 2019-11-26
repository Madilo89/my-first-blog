from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    """
    Cette la classe grace à quoi nous allons structurer notre modele
            """
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """
        la méthode qui se chargera de la publication des données de la base de données
        """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
