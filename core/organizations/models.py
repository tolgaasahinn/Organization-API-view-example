from accounts.models import UserModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from PIL import Image


class Organization(models.Model):
    class OrganizationType(models.TextChoices):
        PERSON = "Person", _("Person")
        CONGLOMERATE = "Conglomerate", _("Conglomerate")
        KOBI = "KOBİ", _("KOBİ")
        STK = "STK", _("STK")

    organisations_user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="organisations_user",
        null=False,
    )
    organisation_name = models.CharField(max_length=150, blank=False, null=False)
    organization_logo = models.ImageField(
        null=True, blank=True, upload_to="organization_logos/%Y/%m/"
    )

    organization_type = models.CharField(
        max_length=15, choices=OrganizationType.choices
    )
    country = CountryField()
    organization_url = models.URLField()
    number_of_employees = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.organization_logo:
            img = Image.open(self.organization_logo.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.organization_logo.path)

    def __str__(self) -> str:
        return self.organisation_name
