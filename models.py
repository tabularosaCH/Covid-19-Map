class WorldMap(models.Model):
    name = models.CharField(max_length=100)
    code3 = models.CharField(max_length=10)
    value = models.FloatField()
    code = models.CharField(max_length=10)
    class Meta:
        app_label = 'tabularosa'

    def __str__(self):
        return self.name
