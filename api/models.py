from django.db import models


class Membership(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, default='')
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True, default='')
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)