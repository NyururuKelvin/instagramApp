# Generated by Django 3.1.2 on 2020-10-18 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ig', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='like',
            new_name='likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_photo',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='No Image', upload_to='posts/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='No Image', upload_to='posts/'),
        ),
    ]