# Generated by Django 4.1.3 on 2022-12-31 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_project_proj_img_alter_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='desc',
            field=models.CharField(default='hello world', max_length=700),
        ),
    ]