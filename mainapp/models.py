from tabnanny import verbose
from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    phone_number = models.CharField(max_length=255, verbose_name="Номер телефона")

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"
        
    def __str__(self):
        return f'{self.name} - {self.phone_number}'


class TradePoint(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE, verbose_name="Работник"
    )

    class Meta:
        verbose_name = "Торговая точка"
        verbose_name_plural = "Торговые точки"
        
    def __str__(self):
        return f'{self.name} - {self.worker.name}'
    
    
    @classmethod
    def get_trade_points(cls, phone):
        return cls.objects.filter(worker__phone_number=phone)


class Visit(models.Model):
    visit_time = models.DateTimeField(auto_now_add=True, verbose_name="Время посещения")
    trade_point = models.ForeignKey(
        TradePoint, on_delete=models.CASCADE, verbose_name="Торговая точка"
    )
    latitude = models.FloatField(max_length=31, verbose_name="Широта")
    longitude = models.FloatField(max_length=31, verbose_name="Долгота")

    class Meta:
        verbose_name = "Посещение"
        verbose_name_plural = "Посещения"
        
    def __str__(self):
        return f'{self.visit_time} - {self.trade_point.name}'
