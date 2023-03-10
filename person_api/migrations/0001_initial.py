# Generated by Django 4.1.7 on 2023-02-17 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=150)),
                ('street_address', models.CharField(max_length=150)),
                ('marital_status', models.CharField(choices=[('single', 'single'), ('married', 'married'), ('divorced', 'divorced')], max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
