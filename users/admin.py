from django.contrib import admin

# Register your models here.
from .models import UserInfo,User
# Register your models here.

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('pk','user_name','user_phone','car_number','car_booking_status','car_site_address',
    'car_slot_no','admin_bit','car_type',)
    # exclude = ('user_name','car_number')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= ('id','username','first_name','last_name','email','is_staff','is_accountant','is_site_manager','is_superuser',)

#     car_site_address = models.CharField(u'Site Number',max_length=20,null=True)
#    car_slot_no = models.CharField(u'Slot Number',max_length=20,null=True)

#    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # ('password', models.CharField(max_length=128, verbose_name='password')),
                # ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                # ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                # ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                # ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                # ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                # ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                # ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                # ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                # ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                # ('is_accountant', models.BooleanField(default=False)),
                # ('is_site_manager', models.BooleanField(default=False)),
                # ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                # ('user_permissions',