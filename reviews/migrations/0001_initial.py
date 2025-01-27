# Generated by Django 4.2.13 on 2024-06-26 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name of publisher', max_length=50)),
                ('website', models.URLField(help_text="The Publisher 's website ")),
                ('email', models.EmailField(help_text="The Publisher 's email address . ", max_length=254)),
            ],
        ),
    ]
