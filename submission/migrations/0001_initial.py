# Generated by Django 4.2.3 on 2023-07-15 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hackathon', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('summ', models.CharField(blank=True, max_length=500)),
                ('file', models.FileField(upload_to='static/')),
                ('link', models.URLField()),
                ('image', models.ImageField(upload_to='static/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('hack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackathon.hackathon')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
