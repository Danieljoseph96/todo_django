# Generated by Django 5.0.3 on 2024-03-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('type', models.IntegerField(choices=[(1, 'crital'), (0, 'normal')], default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
