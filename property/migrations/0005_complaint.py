# Generated by Django 2.2.4 on 2020-09-20 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0004_auto_20200920_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID'
                    )),
                ('apartment_number', models.IntegerField(
                    verbose_name='Квартира, на которую пожаловались:'
                    )),
                ('text_of_complaint', models.TextField(
                    verbose_name='Текст жалобы:'
                    )),
                ('complainer', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='complaints',
                    to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался:'
                )),
            ],
        ),
    ]
