# Generated by Django 4.2.3 on 2023-07-09 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todo_checkbox_alter_todo_todolist'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='checkbox',
            field=models.BooleanField(default=False, verbose_name='체크'),
        ),
    ]
