from django.db import models 

class Level(models.Model):
    level_id = models.BigAutoField(primary_key=True, blank=False)
    year_level = models.CharField(max_length=55, blank=False)
    
    class Meta:
        db_table = 'level'
        
class Students(models.Model):
    student_id = models.BigAutoField(primary_key=True, blank=False)
    first_name = models.CharField(max_length=55, blank=55)
    middle_name = models.CharField(max_length=55, blank=True)
    last_name = models.CharField(max_length=55, blank=False)
    age = models.IntegerField(blank=False)
    birth_date = models.DateTimeField(blank=False)
    year_level = models.CharField(max_length=55, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)    
    
    class Meta:
        db_table = 'users' 