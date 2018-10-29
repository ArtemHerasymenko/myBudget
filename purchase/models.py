from django.db import models

# Create your models here.


class Purchase(models.Model):
    name = models.CharField(max_length = 200, blank = False, null = False)
    moneyAmount = models.IntegerField(default = 0)
    whenWasMade = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
    	return self.name