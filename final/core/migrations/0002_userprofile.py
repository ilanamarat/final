# Generated by Django 4.0.4 on 2022-05-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=200)),
                ('roles', models.CharField(choices=[('SA', 'SuperAdmin'), ('G', 'Guest')], default='G', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]