# Generated by Django 3.2.6 on 2021-09-06 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '0009_auto_20210905_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct_answer', models.BooleanField()),
                ('answer_number', models.IntegerField()),
                ('user_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.useranswer')),
            ],
        ),
    ]
