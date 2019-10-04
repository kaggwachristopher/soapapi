# Generated by Django 2.2.5 on 2019-10-03 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='RefactoryUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('Primary_Contact', models.CharField(blank=True, max_length=255, null=True)),
                ('Secondary_Contact', models.CharField(blank=True, max_length=255, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('Admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('Admin_Photo', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=20)),
                ('role_description', models.CharField(max_length=20)),
                ('registration_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('Staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('Staff_Photo', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Admin_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='refactory.Administrator')),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='refactory.Administrator')),
            ],
        ),
        migrations.CreateModel(
            name='StaffRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='refactory.Role')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='refactory.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='refactory.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('applicant_id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(blank=True, max_length=255, null=True)),
                ('applicant_Photo', models.CharField(blank=True, max_length=255, null=True)),
                ('Gender', models.CharField(blank=True, max_length=255, null=True)),
                ('DateofBirth', models.DateField(blank=True, null=True)),
                ('Town_Residential', models.CharField(blank=True, max_length=255, null=True)),
                ('Country', models.CharField(blank=True, max_length=255, null=True)),
                ('Nationality', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdministratorRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administrator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='refactory.Administrator')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='refactory.Role')),
            ],
        ),
    ]
