# Generated by Django 4.2 on 2023-05-11 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('guardian_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('village', models.CharField(max_length=100)),
                ('ward', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=50)),
                ('shelter', models.CharField(max_length=100)),
                ('primary_school', models.CharField(max_length=20)),
                ('second_school', models.CharField(max_length=20)),
                ('tertially_school', models.CharField(max_length=200)),
                ('date_of_adm', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('lever', models.IntegerField()),
                ('scholarship_npf', models.BooleanField()),
                ('scholarship_other', models.BooleanField()),
                ('date_of_graduation', models.DateTimeField()),
                ('cohort', models.IntegerField()),
                ('date_of_birth', models.DateTimeField()),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='student_profile_photos/')),
            ],
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]