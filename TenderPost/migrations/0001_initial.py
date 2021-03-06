# Generated by Django 2.2.5 on 2020-09-21 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owner', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenderBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('amount', models.IntegerField()),
                ('product_description', models.CharField(max_length=650)),
                ('delivery_date', models.DateField()),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.Tender')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PD', 'Pending'), ('SC', 'Successful')], default='PD', max_length=2)),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TenderPost.TenderBid')),
            ],
        ),
    ]
