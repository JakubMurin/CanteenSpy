from django.db import models

class Canteen(models.Model):
    name = models.CharField(max_length=100)
    hours = models.TextField()
    avg_rating = models.IntegerField(default=0)
    web = models.TextField()
    address = models.TextField()
    location = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=100, null=True)
    closing = models.CharField(max_length=10, default="16:00")
    low_price = models.DecimalField(max_digits=10, decimal_places=2, default=4.2)

    def __str__(self) -> str:
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    day = models.DateField(null=True)
    available = models.IntegerField(default=0)
    unavailable = models.IntegerField(default=0)
    avg_rating = models.IntegerField(default=0)
    meat = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    soup = models.BooleanField(default=False)
    canteen_id = models.ForeignKey(Canteen, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name
    
class Rating(models.Model):
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    stars = models.IntegerField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "Rating" + self.menu_id.name + " " + self.created_at.strftime("%Y-%m-%d %H:%M:%S")