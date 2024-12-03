from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, verbose_name="Город")
    address = models.CharField(max_length=255, verbose_name="Улица, дом")
    postal_code = models.CharField(max_length=12, verbose_name="Почтовый индекс")

    def __str__(self):
        return f"{self.postal_code}, {self.city}, {self.address}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    tel = models.CharField(max_length=11, blank=True, verbose_name="Телефон")

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def update_profile(sender, instance, **kwargs):
    instance.profile.save()




