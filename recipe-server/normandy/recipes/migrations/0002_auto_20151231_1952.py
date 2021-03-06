# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 19:52
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields
import normandy.recipes.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='content_hash',
            field=normandy.recipes.fields.AutoHashField('content', unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='end_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='locale',
            field=normandy.recipes.fields.LocaleField(blank=True, choices=[('en-GB', 'English (British)'), ('mr', 'Marathi'), ('sq', 'Albanian'), ('fi', 'Finnish'), ('ml', 'Malayalam'), ('cy', 'Welsh'), ('mai', 'Maithili'), ('sv-SE', 'Swedish'), ('hy-AM', 'Armenian'), ('ur', 'Urdu'), ('lij', 'Ligurian'), ('am-et', 'Amharic'), ('ga-IE', 'Irish'), ('ee', 'Ewe'), ('eo', 'Esperanto'), ('brx', 'Bodo'), ('te', 'Telugu'), ('ts', 'Tsonga'), ('ro', 'Romanian'), ('zh-TW', 'Chinese (Traditional)'), ('is', 'Icelandic'), ('ta', 'Tamil'), ('bg', 'Bulgarian'), ('km', 'Khmer'), ('lv', 'Latvian'), ('ku', 'Kurdish'), ('de-AT', 'German (Austria)'), ('ast', 'Asturian'), ('gl', 'Galician'), ('as', 'Assamese'), ('hi', 'Hindi'), ('ca-valencia', 'Catalan (Valencian)'), ('ja', 'Japanese'), ('ja-JP-mac', 'Japanese'), ('gd', 'Gaelic (Scotland)'), ('fa', 'Persian'), ('en-AU', 'English (Australian)'), ('pt-BR', 'Portuguese (Brazilian)'), ('ta-LK', 'Tamil (Sri Lanka)'), ('nl', 'Dutch'), ('rm', 'Romansh'), ('el', 'Greek'), ('ka', 'Georgian'), ('cs', 'Czech'), ('ar', 'Arabic'), ('en-NZ', 'English (New Zealand)'), ('da', 'Danish'), ('ach', 'Acholi'), ('dbg', 'Debug Robot'), ('pa', 'Punjabi'), ('ig', 'Igbo'), ('fy-NL', 'Frisian'), ('cak', 'Kaqchikel'), ('sl', 'Slovenian'), ('bm', 'Bambara'), ('gu-IN', 'Gujarati (India)'), ('uz', 'Uzbek'), ('he', 'Hebrew'), ('an', 'Aragonese'), ('csb', 'Kashubian'), ('en-CA', 'English (Canadian)'), ('dsb', 'Lower Sorbian'), ('bn-BD', 'Bengali (Bangladesh)'), ('mg', 'Malagasy'), ('bs', 'Bosnian'), ('mi', 'Maori (Aotearoa)'), ('hsb', 'Upper Sorbian'), ('gu', 'Gujarati'), ('it', 'Italian'), ('oc', 'Occitan (Lengadocian)'), ('eu', 'Basque'), ('et', 'Estonian'), ('id', 'Indonesian'), ('en-ZA', 'English (South African)'), ('uk', 'Ukrainian'), ('pa-IN', 'Punjabi (India)'), ('ms', 'Malay'), ('pt-PT', 'Portuguese (Portugal)'), ('sr-Latn', 'Serbian'), ('nr', 'Ndebele, South'), ('kok', 'Konkani'), ('hi-IN', 'Hindi (India)'), ('de-CH', 'German (Switzerland)'), ('tt-RU', 'Tatar'), ('rw', 'Kinyarwanda'), ('fr', 'French'), ('lo', 'Lao'), ('nb-NO', 'Norwegian (Bokmål)'), ('ak', 'Akan'), ('es-CL', 'Spanish (Chile)'), ('de', 'German'), ('fj-FJ', 'Fijian'), ('bn-IN', 'Bengali (India)'), ('kn', 'Kannada'), ('en-US', 'English (US)'), ('gn', 'Guarani'), ('az', 'Azerbaijani'), ('fur-IT', 'Friulian'), ('zh-CN', 'Chinese (Simplified)'), ('la', 'Latin'), ('ha', 'Hausa'), ('x-testing', 'Testing'), ('si', 'Sinhala'), ('af', 'Afrikaans'), ('son', 'Songhai'), ('kk', 'Kazakh'), ('tl', 'Tagalog'), ('es', 'Spanish'), ('sw', 'Swahili'), ('es-AR', 'Spanish (Argentina)'), ('ru', 'Russian'), ('es-MX', 'Spanish (Mexico)'), ('xh', 'Xhosa'), ('nn-NO', 'Norwegian (Nynorsk)'), ('hu', 'Hungarian'), ('ne-NP', 'Nepali'), ('sat', 'Santali'), ('ta-IN', 'Tamil (India)'), ('lt', 'Lithuanian'), ('hr', 'Croatian'), ('sa', 'Sanskrit'), ('mn', 'Mongolian'), ('nso', 'Northern Sotho'), ('lg', 'Luganda'), ('my', 'Burmese'), ('be', 'Belarusian'), ('ln', 'Lingala'), ('sr-Cyrl', 'Serbian'), ('tr', 'Turkish'), ('mk', 'Macedonian'), ('sah', 'Sakha'), ('wo', 'Wolof'), ('de-DE', 'German (Germany)'), ('zu', 'Zulu'), ('ca', 'Catalan'), ('pl', 'Polish'), ('br', 'Breton'), ('tn', 'Tswana'), ('vi', 'Vietnamese'), ('es-ES', 'Spanish (Spain)'), ('ve', 'Venda'), ('ga', 'Irish'), ('tsz', 'Purépecha'), ('ss', 'Siswati'), ('ks', 'Kashmiri'), ('sk', 'Slovak'), ('sr', 'Serbian'), ('ff', 'Fulah'), ('st', 'Southern Sotho'), ('yo', 'Yoruba'), ('th', 'Thai'), ('ko', 'Korean'), ('or', 'Oriya')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='start_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
