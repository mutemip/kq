# Generated by Django 5.1 on 2024-08-26 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_name', models.CharField(max_length=255)),
                ('review_text', models.TextField()),
                ('review_content', models.TextField()),
                ('rating', models.CharField(max_length=10)),
                ('sentiment', models.CharField(max_length=10)),
            ],
        ),
    ]
