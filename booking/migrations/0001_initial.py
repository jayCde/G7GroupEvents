# Generated by Django 3.1 on 2020-09-15 13:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('room_capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tag_line', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('start_hour', models.CharField(blank=True, choices=[('0 am', '1 am'), ('1 am', '1 am'), ('2 am', '2 am'), ('3 am', '3 am'), ('4 am', '4 am'), ('5 am', '5 am'), ('6 am', '6 am'), ('7 am', '7 am'), ('8 am', '8 am'), ('9 am', '9 am'), ('10 am', '10 am'), ('11 am', '11 am'), ('1 pm', '1 pm'), ('2 pm', '2 pm'), ('3 pm', '3 pm'), ('4 pm', '4 pm'), ('5 pm', '5 pm'), ('6 pm', '6 pm'), ('7 pm', '7 pm'), ('8 pm', '8 pm'), ('9 pm', '9 pm'), ('10 pm', '10 pm'), ('11 pm', '11 pm')], max_length=5)),
                ('start_minutes', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(59)])),
                ('end_date', models.DateField()),
                ('end_hour', models.CharField(blank=True, choices=[('0 am', '1 am'), ('1 am', '1 am'), ('2 am', '2 am'), ('3 am', '3 am'), ('4 am', '4 am'), ('5 am', '5 am'), ('6 am', '6 am'), ('7 am', '7 am'), ('8 am', '8 am'), ('9 am', '9 am'), ('10 am', '10 am'), ('11 am', '11 am'), ('1 pm', '1 pm'), ('2 pm', '2 pm'), ('3 pm', '3 pm'), ('4 pm', '4 pm'), ('5 pm', '5 pm'), ('6 pm', '6 pm'), ('7 pm', '7 pm'), ('8 pm', '8 pm'), ('9 pm', '9 pm'), ('10 pm', '10 pm'), ('11 pm', '11 pm')], max_length=5)),
                ('end_minutes', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(59)])),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.location')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.event')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
