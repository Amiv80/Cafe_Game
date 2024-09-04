from django.db import models

class Member(models.Model):
    name = models.CharField(verbose_name=("Name"), max_length=50)
    vip_member = models.BooleanField(verbose_name=("VIP Members"), default=False)
    date_add = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        db_table = "Member"
        verbose_name = "Member"
        verbose_name_plural = "Members"

    def __str__(self):
        return self.name

