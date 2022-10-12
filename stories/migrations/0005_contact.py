# Generated by Django 2.2.13 on 2022-10-11 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20221008_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('e_mail', models.EmailField(max_length=250)),
                ('phone_number', models.IntegerField()),
                ('contact_message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]