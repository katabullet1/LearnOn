# Generated by Django 4.0.4 on 2024-08-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_messages_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='lesson',
            field=models.TextField(),
        ),
    ]
