# Generated by Django 4.2.14 on 2024-09-24 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_developer_user_alter_project_developers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='user.projectmanager'),
        ),
    ]
