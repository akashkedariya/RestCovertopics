# Generated by Django 4.2.14 on 2024-09-30 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_employee_personproxy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PersonProxy',
        ),
        migrations.CreateModel(
            name='EmployeeProxy',
            fields=[
            ],
            options={
                'ordering': ['age'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('user.person',),
        ),
    ]
