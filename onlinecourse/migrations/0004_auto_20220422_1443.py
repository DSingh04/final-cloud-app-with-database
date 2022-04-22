# Generated by Django 3.1.3 on 2022-04-22 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_auto_20220418_0539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='content',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='content',
        ),
        migrations.AddField(
            model_name='choice',
            name='text',
            field=models.CharField(max_length=550, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=550, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=550, null=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.FloatField(default=5.0),
        ),
    ]