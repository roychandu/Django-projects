# Generated by Django 5.0.8 on 2024-08-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact', models.BigIntegerField()),
                ('address1_field', models.CharField(max_length=50)),
                ('address2_field', models.CharField(max_length=50)),
                ('state_field', models.CharField(max_length=50)),
                ('country_field', models.CharField(max_length=50)),
                ('post_field', models.CharField(max_length=50)),
                ('area_field', models.CharField(max_length=50)),
            ],
        ),
    ]
