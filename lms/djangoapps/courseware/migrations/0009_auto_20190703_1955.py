# Generated by Django 1.11.22 on 2019-07-03 19:55


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseware', '0008_move_idde_to_edx_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodulehistory',
            name='student_module',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='courseware.StudentModule'),
        ),
    ]