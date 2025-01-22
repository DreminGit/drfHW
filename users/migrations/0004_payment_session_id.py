from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_payment_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='session_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID сессии'),
        ),
    ]