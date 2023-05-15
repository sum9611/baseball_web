# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BaseballsTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    player_id = models.PositiveIntegerField()
    player_name = models.CharField(max_length=200)
    player_birth = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'baseballs_test'


class BattingInfo(models.Model):
    yyyymmdd = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=10)
    player_birth = models.DateField()
    team = models.CharField(max_length=10)
    p = models.CharField(db_column='P', max_length=10)  # Field name made lowercase.
    tpa = models.IntegerField(db_column='TPA', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    rbi = models.IntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    go = models.IntegerField(db_column='GO', blank=True, null=True)  # Field name made lowercase.
    fo = models.IntegerField(db_column='FO', blank=True, null=True)  # Field name made lowercase.
    pit = models.IntegerField(db_column='PIT', blank=True, null=True)  # Field name made lowercase.
    gdp = models.IntegerField(db_column='GDP', blank=True, null=True)  # Field name made lowercase.
    lob = models.IntegerField(db_column='LOB', blank=True, null=True)  # Field name made lowercase.
    avg = models.DecimalField(db_column='AVG', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    ops = models.DecimalField(db_column='OPS', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    li = models.DecimalField(db_column='LI', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    wpa = models.DecimalField(db_column='WPA', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    re24 = models.DecimalField(db_column='RE24', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'batting_info'
        unique_together = (('yyyymmdd', 'player_name', 'player_birth'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PitchingInfo(models.Model):
    yyyymmdd = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=10)
    player_birth = models.DateField()
    team = models.CharField(max_length=10)
    today_type = models.CharField(max_length=10, blank=True, null=True)
    ip = models.FloatField(db_column='IP', blank=True, null=True)  # Field name made lowercase.
    tbf = models.IntegerField(db_column='TBF', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    k = models.IntegerField(db_column='K', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    go_fo = models.CharField(db_column='GO-FO', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pit_s = models.CharField(db_column='PIT-S', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ir_is = models.CharField(db_column='IR-IS', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gsc = models.IntegerField(db_column='GSC', blank=True, null=True)  # Field name made lowercase.
    era = models.DecimalField(db_column='ERA', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    whip = models.CharField(db_column='WHIP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    li = models.DecimalField(db_column='LI', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    wpa = models.DecimalField(db_column='WPA', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    re24 = models.DecimalField(db_column='RE24', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pitching_info'
        unique_together = (('yyyymmdd', 'player_name', 'player_birth'),)


class PlayerInfo(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=10)
    player_birth = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_info'


class WeeklyBattingInfo(models.Model):
    week = models.CharField(primary_key=True, max_length=10)
    player_name = models.CharField(max_length=10)
    player_birth = models.DateField()
    team = models.CharField(max_length=10)
    tpa = models.IntegerField(db_column='TPA', blank=True, null=True)  # Field name made lowercase.
    rtpa = models.FloatField(db_column='RTPA', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    rbi = models.IntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    so = models.IntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    go = models.IntegerField(db_column='GO', blank=True, null=True)  # Field name made lowercase.
    fo = models.IntegerField(db_column='FO', blank=True, null=True)  # Field name made lowercase.
    pit = models.IntegerField(db_column='PIT', blank=True, null=True)  # Field name made lowercase.
    gdp = models.IntegerField(db_column='GDP', blank=True, null=True)  # Field name made lowercase.
    lob = models.IntegerField(db_column='LOB', blank=True, null=True)  # Field name made lowercase.
    avg = models.DecimalField(db_column='AVG', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    game_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weekly_batting_info'
        unique_together = (('week', 'player_name', 'player_birth'),)


class WeeklyPitchingInfo(models.Model):
    week = models.CharField(primary_key=True, max_length=10)
    player_name = models.CharField(max_length=10)
    player_birth = models.DateField()
    team = models.CharField(max_length=10)
    today_type = models.CharField(max_length=10, blank=True, null=True)
    ip = models.FloatField(db_column='IP', blank=True, null=True)  # Field name made lowercase.
    rip = models.FloatField(db_column='RIP', blank=True, null=True)  # Field name made lowercase.
    tbf = models.IntegerField(db_column='TBF', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    k = models.IntegerField(db_column='K', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    game_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weekly_pitching_info'
        unique_together = (('week', 'player_name', 'player_birth'),)
