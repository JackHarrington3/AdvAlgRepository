# Generated by Django 4.2.6 on 2023-10-30 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wrongGuesses', models.CharField(max_length=6)),
                ('word', models.CharField(max_length=40)),
                ('wordBlanks', models.CharField(max_length=80)),
                ('origWord', models.CharField(max_length=40)),
                ('prevGuesses', models.CharField(max_length=26)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]