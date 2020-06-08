# Generated by Django 3.0.7 on 2020-06-07 15:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('mobile_number', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=120)),
                ('total_amount', models.IntegerField()),
                ('due_date', models.DateTimeField()),
                ('inovice_datetime', models.DateTimeField(blank=True, default=datetime.datetime.utcnow)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.IntegerField(default=1)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Invoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Product')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='product',
            field=models.ManyToManyField(through='api.InvoiceProduct', to='api.Product'),
        ),
    ]