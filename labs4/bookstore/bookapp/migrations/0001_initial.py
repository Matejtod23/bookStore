# Generated by Django 5.0.3 on 2024-05-19 21:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('year_established', models.IntegerField()),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('isbn', models.CharField(max_length=30)),
                ('publishing_year', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('size', models.IntegerField()),
                ('price', models.IntegerField()),
                ('category', models.CharField(choices=[('Romance', 'Romance'), ('Thriller', 'Thriller'), ('Biography', 'Biography'), ('Classic', 'Classic'), ('Drama', 'Drama'), ('History', 'History')], max_length=30)),
                ('cover', models.CharField(choices=[('Soft', 'Soft'), ('Hard', 'Hard')], max_length=30)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.publicationhouse')),
            ],
        ),
    ]
