# Generated by Django 3.0.7 on 2020-08-02 15:33

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200802_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billing_address',
            name='countries',
        ),
        migrations.AddField(
            model_name='billing_address',
            name='country',
            field=django_countries.fields.CountryField(default='al', max_length=2),
            preserve_default=False,
        ),
    ]
