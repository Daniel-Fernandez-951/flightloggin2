from django.db import models
from django.contrib.auth.models import User
from constants import *

class Profile(models.Model):
    user =           models.ForeignKey(User, primary_key=True)
				
    dob =            models.DateField(             "Date of Birth",             blank=True, default="1900-01-01")
    style =          models.IntegerField(                                       choices=STYLES, default=1)
    date_format =    models.IntegerField(          "Date Format",               choices=DATE_FORMATS, default=1)

    real_name =      models.CharField(             "Real Name",                 blank=True, max_length=32)
    per_page =       models.PositiveIntegerField(  "Logbook Entries Per Page",  default=50)
    backup_email =   models.EmailField(            "Backup Email",              blank=True, help_text="Leave blank to use the email listed above")
    backup_freq =    models.IntegerField(          "Backup Frequency",          choices=BACKUP_FREQUENCY, default=0)
    type_str =       models.CharField(                                          blank=True, max_length=128)
	
    def __unicode__(self):
        return u"%s - %s" % (self.user, self.real_name)
			
    class Meta:
        pass
