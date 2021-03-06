# Generated by Django 2.1.7 on 2020-03-31 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Categories', '0002_auto_20200324_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('regular_price', models.FloatField()),
                ('promotional_price', models.FloatField(default=0.0)),
                ('weight', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Categories.Category')),
            ],
        ),
    ]
