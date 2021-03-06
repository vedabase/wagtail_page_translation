# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-20 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid
import wagtail_page_translation.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False,
                    verbose_name='ID')),
                ('code', models.CharField(
                    help_text='One of the languages defined in LANGUAGES',
                    max_length=12)),
                ('is_default', models.BooleanField(
                    default=False,
                    help_text='\n        Visitors with no language preference '
                              'will see the site in this\n        '
                              'language\n        ')),
                ('order', models.IntegerField(
                    default=0,
                    help_text='\n        Language choices and translations '
                              'will be displayed in this order\n        ')),
                ('live', models.BooleanField(
                    default=True,
                    help_text='Is this language available for visitors '
                              'to view?')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='TranslatablePage',
            fields=[
                ('translatable_page_ptr', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True, primary_key=True, related_name='+',
                    serialize=False, to='wagtailcore.Page')),
                ('translation_key', models.UUIDField(
                    db_index=True, default=uuid.uuid4)),
                ('language', models.ForeignKey(
                    default=wagtail_page_translation.models._language_default,
                    on_delete=django.db.models.deletion.PROTECT,
                    to='wagtail_page_translation.Language')),
            ],
            bases=('wagtailcore.page',),
        ),
    ]
