from django.db import models

# Create your models here.
class Company(models.Model):
    using = 'logportal'
    class Meta:
        db_table = 'portal_logistics_data'
    Company_Display_Name = models.CharField(max_length=200, blank=True,
        help_text="This is will be printed in official marketing material.")
    Company_Description = models.TextField(blank=True,
        help_text="Please limit your description to <span id=\"form-description-limit\"></span> words. Longer descriptions will need to be truncated to fit in the booklet.")
    Company_Logo = models.URLField(max_length=500, blank=True,
        help_text="Higher quality logos are preferred to ensure they look great in printed material. Please upload a PNG or JPEG format image.")