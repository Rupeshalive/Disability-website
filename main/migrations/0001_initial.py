# Generated by Django 3.0.8 on 2020-07-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_title', models.CharField(max_length=200)),
                ('web_content', models.TextField()),
                ('web_published', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]