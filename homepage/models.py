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
    image = models.ImageField(upload_to='media/item_images', null=True, blank=True)
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

class Board(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    CATEGORY1_CHOICES = (
        ('White_Board', 'White Board'),
        ('Black_Board', 'Black Board'),
        ('Notice_Board','Notice Board'),
    )
    CATEGORY2_CHOICES = (
        ('steel', 'Steel'),
        ('wooden', 'Wooden'),
    )
    CATEGORY3_CHOICES = (
        ('close_type', 'Close Type'),
        ('normal_type', 'Normal Type'),
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

class Cupboard(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    
    CATEGORY1_CHOICES = (
        ('steel_Cupboard', 'Steel Cupboard'),
        ('wooden_Cupboard', 'Wooden Cupboard'),
    )
    CATEGORY3_CHOICES = (
        ('No Door', 'No Door'),
        ('Glass_Door', 'Glass Door'),
        ('Steel_Door','Steel Door'),
    )
    CATEGORY2_CHOICES = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large','Large'),
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


#-------------------------------- starting of consumables... ------------------------------------------

class Keyboard(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    
    CATEGORY1_CHOICES = (
        ('Wireless_keyboard', 'Wireless keyboard'),
        ('ps/2 keyboard', 'ps/2 keyboard'),
        ('usb_keyboard','usb keyboard'),
    )
    category1 = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    brand = models.CharField(max_length=255, blank=False)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name



class Mouse(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    
    CATEGORY1_CHOICES = (
        ('Wireless_Mouse', 'Wireless Mouse'),
        ('ps/2 Mouse', 'ps/2 Mouse'),
        ('usb_Mouse','usb Mouse'),
    )
    category1 = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    brand = models.CharField(max_length=255, blank=True)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name



class Camera(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    
    CATEGORY1_CHOICES = (
        ('Webcam', 'Webcam'),
        ('Video_Conference_Cam', 'Video_Conference_Cam'),

    )
    category1 = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    brand = models.CharField(max_length=255, blank=True)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name



# ------------------ Electrical items -----------------


class TubeLight(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    
    CATEGORY1_CHOICES = (
        ('LED Bulb', 'LED Bulb'),
        ('electrical choke', 'Electrical choke'),
        ('only choke','only choke'),

    )
    category1 = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name


class Fan(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    
    CATEGORY1_CHOICES = (
        ('ceiling', 'ceiling'),
        ('wall mount', 'wall mount'),
        ('Stand type','Stand type'),

    )
    category1 = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name


class Cctv(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    
    CATEGORY1_CHOICES = (
        ('Dome Camera', 'Dome Camera'),
        ('Bullet Camera', 'Bullet Camera'),
        ('PTZ Camera','PTZ Camera'),
        ('Box Camera','Box Camera'),
        ('IP camera','IP camera'),

    )
    CATEGORY2_CHOICES = (
        ('IR camera', 'IR camera'),
        ('Normal', 'Normal'),


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



class Biometric(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    
    CATEGORY1_CHOICES = (
        ('FingerPrint', 'FingerPrint'),
        ('EyeBall', 'EyeBall'),
       

    )
    
    category1 = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    brand = models.CharField(max_length=255, blank=True)    
    model = models.CharField(max_length=255, blank=True)    

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name


#--------------------Capital Equipments ----------------------------

class Monitor(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)
    # category1 = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    brand = models.CharField(max_length=255, blank=True)    
    model = models.CharField(max_length=255, blank=True)    

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name


class Cpu(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)
    # category1 = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    brand = models.CharField(max_length=255, blank=True)    
       

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name

class Network_Switch(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    CATEGORY1_CHOICES = (
        ('', ''),
        ('', ''),
    )
    CATEGORY2_CHOICES = (
        ('', ''),
        ('', ''),
    )
    category1 = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    category2 = models.CharField(max_length=20, choices=CATEGORY2_CHOICES)
    brand = models.CharField(max_length=255, blank=True)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('Scrap','Scrap'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name

#------------------------miscellaneous---------------------------


class Projector(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)
    brand = models.CharField(max_length=255, blank=True)

    Mounting_Options = (
        ('wall mounts', 'wall mounts'),
        ('ceiling mounts', 'ceiling mounts'),
        ('tripod mounts', 'tripod mounts'),
    )

    Mounting_Options = models.CharField(max_length=20, choices=Mounting_Options)
    

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('Scrap','Scrap'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name


class Printer(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)
    brand = models.CharField(max_length=255, blank=True)
    model = models.CharField(max_length=255, blank=True)



    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('Scrap','Scrap'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name


class Socket(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    CATEGORY1_CHOICES = (
        ('Steel', 'Steel'),
        ('Fiber', 'Fiber'),
        ('Wooden', 'Wooden'),
    )
    CATEGORY2_CHOICES = (
        ('2_model', '2_model'),
        ('4_model', '4_model'),
        ('6_model', '6_model'),
        ('8_model', '8_model'),
    )
    CATEGORY3_CHOICES = (
        ('5_AMP', '5_AMP'),
        ('15_AMP', '15_AMP'),
        
    )
    category1 = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    category2 = models.CharField(max_length=20, choices=CATEGORY2_CHOICES)
    category3 = models.CharField(max_length=20, choices=CATEGORY3_CHOICES)

   

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('Scrap','Scrap'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name

class Projector_Screen(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    CATEGORY1_CHOICES = (
        ('Tripod', 'Tripod'),
        ('Wall_Mount', 'Wall_Mount'),
    )

    category1 = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    brand = models.CharField(max_length=255, blank=True)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('Scrap','Scrap'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name


class Extension_Box(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    CATEGORY1_CHOICES = (
        ('Steel', 'Steel'),
        ('Fiber', 'Fiber'),
        ('Wooden', 'Wooden'),
    )
    CATEGORY2_CHOICES = (
        ('2_model', '2_model'),
        ('4_model', '4_model'),
        ('6_model', '6_model'),
        ('8_model', '8_model'),
    )
    CATEGORY3_CHOICES = (
        ('5_AMP', '5_AMP'),
        ('15_AMP', '15_AMP'),
        
    )
    category1 = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    category2 = models.CharField(max_length=20, choices=CATEGORY2_CHOICES)
    category3 = models.CharField(max_length=20, choices=CATEGORY3_CHOICES)

   

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('Scrap','Scrap'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name


class Connecting_Wire(models.Model):
    LAB_CHOICES = (
        ('cc', 'CC Lab'),
        ('ibm', 'IBM Lab'),
        ('is', 'IS Lab'),
        ('project', 'Project Lab'),
        ('research', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    CATEGORY1_CHOICES = (
        ('HDMI', 'HDMI'),
        ('VGA', 'VGA'),
        ('USB', 'USB'),
        ('RJ_45', 'RJ_45'),
        ('OTHERS', 'OTHERS'),
    )

    category1 = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    quantity = models.IntegerField(null=True, blank=True)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('Scrap','Scrap'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.lab_name

    






