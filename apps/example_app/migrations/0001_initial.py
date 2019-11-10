# Generated by Django 2.2.7 on 2019-11-10 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('now', models.IntegerField(default=0, verbose_name='現在の進捗')),
                ('total', models.IntegerField(default=100, verbose_name='全ステップ数')),
            ],
        ),
    ]
