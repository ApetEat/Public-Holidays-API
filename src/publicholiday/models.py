from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from location.models import City


class PublicHoliday(models.Model):
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        db_index=True
    )
    date = models.DateField(
        _('Date'),
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['date']
        verbose_name = _('Public Holiday')
        verbose_name_plural = _('Public Holidays')


    def __str__(self):
        return 'Public holiday: {} - {}'.format(self.date, self.city.name)