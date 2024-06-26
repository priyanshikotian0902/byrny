# Generated by Django 5.0.4 on 2024-04-18 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_remove_customerprofile_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('attachment', models.FileField(upload_to='service_request_attachments/')),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customerprofile')),
            ],
        ),
    ]
