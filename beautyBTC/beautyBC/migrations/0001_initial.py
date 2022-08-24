# Generated by Django 3.2.12 on 2022-08-18 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name_category', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('mark_id', models.AutoField(primary_key=True, serialize=False)),
                ('name_mark', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'mark',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name_product', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('provider_id', models.AutoField(primary_key=True, serialize=False)),
                ('provider_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=25)),
                ('provider_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'providers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('purchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_date', models.DateField()),
                ('factura', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'purchases',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('sale_id', models.AutoField(primary_key=True, serialize=False)),
                ('sale_date', models.DateField()),
                ('amount', models.IntegerField()),
            ],
            options={
                'db_table': 'sales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_price', models.IntegerField()),
                ('sales_price', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('saless', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'stock',
                'managed': False,
            },
        ),
    ]
