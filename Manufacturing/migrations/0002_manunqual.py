# Generated by Django 2.2.5 on 2021-01-02 12:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Manufacturing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManUnqual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=32, null=True)),
                ('inform', models.CharField(max_length=32, null=True)),
                ('type', models.CharField(max_length=32, null=True)),
                ('fac', models.CharField(max_length=32, null=True)),
                ('found_date', models.CharField(max_length=32, null=True)),
                ('creat_date', models.CharField(max_length=32, null=True)),
                ('gongying', models.CharField(max_length=32, null=True)),
                ('result', models.CharField(max_length=32, null=True)),
                ('defect_text', models.CharField(max_length=32, null=True)),
                ('problem', models.TextField(default='', null=True)),
                ('pro_detail', models.TextField(default='', null=True)),
                ('chuzhi', models.TextField(default='', null=True)),
            ],
        ),
    ]
