from django.db import models

class Day(models.Model):
    ALIAS_CHOICES = ['F', 'E', 'D', 'C', 'B', 'A', 'S']

    alias = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    activities = models.TextField()
    
    # New fields for ratings
    workout = models.CharField(max_length=1, choices=[(choice, choice) for choice in ALIAS_CHOICES], default='F')
    academic = models.CharField(max_length=1, choices=[(choice, choice) for choice in ALIAS_CHOICES], default='D')
    sr = models.CharField(max_length=1, choices=[(choice, choice) for choice in ALIAS_CHOICES], default='D')
    economics = models.CharField(max_length=1, choices=[(choice, choice) for choice in ALIAS_CHOICES], default='C')

    def __str__(self):
        return self.alias