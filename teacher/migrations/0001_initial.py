# Generated by Django 4.1.4 on 2023-01-12 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0015_alter_student_name_alter_teacher_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(default='Question Here.', max_length=200)),
                ('answer', models.TextField(default='Answer Here.', max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.teacher')),
            ],
        ),
    ]
