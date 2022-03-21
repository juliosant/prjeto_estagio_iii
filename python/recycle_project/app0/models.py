from django.db import models

# Create your models here.

class AgendamentoDoacao(models.Model):
    dat_agendamento = models.DateTimeField()
    des_destinatario = models.CharField(max_length=100)
    dat_criacao = models.DateTimeField(auto_now=True)
    dat_atualizacao = models.DateTimeField(auto_now_add=True)
    mensagem = models.TextField(max_length=300)

    def __str__(self):
        return str(self.dat_agendamento) + ' - ' + self.des_destinatario

    
    class Meta:
        ordering = ['-dat_atualizacao']