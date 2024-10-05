# Generated by Django 5.1.1 on 2024-10-03 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='type',
            field=models.CharField(choices=[('galaxy', 'Galaxy'), ('planet', 'Planet'), ('star', 'Star'), ('universe', 'Universe')], default='galaxy', help_text='Select the type of the gallery item.', max_length=10, verbose_name='Type'),
        ),
    ]
