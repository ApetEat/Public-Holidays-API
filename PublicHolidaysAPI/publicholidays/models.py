from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Community(models.Model): ç
    code = models.IntegerField(
        _('Official code'),
        max_length=2,
        blank=False,
        unique=True,
    )
    name = models.CharField(
        _('Autonomous Community'),
        max_length=100,
        blank=False,
    )
    country = models.CharField(
        _('Country'),
        default='Spain',
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
    code = models.IntegerField(
        _('Official code'),
        max_length=2,
        blank=False,
        unique=True,
    )
    name = models.CharField(
        _('Province'),
        max_length=100,
        blank=False,)
    community = models.ForeignKey(
        Community,
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
    code = models.IntegerField(
        _('Official code'),
        max_length=3,
        blank=False,
        unique=True,
    )
    name = models.CharField(
        _('Locality'),
        max_length=200,
        blank=False,
    )
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
    )
    dc = models.IntegerField(
        _('Control Digit'),
        max_length=1,
        blank=False,
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
    community = models.ForeignKey(
        Community,
        on_delete=models.CASCADE,
    )
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
    )
    locality = models.ForeignKey(
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
