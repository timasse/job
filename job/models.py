from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

STATUS = (
    ('1','Standby'),
    ('2','Fait'),
    ('3','Cancel'),
)
class Job(models.Model):
	
	title = models.CharField('Num. du client', max_length = 250)
	description = models.TextField('Description', max_length = 250)
	client_name = models.CharField('Nom du client', max_length = 250)
	client_address = models.CharField('Adresse du client', max_length = 250)
	client_phone = models.IntegerField('Numéro de téléphone du client', max_length = 250)
	#picture = models.ImageField('Photo', upload_to="job_photo")
	#pdf = models.FileField('PDF', upload_to="job_pdf")
	date = models.DateTimeField('Date', default=datetime.now)
	status = models.CharField(max_length=250,choices=STATUS)
	user = models.ForeignKey( User, unique=True, blank=True)

	def __str__(self):
		return self.title
		
	def get_job_images(self):
	    images = JobImage.objects.filter(job = self)
	    return images
	def get_job_pdfs(self):
	    pdfs = JobPdf.objects.filter(job = self)
	    return pdfs
		
class JobImage(models.Model):
    job = models.ForeignKey(Job, related_name='images')
    image = models.ImageField()
	
class JobPdf(models.Model):
    job = models.ForeignKey(Job, related_name='pdf')
    pdf = models.FileField()
