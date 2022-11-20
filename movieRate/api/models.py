from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)
    def __str__(self):
        return self.title

    def no_of_ratings(self):
        rating = Rating.objects.filter(movie=self)
        return len(rating)

    def avg_rating(self):
        rating = Rating.objects.filter(movie=self)
        sum = 0
        try:
            for rate in rating:
                sum += rate.stars
            return sum / len(rating)
        except ZeroDivisionError:
            return 0


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)
