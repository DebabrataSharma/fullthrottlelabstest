from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.CharField(primary_key=True, max_length=9)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(default='Asia/Kolkata', max_length=40)

    def __str__(self):
        return self.real_name

class ActivityPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='activity_period')

    class Meta:
        verbose_name = 'ActivityPeriod'
        verbose_name_plural = 'ActivityPeriods'

    def __str__(self):
        return "{'start_time': %s, 'end_time': %s}" %(repr(self.start_time.strftime("%b %d, %Y %I:%M%p")), repr(self.end_time.strftime("%b %d, %Y %I:%M%p")))