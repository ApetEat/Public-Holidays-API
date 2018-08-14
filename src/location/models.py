from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    code = models.CharField(
        _('Official code'),
        max_length=3,
        blank=False,
        unique=True,
    )
    name = models.CharField(
        _('Country'),
        max_length=50,
        blank=False,
        unique=True,
    )


    class Meta:
        verbose_name_plural = _('Countries')

    def __str__(self):
        return 'Country: {} - {}'.format(self.code, self.name)


class Region(models.Model):
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    code = models.CharField(
        _('Official code'),
        max_length=3,
        blank=False,
        unique=True,
    )
    name = models.CharField(
        _('Region'),
        max_length=100,
        blank=False,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
    )


    class Meta:
        verbose_name_plural = _('Regions')

    def __str__(self):
        return 'Region: {} - {}'.format(self.code, self.name)


class Province(models.Model):
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    code = models.CharField(
        _('Official code'),
        max_length=3,
        blank=False,
        unique=True,
    )
    name = models.CharField(
        _('Province'),
        max_length=100,
        blank=False,
    )
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return 'Province: {} - {}'.format(self.code, self.name)


class City(models.Model):
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    code = models.CharField(
        _('Official code'),
        max_length=3,
        blank=False,
        unique=True,
    )
    name = models.CharField(
        _('City'),
        max_length=200,
        blank=False,
    )
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
    )


    class Meta:
        verbose_name_plural = _('Cities')

    def __str__(self):
        return 'City: {} - {}'.format(self.code, self.name)