# Generated by Django 3.2.4 on 2021-07-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_board_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='choice',
            field=models.CharField(choices=[('1', '대변'), ('3', '방귀'), ('2', '소변')], max_length=80, null=True),
        ),
    ]
