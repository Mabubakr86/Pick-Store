from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 
from django.utils import timezone
from django.urls import reverse
from PIL import Image


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class CustomerProfile(models.Model):
    customer = models.OneToOneField(to=Customer, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    c_photo = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.customer.name} profile'

    class Meta:
        verbose_name_plural = 'profiles'
        ordering = ('customer',)


class Product(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, 
                                null=True, blank=True)
    category = models.ManyToManyField(to='Category', null=True, blank=True)
    short_desc = models.CharField(max_length=100,null=True, blank=True)
    long_desc = models.TextField(blank=True)
    p_photo = models.ImageField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)


    @property
    def slug(self):
        return slugify(self.name)

    def get_absolute_url(self):
        return reverse(viewname='store:product', kwargs={'pk':self.id})

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     res_photo = Image.open(self.p_photo.path)
    #     req_size = (350,350)
    #     res_photo.thumbnail(req_size)
    #     p_photo = res_photo.save(self.p_photo.path)
    #     super().save(*args,**kwargs)


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default= timezone.now())
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer.name} order'

class OrderItem(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default= timezone.now())
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name
    




