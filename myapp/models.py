from django.db import models

STATUS = (
    ('yetkazib berilgan', 'Yetkazib berilgan'),
    ('tayyorlanyabdi','Tayyorlanyabdi'),
)

# Create your models here.
class MyModel(models.Model):
#     """
#     bu mening birinchi modilim
    # """
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']# Adan Z gacha terib beradi
        verbose_name_plural = 'Mening Modelim'# Model nomini o'zgartirib beradi
    def __str__(self):
        return self.name
class Dostavka(models.Model):# Dostavka uchun 
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)#maxsulotning nomi
    count = models.PositiveIntegerField(default=1, null=True, blank=True)
    price =models.PositiveIntegerField(default=0, null= True, blank=True)
    all_price =models.PositiveIntegerField(default=0, null= True, blank=True)
    location = models.CharField(max_length=255)#qayerga yetkazib berishi
    created_at = models.DateTimeField(auto_now_add=True)# Zakaz berish vaqti(qachon zakaz berilganini)
    status = models.CharField(max_length=255, choices=STATUS, default='tayorlanyabdi')





    class Meta: 
        ordering = ['id']
        verbose_name = "Dastavka"
        verbose_name_plural = "Dastavka"
    def __str__(self):
        return f"{self.full_name} {self.title}"

    def product_prise(self):
        return self.count*self.price 