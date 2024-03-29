# Generated by Django 4.2.5 on 2023-09-11 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokdx',
            fields=[
                ('attack', models.IntegerField()),
                ('classfication', models.CharField(max_length=51)),
                ('defense', models.IntegerField()),
                ('height_m', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('hp', models.IntegerField()),
                ('japanese_name', models.CharField(max_length=33)),
                ('name', models.CharField(max_length=12)),
                ('pokedex_number', models.IntegerField(primary_key=True, serialize=False)),
                ('sp_attack', models.IntegerField()),
                ('sp_defense', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('type1', models.CharField(max_length=8)),
                ('type2', models.CharField(blank=True, max_length=8, null=True)),
                ('weight_kg', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('generation', models.IntegerField()),
                ('is_legendary', models.IntegerField()),
            ],
            options={
                'db_table': 'pokdx',
                'managed': False,
            },
        ),
    ]
