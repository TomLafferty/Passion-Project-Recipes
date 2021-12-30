from django.db import models

# Create your models here.

class Recipe(models.Model):
    author = models.CharField(max_length=60)
    title = models.CharField(max_length=150)
    intro = models.TextField()
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    servings = models.IntegerField()

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

 
class Category(models.Model):
    name = models.CharField(max_length=20)
 
# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     last_modified = models.DateTimeField(auto_now=True)
#     categories = models.ManyToManyField('Category', related_name='posts')

# class Comment(models.Model):
#     author = models.CharField(max_length=60)
#     body = models.TextField()
    # created_on = models.DateTimeField(auto_now_add=True)
    # post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.name