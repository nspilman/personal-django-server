# Generated by Django 2.1.3 on 2019-02-06 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_post', models.CharField(max_length=20)),
                ('comment_text', models.TextField()),
                ('author', models.CharField(default='anonymous', max_length=100)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]
