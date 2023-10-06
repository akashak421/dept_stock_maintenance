from django.db import models
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/category_images', null=True, blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    # description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Chairs(models.Model):

    # Define choices for lab_name
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    # Define choices for categories
    CATEGORY1_CHOICES = (
        ('with_arm', 'With Arm'),
        ('without_arm', 'Without Arm'),
    )
    CATEGORY2_CHOICES = (
        ('steel', 'Steel'),
        ('plastic', 'Plastic'),
        ('wooden', 'Wooden'),
        ('fiber', 'Fiber'),
    )
    CATEGORY3_CHOICES = (
        ('rolling', 'Rolling'),
        ('non_rolling', 'Non-Rolling'),
    )
    
    category1 = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    category2 = models.CharField(max_length=20, choices=CATEGORY2_CHOICES)
    category3 = models.CharField(max_length=20, choices=CATEGORY3_CHOICES)
    
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name
    
class Tables(models.Model):
    # name = models.CharField(max_length=100)
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    CATEGORY1_CHOICES = (
        ('conference_table', 'Conference Table'),
        ('staff_table', 'Staff Table'),
        ('desktop_table','Desktop Table'),
    )
    CATEGORY2_CHOICES = (
        ('steel', 'Steel'),
        ('wooden', 'Wooden'),
    )
    
    category1 = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    category2 = models.CharField(max_length=20, choices=CATEGORY2_CHOICES)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name