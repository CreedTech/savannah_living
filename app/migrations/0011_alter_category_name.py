# Generated by Django 4.2 on 2023-04-26 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_alter_livingoptions_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.livingoptions"
            ),
        ),
    ]
