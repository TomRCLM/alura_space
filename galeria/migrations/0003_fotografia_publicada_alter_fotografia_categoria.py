# Generated by Django 4.2.1 on 2023-05-18 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0002_fotografia_categoria"),
    ]

    operations = [
        migrations.AddField(
            model_name="fotografia",
            name="publicada",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="fotografia",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("NEBULOSA", "Nebulosa"),
                    ("ESTRELA", "Estrela"),
                    ("GALÁXIA", "Galáxia"),
                    ("PLANETA", "Planeta"),
                ],
                default="",
                max_length=100,
            ),
        ),
    ]
