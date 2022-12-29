# Generated by Django 4.1.3 on 2022-12-28 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_studata_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachername', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=150)),
                ('stuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.studata')),
            ],
        ),
    ]