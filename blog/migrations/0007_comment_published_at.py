# Generated by Django 2.2.5 on 2019-09-11 18:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_auto_20190910_2042"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="published_at",
            field=models.DateTimeField(default="1000-01-01"),
            preserve_default=False,
        ),
    ]
