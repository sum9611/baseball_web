# Generated by Django 3.2.18 on 2023-05-13 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.PositiveIntegerField()),
                ('player_name', models.CharField(max_length=200)),
                ('player_birth', models.DateTimeField()),
            ],
        ),
    ]
