from django.test import TestCase
from django.core.mail import send_mail
from django.conf import settings

settings.configure()
send_mail('Test Mail', 'hello user', 'akshbusinessemail@gmail.com', ['sisodiyaaksh@gmail.com'])

# send_mail('Test','body','akshbusinessemail@gmail.com',['sisodiyaaksh@gmail.com'],fail_silently=False)