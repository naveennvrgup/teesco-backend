# Generated by Django 3.0.5 on 2020-04-21 08:16

from django.db import migrations
import org.custom_model_field


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='perm',
            field=org.custom_model_field.PermissionSetField(max_length=8196, null=True),
        ),
    ]
