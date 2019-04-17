from django.db import models

class Cliente(models.Model):

	cpf_cnpj = models.CharField(max_length=16, null=False)
	nm_costume = models.CharField(max_length=255, null=False)
	is_active = models.CharField(max_length=1, null=False)
	vl_total = models.DecimalField(max_digits=10, decimal_places=2)
