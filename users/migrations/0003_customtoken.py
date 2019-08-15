# Generated by Django 2.2.4 on 2019-08-15 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0002_auto_20160226_1747'),
        ('users', '0002_auto_20190814_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomToken',
            fields=[
                ('token_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authtoken.Token')),
                ('lastused', models.DateTimeField(auto_now=True, verbose_name='Last used time')),
            ],
            bases=('authtoken.token',),
        ),
    ]
