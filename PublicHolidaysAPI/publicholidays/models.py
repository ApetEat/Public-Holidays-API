from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .managers import PublicHolidayManager
from locations.models import Locality, Province, Community, Country


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
