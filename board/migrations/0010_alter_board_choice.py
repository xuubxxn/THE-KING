# Generated by Django 3.2.5 on 2021-07-27 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_alter_board_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='choice',
            field=models.CharField(choices=[('1', '대변'), ('3', '방귀'), ('2', '소변')], max_length=80, null=True),
        ),
    ]
