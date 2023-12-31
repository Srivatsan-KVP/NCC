# Generated by Django 4.2.5 on 2023-09-23 13:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cadet',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.batch')),
            ],
        ),
    ]
