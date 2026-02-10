from django.db import models

class Order(models.Model):
    orderId = models.CharField(max_length=20)
    bookId = models.CharField(max_length=20)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.orderId}"