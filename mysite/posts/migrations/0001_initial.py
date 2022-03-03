# Generated by Django 4.0.2 on 2022-03-01 07:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=1000)),
                ('votes', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.SmallIntegerField(default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='posts.post')),
            ],
        ),
    ]