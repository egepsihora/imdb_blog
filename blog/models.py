from django.db import models
from django.utils import timezone


# class Country(models.Model):
#     name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name


# class Role(models.Model):
#     ROLES_TITLE = (
#         ('D', 'Director'),
#         ('P', 'Player'),
#     )
#     role_title = models.CharField(max_length=2, choices=ROLES_TITLE)


# class Person(models.Model):
#     name = models.CharField(max_length=200)
#     born_date = models.DateTimeField()
#     born_place = models.CharField(max_length=50)
#     citizenship = models.ForeignKey(Country, on_delete=models.CASCADE)
#     nationality = models.CharField(max_length=50)
#     awards = models.CharField(max_length=400)
#
#     def __str__(self):
#         return self.name

#
# class Film(models.Model):
#     title = models.CharField(max_length=200)
#     director = models.ForeignKey(Person, on_delete=models.CASCADE)
#     created_date = models.DateTimeField()
#     cast_list = models.ForeignKey(Cast, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title





class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

