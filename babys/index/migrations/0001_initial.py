# Generated by Django 3.1.7 on 2021-04-06 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(null=True)),
                ('hireDate', models.DateField()),
            ],
            options={
                'verbose_name': '人员信息',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('job', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('payment', models.IntegerField(blank=True, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ps', to='index.personinfo')),
            ],
            options={
                'verbose_name': '职业信息',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('performer', models.ManyToManyField(to='index.Performer')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('living', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.city')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.province'),
        ),
    ]