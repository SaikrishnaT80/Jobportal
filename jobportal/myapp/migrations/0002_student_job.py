# Generated by Django 4.2.6 on 2024-01-03 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('qualification', models.CharField(max_length=200)),
                ('skill', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=30)),
                ('resume', models.FileField(null=True, upload_to='files')),
                ('experience', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], default='male', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('experience', models.PositiveIntegerField()),
                ('salary', models.PositiveIntegerField()),
                ('qualification', models.CharField(max_length=200)),
                ('skills', models.CharField(max_length=200)),
                ('poster', models.ImageField(null=True, upload_to='poster')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.category')),
            ],
        ),
    ]
