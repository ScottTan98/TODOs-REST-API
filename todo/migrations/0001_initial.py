# Generated by Django 4.1.7 on 2023-03-02 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('due_date', models.DateTimeField()),
                ('status', models.CharField(max_length=30)),
                ('priority', models.CharField(max_length=20, null=True)),
                ('category', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
