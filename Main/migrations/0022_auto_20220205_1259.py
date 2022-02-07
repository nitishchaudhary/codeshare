# Generated by Django 3.1.1 on 2022-02-05 07:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0021_auto_20220205_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 7, 29, 56, 575614, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='project_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('comment_date', models.DateTimeField(default=datetime.datetime(2022, 2, 5, 7, 29, 56, 575614, tzinfo=utc))),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Main.project')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='like_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='Main.project')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]