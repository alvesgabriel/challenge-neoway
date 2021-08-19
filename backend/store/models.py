from django.db import models
from django.utils.translation import gettext_lazy as _


class File(models.Model):
    filename = models.FileField()
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)


class Sale(models.Model):
    file = models.ForeignKey(File, on_delete=models.DO_NOTHING)
    buyer_doc = models.CharField(max_length=14)
    private = models.BooleanField()
    incomplete = models.BooleanField()
    ticket = models.DecimalField(null=True, max_digits=12, decimal_places=2)
    seller_doc = models.CharField(null=True, max_length=14)
    ticket_average = models.DecimalField(
        null=True,
        max_digits=12,
        decimal_places=2,
    )
    seller_doc_most_frequency = models.CharField(null=True, max_length=14)
    created_at = models.DateTimeField(null=True)
    invalid_buyer_doc = models.BooleanField()
    invalid_seller_doc = models.BooleanField()
    invalid_seller_doc_most_frequency = models.BooleanField()
