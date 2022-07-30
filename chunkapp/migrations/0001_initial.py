

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChunkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, max_length=200, null=True)),

                ('zip_file', models.FileField(blank=True, null=True, upload_to='')),
                ('chunk_size', models.IntegerField()),

                ('chunk_size', models.IntegerField()),
                ('zip_link', models.CharField(blank=True, max_length=300, null=True)), 
                ('created', models.DateTimeField(auto_now_add=True)),
                ('custom_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
