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

    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    # Define choices for categories
    ARM_CHOICES = (
        ('with_arm', 'With Arm'),
        ('without_arm', 'Without Arm'),
    )
    MATERIAL_CHOICES = (
        ('steel', 'Steel'),
        ('plastic', 'Plastic'),
        ('wooden', 'Wooden'),
        ('fiber', 'Fiber'),
    )
    ROLLING_CHOICES = (
        ('rolling', 'Rolling'),
        ('non_rolling', 'Non-Rolling'),
    )

    arm_type = models.CharField(max_length=20, choices=ARM_CHOICES)
    material_type = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    roll_type = models.CharField(max_length=20, choices=ROLLING_CHOICES)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Chairs.objects.filter(id__startswith=f'{lab_prefix}-FU-CHA-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-FU-CHA-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Chairs, self).save(*args, **kwargs)
    def __str__(self):
        return self.lab_name

class Tables(models.Model):
    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
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
    
    table_type = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    material_type = models.CharField(max_length=20, choices=CATEGORY2_CHOICES)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Tables.objects.filter(id__startswith=f'{lab_prefix}-FU-TAB-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-FU-TAB-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Tables, self).save(*args, **kwargs)

    def __str__(self):
        return self.lab_name

class Board(models.Model):
    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
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

    board_type = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    material_type = models.CharField(max_length=20, choices=CATEGORY2_CHOICES)
    installation_type = models.CharField(max_length=20, choices=CATEGORY3_CHOICES)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Board.objects.filter(id__startswith=f'{lab_prefix}-FU-BOA-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-FU-BOA-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Board, self).save(*args, **kwargs)
    def __str__(self):
        return self.lab_name

class Cupboard(models.Model):
    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
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

    cupboard_type = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    size = models.CharField(max_length=20, choices=CATEGORY2_CHOICES)
    door_type = models.CharField(max_length=20, choices=CATEGORY3_CHOICES)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Cupboard.objects.filter(id__startswith=f'{lab_prefix}-MFU-CUB-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-FU-CUB-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Cupboard, self).save(*args, **kwargs)
    def __str__(self):
        return self.lab_name


#-------------------------------- starting of consumables... ------------------------------------------

class Keyboard(models.Model):
    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    
    CATEGORY1_CHOICES = (
        ('Wireless_keyboard', 'Wireless keyboard'),
        ('ps/2 keyboard', 'ps/2 keyboard'),
        ('usb_keyboard','usb keyboard'),
    )
    BRAND_CHOICES = (
        ('ASUS','ASUS'),
        ('Logitech','Logitech'),
        ('HP (Hewlett-Packard)','HP (Hewlett-Packard)'),
        ('Dell','Dell'),
        ('Microsoft','Microsoft'),
        ('Other','Other')
    )
    keyboard_type = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Keyboard.objects.filter(id__startswith=f'{lab_prefix}-CO-KEY-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-CO-KEY-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Keyboard, self).save(*args, **kwargs)
    def __str__(self):
        return self.lab_name



class Mouse(models.Model):
    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    
    CATEGORY1_CHOICES = (
        ('Wireless_Mouse', 'Wireless Mouse'),
        ('ps/2 Mouse', 'ps/2 Mouse'),
        ('usb_Mouse','usb Mouse'),
    )
    BRAND_CHOICES = (
        ('ASUS','ASUS'),
        ('Logitech','Logitech'),
        ('HP (Hewlett-Packard)','HP (Hewlett-Packard)'),
        ('Dell','Dell'),
        ('Microsoft','Microsoft'),
        ('Other','Other')
    )
    mouse_type = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Mouse.objects.filter(id__startswith=f'{lab_prefix}-CO-MOU-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-CO-MOU-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Mouse, self).save(*args, **kwargs)
    def __str__(self):
        return self.lab_name



class Camera(models.Model):
    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    
    CATEGORY1_CHOICES = (
        ('Webcam', 'Webcam'),
        ('Video_Conference_Cam', 'Video_Conference_Cam'),
    )
    BRAND_CHOICES = (
        ('Cisco','Cisco'),
        ('Logitech','Logitech'),
        ('HP (Hewlett-Packard)','HP (Hewlett-Packard)'),
        ('Sony','Sony'),
        ('Microsoft','Microsoft'),
        ('Other','Other')
    )
    web_cam_type = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Camera.objects.filter(id__startswith=f'{lab_prefix}-CO-CAM-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-CO-CAM-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Camera, self).save(*args, **kwargs)
    def __str__(self):
        return self.lab_name



# ------------------ Electrical items -----------------


class TubeLight(models.Model):
    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    
    CATEGORY1_CHOICES = (
        ('LED Bulb', 'LED Bulb'),
        ('electrical choke', 'Electrical choke'),
        ('only choke','only choke'),

    )
    light_type = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = TubeLight.objects.filter(id__startswith=f'{lab_prefix}-EQ-LIG-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-EQ-LIG-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(TubeLight, self).save(*args, **kwargs)
    def __str__(self):
        return self.lab_name


class Fan(models.Model):
    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    
    CATEGORY1_CHOICES = (
        ('ceiling', 'ceiling'),
        ('wall mount', 'wall mount'),
        ('Stand type','Stand type'),

    )
    fan_type = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Fan.objects.filter(id__startswith=f'{lab_prefix}-EQ-FAN-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-EQ-FAN-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Fan, self).save(*args, **kwargs)
    def __str__(self):
        return self.lab_name


class Cctv(models.Model):
    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
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
    camera_type = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    camera_mode = models.CharField(max_length=20, choices=CATEGORY2_CHOICES)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Cctv.objects.filter(id__startswith=f'{lab_prefix}-EQ-CCT-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-EQ-CCT-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Cctv, self).save(*args, **kwargs)
    def __str__(self):
        return self.lab_name



class Biometric(models.Model):
    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    
    CATEGORY1_CHOICES = (
        ('FingerPrint', 'FingerPrint'),
        ('EyeBall', 'EyeBall'),
    )
    BRAND_CHOICES = (
        ('ZKTeco', 'ZKTeco'),
        ('Suprema', 'Suprema'),
        ('HID Global','HID Global'),
        ('Morpho (Safran)', 'Morpho (Safran)'),
        ('Crossmatch', 'Crossmatch'),
        ('Other', 'Other'),
    )
    MODEL_CHOICES = (
        ('ZKTeco SF300', 'ZKTeco SF300'),
        ('Suprema BioLite N2', 'Suprema BioLite N2'),
        ('HID Global Lumidigm V371', 'HID Global Lumidigm V371'),
        ('Morpho (Safran) MSO 1300 E2', 'Morpho (Safran) MSO 1300 E2'),
        ('Crossmatch Verifier 320 LC', 'Crossmatch Verifier 320 LC'),
        ('Other','Other'),
    )
    biometric_type = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)
    model = models.CharField(max_length=255, choices=MODEL_CHOICES)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Biometric.objects.filter(id__startswith=f'{lab_prefix}-EQ-BIO-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-EQ-BIO-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Biometric, self).save(*args, **kwargs)
    def __str__(self):
        return self.lab_name


#--------------------Capital Equipments ----------------------------

class Monitor(models.Model):
    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
    )
    BRAND_CHOICES = (
        ('Dell', 'Dell'),
        ('HP', 'HP'),
        ('LG', 'LG'),
        ('Acer', 'Acer'),
        ('Other', 'Other'),
    )
    MODEL_CHOICES = (
        ('Dell Ultrasharp U2719DX', 'Dell Ultrasharp U2719DX'),
        ('HP Pavilion 22CWA', 'HP Pavilion 22CWA'),
        ('LG 27UK850-W', 'LG 27UK850-W'),
        ('Acer Predator X27', 'Acer Predator X27'),
        ('Other', 'Other')
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    model = models.CharField(max_length=50, choices=MODEL_CHOICES)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Monitor.objects.filter(id__startswith=f'{lab_prefix}-CE-MON-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-CE-MON-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Monitor, self).save(*args, **kwargs)
    def __str__(self):
        return self.lab_name


class Cpu(models.Model):
    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
    )
    BRAND_CHOICES = (
        ('IBM', 'IBM'),
        ('Qualcomm', 'Qualcomm'),
        ('AMD (Advanced Micro Devices)', 'AMD (Advanced Micro Devices)'),
        ('Intel', 'Intel'),
        ('Other', 'Other'),
    )
    lab_name = models.CharField(max_length=50, choices=LAB_CHOICES)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Cpu.objects.filter(id__startswith=f'{lab_prefix}-CE-CPU-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-CE-CPU-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Cpu, self).save(*args, **kwargs)
    def __str__(self):
        return self.lab_name

class Network_Switch(models.Model):
    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    CATEGORY1_CHOICES = (
        ('Fast Ethernet Switch', 'Fast Ethernet Switch'),
        ('Gigabit Ethernet Switch', 'Gigabit Ethernet Switch'),
        ('Smart Switch', 'Smart Switch'),
        ('Layer 3 Switch', 'Layer 3 Switch'),
        ('Layer 2 Switch', 'Layer 2 Switch'),
        ('Other', 'Other'),
    )
    BRAND_CHOICES = (
        ('TP-Link', 'TP-Link'),
        ('HPE (Hewlett Packard Enterprise)', 'HPE (Hewlett Packard Enterprise)'),
        ('Ubiquiti', 'Ubiquiti'),
        ('D-Link', 'D-Link'),
        ('Huawei', 'Huawei'),
        ('Other', 'Other'),
    )
    MODEL_CHOICES = (
        ('TP-Link Smart Series', 'TP-Link Smart Series'),
        ('HPE FlexNetwork 5130 Series', 'HPE FlexNetwork 5130 Series'),
        ('Ubiquiti EdgeSwitch Series', 'Ubiquiti EdgeSwitch Series'),
        ('D-Link DGS Series:', 'D-Link DGS Series:'),
        ('Huawei S5700 Series:', 'Huawei S5700 Series:'),
        ('Other', 'Other'),
    )
    switch_type = models.CharField(max_length=50, choices=CATEGORY1_CHOICES)
    brand = models.CharField(max_length=50, choices=MODEL_CHOICES)
    model = models.CharField(max_length=50, choices=BRAND_CHOICES)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('Scrap','Scrap'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Network_Switch.objects.filter(id__startswith=f'{lab_prefix}-CE-NTS-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-CE-NTS-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Network_Switch, self).save(*args, **kwargs)
    def __str__(self):
        return self.lab_name

#------------------------miscellaneous---------------------------


class Projector(models.Model):
    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
    )
    BRAND_CHOICES = (
        ('Epson','Epson'),
        ('Sony','Sony'),
        ('ViewSonic','ViewSonic'),
        ('LG','LG'),
        ('Other','Other'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)

    Mounting_Options = (
        ('wall mounts', 'wall mounts'),
        ('ceiling mounts', 'ceiling mounts'),
        ('tripod mounts', 'tripod mounts'),
    )

    mounting_options = models.CharField(max_length=20, choices=Mounting_Options)


    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('Scrap','Scrap'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Projector.objects.filter(id__startswith=f'{lab_prefix}-MI-PRO-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-MI-PRO-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Projector, self).save(*args, **kwargs)

    def __str__(self):
        return self.lab_name


class Printer(models.Model):
    id=models.CharField(max_length=14,primary_key=True)

    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
    )
    BRAND_CHOICES = (
        ('Dell', 'Dell'),
        ('Samsung', 'Samsung'),
        ('Epson', 'Epson'),
        ('Canon', 'Canon'),
        ('HP (Hewlett-Packard)', 'HP (Hewlett-Packard)'),
        ('Other', 'Other'),
    )
    MODEL_CHOICES = (
        ('Dell C1760nw', 'Dell C1760nw'),
        ('Samsung Xpress C1860FW', 'Samsung Xpress C1860FW'),
        ('Epson EcoTank ET-2760', 'Epson EcoTank ET-2760'),
        ('Canon PIXMA TS9120', 'Canon PIXMA TS9120'),
        ('HP LaserJet Pro M281fdw', 'HP LaserJet Pro M281fdw'),
        ('Other', 'Other'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)
    brand = models.CharField(max_length=255, choices=BRAND_CHOICES)
    model = models.CharField(max_length=255, choices=MODEL_CHOICES)



    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('Scrap','Scrap'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Printer.objects.filter(id__startswith=f'{lab_prefix}-MI-PRI-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-MI-PRI-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Printer, self).save(*args, **kwargs)

    def __str__(self):
        return self.lab_name


class Socket(models.Model):
    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
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
        ('10_AMP', '10_AMP'),
        ('15_AMP', '15_AMP'),
        ('20_AMP', '20_AMP'),
        ('25_AMP', '25_AMP'),
    )
    material_type = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    model = models.CharField(max_length=20, choices=CATEGORY2_CHOICES)
    capacity = models.CharField(max_length=20, choices=CATEGORY3_CHOICES)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('Scrap','Scrap'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Socket.objects.filter(id__startswith=f'{lab_prefix}-MI-SOC-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-MI-SOC-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Socket, self).save(*args, **kwargs)

    def __str__(self):
        return self.lab_name

class Projector_Screen(models.Model):
    id=models.CharField(max_length=14,primary_key=True)
    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    BRAND_CHOICES = (
        ('Screen Innovations', 'Screen Innovations'),
        ('Elite Screens', 'Elite Screens'),
        ('Visual Apex', 'Visual Apex'),
        ('Grandview', 'Grandview'),
        ('Other', 'Other'),
    )
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('Scrap','Scrap'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Projector_Screen.objects.filter(id__startswith=f'{lab_prefix}-MI-SCR-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-MI-SCR-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Projector_Screen, self).save(*args, **kwargs)

    def __str__(self):
        return self.lab_name


class Extension_Box(models.Model):
    id=models.CharField(max_length=14,primary_key=True)

    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
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
        ('10_AMP', '10_AMP'),
        ('15_AMP', '15_AMP'),
        ('20_AMP', '20_AMP'),
        ('25_AMP', '25_AMP'),
    )
    material_type = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    model = models.CharField(max_length=20, choices=CATEGORY2_CHOICES)
    ampere_rating = models.CharField(max_length=20, choices=CATEGORY3_CHOICES)

   

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('Scrap','Scrap'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Extension_Box.objects.filter(id__startswith=f'{lab_prefix}-MI-EXT-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-MI-EXT-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Extension_Box, self).save(*args, **kwargs)

    def __str__(self):
        return self.lab_name


class Connecting_Wire(models.Model):
    id=models.CharField(max_length=14,primary_key=True)

    LAB_CHOICES = (
        ('cclab', 'CC Lab'),
        ('ibmlab', 'IBM Lab'),
        ('islab', 'IS Lab'),
        ('projectlab', 'Project Lab'),
        ('researchlab', 'Research Lab'),
    )
    lab_name = models.CharField(max_length=20, choices=LAB_CHOICES)

    CATEGORY1_CHOICES = (
        ('HDMI', 'HDMI'),
        ('VGA', 'VGA'),
        ('USB', 'USB'),
        ('RJ_45', 'RJ_45'),
        ('OTHERS', 'OTHERS'),
    )

    wire_type = models.CharField(max_length=20, choices=CATEGORY1_CHOICES)
    quantity = models.IntegerField(null=True, blank=True)

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('Scrap','Scrap'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.id:
            lab_prefix = self.lab_name[:2].upper()

            # Get the maximum existing ID with the same prefix and suffix
            max_id = Connecting_Wire.objects.filter(id__startswith=f'{lab_prefix}-MI-WIR-').aggregate(models.Max('id'))
            if max_id['id__max']:
                # Extract the count from the maximum ID and increment it by 1
                count = int(max_id['id__max'].split('-')[-1]) + 1
            else:
                # If no existing records, start the count from 1
                count = 1

            # Create the new ID
            self.id = f'{lab_prefix}-MI-WIR-{count:04d}'  # Combine lab prefix, lab suffix, and count with leading zeros

        super(Connecting_Wire, self).save(*args, **kwargs)

    def __str__(self):
        return self.lab_name