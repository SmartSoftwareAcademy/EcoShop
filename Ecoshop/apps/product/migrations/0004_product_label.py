# Generated by Django 3.1.5 on 2021-02-06 06:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0003_product_additional_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], default='P',
                                   max_length=1),
            preserve_default=False,
        ),
    ]
