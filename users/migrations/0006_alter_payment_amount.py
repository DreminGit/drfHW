from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_payment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.PositiveIntegerField(verbose_name='Сумма оплаты'),
        ),
    ]