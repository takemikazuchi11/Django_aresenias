# Generated by Django 4.1.4 on 2022-12-23 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
                ('fname', models.CharField(max_length=50)),
                ('mname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
    ]
