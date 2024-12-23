# Generated by Django 5.1.3 on 2024-11-26 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_avaliacaoong_data_avaliacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ong',
            name='capacidade_maxima',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='ong',
            name='telefone',
            field=models.CharField(default='(00) 00000-0000', max_length=30),
        ),
        migrations.AddField(
            model_name='ong',
            name='whatsapp',
            field=models.CharField(default='http://wa.me/5581994382896', max_length=30),
        ),
        migrations.AlterField(
            model_name='ong',
            name='imagem',
            field=models.CharField(blank=True, default='https://www.google.com/imgres?q=default%20coloque%20sua%20imagem&imgurl=https%3A%2F%2Fwww.quadrorama.com.br%2Fwp-content%2Fuploads%2F2018%2F05%2Fquadro-com-foto-imagem-personalizada.png&imgrefurl=https%3A%2F%2Fwww.quadrorama.com.br%2Fproduto%2Ffoto-personalizada%2F&docid=Rf3tWzXG5ZJ58M&tbnid=JyJzwRzOMJN5vM&vet=12ahUKEwiPsNa60_qJAxVYq5UCHfzfCAYQM3oECFAQAA..i&w=351&h=497&hcb=2&ved=2ahUKEwiPsNa60_qJAxVYq5UCHfzfCAYQM3oECFAQAA', max_length=1000, null=True),
        ),
        migrations.DeleteModel(
            name='Armazenamento',
        ),
    ]
