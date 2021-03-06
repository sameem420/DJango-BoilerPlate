# Generated by Django 3.1.5 on 2021-01-26 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proplistapp', '0002_postad_uploaded_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('password_repeat', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('profile_picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
