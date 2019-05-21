# Generated by Django 2.2.1 on 2019-05-21 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=70)),
                ('short_description', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('image', models.URLField(blank=True, null=True)),
                ('video', models.URLField(blank=True, null=True)),
                ('publish_Date', models.DateTimeField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
