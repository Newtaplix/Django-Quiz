# Generated by Django 5.1.3 on 2024-12-14 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0009_alter_account_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_image',
            field=models.CharField(blank=True, default='accounts/profiles/pic2.jpg', max_length=255),
        ),
    ]