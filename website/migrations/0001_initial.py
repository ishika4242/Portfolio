# Generated by Django 3.0.8 on 2020-07-10 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Working',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descreption', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
