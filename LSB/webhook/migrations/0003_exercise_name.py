# Generated by Django 4.2 on 2023-05-01 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhook', '0002_remove_rule_id_rule_ruleid'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='Name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]