# Generated by Django 4.1.3 on 2022-12-18 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangaRoll_app', '0003_rename_image_manga_images_rename_pdf_manga_pdfs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='images',
            field=models.FileField(upload_to='mangaroll'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='pdfs',
            field=models.FileField(upload_to='mangaroll'),
        ),
        migrations.AlterField(
            model_name='manger',
            name='profile_image',
            field=models.ImageField(upload_to='mangaroll'),
        ),
    ]
