# Generated by Django 3.0.4 on 2020-03-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=30, null=True)),
                ('sobrenome', models.CharField(blank=True, max_length=30, null=True)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]
