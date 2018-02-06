from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Country(models.Model):
    name = models.CharField(
        _('Country'),
        max_length=100,
        blank=False,
        unique=True,
    )
    created = models.DateTimeField(
        _('Created'),
        default=timezone.now,
        editable=False,
    )
    updated = models.DateTimeField(
        _('Updated'),
        blank=True,
        null=True,
        editable=True,
    )

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class AutonomousCommunity(models.Model):
    name = models.CharField(
        _('Autonomous Community'),
        max_length=100,
        blank=False,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(
        _('Created'),
        default=timezone.now,
        editable=False,
    )
    updated = models.DateTimeField(
        _('Updated'),
        blank=True,
        null=True,
        editable=True,
    )

    class Meta:
        verbose_name = _('Autonomous Community')
        verbose_name_plural = _('Autonomous Communities')


class Province(models.Model):
    name = models.CharField(
        _('Province'),
        max_length=100,
        blank=False,
    )
    community = models.ForeignKey(
        AutonomousCommunity,
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(
        _('Created'),
        default=timezone.now,
        editable=False,
    )
    updated = models.DateTimeField(
        _('Updated'),
        blank=True,
        null=True,
        editable=True,
    )


class Locality(models.Model):
    name = models.CharField(
        _('Locality'),
        max_length=200,
        blank=False,
    )
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
    )
    is_apeteat = models.BooleanField(
        _('Is ApetEat service'),
        default=False,
    )
    created = models.DateTimeField(
        _('Created'),
        default=timezone.now,
        editable=False,
    )
    updated = models.DateTimeField(
        _('Updated'),
        blank=True,
        null=True,
        editable=True,
    )

    class Meta:
        verbose_name = _('Locality')
        verbose_name_plural = _('Localities')


class PublicHolidaysCalendar(models.Model):
    date = models.DateTimeField(
        _('Date'),
        blank=True,
        null=True,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
    )
    community = models.ForeignKey(
        AutonomousCommunity,
        on_delete=models.CASCADE,
    )
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
    )
    localities = models.ForeignKey(
        Locality,
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(
        _('Created'),
        default=timezone.now,
        editable=False,
    )
    updated = models.DateTimeField(
        _('Updated'),
        blank=True,
        null=True,
        editable=True,
    )
