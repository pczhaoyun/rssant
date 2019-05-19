# Generated by Django 2.1.7 on 2019-05-19 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ool


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rssant_api', '0009_auto_20190518_0659'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedCreation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_version', ool.VersionField(default=0)),
                ('_created', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('_updated', models.DateTimeField(auto_now=True, help_text='更新时间')),
                ('url', models.TextField(help_text='用户输入的供稿地址')),
                ('is_from_bookmark', models.BooleanField(blank=True, default=False, help_text='是否从书签导入', null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('updating', 'updating'), ('ready', 'ready'), ('error', 'error')], default='pending', help_text='状态', max_length=20)),
                ('message', models.TextField(help_text='查找订阅的日志信息')),
                ('dt_created', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('dt_updated', models.DateTimeField(blank=True, help_text='更新时间', null=True)),
            ],
            bases=(ool.VersionedMixin, models.Model),
        ),
        migrations.RemoveIndex(
            model_name='userstory',
            name='rssant_api__user_fe_cfb4de_idx',
        ),
        migrations.RemoveIndex(
            model_name='userstory',
            name='rssant_api__user_id_3bc826_idx',
        ),
        migrations.RemoveField(
            model_name='userfeed',
            name='status',
        ),
        migrations.RemoveField(
            model_name='userfeed',
            name='url',
        ),
        migrations.AlterUniqueTogether(
            name='userstory',
            unique_together={('user', 'feed', 'offset'), ('user_feed', 'offset'), ('user', 'story')},
        ),
        migrations.AddIndex(
            model_name='userstory',
            index=models.Index(fields=['user', 'feed', 'offset'], name='rssant_api__user_id_1aed91_idx'),
        ),
        migrations.AddIndex(
            model_name='userstory',
            index=models.Index(fields=['user', 'feed', 'story'], name='rssant_api__user_id_c419be_idx'),
        ),
        migrations.AddField(
            model_name='feedcreation',
            name='feed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rssant_api.Feed'),
        ),
        migrations.AddField(
            model_name='feedcreation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='feedcreation',
            index=models.Index(fields=['user', 'dt_created'], name='rssant_api__user_id_09d733_idx'),
        ),
    ]