# Generated by Django 4.2.5 on 2024-08-31 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password_hash', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id_token', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField(null=True)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'token',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id_profile', models.AutoField(primary_key=True, serialize=False)),
                ('bio', models.TextField()),
                ('profile_picture_url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
