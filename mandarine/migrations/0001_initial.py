# Generated by Django 2.0.4 on 2018-04-14 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mandarine.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mandarin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('size', mandarine.models.IntegerRangeField()),
                ('round', mandarine.models.IntegerRangeField()),
                ('smooth', mandarine.models.IntegerRangeField()),
                ('soft', mandarine.models.IntegerRangeField()),
                ('elasticity', mandarine.models.IntegerRangeField()),
                ('orange', mandarine.models.IntegerRangeField()),
                ('smell', mandarine.models.IntegerRangeField()),
                ('hand_smell', mandarine.models.IntegerRangeField()),
                ('beautiful', mandarine.models.IntegerRangeField()),
                ('trump', mandarine.models.IntegerRangeField()),
                ('brown', mandarine.models.IntegerRangeField()),
                ('mold', mandarine.models.IntegerRangeField()),
                ('hand_feel', mandarine.models.IntegerRangeField()),
                ('spot_depth', mandarine.models.IntegerRangeField()),
                ('temperature', mandarine.models.IntegerRangeField()),
                ('damage', mandarine.models.IntegerRangeField()),
                ('symmetrical', mandarine.models.IntegerRangeField()),
                ('plastic', mandarine.models.IntegerRangeField()),
                ('stem_loose', mandarine.models.IntegerRangeField()),
                ('opening', mandarine.models.IntegerRangeField()),
                ('skin_thick', mandarine.models.IntegerRangeField()),
                ('slice_size', mandarine.models.IntegerRangeField()),
                ('pith_amount', mandarine.models.IntegerRangeField()),
                ('pith_color', mandarine.models.IntegerRangeField()),
                ('seeds', mandarine.models.IntegerRangeField()),
                ('taste', mandarine.models.IntegerRangeField()),
            ],
        ),
        migrations.CreateModel(
            name='testi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='mandarin',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mandarine.UserProfile'),
        ),
    ]