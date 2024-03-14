from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    progress = models.IntegerField()
    isDisabled = models.BooleanField(default=False)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    project_manager_name = models.CharField(max_length=100)
    project_manager_email = models.EmailField()
    project_manager_phone = models.CharField(max_length=20)
    architect_name = models.CharField(max_length=100)
    architect_email = models.EmailField()
    architect_phone = models.CharField(max_length=20)
    engineer_name = models.CharField(max_length=100)
    engineer_email = models.EmailField()
    engineer_phone = models.CharField(max_length=20)
    contractor_name = models.CharField(max_length=100)
    contractor_email = models.EmailField()
    contractor_phone = models.CharField(max_length=20)
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    timeline = models.CharField(max_length=50)
    scope_of_work = models.TextField()
    permits_and_approvals = models.TextField()
    labor = models.IntegerField()
    equipment = models.CharField(max_length=200)
    safety_measures = models.TextField()
    environmental_impact = models.TextField()
    stakeholders = models.TextField()
    risk_assessment = models.TextField()
    quality_control = models.TextField()
    progress_reports = models.TextField()
    dependencies = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name

