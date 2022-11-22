# Generated by Django 3.1.14 on 2022-03-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security_backends_sql', '0003_migration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celerytaskinvocationlog',
            name='is_duplicate',
        ),
        migrations.AddField(
            model_name='celerytaskinvocationlog',
            name='error_message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='celerytaskinvocationloggenericmanytomanyrelation',
            name='changed_at',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='changed at'),
        ),
        migrations.AlterField(
            model_name='celerytaskinvocationloggenericmanytomanyrelation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='celerytaskinvocationloggenericmanytomanyrelation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='celerytaskinvocationloggenericmanytomanyrelation',
            name='object_ct_id',
            field=models.PositiveSmallIntegerField(db_index=True, verbose_name='content type of the related object'),
        ),
        migrations.AlterField(
            model_name='celerytaskinvocationloggenericmanytomanyrelation',
            name='object_id',
            field=models.TextField(db_index=True, verbose_name='ID of the related object'),
        ),
        migrations.AlterField(
            model_name='celerytaskrunloggenericmanytomanyrelation',
            name='changed_at',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='changed at'),
        ),
        migrations.AlterField(
            model_name='celerytaskrunloggenericmanytomanyrelation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='celerytaskrunloggenericmanytomanyrelation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='celerytaskrunloggenericmanytomanyrelation',
            name='object_ct_id',
            field=models.PositiveSmallIntegerField(db_index=True, verbose_name='content type of the related object'),
        ),
        migrations.AlterField(
            model_name='celerytaskrunloggenericmanytomanyrelation',
            name='object_id',
            field=models.TextField(db_index=True, verbose_name='ID of the related object'),
        ),
        migrations.AlterField(
            model_name='commandlog',
            name='error_message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commandloggenericmanytomanyrelation',
            name='changed_at',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='changed at'),
        ),
        migrations.AlterField(
            model_name='commandloggenericmanytomanyrelation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='commandloggenericmanytomanyrelation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='commandloggenericmanytomanyrelation',
            name='object_ct_id',
            field=models.PositiveSmallIntegerField(db_index=True, verbose_name='content type of the related object'),
        ),
        migrations.AlterField(
            model_name='commandloggenericmanytomanyrelation',
            name='object_id',
            field=models.TextField(db_index=True, verbose_name='ID of the related object'),
        ),
        migrations.AlterField(
            model_name='inputrequestloggenericmanytomanyrelation',
            name='changed_at',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='changed at'),
        ),
        migrations.AlterField(
            model_name='inputrequestloggenericmanytomanyrelation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='inputrequestloggenericmanytomanyrelation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='inputrequestloggenericmanytomanyrelation',
            name='object_ct_id',
            field=models.PositiveSmallIntegerField(db_index=True, verbose_name='content type of the related object'),
        ),
        migrations.AlterField(
            model_name='inputrequestloggenericmanytomanyrelation',
            name='object_id',
            field=models.TextField(db_index=True, verbose_name='ID of the related object'),
        ),
        migrations.AlterField(
            model_name='outputrequestloggenericmanytomanyrelation',
            name='changed_at',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='changed at'),
        ),
        migrations.AlterField(
            model_name='outputrequestloggenericmanytomanyrelation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='outputrequestloggenericmanytomanyrelation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='outputrequestloggenericmanytomanyrelation',
            name='object_ct_id',
            field=models.PositiveSmallIntegerField(db_index=True, verbose_name='content type of the related object'),
        ),
        migrations.AlterField(
            model_name='outputrequestloggenericmanytomanyrelation',
            name='object_id',
            field=models.TextField(db_index=True, verbose_name='ID of the related object'),
        ),
        migrations.AddField(
            model_name='celerytaskinvocationlog',
            name='version',
            field=models.PositiveSmallIntegerField(default=9999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='celerytaskrunlog',
            name='version',
            field=models.PositiveSmallIntegerField(default=9999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commandlog',
            name='version',
            field=models.PositiveSmallIntegerField(default=9999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inputrequestlog',
            name='version',
            field=models.PositiveSmallIntegerField(default=9999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outputrequestlog',
            name='version',
            field=models.PositiveSmallIntegerField(default=9999),
            preserve_default=False,
        ),
    ]
