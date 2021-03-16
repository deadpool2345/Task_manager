# Generated by Django 3.1.7 on 2021-03-16 07:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('A', 'assigned'), ('O', 'ongoing'), ('C', 'completed')], max_length=1)),
                ('users', models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
