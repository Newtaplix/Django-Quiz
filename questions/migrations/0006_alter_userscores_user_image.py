# Generated by Django 5.1.3 on 2024-12-15 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_userscores_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userscores',
            name='user_image',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
