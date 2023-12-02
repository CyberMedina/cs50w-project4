# Generated by Django 4.2.7 on 2023-12-02 13:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0002_alter_producto_imagen_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('exact_address', models.TextField()),
                ('house_number', models.CharField(blank=True, max_length=50)),
                ('delivery_instructions', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('delivery_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.deliveryinformation')),
                ('products', models.ManyToManyField(to='shop.producto')),
            ],
        ),
    ]
