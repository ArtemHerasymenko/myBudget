# Generated by Django 2.1.2 on 2018-10-29 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('moneyAmount', models.IntegerField(default=0)),
                ('whenWasMade', models.DateTimeField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]