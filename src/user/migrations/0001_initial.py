# Generated by Django 5.1 on 2024-09-08 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('pseudo', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.roleusermodel')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.schoolmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
