# Generated by Django 5.0.2 on 2024-03-31 07:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0007_rename_uuid_useranswer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='created_by',
            new_name='user',
        ),
    ]
