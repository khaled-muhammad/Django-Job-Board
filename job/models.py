from django.db import models

# Create your models here.

JTchoices = (
    ("Full time job", "Full time job"),
    ("Part time job", "Part time job")
)

class job(models.Model):
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=20, choices=JTchoices)
    job_description = models.TextField(max_length=1000)
    job_published_at = models.DateTimeField(auto_now=True)
    job_vacancy = models.IntegerField(default=1)
    job_salary = models.IntegerField(default=0)
    job_category = models.ForeignKey('job_category', on_delete=models.CASCADE)
    exprience = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class job_category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name