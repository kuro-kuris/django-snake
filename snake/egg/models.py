from django.db import models


# encapsulating data
class Saving_Account(models.Model):
    savings_id = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)

class Milestone
