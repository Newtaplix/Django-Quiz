# Generated by Django 5.1.3 on 2024-12-14 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_useranswer_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='quiz',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
