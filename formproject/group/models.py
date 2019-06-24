from django.db import models

class Group(models.Model):
    name = model.charField(max_length=200)
    leader = model.charField(max_length=50)
    create_date = model.charField()
    location = model.charField(max_length=200)
    introduce = model.charFilkd(max_length=1000)

# Create your models here.
