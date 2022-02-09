from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from django.urls import reverse
from django.utils.text import slugify
from datetime import timedelta, datetime


# Create your models here.


class Client(models.Model):

    GENDER = (
        ('Male', 'Male'),
        ('Femal', 'Femal'),
    )

    RESULT = (
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
    )

    RESET = (
        ('RESET', 'RESET'),
        ('NO-RESET', 'NO-RESET'),
    )


    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_day = models.DateField()
    nationality = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=50, choices=GENDER)
    phone = models.CharField(max_length=50, blank=True)
    identification_type = models.CharField(max_length=50)
    identification_ID = models.CharField(max_length=50)
    covid_test_result = models.CharField(max_length=50, choices=RESULT)
    qr_code = models.ImageField(upload_to='qr_codes/%Y/%m/', blank=True)
    qr_url = models.URLField(blank=True)
    time_deadline = models.DateTimeField(blank=True)
    reset_deadline = models.CharField(max_length=50, choices=RESET, default='NO-RESET')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='',unique=True,editable=False,max_length=255,)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):

      #Prepopulated time_deadline field
      if self.covid_test_result == 'Positive':
          self.time_deadline = datetime.now() + timedelta(days=3)
      else:
          self.time_deadline = datetime.now()

      # Rest time Deadline
      if self.reset_deadline == 'RESET':
          self.time_deadline = datetime.now() + timedelta(days=3)
          self.reset_deadline = 'NO-RESET'
      else:
          pass

      # Prepopulated slug
      value = self.name + '-' + datetime.now().strftime('%Y-%m-%d-%f')
      self.slug = slugify(value)

      # Qr code generator
      url = self.qr_url + self.get_absolute_url()
      qrcode_img = qrcode.make(url)
      fname = f'{self.name}-qr_code.png'
      buffer = BytesIO()
      qrcode_img.save(buffer, 'PNG')
      self.qr_code.save(fname, File(buffer), save=False)
      super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('client_detail', kwargs={'slug': self.slug})
