# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import django.utils.timezone
import django.db.models.deletion
from django.conf import settings
import db.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DbUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=75, db_index=True)),
                ('first_name', models.CharField(max_length=254, blank=True)),
                ('last_name', models.CharField(max_length=254, blank=True)),
                ('institution', models.CharField(max_length=254, blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text=b'Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, help_text=b'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=db.timezone.now)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DbAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=1024, db_index=True)),
                ('datatype', models.CharField(default=b'none', max_length=10, db_index=True, choices=[(b'float', b'float'), (b'int', b'int'), (b'txt', b'txt'), (b'bool', b'bool'), (b'date', b'date'), (b'json', b'json'), (b'dict', b'dict'), (b'list', b'list'), (b'none', b'none')])),
                ('tval', models.TextField(default=b'', blank=True)),
                ('fval', models.FloatField(default=None, null=True)),
                ('ival', models.IntegerField(default=None, null=True)),
                ('bval', models.NullBooleanField(default=None)),
                ('dval', models.DateTimeField(default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DbAuthInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auth_params', models.TextField(default=b'{}')),
                ('metadata', models.TextField(default=b'{}')),
                ('enabled', models.BooleanField(default=True)),
                ('aiidauser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DbCalcState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(db_index=True, max_length=25, choices=[(b'RETRIEVALFAILED', b'RETRIEVALFAILED'), (b'COMPUTED', b'COMPUTED'), (b'RETRIEVING', b'RETRIEVING'), (b'WITHSCHEDULER', b'WITHSCHEDULER'), (b'SUBMISSIONFAILED', b'SUBMISSIONFAILED'), (b'PARSING', b'PARSING'), (b'FAILED', b'FAILED'), (b'FINISHED', b'FINISHED'), (b'TOSUBMIT', b'TOSUBMIT'), (b'SUBMITTING', b'SUBMITTING'), (b'IMPORTED', b'IMPORTED'), (b'NEW', b'NEW'), (b'PARSINGFAILED', b'PARSINGFAILED')])),
                ('time', models.DateTimeField(default=db.timezone.now, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DbComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', django_extensions.db.fields.UUIDField(editable=False, blank=True)),
                ('ctime', models.DateTimeField(default=db.timezone.now, editable=False)),
                ('mtime', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DbComputer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', django_extensions.db.fields.UUIDField(editable=False, blank=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('hostname', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('enabled', models.BooleanField(default=True)),
                ('transport_type', models.CharField(max_length=255)),
                ('scheduler_type', models.CharField(max_length=255)),
                ('transport_params', models.TextField(default=b'{}')),
                ('metadata', models.TextField(default=b'{}')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DbExtra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=1024, db_index=True)),
                ('datatype', models.CharField(default=b'none', max_length=10, db_index=True, choices=[(b'float', b'float'), (b'int', b'int'), (b'txt', b'txt'), (b'bool', b'bool'), (b'date', b'date'), (b'json', b'json'), (b'dict', b'dict'), (b'list', b'list'), (b'none', b'none')])),
                ('tval', models.TextField(default=b'', blank=True)),
                ('fval', models.FloatField(default=None, null=True)),
                ('ival', models.IntegerField(default=None, null=True)),
                ('bval', models.NullBooleanField(default=None)),
                ('dval', models.DateTimeField(default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DbGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', django_extensions.db.fields.UUIDField(editable=False, blank=True)),
                ('name', models.CharField(max_length=255, db_index=True)),
                ('type', models.CharField(default=b'', max_length=255, db_index=True)),
                ('time', models.DateTimeField(default=db.timezone.now, editable=False)),
                ('description', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DbLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=255, db_index=True)),
                ('type', models.CharField(db_index=True, max_length=255, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DbLock',
            fields=[
                ('key', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('creation', models.DateTimeField(default=db.timezone.now, editable=False)),
                ('timeout', models.IntegerField(editable=False)),
                ('owner', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DbLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=db.timezone.now, editable=False)),
                ('loggername', models.CharField(max_length=255, db_index=True)),
                ('levelname', models.CharField(max_length=50, db_index=True)),
                ('objname', models.CharField(db_index=True, max_length=255, blank=True)),
                ('objpk', models.IntegerField(null=True, db_index=True)),
                ('message', models.TextField(blank=True)),
                ('metadata', models.TextField(default=b'{}')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DbNode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', django_extensions.db.fields.UUIDField(db_index=True, editable=False, blank=True)),
                ('type', models.CharField(max_length=255, db_index=True)),
                ('label', models.CharField(db_index=True, max_length=255, blank=True)),
                ('description', models.TextField(blank=True)),
                ('ctime', models.DateTimeField(default=db.timezone.now, editable=False, db_index=True)),
                ('mtime', models.DateTimeField(auto_now=True, db_index=True)),
                ('nodeversion', models.IntegerField(default=1, editable=False)),
                ('public', models.BooleanField(default=False)),
                ('dbcomputer', models.ForeignKey(related_name='dbnodes', on_delete=django.db.models.deletion.PROTECT, to='db.DbComputer', null=True)),
                ('outputs', models.ManyToManyField(related_name='inputs', through='db.DbLink', to='db.DbNode')),
                ('user', models.ForeignKey(related_name='dbnodes', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DbSetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=1024, db_index=True)),
                ('datatype', models.CharField(default=b'none', max_length=10, db_index=True, choices=[(b'float', b'float'), (b'int', b'int'), (b'txt', b'txt'), (b'bool', b'bool'), (b'date', b'date'), (b'json', b'json'), (b'dict', b'dict'), (b'list', b'list'), (b'none', b'none')])),
                ('tval', models.TextField(default=b'', blank=True)),
                ('fval', models.FloatField(default=None, null=True)),
                ('ival', models.IntegerField(default=None, null=True)),
                ('bval', models.NullBooleanField(default=None)),
                ('dval', models.DateTimeField(default=None, null=True)),
                ('description', models.TextField(blank=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DbWorkflow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', django_extensions.db.fields.UUIDField(editable=False, blank=True)),
                ('ctime', models.DateTimeField(default=db.timezone.now, editable=False)),
                ('mtime', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(db_index=True, max_length=255, blank=True)),
                ('description', models.TextField(blank=True)),
                ('nodeversion', models.IntegerField(default=1, editable=False)),
                ('lastsyncedversion', models.IntegerField(default=0, editable=False)),
                ('state', models.CharField(default='INITIALIZED', max_length=255, choices=[(b'CREATED', b'CREATED'), (b'FINISHED', b'FINISHED'), (b'RUNNING', b'RUNNING'), (b'SLEEP', b'SLEEP'), (b'ERROR', b'ERROR'), (b'INITIALIZED', b'INITIALIZED')])),
                ('report', models.TextField(blank=True)),
                ('module', models.TextField()),
                ('module_class', models.TextField()),
                ('script_path', models.TextField()),
                ('script_md5', models.CharField(max_length=255)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DbWorkflowData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('time', models.DateTimeField(default=db.timezone.now, editable=False)),
                ('data_type', models.CharField(default='PARAMETER', max_length=255)),
                ('value_type', models.CharField(default='NONE', max_length=255)),
                ('json_value', models.TextField(blank=True)),
                ('aiida_obj', models.ForeignKey(blank=True, to='db.DbNode', null=True)),
                ('parent', models.ForeignKey(related_name='data', to='db.DbWorkflow')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DbWorkflowStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('time', models.DateTimeField(default=db.timezone.now, editable=False)),
                ('nextcall', models.CharField(default=b'none', max_length=255)),
                ('state', models.CharField(default='CREATED', max_length=255, choices=[(b'CREATED', b'CREATED'), (b'FINISHED', b'FINISHED'), (b'RUNNING', b'RUNNING'), (b'SLEEP', b'SLEEP'), (b'ERROR', b'ERROR'), (b'INITIALIZED', b'INITIALIZED')])),
                ('calculations', models.ManyToManyField(related_name='workflow_step', to='db.DbNode')),
                ('parent', models.ForeignKey(related_name='steps', to='db.DbWorkflow')),
                ('sub_workflows', models.ManyToManyField(related_name='parent_workflow_step', to='db.DbWorkflow')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='dbworkflowstep',
            unique_together=set([('parent', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='dbworkflowdata',
            unique_together=set([('parent', 'name', 'data_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='dbsetting',
            unique_together=set([('key',)]),
        ),
        migrations.AddField(
            model_name='dblink',
            name='input',
            field=models.ForeignKey(related_name='output_links', on_delete=django.db.models.deletion.PROTECT, to='db.DbNode'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dblink',
            name='output',
            field=models.ForeignKey(related_name='input_links', to='db.DbNode'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dbgroup',
            name='dbnodes',
            field=models.ManyToManyField(related_name='dbgroups', to='db.DbNode'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dbgroup',
            name='user',
            field=models.ForeignKey(related_name='dbgroups', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='dbgroup',
            unique_together=set([('name', 'type')]),
        ),
        migrations.AddField(
            model_name='dbextra',
            name='dbnode',
            field=models.ForeignKey(related_name='dbextras', to='db.DbNode'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='dbextra',
            unique_together=set([('dbnode', 'key')]),
        ),
        migrations.AddField(
            model_name='dbcomment',
            name='dbnode',
            field=models.ForeignKey(related_name='dbcomments', to='db.DbNode'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dbcomment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dbcalcstate',
            name='dbnode',
            field=models.ForeignKey(related_name='dbstates', to='db.DbNode'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='dbcalcstate',
            unique_together=set([('dbnode', 'state')]),
        ),
        migrations.AddField(
            model_name='dbauthinfo',
            name='dbcomputer',
            field=models.ForeignKey(to='db.DbComputer'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='dbauthinfo',
            unique_together=set([('aiidauser', 'dbcomputer')]),
        ),
        migrations.AddField(
            model_name='dbattribute',
            name='dbnode',
            field=models.ForeignKey(related_name='dbattributes', to='db.DbNode'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='dbattribute',
            unique_together=set([('dbnode', 'key')]),
        ),
    ]
