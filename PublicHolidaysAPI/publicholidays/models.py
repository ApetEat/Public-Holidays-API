from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .managers import PublicHolidayManager

# Create your models here.


class Country(models.Model):
    code = models.CharField(
        _('Official code'),
        max_length=2,
        blank=False,
        unique=True,
    )
    name = models.CharField(
        _('Country'),
        max_length=50,
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
        verbose_name_plural = _('Countries')

    def __str__(self):
        return 'Country: {} - {}'.format(self.code, self.name)


class Community(models.Model):
    code = models.IntegerField(
        _('Official code'),
        blank=False,
        unique=True,
    )
    name = models.CharField(
        _('Community'),
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
        verbose_name_plural = _('Communities')

    def __str__(self):
        return 'Community: {} - {}'.format(self.code, self.name)


class Province(models.Model):
    code = models.IntegerField(
        _('Official code'),
        blank=False,
        unique=True,
    )
    name = models.CharField(
        _('Province'),
        max_length=100,
        blank=False,
    )
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

    def __str__(self):
        return 'Province: {} - {}'.format(self.code, self.name)


class Locality(models.Model):
    code = models.IntegerField(
        _('Official code'),
        blank=False,
        unique=False,
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
        blank=True,
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
        verbose_name_plural = _('Localities')

    def __str__(self):
        return 'Locality: {} - {}'.format(self.code, self.name)


class PublicHolidayCalendar(models.Model):
    date = models.DateField(
        _('Date'),
        blank=False,
        null=False,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
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

    class Meta:
        ordering = ['date']
        verbose_name = _('Public Holiday Calendar')
        verbose_name_plural = _('Public Holiday Calendars')

    objects = PublicHolidayManager()

    def __str__(self):
        return 'Public holiday: {} - {}'.format(self.date, self.locality)
