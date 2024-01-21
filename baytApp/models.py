from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    companyName = models.CharField(max_length=200)
    companyRegion = models.CharField(max_length=200)
    salaryRange = models.CharField(max_length=200)     
    jobDescription = models.CharField(max_length=900)
    applicationDate= models.CharField(max_length=200)
    jobRequirements = models.CharField(max_length=900)
    applicationLink = models.CharField(max_length=400)

    def __str__(self):
        return self.name
