# Generated by Django 4.1 on 2022-09-02 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_remove_booking_id_alter_booking_aadharno'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newstext', models.TextField()),
                ('newsdate', models.CharField(max_length=30)),
            ],
        ),
    ]
