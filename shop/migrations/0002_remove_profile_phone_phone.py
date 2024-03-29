# Generated by Django 4.1.7 on 2023-04-09 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(max_length=11)),
                ('verify_code', models.IntegerField(max_length=6)),
                ('profiles', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='phone', to='shop.profile')),
            ],
        ),
    ]
