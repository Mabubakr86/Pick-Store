from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image


class ReviewManger(models.Manager):

    def get_last_reviews(self,prod):
        if len(self.filter(product=prod)) > 5:
            return self.filter(product=prod)[:5]
        else: 
            return self.filter(product=prod)


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
    price = models.DecimalField(max_digits=12, decimal_places=2, 
                                null=True, blank=True)
    category = models.ManyToManyField(to='Category', null=True, blank=True)
    short_desc = models.CharField(max_length=100,null=True, blank=True)
    long_desc = models.TextField(blank=True)
    p_photo = models.ImageField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    rating = models.IntegerField(null=True, blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse(viewname='store:product', kwargs={'slug':self.slug})

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

    @property
    def get_total_items_count(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

    @property
    def get_total_items_price(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total_price for item in orderitems])
        return total 

    # def get_total_items_price(self):
    #     return self.orderItem_set.all().count()

    def __str__(self):
        return f'{self.customer.name} order'

class OrderItem(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default= timezone.now())
    quantity = models.IntegerField(default=0)

    @property
    def get_total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'{self.product.name}-{self.quantity}'


class ProductReviw(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=100)
    review = models.TextField(null=True, blank=True)
    score = models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    
    class Meta:
        ordering = ('-id',)

    objects = ReviewManger()


    def __str__(self):
        return self.product.name



