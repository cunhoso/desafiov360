from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    todo_list = models.ForeignKey(ToDoList, related_name='items', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
