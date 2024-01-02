# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AcActividad(models.Model):
    act_id = models.AutoField(db_column='ACT_ID', primary_key=True)  # Field name made lowercase.
    act_nom = models.CharField(db_column='ACT_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    act_des = models.CharField(db_column='ACT_DES', max_length=100, blank=True, null=True)  # Field name made lowercase.
    act_fcrea = models.DateTimeField(db_column='ACT_FCREA', blank=True, null=True)  # Field name made lowercase.
    act_ucrea = models.CharField(db_column='ACT_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_ACTIVIDAD'


class AcAhandheld(models.Model):
    w_tipo = models.CharField(db_column='W_TIPO', primary_key=True, max_length=1)  # Field name made lowercase.
    w_fechat = models.DateTimeField(db_column='W_FECHAT')  # Field name made lowercase.
    w_tarjeta = models.CharField(db_column='W_TARJETA', max_length=25)  # Field name made lowercase.
    w_equipo = models.CharField(db_column='W_EQUIPO', max_length=10)  # Field name made lowercase.
    w_codpermiso = models.CharField(db_column='W_CODPERMISO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    w_placa = models.CharField(db_column='W_PLACA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    w_tipom = models.CharField(db_column='W_TIPOM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    w_fechaup = models.DateTimeField(db_column='W_FECHAUP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_AHANDHELD'
        unique_together = (('w_tipo', 'w_fechat', 'w_tarjeta'),)


class AcArea(models.Model):
    area_id = models.AutoField(db_column='AREA_ID', primary_key=True)  # Field name made lowercase.
    area_nom = models.CharField(db_column='AREA_NOM', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    area_des = models.CharField(db_column='AREA_DES', max_length=100, blank=True, null=True)  # Field name made lowercase.
    area_fcrea = models.DateTimeField(db_column='AREA_FCREA', blank=True, null=True)  # Field name made lowercase.
    area_ucrea = models.CharField(db_column='AREA_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_AREA'


class AcAsistnow(models.Model):
    asis_tipopermiso = models.IntegerField(db_column='ASIS_TIPOPERMISO', primary_key=True)  # Field name made lowercase.
    asis_id = models.CharField(db_column='ASIS_ID', max_length=6)  # Field name made lowercase.
    asis_ing = models.DateTimeField(db_column='ASIS_ING')  # Field name made lowercase.
    asis_zona = models.CharField(db_column='ASIS_ZONA', max_length=20)  # Field name made lowercase.
    asis_fecha = models.DateTimeField(db_column='ASIS_FECHA', blank=True, null=True)  # Field name made lowercase.
    asis_hora = models.CharField(db_column='ASIS_HORA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    asis_tipo = models.CharField(db_column='ASIS_TIPO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    asis_res = models.CharField(db_column='ASIS_RES', max_length=20, blank=True, null=True)  # Field name made lowercase.
    asis_f = models.IntegerField(db_column='ASIS_F', blank=True, null=True)  # Field name made lowercase.
    asis_fn = models.DateTimeField(db_column='ASIS_FN', blank=True, null=True)  # Field name made lowercase.
    asis_hn = models.DateTimeField(db_column='ASIS_HN', blank=True, null=True)  # Field name made lowercase.
    asis_conductor = models.CharField(db_column='ASIS_CONDUCTOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    asis_vehiculo = models.CharField(db_column='ASIS_VEHICULO', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_ASISTNOW'
        unique_together = (('asis_tipopermiso', 'asis_id', 'asis_ing', 'asis_zona'),)


class AcConductor(models.Model):
    co_id = models.CharField(db_column='CO_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    co_empresa = models.DecimalField(db_column='CO_EMPRESA', max_digits=18, decimal_places=0)  # Field name made lowercase.
    co_fcrea = models.DateTimeField(db_column='CO_FCREA', blank=True, null=True)  # Field name made lowercase.
    co_ucrea = models.CharField(db_column='CO_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_CONDUCTOR'


class AcDetalleCpp(models.Model):
    ppd_id_m = models.OneToOneField('AcMaestroCpp', models.DO_NOTHING, db_column='PPD_ID_M', primary_key=True)  # Field name made lowercase.
    ppd_ced = models.CharField(db_column='PPD_CED', max_length=12)  # Field name made lowercase.
    ppd_id = models.CharField(db_column='PPD_ID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ppd_nom = models.CharField(db_column='PPD_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ppd_obs1 = models.CharField(db_column='PPD_OBS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ppd_obs2 = models.CharField(db_column='PPD_OBS2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ppd_fcrea = models.DateTimeField(db_column='PPD_FCREA', blank=True, null=True)  # Field name made lowercase.
    ppd_ucrea = models.CharField(db_column='PPD_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ppd_flagn = models.BooleanField(db_column='PPD_FLAGN', blank=True, null=True)  # Field name made lowercase.
    ppd_bloqueo = models.CharField(db_column='PPD_BLOQUEO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ppd_finger = models.CharField(db_column='PPD_FINGER', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_DETALLE_CPP'
        unique_together = (('ppd_id_m', 'ppd_ced'),)


class AcHandheldhuellas(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=12)  # Field name made lowercase.
    huella1 = models.BinaryField(db_column='HUELLA1', blank=True, null=True)  # Field name made lowercase.
    huella2 = models.BinaryField(db_column='HUELLA2', blank=True, null=True)  # Field name made lowercase.
    now = models.DateTimeField(db_column='NOW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_HandHeldHuellas'


class AcMaestroCpp(models.Model):
    pp_id = models.AutoField(db_column='PP_ID', primary_key=True)  # Field name made lowercase.
    pp_id_sol = models.CharField(db_column='PP_ID_SOL', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pp_ced_sol = models.CharField(db_column='PP_CED_SOL', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pp_nom_sol = models.CharField(db_column='PP_NOM_SOL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_emp_id = models.DecimalField(db_column='PP_EMP_ID', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pp_emp_nom = models.CharField(db_column='PP_EMP_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_area_id = models.DecimalField(db_column='PP_AREA_ID', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pp_area_nom = models.CharField(db_column='PP_AREA_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_act_id = models.DecimalField(db_column='PP_ACT_ID', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pp_act_nom = models.CharField(db_column='PP_ACT_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_finicio = models.DateTimeField(db_column='PP_FINICIO', blank=True, null=True)  # Field name made lowercase.
    pp_ffinal = models.DateTimeField(db_column='PP_FFINAL', blank=True, null=True)  # Field name made lowercase.
    pp_fcrea = models.DateTimeField(db_column='PP_FCREA', blank=True, null=True)  # Field name made lowercase.
    pp_ucrea = models.CharField(db_column='PP_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pp_bloqueo = models.CharField(db_column='PP_BLOQUEO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pp_uauto = models.CharField(db_column='PP_UAUTO', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_MAESTRO_CPP'


class AcMaestroCvp(models.Model):
    pp_id = models.AutoField(db_column='PP_ID', primary_key=True)  # Field name made lowercase.
    pp_id_sol = models.CharField(db_column='PP_ID_SOL', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pp_ced_sol = models.CharField(db_column='PP_CED_SOL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_nom_sol = models.CharField(db_column='PP_NOM_SOL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_emp_id = models.DecimalField(db_column='PP_EMP_ID', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pp_emp_nom = models.CharField(db_column='PP_EMP_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_area_id = models.DecimalField(db_column='PP_AREA_ID', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pp_area_nom = models.CharField(db_column='PP_AREA_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_act_id = models.DecimalField(db_column='PP_ACT_ID', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pp_act_nom = models.CharField(db_column='PP_ACT_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_placa = models.CharField(db_column='PP_PLACA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pp_tipov = models.CharField(db_column='PP_TIPOV', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pp_color = models.CharField(db_column='PP_COLOR', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pp_marca = models.CharField(db_column='PP_MARCA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pp_modelo = models.CharField(db_column='PP_MODELO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pp_finicio = models.DateTimeField(db_column='PP_FINICIO', blank=True, null=True)  # Field name made lowercase.
    pp_ffinal = models.DateTimeField(db_column='PP_FFINAL', blank=True, null=True)  # Field name made lowercase.
    pp_fcrea = models.DateTimeField(db_column='PP_FCREA', blank=True, null=True)  # Field name made lowercase.
    pp_ucrea = models.CharField(db_column='PP_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pp_obs1 = models.CharField(db_column='PP_OBS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_obs2 = models.CharField(db_column='PP_OBS2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_flagn = models.BooleanField(db_column='PP_FLAGN', blank=True, null=True)  # Field name made lowercase.
    pp_bloqueo = models.CharField(db_column='PP_BLOQUEO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pp_uauto = models.CharField(db_column='PP_UAUTO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pp_tarjeta = models.CharField(db_column='PP_TARJETA', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_MAESTRO_CVP'


class AcMaestroCvp1(models.Model):
    pp_id = models.AutoField(db_column='PP_ID', primary_key=True)  # Field name made lowercase.
    pp_id_sol = models.CharField(db_column='PP_ID_SOL', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pp_ced_sol = models.CharField(db_column='PP_CED_SOL', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pp_nom_sol = models.CharField(db_column='PP_NOM_SOL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_emp_id = models.DecimalField(db_column='PP_EMP_ID', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pp_emp_nom = models.CharField(db_column='PP_EMP_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_area_id = models.DecimalField(db_column='PP_AREA_ID', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pp_area_nom = models.CharField(db_column='PP_AREA_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_act_id = models.DecimalField(db_column='PP_ACT_ID', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pp_act_nom = models.CharField(db_column='PP_ACT_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_placa = models.CharField(db_column='PP_PLACA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pp_tipov = models.CharField(db_column='PP_TIPOV', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pp_color = models.CharField(db_column='PP_COLOR', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pp_marca = models.CharField(db_column='PP_MARCA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pp_modelo = models.CharField(db_column='PP_MODELO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pp_finicio = models.DateTimeField(db_column='PP_FINICIO', blank=True, null=True)  # Field name made lowercase.
    pp_ffinal = models.DateTimeField(db_column='PP_FFINAL', blank=True, null=True)  # Field name made lowercase.
    pp_fcrea = models.DateTimeField(db_column='PP_FCREA', blank=True, null=True)  # Field name made lowercase.
    pp_ucrea = models.CharField(db_column='PP_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pp_obs1 = models.CharField(db_column='PP_OBS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_obs2 = models.CharField(db_column='PP_OBS2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pp_flagn = models.BooleanField(db_column='PP_FLAGN', blank=True, null=True)  # Field name made lowercase.
    pp_bloqueo = models.CharField(db_column='PP_BLOQUEO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pp_uauto = models.CharField(db_column='PP_UAUTO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pp_tarjeta = models.CharField(db_column='PP_TARJETA', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_MAESTRO_CVP1'


class AcNomina(models.Model):
    nomina_id = models.CharField(db_column='NOMINA_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    nomina_ape = models.CharField(db_column='NOMINA_APE', max_length=100)  # Field name made lowercase.
    nomina_nom = models.CharField(db_column='NOMINA_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomina_ced = models.CharField(db_column='NOMINA_CED', max_length=12, blank=True, null=True)  # Field name made lowercase.
    nomina_emp = models.ForeignKey('Externoe', models.DO_NOTHING, db_column='NOMINA_EMP', blank=True, null=True)  # Field name made lowercase.
    nomina_cargo = models.ForeignKey('Califica', models.DO_NOTHING, db_column='NOMINA_CARGO', blank=True, null=True)  # Field name made lowercase.
    nomina_cargoc = models.ForeignKey('Califica', models.DO_NOTHING, db_column='NOMINA_CARGOC', blank=True, null=True)  # Field name made lowercase.
    nomina_obs = models.CharField(db_column='NOMINA_OBS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomina_foto = models.BinaryField(db_column='NOMINA_FOTO', blank=True, null=True)  # Field name made lowercase.
    nomina_firma = models.BinaryField(db_column='NOMINA_FIRMA', blank=True, null=True)  # Field name made lowercase.
    nomina_cre = models.BinaryField(db_column='NOMINA_CRE', blank=True, null=True)  # Field name made lowercase.
    nomina_hf1 = models.BinaryField(db_column='NOMINA_HF1', blank=True, null=True)  # Field name made lowercase.
    nomina_hi1 = models.BinaryField(db_column='NOMINA_HI1', blank=True, null=True)  # Field name made lowercase.
    nomina_hd1 = models.CharField(db_column='NOMINA_HD1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nomina_hf2 = models.BinaryField(db_column='NOMINA_HF2', blank=True, null=True)  # Field name made lowercase.
    nomina_hi2 = models.BinaryField(db_column='NOMINA_HI2', blank=True, null=True)  # Field name made lowercase.
    nomina_hd2 = models.CharField(db_column='NOMINA_HD2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nomina_fcrea = models.DateTimeField(db_column='NOMINA_FCREA', blank=True, null=True)  # Field name made lowercase.
    nomina_ucrea = models.CharField(db_column='NOMINA_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nomina_flag = models.CharField(db_column='NOMINA_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_NOMINA'


class AcNomPuerta(models.Model):
    nom = models.OneToOneField('Nomina', models.DO_NOTHING, db_column='NOM_ID', primary_key=True)  # Field name made lowercase.
    puer = models.ForeignKey('AcPuerta', models.DO_NOTHING, db_column='PUER_ID')  # Field name made lowercase.
    turn_id = models.IntegerField(db_column='TURN_ID', blank=True, null=True)  # Field name made lowercase.
    turn_feci = models.DateTimeField(db_column='TURN_FECI', blank=True, null=True)  # Field name made lowercase.
    turn_fecf = models.DateTimeField(db_column='TURN_FECF', blank=True, null=True)  # Field name made lowercase.
    turn_tipo = models.IntegerField(db_column='TURN_TIPO', blank=True, null=True)  # Field name made lowercase.
    turn_sta = models.IntegerField(db_column='TURN_STA', blank=True, null=True)  # Field name made lowercase.
    turn_now = models.DateTimeField(db_column='TURN_NOW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_NOM_PUERTA'
        unique_together = (('nom', 'puer'),)


class AcPuerta(models.Model):
    prt_cod = models.CharField(db_column='PRT_COD', primary_key=True, max_length=4)  # Field name made lowercase.
    pri_des = models.CharField(db_column='PRI_DES', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pri_loc = models.CharField(db_column='PRI_LOC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pri_p = models.IntegerField(db_column='PRI_P', blank=True, null=True)  # Field name made lowercase.
    pri_area = models.ForeignKey('Area', models.DO_NOTHING, db_column='PRI_AREA')  # Field name made lowercase.
    pri_area1 = models.CharField(db_column='PRI_AREA1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pri_ip = models.CharField(db_column='PRI_IP', unique=True, max_length=16, blank=True, null=True)  # Field name made lowercase.
    pri_fec = models.DateTimeField(db_column='PRI_FEC', blank=True, null=True)  # Field name made lowercase.
    pri_sta = models.CharField(db_column='PRI_STA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pri_st = models.CharField(db_column='PRI_ST', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pri_pto = models.CharField(db_column='PRI_PTO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    pri_tipo = models.CharField(db_column='PRI_TIPO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pri_virdi = models.CharField(db_column='PRI_VIRDI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pri_ti = models.CharField(db_column='PRI_TI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pri_te = models.CharField(db_column='PRI_TE', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_PUERTA'


class AcServer(models.Model):
    pr_id = models.CharField(db_column='PR_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    pr_ucod = models.CharField(db_column='PR_UCOD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pr_coda = models.BooleanField(db_column='PR_CODA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_SERVER'


class AcUser(models.Model):
    ac_user = models.OneToOneField('Nomina', models.DO_NOTHING, db_column='AC_USER', primary_key=True)  # Field name made lowercase.
    ac_p1 = models.BooleanField(db_column='AC_P1', blank=True, null=True)  # Field name made lowercase.
    ac_p2 = models.BooleanField(db_column='AC_P2', blank=True, null=True)  # Field name made lowercase.
    ac_p3 = models.BooleanField(db_column='AC_P3', blank=True, null=True)  # Field name made lowercase.
    ac_p4 = models.BooleanField(db_column='AC_P4', blank=True, null=True)  # Field name made lowercase.
    ac_p5 = models.BooleanField(db_column='AC_P5', blank=True, null=True)  # Field name made lowercase.
    ac_p6 = models.BooleanField(db_column='AC_P6', blank=True, null=True)  # Field name made lowercase.
    ac_p7 = models.BooleanField(db_column='AC_P7', blank=True, null=True)  # Field name made lowercase.
    ac_p8 = models.BooleanField(db_column='AC_P8', blank=True, null=True)  # Field name made lowercase.
    ac_p9 = models.BooleanField(db_column='AC_P9', blank=True, null=True)  # Field name made lowercase.
    ac_p10 = models.BooleanField(db_column='AC_P10', blank=True, null=True)  # Field name made lowercase.
    ac_p11 = models.BooleanField(db_column='AC_P11', blank=True, null=True)  # Field name made lowercase.
    ac_p12 = models.BooleanField(db_column='AC_P12', blank=True, null=True)  # Field name made lowercase.
    ac_p13 = models.BooleanField(db_column='AC_P13', blank=True, null=True)  # Field name made lowercase.
    ac_p14 = models.BooleanField(db_column='AC_P14', blank=True, null=True)  # Field name made lowercase.
    ac_p15 = models.BooleanField(db_column='AC_P15', blank=True, null=True)  # Field name made lowercase.
    ac_p16 = models.BooleanField(db_column='AC_P16', blank=True, null=True)  # Field name made lowercase.
    ac_p17 = models.BooleanField(db_column='AC_P17', blank=True, null=True)  # Field name made lowercase.
    ac_p18 = models.BooleanField(db_column='AC_P18', blank=True, null=True)  # Field name made lowercase.
    ac_p19 = models.BooleanField(db_column='AC_P19', blank=True, null=True)  # Field name made lowercase.
    ac_p20 = models.BooleanField(db_column='AC_P20', blank=True, null=True)  # Field name made lowercase.
    ac_ucrea = models.CharField(db_column='AC_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ac_fcrea = models.DateTimeField(db_column='AC_FCREA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_USER'


class AcVehiculos(models.Model):
    ve_id = models.AutoField(db_column='VE_ID', primary_key=True)  # Field name made lowercase.
    ve_placa = models.CharField(db_column='VE_PLACA', unique=True, max_length=10, blank=True, null=True)  # Field name made lowercase.
    ve_tipo = models.ForeignKey('AcVTipo', models.DO_NOTHING, db_column='VE_TIPO', blank=True, null=True)  # Field name made lowercase.
    ve_marca = models.ForeignKey('AcVModelo', models.DO_NOTHING, db_column='VE_MARCA', blank=True, null=True)  # Field name made lowercase.
    ve_modelo = models.ForeignKey('AcVModelo', models.DO_NOTHING, db_column='VE_MODELO', blank=True, null=True)  # Field name made lowercase.
    ve_empresa = models.ForeignKey('Externoe', models.DO_NOTHING, db_column='VE_EMPRESA', blank=True, null=True)  # Field name made lowercase.
    ve_color = models.CharField(db_column='VE_COLOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ve_matricula = models.BinaryField(db_column='VE_MATRICULA', blank=True, null=True)  # Field name made lowercase.
    ve_propnom = models.CharField(db_column='VE_PROPNOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ve_propced = models.CharField(db_column='VE_PROPCED', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ve_obs = models.CharField(db_column='VE_OBS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ve_fcrea = models.DateTimeField(db_column='VE_FCREA', blank=True, null=True)  # Field name made lowercase.
    ve_ucrea = models.CharField(db_column='VE_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_VEHICULOS'


class AcVMarca(models.Model):
    vm_marca = models.CharField(db_column='VM_MARCA', primary_key=True, max_length=25)  # Field name made lowercase.
    vm_des = models.CharField(db_column='VM_DES', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vm_fcrea = models.DateTimeField(db_column='VM_FCREA', blank=True, null=True)  # Field name made lowercase.
    vm_ucrea = models.CharField(db_column='VM_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_V_MARCA'


class AcVModelo(models.Model):
    vmo_modelo = models.CharField(db_column='VMO_MODELO', primary_key=True, max_length=25)  # Field name made lowercase.
    vmo_marca = models.ForeignKey(AcVMarca, models.DO_NOTHING, db_column='VMO_MARCA')  # Field name made lowercase.
    vmo_fcrea = models.DateTimeField(db_column='VMO_FCREA', blank=True, null=True)  # Field name made lowercase.
    vmo_ucrea = models.CharField(db_column='VMO_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_V_MODELO'
        unique_together = (('vmo_modelo', 'vmo_marca'),)


class AcVTipo(models.Model):
    vt_nom = models.CharField(db_column='VT_NOM', primary_key=True, max_length=25)  # Field name made lowercase.
    vt_des = models.CharField(db_column='VT_DES', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vt_fcrea = models.DateTimeField(db_column='VT_FCREA', blank=True, null=True)  # Field name made lowercase.
    vt_ucrea = models.CharField(db_column='VT_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AC_V_TIPO'


class AigCategoria(models.Model):
    c_id = models.CharField(db_column='C_ID', primary_key=True, max_length=35)  # Field name made lowercase.
    c_des = models.CharField(db_column='C_DES', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_nivel = models.CharField(db_column='C_NIVEL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    c_ucrea = models.CharField(db_column='C_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    c_fcrea = models.DateTimeField(db_column='C_FCREA', blank=True, null=True)  # Field name made lowercase.
    c_estructura = models.ForeignKey('AigEstruc', models.DO_NOTHING, db_column='C_ESTRUCTURA', blank=True, null=True)  # Field name made lowercase.
    c_estado = models.CharField(db_column='C_ESTADO', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AIG_CATEGORIA'


class AigCatArbol(models.Model):
    im_cedula = models.CharField(db_column='IM_CEDULA', primary_key=True, max_length=20)  # Field name made lowercase.
    im_categ1 = models.CharField(db_column='IM_CATEG1', max_length=35)  # Field name made lowercase.
    im_categ2 = models.CharField(db_column='IM_CATEG2', max_length=35)  # Field name made lowercase.
    im_categ3 = models.CharField(db_column='IM_CATEG3', max_length=35)  # Field name made lowercase.
    im_pos = models.IntegerField(db_column='IM_POS')  # Field name made lowercase.
    im_ucrea = models.CharField(db_column='IM_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    im_fcrea = models.DateTimeField(db_column='IM_FCREA', blank=True, null=True)  # Field name made lowercase.
    im_estado = models.CharField(db_column='IM_ESTADO', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AIG_CAT_ARBOL'
        unique_together = (('im_cedula', 'im_categ1', 'im_categ2', 'im_categ3'),)


class AigEstruc(models.Model):
    td_id = models.CharField(db_column='TD_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    td_nom = models.CharField(db_column='TD_NOM', unique=True, max_length=50)  # Field name made lowercase.
    td_des = models.CharField(db_column='TD_DES', max_length=50, blank=True, null=True)  # Field name made lowercase.
    td_ncampos = models.SmallIntegerField(db_column='TD_NCAMPOS', blank=True, null=True)  # Field name made lowercase.
    td_tipo = models.CharField(db_column='TD_TIPO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    td_ruta = models.CharField(db_column='TD_RUTA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    td_ucrea = models.CharField(db_column='TD_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    td_fcrea = models.DateTimeField(db_column='TD_FCREA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AIG_ESTRUC'


class AigEstCampos(models.Model):
    tc_est = models.OneToOneField(AigEstruc, models.DO_NOTHING, db_column='TC_EST', primary_key=True)  # Field name made lowercase.
    tc_num = models.SmallIntegerField(db_column='TC_NUM')  # Field name made lowercase.
    tc_tipo = models.CharField(db_column='TC_TIPO', max_length=10)  # Field name made lowercase.
    tc_nom = models.CharField(db_column='TC_NOM', max_length=50)  # Field name made lowercase.
    tc_len = models.IntegerField(db_column='TC_LEN')  # Field name made lowercase.
    tc_ucrea = models.CharField(db_column='TC_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tc_fcrea = models.DateTimeField(db_column='TC_FCREA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AIG_EST_CAMPOS'
        unique_together = (('tc_est', 'tc_num'),)


class AigMedia(models.Model):
    im_cedula = models.CharField(db_column='IM_CEDULA', primary_key=True, max_length=20)  # Field name made lowercase.
    im_categ1 = models.CharField(db_column='IM_CATEG1', max_length=35)  # Field name made lowercase.
    im_categ2 = models.CharField(db_column='IM_CATEG2', max_length=35)  # Field name made lowercase.
    im_categ3 = models.CharField(db_column='IM_CATEG3', max_length=35)  # Field name made lowercase.
    im_key = models.AutoField(db_column='IM_KEY')  # Field name made lowercase.
    im_idx1 = models.CharField(db_column='IM_IDX1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    im_idx2 = models.CharField(db_column='IM_IDX2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    im_idx3 = models.CharField(db_column='IM_IDX3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    im_idx4 = models.CharField(db_column='IM_IDX4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    im_idx5 = models.CharField(db_column='IM_IDX5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    im_len = models.DecimalField(db_column='IM_LEN', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    im_tipo = models.CharField(db_column='IM_TIPO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    im_ucrea = models.CharField(db_column='IM_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    im_fcrea = models.DateTimeField(db_column='IM_FCREA', blank=True, null=True)  # Field name made lowercase.
    im_umod = models.CharField(db_column='IM_UMOD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    im_fmod = models.DateTimeField(db_column='IM_FMOD', blank=True, null=True)  # Field name made lowercase.
    im_media = models.BinaryField(db_column='IM_MEDIA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AIG_MEDIA'
        unique_together = (('im_cedula', 'im_categ1', 'im_categ2', 'im_categ3', 'im_key'),)


class Apbmaster(models.Model):
    apb_id = models.CharField(db_column='APB_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    nomina_controlapb1 = models.BooleanField(db_column='NOMINA_CONTROLAPB1', blank=True, null=True)  # Field name made lowercase.
    nomina_statusapb1 = models.IntegerField(db_column='NOMINA_STATUSAPB1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APBMASTER'


class Area(models.Model):
    area_id = models.AutoField(db_column='AREA_ID', primary_key=True)  # Field name made lowercase.
    area_nom = models.CharField(db_column='AREA_NOM', unique=True, max_length=100)  # Field name made lowercase.
    area_des = models.CharField(db_column='AREA_DES', max_length=40, blank=True, null=True)  # Field name made lowercase.
    area_obs = models.CharField(db_column='AREA_OBS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    area_em = models.CharField(db_column='AREA_EM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    area_sel = models.CharField(db_column='AREA_SEL', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AREA'
        unique_together = (('area_id', 'area_nom'),)


class Asistarjeta(models.Model):
    asis_id = models.CharField(db_column='ASIS_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    asis_ing = models.DateTimeField(db_column='ASIS_ING')  # Field name made lowercase.
    asis_zona = models.CharField(db_column='ASIS_ZONA', max_length=20)  # Field name made lowercase.
    asis_fecha = models.DateTimeField(db_column='ASIS_FECHA', blank=True, null=True)  # Field name made lowercase.
    asis_hora = models.CharField(db_column='ASIS_HORA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    asis_tipo = models.CharField(db_column='ASIS_TIPO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    asis_res = models.CharField(db_column='ASIS_RES', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ASISTARJETA'
        unique_together = (('asis_id', 'asis_ing', 'asis_zona'),)


class Asistnow(models.Model):
    asis_id = models.CharField(db_column='ASIS_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    asis_ing = models.DateTimeField(db_column='ASIS_ING')  # Field name made lowercase.
    asis_zona = models.CharField(db_column='ASIS_ZONA', max_length=20)  # Field name made lowercase.
    asis_fecha = models.DateTimeField(db_column='ASIS_FECHA', blank=True, null=True)  # Field name made lowercase.
    asis_hora = models.CharField(db_column='ASIS_HORA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    asis_tipo = models.CharField(db_column='ASIS_TIPO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    asis_res = models.CharField(db_column='ASIS_RES', max_length=20, blank=True, null=True)  # Field name made lowercase.
    asis_f = models.IntegerField(db_column='ASIS_F', blank=True, null=True)  # Field name made lowercase.
    asis_fn = models.DateTimeField(db_column='ASIS_FN', blank=True, null=True)  # Field name made lowercase.
    asis_hn = models.DateTimeField(db_column='ASIS_HN', blank=True, null=True)  # Field name made lowercase.
    asis_print = models.IntegerField(db_column='ASIS_PRINT', blank=True, null=True)  # Field name made lowercase.
    asis_novedad = models.CharField(db_column='ASIS_NOVEDAD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    asis_mm = models.CharField(db_column='ASIS_MM', max_length=1, blank=True, null=True)  # Field name made lowercase.
    asis_mail = models.SmallIntegerField(db_column='ASIS_MAIL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ASISTNOW'
        unique_together = (('asis_id', 'asis_ing', 'asis_zona'),)


class AsistnowImg(models.Model):
    asis_id = models.CharField(db_column='ASIS_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    asis_ing = models.DateTimeField(db_column='ASIS_ING')  # Field name made lowercase.
    asis_zona = models.CharField(db_column='ASIS_ZONA', max_length=20)  # Field name made lowercase.
    asis_imagen = models.BinaryField(db_column='ASIS_IMAGEN', blank=True, null=True)  # Field name made lowercase.
    asis_tipo = models.CharField(db_column='ASIS_TIPO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    asis_res = models.CharField(db_column='ASIS_RES', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ASISTNOW_IMG'
        unique_together = (('asis_id', 'asis_ing', 'asis_zona'),)


class AuxNomina(models.Model):
    anom_id = models.CharField(db_column='ANOM_ID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    anom_ape = models.CharField(db_column='ANOM_APE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    anom_nom = models.CharField(db_column='ANOM_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    anom_ced = models.CharField(db_column='ANOM_CED', max_length=15, blank=True, null=True)  # Field name made lowercase.
    anom_emp = models.CharField(db_column='ANOM_EMP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    anom_area = models.CharField(db_column='ANOM_AREA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    anom_dpto = models.CharField(db_column='ANOM_DPTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    anom_car = models.CharField(db_column='ANOM_CAR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    anom_fecn = models.DateTimeField(db_column='ANOM_FECN', blank=True, null=True)  # Field name made lowercase.
    anom_obs = models.CharField(db_column='ANOM_OBS', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUX_NOMINA'


class CafePosicionDatos(models.Model):
    cafe_datos = models.CharField(db_column='CAFE_DATOS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cafe_posicionx = models.DecimalField(db_column='CAFE_POSICIONX', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    cafe_posiciony = models.DecimalField(db_column='CAFE_POSICIONY', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    cafe_estado = models.CharField(db_column='CAFE_ESTADO', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAFE_POSICION_DATOS'


class CafeTicket(models.Model):
    fecha_ticket = models.DateTimeField(db_column='FECHA_TICKET', primary_key=True)  # Field name made lowercase.
    num_ticket = models.IntegerField(db_column='NUM_TICKET', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAFE_TICKET'


class Califica(models.Model):
    cali_id = models.AutoField(db_column='CALI_ID', primary_key=True)  # Field name made lowercase.
    cali_nom = models.CharField(db_column='CALI_NOM', unique=True, max_length=100)  # Field name made lowercase.
    cali_des = models.CharField(db_column='CALI_DES', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CALIFICA'
        unique_together = (('cali_id', 'cali_nom'),)


class CcAsist(models.Model):
    c_now = models.DateTimeField(db_column='C_NOW', primary_key=True)  # Field name made lowercase.
    c_user = models.CharField(db_column='C_USER', max_length=10)  # Field name made lowercase.
    c_zona = models.CharField(db_column='C_ZONA', max_length=20)  # Field name made lowercase.
    c_tipo = models.CharField(db_column='C_TIPO', max_length=10)  # Field name made lowercase.
    c_cccod = models.CharField(db_column='C_CCCOD', max_length=10)  # Field name made lowercase.
    c_ccnom = models.CharField(db_column='C_CCNOM', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CC_ASIST'
        unique_together = (('c_now', 'c_user', 'c_zona', 'c_tipo', 'c_cccod'),)


class CcAsistenciaConsolid(models.Model):
    cc_id_emp = models.CharField(db_column='CC_ID_EMP', max_length=10)  # Field name made lowercase.
    cc_fecha_ingreso = models.DateTimeField(db_column='CC_FECHA_INGRESO')  # Field name made lowercase.
    cc_fecha_salida = models.DateTimeField(db_column='CC_FECHA_SALIDA', blank=True, null=True)  # Field name made lowercase.
    cc_hora_ingreso = models.DateTimeField(db_column='CC_HORA_INGRESO', blank=True, null=True)  # Field name made lowercase.
    cc_hora_salida = models.DateTimeField(db_column='CC_HORA_SALIDA', blank=True, null=True)  # Field name made lowercase.
    cc_horas_laboradas = models.DateTimeField(db_column='CC_HORAS_LABORADAS', blank=True, null=True)  # Field name made lowercase.
    cc_minutos_laborados = models.SmallIntegerField(db_column='CC_MINUTOS_LABORADOS', blank=True, null=True)  # Field name made lowercase.
    cc_cod_cc = models.CharField(db_column='CC_COD_CC', max_length=10)  # Field name made lowercase.
    cc_contador = models.SmallIntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CC_ASISTENCIA_CONSOLID'


class CcGrupo(models.Model):
    c_mid = models.CharField(db_column='C_MID', primary_key=True, max_length=50)  # Field name made lowercase.
    c_des = models.CharField(db_column='C_DES', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_fcrea = models.DateTimeField(db_column='C_FCREA', blank=True, null=True)  # Field name made lowercase.
    c_ucrea = models.CharField(db_column='C_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CC_GRUPO'


class CcMaestro(models.Model):
    cc_id = models.CharField(db_column='CC_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    cc_nom = models.CharField(db_column='CC_NOM', unique=True, max_length=50)  # Field name made lowercase.
    cc_fcrea = models.DateTimeField(db_column='CC_FCREA', blank=True, null=True)  # Field name made lowercase.
    cc_ucrea = models.CharField(db_column='CC_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cc_org = models.CharField(db_column='CC_ORG', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CC_MAESTRO'


class Config(models.Model):
    co_id = models.CharField(db_column='CO_ID', max_length=50)  # Field name made lowercase.
    co_ip = models.CharField(db_column='CO_IP', max_length=50)  # Field name made lowercase.
    co_nom = models.CharField(db_column='CO_NOM', max_length=50)  # Field name made lowercase.
    co_lid = models.IntegerField(db_column='CO_LID')  # Field name made lowercase.
    co_localidad = models.CharField(db_column='CO_LOCALIDAD', max_length=50)  # Field name made lowercase.
    co_aid = models.IntegerField(db_column='CO_AID')  # Field name made lowercase.
    co_agencia = models.CharField(db_column='CO_AGENCIA', max_length=50)  # Field name made lowercase.
    co_nivel = models.CharField(db_column='CO_NIVEL', max_length=50)  # Field name made lowercase.
    co_digitos = models.IntegerField(db_column='CO_DIGITOS')  # Field name made lowercase.
    co_tipo = models.CharField(db_column='CO_TIPO', max_length=50)  # Field name made lowercase.
    co_hora = models.CharField(db_column='CO_HORA', max_length=50)  # Field name made lowercase.
    co_modo = models.CharField(db_column='CO_MODO', max_length=50)  # Field name made lowercase.
    co_forzar = models.IntegerField(db_column='CO_FORZAR')  # Field name made lowercase.
    co_costo = models.IntegerField(db_column='CO_COSTO')  # Field name made lowercase.
    co_normal = models.IntegerField(db_column='CO_NORMAL')  # Field name made lowercase.
    co_logo = models.IntegerField(db_column='CO_LOGO')  # Field name made lowercase.
    co_max = models.IntegerField(db_column='CO_MAX')  # Field name made lowercase.
    co_contador = models.IntegerField(db_column='CO_CONTADOR')  # Field name made lowercase.
    co_teclado = models.BooleanField(db_column='CO_TECLADO', blank=True, null=True)  # Field name made lowercase.
    co_tickets = models.BooleanField(db_column='CO_TICKETS', blank=True, null=True)  # Field name made lowercase.
    co_cod = models.IntegerField(db_column='CO_COD', blank=True, null=True)  # Field name made lowercase.
    co_hmarcaante = models.IntegerField(db_column='CO_HMARCAANTE', blank=True, null=True)  # Field name made lowercase.
    co_horario = models.BooleanField(db_column='CO_HORARIO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONFIG'


class CrDatos(models.Model):
    cr_id = models.CharField(db_column='CR_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    cr_c0 = models.CharField(db_column='CR_C0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cr_c1 = models.CharField(db_column='CR_C1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cr_c2 = models.CharField(db_column='CR_C2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cr_c3 = models.CharField(db_column='CR_C3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cr_c4 = models.CharField(db_column='CR_C4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cr_c5 = models.CharField(db_column='CR_C5', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR_DATOS'


class Dpto(models.Model):
    dep_id = models.AutoField(db_column='DEP_ID', primary_key=True)  # Field name made lowercase.
    dep_are = models.DecimalField(db_column='DEP_ARE', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dep_nom = models.CharField(db_column='DEP_NOM', max_length=100)  # Field name made lowercase.
    dep_desc = models.CharField(db_column='DEP_DESC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dep_obs = models.CharField(db_column='DEP_OBS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dep_em = models.CharField(db_column='DEP_EM', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DPTO'
        unique_together = (('dep_id', 'dep_nom'),)


class Externoe(models.Model):
    empe_id = models.AutoField(db_column='EMPE_ID', primary_key=True)  # Field name made lowercase.
    empe_nom = models.CharField(db_column='EMPE_NOM', unique=True, max_length=50)  # Field name made lowercase.
    empe_dir = models.CharField(db_column='EMPE_DIR', max_length=70, blank=True, null=True)  # Field name made lowercase.
    empe_ruc = models.CharField(db_column='EMPE_RUC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    empe_rep = models.CharField(db_column='EMPE_REP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    empe_telf = models.CharField(db_column='EMPE_TELF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    empe_fax = models.CharField(db_column='EMPE_FAX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    empe_web = models.CharField(db_column='EMPE_WEB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    empe_cont = models.CharField(db_column='EMPE_CONT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    empe_obs = models.CharField(db_column='EMPE_OBS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    empe_code = models.CharField(db_column='EMPE_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EXTERNOE'


class FcTagControl(models.Model):
    tg_id = models.AutoField(db_column='TG_ID', primary_key=True)  # Field name made lowercase.
    tg_num_print = models.CharField(db_column='TG_NUM_PRINT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tg_num_rf = models.CharField(db_column='TG_NUM_RF', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tg_now = models.DateTimeField(db_column='TG_NOW', blank=True, null=True)  # Field name made lowercase.
    tg_estado = models.CharField(db_column='TG_ESTADO', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FC_TAG_CONTROL'


class Huellas(models.Model):
    id = models.AutoField()
    cedulas = models.CharField(primary_key=True, max_length=10)
    h_1 = models.BinaryField(db_column='H_1', blank=True, null=True)  # Field name made lowercase.
    h_2 = models.BinaryField(db_column='H_2', blank=True, null=True)  # Field name made lowercase.
    h_3 = models.BinaryField(db_column='H_3', blank=True, null=True)  # Field name made lowercase.
    h_4 = models.BinaryField(db_column='H_4', blank=True, null=True)  # Field name made lowercase.
    h_5 = models.BinaryField(db_column='H_5', blank=True, null=True)  # Field name made lowercase.
    h_6 = models.BinaryField(db_column='H_6', blank=True, null=True)  # Field name made lowercase.
    h_7 = models.BinaryField(db_column='H_7', blank=True, null=True)  # Field name made lowercase.
    h_8 = models.BinaryField(db_column='H_8', blank=True, null=True)  # Field name made lowercase.
    h_9 = models.BinaryField(db_column='H_9', blank=True, null=True)  # Field name made lowercase.
    h_10 = models.BinaryField(db_column='H_10', blank=True, null=True)  # Field name made lowercase.
    imagen = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUELLAS'


class Hoja1(models.Model):
    codigo = models.CharField(db_column='CODIGO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='APELLIDOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='NOMBRES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cod_area = models.CharField(db_column='COD_AREA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cod_cargo = models.CharField(db_column='COD_CARGO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cod_dpto = models.CharField(db_column='COD_DPTO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cod_emp = models.CharField(db_column='COD_EMP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    migrado = models.CharField(db_column='MIGRADO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nom_area = models.CharField(db_column='NOM_AREA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nom_cargo = models.CharField(db_column='NOM_CARGO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nom_dpto = models.CharField(db_column='NOM_DPTO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nom_emp = models.CharField(db_column='NOM_EMP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nomina_card = models.CharField(db_column='NOMINA_CARD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nomina_cod = models.CharField(db_column='NOMINA_COD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nomina_hwsq1 = models.BinaryField(db_column='NOMINA_HWSQ1', blank=True, null=True)  # Field name made lowercase.
    nomina_hwsq2 = models.BinaryField(db_column='NOMINA_HWSQ2', blank=True, null=True)  # Field name made lowercase.
    nomina_obs = models.CharField(db_column='NOMINA_OBS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    obs_area = models.CharField(db_column='OBS_AREA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    obs_cargo = models.CharField(db_column='OBS_CARGO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    obs_dpto = models.CharField(db_column='OBS_DPTO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    obs_emp = models.CharField(db_column='OBS_EMP', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hoja1'


class NewCredencial(models.Model):
    cr_id = models.CharField(db_column='CR_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    cr_fimpresion = models.DateTimeField(db_column='CR_FIMPRESION')  # Field name made lowercase.
    cr_resultado = models.CharField(db_column='CR_RESULTADO', max_length=1)  # Field name made lowercase.
    cr_cedula = models.CharField(db_column='CR_CEDULA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cr_ciudadano = models.CharField(db_column='CR_CIUDADANO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cr_fcaduda = models.DateTimeField(db_column='CR_FCADUDA', blank=True, null=True)  # Field name made lowercase.
    cr_uimprime = models.CharField(db_column='CR_UIMPRIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cr_aautoriza = models.CharField(db_column='CR_AAUTORIZA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cr_fautoriza = models.DateTimeField(db_column='CR_FAUTORIZA', blank=True, null=True)  # Field name made lowercase.
    cr_tarjeta = models.CharField(db_column='CR_TARJETA', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NEW_CREDENCIAL'
        unique_together = (('cr_id', 'cr_fimpresion', 'cr_resultado'),)


class NewCredencialMaestro(models.Model):
    cr_id = models.CharField(db_column='CR_ID', primary_key=True, max_length=30)  # Field name made lowercase.
    cr_des = models.CharField(db_column='CR_DES', max_length=30)  # Field name made lowercase.
    cr_img = models.BinaryField(db_column='CR_IMG', blank=True, null=True)  # Field name made lowercase.
    cr_firma = models.BooleanField(db_column='CR_FIRMA', blank=True, null=True)  # Field name made lowercase.
    cr_foto = models.BooleanField(db_column='CR_FOTO', blank=True, null=True)  # Field name made lowercase.
    cr_tipo = models.BooleanField(db_column='CR_TIPO', blank=True, null=True)  # Field name made lowercase.
    cr_fotof = models.BooleanField(db_column='CR_FOTOF', blank=True, null=True)  # Field name made lowercase.
    cr_cbarra = models.BooleanField(db_column='CR_CBARRA', blank=True, null=True)  # Field name made lowercase.
    cr_ucrea = models.CharField(db_column='CR_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cr_fcrea = models.DateTimeField(db_column='CR_FCREA', blank=True, null=True)  # Field name made lowercase.
    cr_userri = models.CharField(db_column='CR_UserRI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cr_claveri = models.CharField(db_column='CR_ClaveRI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cr_imgatras = models.BinaryField(db_column='CR_IMGATRAS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NEW_CREDENCIAL_MAESTRO'


class NewListan(models.Model):
    nomina_ced = models.CharField(db_column='NOMINA_CED', primary_key=True, max_length=12)  # Field name made lowercase.
    nomina_fini = models.DateTimeField(db_column='NOMINA_FINI')  # Field name made lowercase.
    nomina_ffin = models.DateTimeField(db_column='NOMINA_FFIN')  # Field name made lowercase.
    nomina_ape = models.CharField(db_column='NOMINA_APE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomina_nom = models.CharField(db_column='NOMINA_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomina_des = models.CharField(db_column='NOMINA_DES', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomina_rep = models.CharField(db_column='NOMINA_REP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomina_fing = models.DateTimeField(db_column='NOMINA_FING', blank=True, null=True)  # Field name made lowercase.
    nomina_uing = models.CharField(db_column='NOMINA_UING', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NEW_LISTAN'
        unique_together = (('nomina_ced', 'nomina_fini', 'nomina_ffin'),)


class NewNovedad(models.Model):
    i_fecha = models.DateTimeField(db_column='I_FECHA', primary_key=True)  # Field name made lowercase.
    i_cod = models.ForeignKey('Nomina', models.DO_NOTHING, db_column='I_COD')  # Field name made lowercase.
    i_tipo = models.CharField(db_column='I_TIPO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    i_texto = models.CharField(db_column='I_TEXTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i_texto1 = models.CharField(db_column='I_TEXTO1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    i_accion = models.CharField(db_column='I_ACCION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    i_usercrea = models.CharField(db_column='I_USERCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    i_fechacrea = models.DateTimeField(db_column='I_FECHACREA', blank=True, null=True)  # Field name made lowercase.
    i_reporta = models.CharField(db_column='I_REPORTA', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NEW_NOVEDAD'
        unique_together = (('i_fecha', 'i_cod'),)


class Nomina(models.Model):
    nomina_id = models.CharField(db_column='NOMINA_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    nomina_ape = models.CharField(db_column='NOMINA_APE', max_length=100)  # Field name made lowercase.
    nomina_nom = models.CharField(db_column='NOMINA_NOM', max_length=50)  # Field name made lowercase.
    nomina_clave = models.CharField(db_column='NOMINA_CLAVE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nomina_cod = models.CharField(db_column='NOMINA_COD', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nomina_tipo = models.CharField(db_column='NOMINA_TIPO', max_length=30)  # Field name made lowercase.
    nomina_cal = models.ForeignKey(Califica, models.DO_NOTHING, db_column='NOMINA_CAL')  # Field name made lowercase.
    nomina_area = models.ForeignKey(Area, models.DO_NOTHING, db_column='NOMINA_AREA')  # Field name made lowercase.
    nomina_dep = models.ForeignKey(Dpto, models.DO_NOTHING, db_column='NOMINA_DEP')  # Field name made lowercase.
    nomina_cal1 = models.ForeignKey(Califica, models.DO_NOTHING, db_column='NOMINA_CAL1', blank=True, null=True)  # Field name made lowercase.
    nomina_area1 = models.ForeignKey(Area, models.DO_NOTHING, db_column='NOMINA_AREA1', blank=True, null=True)  # Field name made lowercase.
    nomina_dep1 = models.ForeignKey(Dpto, models.DO_NOTHING, db_column='NOMINA_DEP1', blank=True, null=True)  # Field name made lowercase.
    nomina_fing = models.DateTimeField(db_column='NOMINA_FING', blank=True, null=True)  # Field name made lowercase.
    nomina_fsal = models.DateTimeField(db_column='NOMINA_FSAL', blank=True, null=True)  # Field name made lowercase.
    nomina_suel = models.DecimalField(db_column='NOMINA_SUEL', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nomina_com = models.DecimalField(db_column='NOMINA_COM', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nomina_auti = models.IntegerField(db_column='NOMINA_AUTI', blank=True, null=True)  # Field name made lowercase.
    nomina_es = models.IntegerField(db_column='NOMINA_ES', blank=True, null=True)  # Field name made lowercase.
    nomina_obs = models.CharField(db_column='NOMINA_OBS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomina_emp = models.DecimalField(db_column='NOMINA_EMP', max_digits=10, decimal_places=0)  # Field name made lowercase.
    nomina_finger = models.CharField(db_column='NOMINA_FINGER', max_length=3, blank=True, null=True)  # Field name made lowercase.
    nomina_f1 = models.BinaryField(db_column='NOMINA_F1', blank=True, null=True)  # Field name made lowercase.
    nomina_ced = models.BinaryField(db_column='NOMINA_CED', blank=True, null=True)  # Field name made lowercase.
    nomina_fir = models.BinaryField(db_column='NOMINA_FIR', blank=True, null=True)  # Field name made lowercase.
    nomina_hd1 = models.CharField(db_column='NOMINA_HD1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nomina_hf1 = models.BinaryField(db_column='NOMINA_HF1', blank=True, null=True)  # Field name made lowercase.
    nomina_hi1 = models.BinaryField(db_column='NOMINA_HI1', blank=True, null=True)  # Field name made lowercase.
    nomina_hd2 = models.CharField(db_column='NOMINA_HD2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nomina_hf2 = models.BinaryField(db_column='NOMINA_HF2', blank=True, null=True)  # Field name made lowercase.
    nomina_hi2 = models.BinaryField(db_column='NOMINA_HI2', blank=True, null=True)  # Field name made lowercase.
    nomina_sel = models.IntegerField(db_column='NOMINA_SEL', blank=True, null=True)  # Field name made lowercase.
    nomina_empc = models.CharField(db_column='NOMINA_EMPC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nomina_empe = models.CharField(db_column='NOMINA_EMPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nomina_p1 = models.BooleanField(db_column='NOMINA_P1', blank=True, null=True)  # Field name made lowercase.
    nomina_p2 = models.BooleanField(db_column='NOMINA_P2', blank=True, null=True)  # Field name made lowercase.
    nomina_p3 = models.BooleanField(db_column='NOMINA_P3', blank=True, null=True)  # Field name made lowercase.
    nomina_p4 = models.BooleanField(db_column='NOMINA_P4', blank=True, null=True)  # Field name made lowercase.
    nomina_p5 = models.BooleanField(db_column='NOMINA_P5', blank=True, null=True)  # Field name made lowercase.
    nomina_p6 = models.BooleanField(db_column='NOMINA_P6', blank=True, null=True)  # Field name made lowercase.
    nomina_p7 = models.BooleanField(db_column='NOMINA_P7', blank=True, null=True)  # Field name made lowercase.
    nomina_p8 = models.BooleanField(db_column='NOMINA_P8', blank=True, null=True)  # Field name made lowercase.
    nomina_p9 = models.BooleanField(db_column='NOMINA_P9', blank=True, null=True)  # Field name made lowercase.
    nomina_p10 = models.BooleanField(db_column='NOMINA_P10', blank=True, null=True)  # Field name made lowercase.
    nomina_p11 = models.BooleanField(db_column='NOMINA_P11', blank=True, null=True)  # Field name made lowercase.
    nomina_p12 = models.BooleanField(db_column='NOMINA_P12', blank=True, null=True)  # Field name made lowercase.
    nomina_p13 = models.BooleanField(db_column='NOMINA_P13', blank=True, null=True)  # Field name made lowercase.
    nomina_p14 = models.BooleanField(db_column='NOMINA_P14', blank=True, null=True)  # Field name made lowercase.
    nomina_p15 = models.BooleanField(db_column='NOMINA_P15', blank=True, null=True)  # Field name made lowercase.
    nomina_p16 = models.BooleanField(db_column='NOMINA_P16', blank=True, null=True)  # Field name made lowercase.
    nomina_p17 = models.BooleanField(db_column='NOMINA_P17', blank=True, null=True)  # Field name made lowercase.
    nomina_p18 = models.BooleanField(db_column='NOMINA_P18', blank=True, null=True)  # Field name made lowercase.
    nomina_p19 = models.BooleanField(db_column='NOMINA_P19', blank=True, null=True)  # Field name made lowercase.
    nomina_p20 = models.BooleanField(db_column='NOMINA_P20', blank=True, null=True)  # Field name made lowercase.
    nomina_doc = models.BinaryField(db_column='NOMINA_DOC', blank=True, null=True)  # Field name made lowercase.
    nomina_pla = models.BinaryField(db_column='NOMINA_PLA', blank=True, null=True)  # Field name made lowercase.
    nomina_f = models.IntegerField(db_column='NOMINA_F', blank=True, null=True)  # Field name made lowercase.
    nomina_card = models.CharField(db_column='NOMINA_CARD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nomina_fcard = models.DateTimeField(db_column='NOMINA_FCARD', blank=True, null=True)  # Field name made lowercase.
    nomina_obs1 = models.CharField(db_column='NOMINA_OBS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomina_now = models.DateTimeField(db_column='NOMINA_NOW', blank=True, null=True)  # Field name made lowercase.
    nomina_cafe = models.BooleanField(db_column='NOMINA_CAFE', blank=True, null=True)  # Field name made lowercase.
    nomina_auto = models.CharField(db_column='NOMINA_AUTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nomina_p21 = models.BooleanField(db_column='NOMINA_P21', blank=True, null=True)  # Field name made lowercase.
    nomina_p22 = models.BooleanField(db_column='NOMINA_P22', blank=True, null=True)  # Field name made lowercase.
    nomina_p23 = models.BooleanField(db_column='NOMINA_P23', blank=True, null=True)  # Field name made lowercase.
    nomina_p24 = models.BooleanField(db_column='NOMINA_P24', blank=True, null=True)  # Field name made lowercase.
    nomina_p25 = models.BooleanField(db_column='NOMINA_P25', blank=True, null=True)  # Field name made lowercase.
    nomina_controlapb = models.BooleanField(db_column='NOMINA_CONTROLAPB', blank=True, null=True)  # Field name made lowercase.
    nomina_statusapb = models.IntegerField(db_column='NOMINA_STATUSAPB', blank=True, null=True)  # Field name made lowercase.
    nomina_cafemenu = models.BooleanField(db_column='NOMINA_CAFEMENU', blank=True, null=True)  # Field name made lowercase.
    nomina_level = models.IntegerField(db_column='NOMINA_LEVEL', blank=True, null=True)  # Field name made lowercase.
    nomina_tipoid = models.CharField(db_column='NOMINA_TIPOID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nomina_tiponom = models.CharField(db_column='NOMINA_TIPONOM', max_length=35, blank=True, null=True)  # Field name made lowercase.
    nomina_hs1 = models.CharField(db_column='NOMINA_HS1', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    nomina_hs2 = models.CharField(db_column='NOMINA_HS2', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    nomina_cafecontrol = models.DecimalField(db_column='NOMINA_CAFECONTROL', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    nomina_serv1 = models.FloatField(db_column='NOMINA_SERV1')  # Field name made lowercase.
    nomina_serv2 = models.FloatField(db_column='NOMINA_SERV2')  # Field name made lowercase.
    nomina_serv3 = models.FloatField(db_column='NOMINA_SERV3')  # Field name made lowercase.
    nomina_serv4 = models.FloatField(db_column='NOMINA_SERV4')  # Field name made lowercase.
    nomina_serv5 = models.FloatField(db_column='NOMINA_SERV5')  # Field name made lowercase.
    nomina_serv6 = models.FloatField(db_column='NOMINA_SERV6')  # Field name made lowercase.
    nomina_serv7 = models.FloatField(db_column='NOMINA_SERV7')  # Field name made lowercase.
    nomina_serv8 = models.FloatField(db_column='NOMINA_SERV8')  # Field name made lowercase.
    nomina_serv9 = models.FloatField(db_column='NOMINA_SERV9')  # Field name made lowercase.
    nomina_cardkey = models.CharField(db_column='NOMINA_CARDKEY', max_length=6)  # Field name made lowercase.
    nomina_tipo_registro = models.IntegerField(db_column='NOMINA_TIPO_REGISTRO')  # Field name made lowercase.
    nomina_hwsq1 = models.BinaryField(db_column='NOMINA_HWSQ1', blank=True, null=True)  # Field name made lowercase.
    nomina_hwsq2 = models.BinaryField(db_column='NOMINA_HWSQ2', blank=True, null=True)  # Field name made lowercase.
    nomina_face = models.CharField(db_column='NOMINA_FACE', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    nomina_face_len = models.IntegerField(db_column='NOMINA_FACE_LEN', blank=True, null=True)  # Field name made lowercase.
    b_matcher_flag = models.CharField(db_column='B_MATCHER_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nomina_p26 = models.BooleanField(db_column='NOMINA_P26', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOMINA'


class NominaDatosAdicional(models.Model):
    nomina_id = models.CharField(db_column='NOMINA_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    nomina_direccion = models.CharField(db_column='NOMINA_DIRECCION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nomina_telefono = models.CharField(db_column='NOMINA_TELEFONO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nomina_celular = models.CharField(db_column='NOMINA_CELULAR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nomina_discapacidad = models.IntegerField(db_column='NOMINA_DISCAPACIDAD', blank=True, null=True)  # Field name made lowercase.
    nomina_discapacida_descr = models.CharField(db_column='NOMINA_DISCAPACIDA_DESCR', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nomina_alergias = models.CharField(db_column='NOMINA_ALERGIAS', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOMINA_DATOS_ADICIONAL'


class NomParamVeh(models.Model):
    p_id = models.CharField(db_column='P_ID', primary_key=True, max_length=4)  # Field name made lowercase.
    p_desc_param = models.CharField(db_column='P_DESC_PARAM', max_length=64)  # Field name made lowercase.
    p_val_param = models.CharField(db_column='P_VAL_PARAM', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOM_PARAM_VEH'


class NomPuerta(models.Model):
    nom = models.OneToOneField(Nomina, models.DO_NOTHING, db_column='NOM_ID', primary_key=True)  # Field name made lowercase.
    puer = models.ForeignKey('Puerta', models.DO_NOTHING, db_column='PUER_ID')  # Field name made lowercase.
    turn_id = models.IntegerField(db_column='TURN_ID', blank=True, null=True)  # Field name made lowercase.
    turn_feci = models.DateTimeField(db_column='TURN_FECI', blank=True, null=True)  # Field name made lowercase.
    turn_fecf = models.DateTimeField(db_column='TURN_FECF', blank=True, null=True)  # Field name made lowercase.
    turn_tipo = models.IntegerField(db_column='TURN_TIPO', blank=True, null=True)  # Field name made lowercase.
    turn_sta = models.IntegerField(db_column='TURN_STA', blank=True, null=True)  # Field name made lowercase.
    turn_now = models.DateTimeField(db_column='TURN_NOW', blank=True, null=True)  # Field name made lowercase.
    turn_marca = models.IntegerField(db_column='TURN_MARCA', blank=True, null=True)  # Field name made lowercase.
    turn_tcod = models.CharField(db_column='TURN_TCOD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    turn_sel = models.CharField(db_column='TURN_SEL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    turn_estado_up = models.DecimalField(db_column='TURN_ESTADO_UP', max_digits=1, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    turn_fecha_up = models.DateTimeField(db_column='TURN_FECHA_UP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOM_PUERTA'
        unique_together = (('nom', 'puer'),)


class NomPuertabackup(models.Model):
    nom_id = models.CharField(db_column='NOM_ID', max_length=6)  # Field name made lowercase.
    puer_id = models.CharField(db_column='PUER_ID', max_length=4)  # Field name made lowercase.
    turn_id = models.IntegerField(db_column='TURN_ID', blank=True, null=True)  # Field name made lowercase.
    turn_feci = models.DateTimeField(db_column='TURN_FECI', blank=True, null=True)  # Field name made lowercase.
    turn_fecf = models.DateTimeField(db_column='TURN_FECF', blank=True, null=True)  # Field name made lowercase.
    turn_tipo = models.IntegerField(db_column='TURN_TIPO', blank=True, null=True)  # Field name made lowercase.
    turn_sta = models.IntegerField(db_column='TURN_STA', blank=True, null=True)  # Field name made lowercase.
    turn_now = models.DateTimeField(db_column='TURN_NOW', blank=True, null=True)  # Field name made lowercase.
    turn_marca = models.IntegerField(db_column='TURN_MARCA', blank=True, null=True)  # Field name made lowercase.
    turn_tcod = models.CharField(db_column='TURN_TCOD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    turn_sel = models.CharField(db_column='TURN_SEL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    turn_estado_up = models.DecimalField(db_column='TURN_ESTADO_UP', max_digits=1, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    turn_fecha_up = models.DateTimeField(db_column='TURN_FECHA_UP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOM_PUERTABACKUP'


class NomPuertaex(models.Model):
    nom_id = models.CharField(db_column='NOM_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    turn_fec = models.DateTimeField(db_column='TURN_FEC')  # Field name made lowercase.
    turn_user = models.CharField(db_column='TURN_USER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    turn_now = models.DateTimeField(db_column='TURN_NOW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOM_PUERTAEX'
        unique_together = (('nom_id', 'turn_fec'),)


class NomPuertalog(models.Model):
    nom_id = models.CharField(db_column='NOM_ID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    puer_id = models.CharField(db_column='PUER_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    turn_id = models.IntegerField(db_column='TURN_ID', blank=True, null=True)  # Field name made lowercase.
    turn_feci = models.DateTimeField(db_column='TURN_FECI', blank=True, null=True)  # Field name made lowercase.
    turn_fecf = models.DateTimeField(db_column='TURN_FECF', blank=True, null=True)  # Field name made lowercase.
    turn_tipo = models.IntegerField(db_column='TURN_TIPO', blank=True, null=True)  # Field name made lowercase.
    turn_sta = models.IntegerField(db_column='TURN_STA', blank=True, null=True)  # Field name made lowercase.
    turn_now = models.DateTimeField(db_column='TURN_NOW', blank=True, null=True)  # Field name made lowercase.
    turn_delnow = models.DateTimeField(db_column='TURN_DELNOW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOM_PUERTALOG'


class NomPuertaCafe(models.Model):
    nom_id = models.CharField(db_column='NOM_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    puer_id = models.CharField(db_column='PUER_ID', max_length=4)  # Field name made lowercase.
    turn_id = models.IntegerField(db_column='TURN_ID')  # Field name made lowercase.
    turn_feci = models.DateTimeField(db_column='TURN_FECI', blank=True, null=True)  # Field name made lowercase.
    turn_fecf = models.DateTimeField(db_column='TURN_FECF', blank=True, null=True)  # Field name made lowercase.
    turn_tipo = models.IntegerField(db_column='TURN_TIPO', blank=True, null=True)  # Field name made lowercase.
    turn_sta = models.IntegerField(db_column='TURN_STA', blank=True, null=True)  # Field name made lowercase.
    turn_now = models.DateTimeField(db_column='TURN_NOW', blank=True, null=True)  # Field name made lowercase.
    turn_marca = models.IntegerField(db_column='TURN_MARCA', blank=True, null=True)  # Field name made lowercase.
    turn_tcod = models.CharField(db_column='TURN_TCOD', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOM_PUERTA_CAFE'
        unique_together = (('nom_id', 'puer_id', 'turn_id'),)


class NomPuertaDel(models.Model):
    nom_id = models.CharField(db_column='NOM_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    puer_id = models.CharField(db_column='PUER_ID', max_length=6)  # Field name made lowercase.
    flag_t = models.DecimalField(db_column='FLAG_T', max_digits=1, decimal_places=0)  # Field name made lowercase.
    turn_estado_del = models.DecimalField(db_column='TURN_ESTADO_DEL', max_digits=1, decimal_places=0)  # Field name made lowercase.
    turn_fecha_del = models.DateTimeField(db_column='TURN_FECHA_DEL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOM_PUERTA_DEL'
        unique_together = (('nom_id', 'puer_id'),)


class NumComidasex(models.Model):
    nomina_id = models.CharField(db_column='NOMINA_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    tot_comida = models.IntegerField(db_column='TOT_COMIDA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NUM_COMIDASEX'


class OcFestivos(models.Model):
    d_festivo = models.DateTimeField(db_column='D_FESTIVO', primary_key=True)  # Field name made lowercase.
    d_desc = models.CharField(db_column='D_DESC', max_length=50)  # Field name made lowercase.
    d_locald = models.CharField(db_column='D_LOCALD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d_ucrea = models.CharField(db_column='D_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    d_fcrea = models.DateTimeField(db_column='D_FCREA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OC_FESTIVOS'


class OcRemoteconfig(models.Model):
    cr_b1 = models.BooleanField(db_column='CR_B1', blank=True, null=True)  # Field name made lowercase.
    cr_b2 = models.BooleanField(db_column='CR_B2', blank=True, null=True)  # Field name made lowercase.
    cr_b3 = models.BooleanField(db_column='CR_B3', blank=True, null=True)  # Field name made lowercase.
    cr_b4 = models.BooleanField(db_column='CR_B4', blank=True, null=True)  # Field name made lowercase.
    cr_activo = models.BooleanField(db_column='CR_ACTIVO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OC_REMOTECONFIG'


class OnlyCafeconsultas(models.Model):
    co_nombre = models.CharField(db_column='CO_NOMBRE', max_length=50)  # Field name made lowercase.
    co_descripcion = models.CharField(db_column='CO_DESCRIPCION', max_length=5000)  # Field name made lowercase.
    co_fecha = models.DateTimeField(db_column='CO_FECHA', blank=True, null=True)  # Field name made lowercase.
    co_maq = models.CharField(db_column='CO_MAQ', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONLY_CAFECONSULTAS'


class OnlyConsultas(models.Model):
    co_nombre = models.CharField(db_column='CO_NOMBRE', primary_key=True, max_length=50)  # Field name made lowercase.
    co_descripcion = models.CharField(db_column='CO_DESCRIPCION', max_length=5000)  # Field name made lowercase.
    co_fecha = models.DateTimeField(db_column='CO_FECHA', blank=True, null=True)  # Field name made lowercase.
    co_maq = models.CharField(db_column='CO_MAQ', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONLY_CONSULTAS'


class OnlyMailConfig(models.Model):
    m_id = models.CharField(db_column='M_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    m_service = models.BooleanField(db_column='M_SERVICE', blank=True, null=True)  # Field name made lowercase.
    m_smtp_server = models.CharField(db_column='M_SMTP_SERVER', max_length=60, blank=True, null=True)  # Field name made lowercase.
    m_puerto_server = models.CharField(db_column='M_PUERTO_SERVER', max_length=60, blank=True, null=True)  # Field name made lowercase.
    m_mail_host = models.CharField(db_column='M_MAIL_HOST', max_length=60, blank=True, null=True)  # Field name made lowercase.
    m_autentificacion = models.BooleanField(db_column='M_Autentificacion', blank=True, null=True)  # Field name made lowercase.
    m_user = models.CharField(db_column='M_USER', max_length=60, blank=True, null=True)  # Field name made lowercase.
    m_clave = models.CharField(db_column='M_CLAVE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    m_timeup = models.IntegerField(db_column='M_TIMEUP', blank=True, null=True)  # Field name made lowercase.
    m_fallido = models.IntegerField(db_column='M_Fallido', blank=True, null=True)  # Field name made lowercase.
    m_opcion1 = models.BooleanField(db_column='M_OPCION1', blank=True, null=True)  # Field name made lowercase.
    m_opcion2 = models.BooleanField(db_column='M_OPCION2', blank=True, null=True)  # Field name made lowercase.
    m_opcion3 = models.BooleanField(db_column='M_OPCION3', blank=True, null=True)  # Field name made lowercase.
    m_cuenta1 = models.CharField(db_column='M_CUENTA1', max_length=60, blank=True, null=True)  # Field name made lowercase.
    m_cuenta2 = models.CharField(db_column='M_CUENTA2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    m_cuenta3 = models.CharField(db_column='M_CUENTA3', max_length=60, blank=True, null=True)  # Field name made lowercase.
    m_ssl = models.BooleanField(db_column='M_SSL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONLY_MAIL_CONFIG'


class Puerta(models.Model):
    prt_cod = models.CharField(db_column='PRT_COD', primary_key=True, max_length=4)  # Field name made lowercase.
    pri_des = models.CharField(db_column='PRI_DES', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pri_loc = models.CharField(db_column='PRI_LOC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pri_p = models.IntegerField(db_column='PRI_P', blank=True, null=True)  # Field name made lowercase.
    pri_area = models.ForeignKey(Area, models.DO_NOTHING, db_column='PRI_AREA')  # Field name made lowercase.
    pri_area1 = models.CharField(db_column='PRI_AREA1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pri_ip = models.CharField(db_column='PRI_IP', max_length=16, blank=True, null=True)  # Field name made lowercase.
    pri_fec = models.DateTimeField(db_column='PRI_FEC', blank=True, null=True)  # Field name made lowercase.
    pri_sta = models.CharField(db_column='PRI_STA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pri_st = models.CharField(db_column='PRI_ST', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pri_pto = models.CharField(db_column='PRI_PTO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    pri_tipo = models.CharField(db_column='PRI_TIPO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pri_virdi = models.CharField(db_column='PRI_VIRDI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pri_ti = models.CharField(db_column='PRI_TI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pri_te = models.CharField(db_column='PRI_TE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    pri_printer = models.CharField(db_column='PRI_PRINTER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pri_valclave = models.BooleanField(db_column='PRI_VALCLAVE', blank=True, null=True)  # Field name made lowercase.
    pri_sel = models.IntegerField(db_column='PRI_SEL', blank=True, null=True)  # Field name made lowercase.
    pri_lastuser = models.CharField(db_column='PRI_LASTUSER', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pri_lastmarca = models.DateTimeField(db_column='PRI_LASTMARCA', blank=True, null=True)  # Field name made lowercase.
    pri_open = models.IntegerField(db_column='PRI_OPEN', blank=True, null=True)  # Field name made lowercase.
    pri_tiempo = models.IntegerField(db_column='PRI_TIEMPO', blank=True, null=True)  # Field name made lowercase.
    pri_verifica = models.IntegerField(db_column='PRI_VERIFICA', blank=True, null=True)  # Field name made lowercase.
    pri_last_id = models.CharField(db_column='PRI_LAST_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pri_now = models.DateTimeField(db_column='PRI_NOW', blank=True, null=True)  # Field name made lowercase.
    pri_valida = models.IntegerField(db_column='PRI_VALIDA', blank=True, null=True)  # Field name made lowercase.
    pri_evento = models.CharField(db_column='PRI_EVENTO', max_length=300, blank=True, null=True)  # Field name made lowercase.
    pri_envia_alerta = models.IntegerField(db_column='PRI_ENVIA_ALERTA', blank=True, null=True)  # Field name made lowercase.
    pri_empresa = models.IntegerField(db_column='PRI_EMPRESA', blank=True, null=True)  # Field name made lowercase.
    pri_empresa_nom = models.CharField(db_column='PRI_EMPRESA_NOM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pri_server = models.DecimalField(db_column='PRI_SERVER', max_digits=1, decimal_places=0)  # Field name made lowercase.
    pri_cam = models.BooleanField(db_column='PRI_CAM')  # Field name made lowercase.
    pri_cam_ip = models.CharField(db_column='PRI_CAM_IP', max_length=16, blank=True, null=True)  # Field name made lowercase.
    pri_cam_pass = models.CharField(db_column='PRI_CAM_PASS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pri_cam_user = models.CharField(db_column='PRI_CAM_USER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pri_cam_url = models.CharField(db_column='PRI_CAM_URL', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PUERTA'


class PuertaSta(models.Model):
    p_id = models.CharField(db_column='P_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    p_fecha = models.DateTimeField(db_column='P_Fecha')  # Field name made lowercase.
    p_status = models.CharField(db_column='P_Status', max_length=100, blank=True, null=True)  # Field name made lowercase.
    p_user = models.CharField(db_column='P_User', max_length=60)  # Field name made lowercase.
    p_maq = models.CharField(db_column='P_Maq', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PUERTA_STA'
        unique_together = (('p_id', 'p_fecha', 'p_user'),)


class Tblserver(models.Model):
    pr_id = models.CharField(db_column='PR_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    pr_se = models.CharField(db_column='PR_SE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pr_cod = models.IntegerField(db_column='PR_COD', blank=True, null=True)  # Field name made lowercase.
    pr_log = models.CharField(db_column='PR_Log', max_length=30)  # Field name made lowercase.
    pr_lhora = models.CharField(db_column='PR_LHora', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pr_ip = models.CharField(db_column='PR_IP', max_length=30)  # Field name made lowercase.
    pr_finger = models.CharField(db_column='PR_FINGER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pr_ld = models.BooleanField(db_column='PR_LD', blank=True, null=True)  # Field name made lowercase.
    pr_lt = models.BooleanField(db_column='PR_LT', blank=True, null=True)  # Field name made lowercase.
    pr_f1 = models.CharField(db_column='PR_F1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pr_f2 = models.CharField(db_column='PR_F2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pr_f3 = models.CharField(db_column='PR_F3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pr_f4 = models.CharField(db_column='PR_F4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pr_ucod = models.CharField(db_column='PR_UCOD', max_length=10)  # Field name made lowercase.
    pr_coda = models.BooleanField(db_column='PR_CODA', blank=True, null=True)  # Field name made lowercase.
    base = models.IntegerField(db_column='BASE', blank=True, null=True)  # Field name made lowercase.
    pr_downper = models.BooleanField(db_column='PR_DOWNPER', blank=True, null=True)  # Field name made lowercase.
    pr_antipass = models.BooleanField(db_column='PR_ANTIPASS', blank=True, null=True)  # Field name made lowercase.
    pr_random = models.IntegerField(db_column='PR_RANDOM', blank=True, null=True)  # Field name made lowercase.
    ve_ip = models.CharField(db_column='VE_IP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pr_antipassgen = models.BooleanField(db_column='PR_ANTIPASSGEN', blank=True, null=True)  # Field name made lowercase.
    pr_esclavo = models.CharField(db_column='PR_ESCLAVO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pr_comidadiaria = models.BooleanField(db_column='PR_COMIDADIARIA', blank=True, null=True)  # Field name made lowercase.
    pr_huellasmatcher = models.CharField(db_column='PR_HUELLASMATCHER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pr_restriccion = models.BooleanField(db_column='PR_RESTRICCION', blank=True, null=True)  # Field name made lowercase.
    pr_key_mifare = models.CharField(db_column='PR_KEY_MIFARE', max_length=6)  # Field name made lowercase.
    pr_cantcomida = models.IntegerField(db_column='PR_CANTCOMIDA', blank=True, null=True)  # Field name made lowercase.
    pr_ip_server2 = models.CharField(db_column='PR_IP_SERVER2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pr_ip_server3 = models.CharField(db_column='PR_IP_SERVER3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pr_ip_server4 = models.CharField(db_column='PR_IP_SERVER4', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBLSERVER'


class Tblturno(models.Model):
    tur_id = models.IntegerField(db_column='TUR_ID', primary_key=True)  # Field name made lowercase.
    tur_d = models.CharField(db_column='TUR_D', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tur_f = models.CharField(db_column='TUR_F', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tur_hent = models.DateTimeField(db_column='TUR_HENT', blank=True, null=True)  # Field name made lowercase.
    tur_hing = models.DateTimeField(db_column='TUR_HING', blank=True, null=True)  # Field name made lowercase.
    tur_hsal = models.DateTimeField(db_column='TUR_HSAL', blank=True, null=True)  # Field name made lowercase.
    tur_rn = models.IntegerField(db_column='TUR_RN', blank=True, null=True)  # Field name made lowercase.
    tur_1 = models.IntegerField(db_column='TUR_1', blank=True, null=True)  # Field name made lowercase.
    tur_2 = models.IntegerField(db_column='TUR_2', blank=True, null=True)  # Field name made lowercase.
    tur_3 = models.IntegerField(db_column='TUR_3', blank=True, null=True)  # Field name made lowercase.
    tur_4 = models.IntegerField(db_column='TUR_4', blank=True, null=True)  # Field name made lowercase.
    tur_5 = models.IntegerField(db_column='TUR_5', blank=True, null=True)  # Field name made lowercase.
    tur_6 = models.IntegerField(db_column='TUR_6', blank=True, null=True)  # Field name made lowercase.
    tur_7 = models.IntegerField(db_column='TUR_7', blank=True, null=True)  # Field name made lowercase.
    tur_fer = models.IntegerField(db_column='TUR_FER', blank=True, null=True)  # Field name made lowercase.
    tur_tipo = models.CharField(db_column='TUR_TIPO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBLTURNO'


class TblAdminEmpresa(models.Model):
    id_nomina = models.CharField(db_column='ID_NOMINA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_empe = models.IntegerField(db_column='ID_EMPE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_ADMIN_EMPRESA'


class TblArea(models.Model):
    a_id = models.CharField(db_column='A_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    a_descripcion = models.CharField(db_column='A_DESCRIPCION', max_length=20)  # Field name made lowercase.
    nomina_tipo = models.CharField(max_length=20)
    a_planificado = models.BooleanField(db_column='A_PLANIFICADO', blank=True, null=True)  # Field name made lowercase.
    a_fechai = models.DateTimeField(db_column='A_FECHAI')  # Field name made lowercase.
    a_fechaf = models.DateTimeField(db_column='A_FECHAF')  # Field name made lowercase.
    a_maxcomida = models.IntegerField(db_column='A_MAXCOMIDA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_AREA'
        unique_together = (('a_id', 'a_descripcion', 'nomina_tipo'),)


class TblCafemarca(models.Model):
    c_nomina = models.CharField(db_column='C_NOMINA', primary_key=True, max_length=10)  # Field name made lowercase.
    c_tiempo = models.DateTimeField(db_column='C_TIEMPO')  # Field name made lowercase.
    c_tipouser = models.CharField(db_column='C_TIPOUSER', max_length=20)  # Field name made lowercase.
    c_tipo = models.CharField(db_column='C_TIPO', max_length=20)  # Field name made lowercase.
    c_menu = models.CharField(db_column='C_MENU', max_length=20)  # Field name made lowercase.
    c_num = models.IntegerField(db_column='C_NUM')  # Field name made lowercase.
    c_costo = models.DecimalField(db_column='C_COSTO', max_digits=18, decimal_places=2)  # Field name made lowercase.
    c_total = models.DecimalField(db_column='C_TOTAL', max_digits=18, decimal_places=2)  # Field name made lowercase.
    c_trans = models.IntegerField(db_column='C_TRANS')  # Field name made lowercase.
    c_status = models.CharField(db_column='C_STATUS', max_length=20)  # Field name made lowercase.
    c_ip = models.CharField(db_column='C_IP', max_length=30)  # Field name made lowercase.
    c_area1 = models.CharField(db_column='C_AREA1', max_length=50)  # Field name made lowercase.
    c_cont = models.IntegerField(db_column='C_CONT')  # Field name made lowercase.
    c_planificado = models.BooleanField(db_column='C_PLANIFICADO', blank=True, null=True)  # Field name made lowercase.
    c_ref1 = models.DecimalField(db_column='C_REF1', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    c_ref2 = models.DecimalField(db_column='C_REF2', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    c_totalr1 = models.DecimalField(db_column='C_TOTALR1', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    c_totalr2 = models.DecimalField(db_column='C_TOTALR2', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nomina_ape = models.CharField(db_column='NOMINA_APE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomina_nom = models.CharField(db_column='NOMINA_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c_emp1 = models.CharField(db_column='C_EMP1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_dep1 = models.CharField(db_column='C_DEP1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nomina_cod = models.CharField(db_column='NOMINA_COD', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_CAFEMARCA'
        unique_together = (('c_nomina', 'c_tiempo'),)


class TblCafemarcaex(models.Model):
    c_cont = models.BigAutoField(db_column='C_CONT')  # Field name made lowercase.
    c_nomina = models.CharField(db_column='C_NOMINA', primary_key=True, max_length=10)  # Field name made lowercase.
    c_tiempo = models.DateTimeField(db_column='C_TIEMPO')  # Field name made lowercase.
    c_tipouser = models.CharField(db_column='C_TIPOUSER', max_length=20)  # Field name made lowercase.
    c_tipo = models.CharField(db_column='C_TIPO', max_length=20)  # Field name made lowercase.
    c_menu = models.CharField(db_column='C_MENU', max_length=20)  # Field name made lowercase.
    c_num = models.IntegerField(db_column='C_NUM')  # Field name made lowercase.
    c_costo = models.DecimalField(db_column='C_COSTO', max_digits=18, decimal_places=2)  # Field name made lowercase.
    c_total = models.DecimalField(db_column='C_TOTAL', max_digits=18, decimal_places=2)  # Field name made lowercase.
    c_trans = models.IntegerField(db_column='C_TRANS')  # Field name made lowercase.
    c_status = models.CharField(db_column='C_STATUS', max_length=20)  # Field name made lowercase.
    c_ip = models.CharField(db_column='C_IP', max_length=30)  # Field name made lowercase.
    c_planificado = models.BooleanField(db_column='C_PLANIFICADO', blank=True, null=True)  # Field name made lowercase.
    c_ref1 = models.DecimalField(db_column='C_REF1', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    c_ref2 = models.DecimalField(db_column='C_REF2', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    c_totalr1 = models.DecimalField(db_column='C_TOTALR1', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    c_totalr2 = models.DecimalField(db_column='C_TOTALR2', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nomina_ape = models.CharField(db_column='NOMINA_APE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomina_nom = models.CharField(db_column='NOMINA_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomina_cod = models.CharField(db_column='NOMINA_COD', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_CAFEMARCAEX'
        unique_together = (('c_nomina', 'c_tiempo'),)


class TblConfiguraMail(models.Model):
    m_id = models.CharField(db_column='M_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    m_service = models.BooleanField(db_column='M_SERVICE')  # Field name made lowercase.
    m_smtp_server = models.CharField(db_column='M_SMTP_SERVER', max_length=60, blank=True, null=True)  # Field name made lowercase.
    m_pop_server = models.CharField(db_column='M_POP_SERVER', max_length=60, blank=True, null=True)  # Field name made lowercase.
    m_mail_host = models.CharField(db_column='M_MAIL_HOST', max_length=60, blank=True, null=True)  # Field name made lowercase.
    m_cuenta = models.CharField(db_column='M_Cuenta', max_length=60, blank=True, null=True)  # Field name made lowercase.
    m_autentificacion = models.BooleanField(db_column='M_Autentificacion', blank=True, null=True)  # Field name made lowercase.
    m_user = models.CharField(db_column='M_USER', max_length=60, blank=True, null=True)  # Field name made lowercase.
    m_clave = models.CharField(db_column='M_CLAVE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    m_timeup = models.IntegerField(db_column='M_TIMEUP', blank=True, null=True)  # Field name made lowercase.
    m_fallido = models.IntegerField(db_column='M_Fallido')  # Field name made lowercase.
    m_mail_alterno = models.CharField(db_column='M_Mail_Alterno', max_length=60, blank=True, null=True)  # Field name made lowercase.
    mc_enviar_empleados = models.IntegerField(db_column='MC_ENVIAR_EMPLEADOS')  # Field name made lowercase.
    mc_enviar_jefes = models.IntegerField(db_column='MC_ENVIAR_JEFES')  # Field name made lowercase.
    mc_enviar_cuenta = models.IntegerField(db_column='MC_ENVIAR_CUENTA')  # Field name made lowercase.
    mc_enviar_cuenta_mail = models.CharField(db_column='MC_ENVIAR_CUENTA_MAIL', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_CONFIGURA_MAIL'


class TblCredencial(models.Model):
    atributo = models.CharField(db_column='ATRIBUTO', max_length=50)  # Field name made lowercase.
    x = models.IntegerField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    y = models.IntegerField(db_column='Y', blank=True, null=True)  # Field name made lowercase.
    colorletra = models.IntegerField(db_column='COLORLETRA', blank=True, null=True)  # Field name made lowercase.
    tipoletra = models.CharField(db_column='TIPOLETRA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    visible = models.CharField(db_column='VISIBLE', max_length=1)  # Field name made lowercase.
    n = models.CharField(db_column='N', max_length=1)  # Field name made lowercase.
    k = models.CharField(db_column='K', max_length=1)  # Field name made lowercase.
    s = models.CharField(db_column='S', max_length=1)  # Field name made lowercase.
    empresa = models.CharField(db_column='EMPRESA', max_length=50)  # Field name made lowercase.
    tamano = models.CharField(db_column='TAMANO', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_CREDENCIAL'


class TblEquiposTransf(models.Model):
    equipo = models.CharField(db_column='EQUIPO', primary_key=True, max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_EQUIPOS_TRANSF'


class TblExcep(models.Model):
    ex_nomina = models.CharField(db_column='EX_NOMINA', primary_key=True, max_length=10)  # Field name made lowercase.
    ex_nombre = models.CharField(db_column='EX_NOMBRE', max_length=100)  # Field name made lowercase.
    ex_tipo = models.CharField(db_column='EX_TIPO', max_length=20)  # Field name made lowercase.
    ex_menu = models.CharField(db_column='EX_MENU', max_length=20)  # Field name made lowercase.
    ex_fecha1 = models.DateTimeField(db_column='EX_FECHA1')  # Field name made lowercase.
    ex_fecha2 = models.DateTimeField(db_column='EX_FECHA2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_EXCEP'


class TblGroupPersonal(models.Model):
    gp_id = models.AutoField(db_column='GP_ID')  # Field name made lowercase.
    gp_des = models.CharField(db_column='GP_DES', primary_key=True, max_length=50)  # Field name made lowercase.
    gp_sel = models.DecimalField(db_column='GP_SEL', max_digits=1, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_GROUP_PERSONAL'


class TblGrupoIduser(models.Model):
    id_relacion = models.AutoField(db_column='ID_RELACION')  # Field name made lowercase.
    gp_id = models.DecimalField(db_column='GP_ID', primary_key=True, max_digits=4, decimal_places=0)  # Field name made lowercase.
    nomina_id = models.CharField(db_column='NOMINA_ID', max_length=8)  # Field name made lowercase.
    nomina_ape = models.CharField(db_column='NOMINA_APE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomina_nom = models.CharField(db_column='NOMINA_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id_sel = models.DecimalField(db_column='ID_SEL', max_digits=1, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_GRUPO_IDUSER'
        unique_together = (('gp_id', 'nomina_id'),)


class TblKiosko(models.Model):
    kiosko_id = models.CharField(db_column='KIOSKO_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    kiosko_desc = models.CharField(db_column='KIOSKO_DESC', max_length=50)  # Field name made lowercase.
    kiosko_ip = models.CharField(db_column='KIOSKO_IP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kiosko_dsn = models.CharField(db_column='KIOSKO_DSN', max_length=30)  # Field name made lowercase.
    kiosko_user = models.CharField(db_column='KIOSKO_USER', max_length=30)  # Field name made lowercase.
    kiosko_pass = models.CharField(db_column='KIOSKO_PASS', max_length=30)  # Field name made lowercase.
    kiosko_tipo = models.CharField(db_column='KIOSKO_TIPO', max_length=30)  # Field name made lowercase.
    kiosko_estado = models.CharField(db_column='KIOSKO_ESTADO', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_KIOSKO'


class TblListMail(models.Model):
    mail_id = models.AutoField(db_column='MAIL_ID')  # Field name made lowercase.
    mail_ape_nom = models.CharField(db_column='MAIL_APE_NOM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mail_correo = models.CharField(db_column='MAIL_CORREO', primary_key=True, max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_LIST_MAIL'


class TblMails(models.Model):
    id_msg = models.AutoField(db_column='ID_MSG', primary_key=True)  # Field name made lowercase.
    id_subject = models.CharField(db_column='ID_SUBJECT', max_length=250, blank=True, null=True)  # Field name made lowercase.
    id_desc = models.TextField(db_column='ID_DESC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_status = models.IntegerField(db_column='ID_STATUS')  # Field name made lowercase.
    observacion = models.CharField(db_column='OBSERVACION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fecha_crea = models.DateTimeField(db_column='FECHA_CREA', blank=True, null=True)  # Field name made lowercase.
    fecha_envio = models.DateTimeField(db_column='FECHA_ENVIO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_MAILS'


class TblMenu(models.Model):
    m_tipoc = models.OneToOneField('TblTipocomida', models.DO_NOTHING, db_column='M_TIPOC', primary_key=True)  # Field name made lowercase.
    m_menu = models.CharField(db_column='M_MENU', max_length=20)  # Field name made lowercase.
    m_descrip = models.CharField(db_column='M_DESCRIP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    m_costo = models.FloatField(db_column='M_COSTO', blank=True, null=True)  # Field name made lowercase.
    m_tipo = models.CharField(db_column='M_TIPO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    m_fecha = models.DateTimeField(db_column='M_FECHA', blank=True, null=True)  # Field name made lowercase.
    m_tipob = models.BooleanField(db_column='M_TIPOB', blank=True, null=True)  # Field name made lowercase.
    m_dieta = models.BooleanField(db_column='M_DIETA', blank=True, null=True)  # Field name made lowercase.
    m_ref1 = models.FloatField(db_column='M_REF1', blank=True, null=True)  # Field name made lowercase.
    m_ref2 = models.FloatField(db_column='M_REF2', blank=True, null=True)  # Field name made lowercase.
    m_ticket = models.IntegerField(db_column='M_TICKET', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_MENU'
        unique_together = (('m_tipoc', 'm_menu'),)


class TblMenupersona(models.Model):
    h_nominaid = models.OneToOneField(Nomina, models.DO_NOTHING, db_column='H_NOMINAID', primary_key=True)  # Field name made lowercase.
    h_tipoc = models.ForeignKey(TblMenu, models.DO_NOTHING, db_column='H_TIPOC')  # Field name made lowercase.
    h_menu = models.ForeignKey(TblMenu, models.DO_NOTHING, db_column='H_MENU')  # Field name made lowercase.
    h_fechai = models.DateTimeField(db_column='H_FECHAI', blank=True, null=True)  # Field name made lowercase.
    h_fechaf = models.DateTimeField(db_column='H_FECHAF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_MENUPERSONA'
        unique_together = (('h_nominaid', 'h_tipoc'), ('h_nominaid', 'h_tipoc', 'h_menu'),)


class TblPlanificacion(models.Model):
    pl_fecha = models.DateTimeField(db_column='PL_Fecha')  # Field name made lowercase.
    pl_cantidad = models.IntegerField(db_column='PL_Cantidad')  # Field name made lowercase.
    pl_tipo_comida = models.CharField(db_column='PL_Tipo_Comida', max_length=20)  # Field name made lowercase.
    pl_tipo_menu = models.CharField(db_column='PL_Tipo_Menu', max_length=20)  # Field name made lowercase.
    pl_area = models.CharField(db_column='PL_Area', max_length=10)  # Field name made lowercase.
    pl_observacion = models.CharField(db_column='PL_Observacion', max_length=250, blank=True, null=True)  # Field name made lowercase.
    pl_tipo_planificacion = models.CharField(db_column='PL_TIPO_PLANIFICACION', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_PLANIFICACION'


class TblTipocomida(models.Model):
    tc_tipoc = models.CharField(db_column='TC_TIPOC', primary_key=True, max_length=20)  # Field name made lowercase.
    tc_horai = models.DateTimeField(db_column='TC_HORAI')  # Field name made lowercase.
    tc_horaf = models.DateTimeField(db_column='TC_HORAF')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_TIPOCOMIDA'


class TblWeb(models.Model):
    w_id = models.DecimalField(db_column='W_ID', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    w_source = models.DecimalField(db_column='W_SOURCE', max_digits=10, decimal_places=0)  # Field name made lowercase.
    w_des = models.CharField(db_column='W_DES', max_length=50)  # Field name made lowercase.
    w_url = models.CharField(db_column='W_URL', max_length=60)  # Field name made lowercase.
    w_state = models.BooleanField(db_column='W_STATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_WEB'


class TblZonaequipo(models.Model):
    area_zm_id = models.AutoField(db_column='AREA_ZM_ID')  # Field name made lowercase.
    zm_id = models.DecimalField(db_column='ZM_ID', primary_key=True, max_digits=4, decimal_places=0)  # Field name made lowercase.
    prt_cod = models.CharField(db_column='PRT_COD', max_length=4)  # Field name made lowercase.
    pri_des = models.CharField(db_column='PRI_DES', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prt_sel = models.DecimalField(db_column='PRT_SEL', max_digits=1, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_ZonaEquipo'
        unique_together = (('zm_id', 'prt_cod'),)


class Temp(models.Model):
    tmp_cod = models.CharField(db_column='TMP_COD', max_length=50)  # Field name made lowercase.
    tmp_prueba = models.CharField(db_column='TMP_PRUEBA', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEMP'


class TipoPermiso(models.Model):
    tipo_id = models.CharField(db_column='TIPO_ID', primary_key=True, max_length=5)  # Field name made lowercase.
    tipo_nom = models.CharField(db_column='TIPO_NOM', max_length=35)  # Field name made lowercase.
    tipo_cod_n = models.IntegerField(db_column='TIPO_COD_N', blank=True, null=True)  # Field name made lowercase.
    tipo_cod_a = models.IntegerField(db_column='TIPO_COD_A', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_PERMISO'
        unique_together = (('tipo_id', 'tipo_nom'),)


class Titulo(models.Model):
    tit_linea1 = models.CharField(db_column='TIT_LINEA1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tit_linea2 = models.CharField(db_column='TIT_LINEA2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tit_linea3 = models.CharField(db_column='TIT_LINEA3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tit_logo1 = models.BinaryField(db_column='TIT_LOGO1', blank=True, null=True)  # Field name made lowercase.
    tit_logo2 = models.BinaryField(db_column='TIT_LOGO2', blank=True, null=True)  # Field name made lowercase.
    tit_ruta = models.CharField(db_column='TIT_RUTA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tit_ucod = models.CharField(db_column='TIT_UCOD', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TITULO'


class TmpJefes(models.Model):
    nomina_cod = models.CharField(db_column='NOMINA_COD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nomina_jef = models.CharField(db_column='NOMINA_JEF', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMP_JEFES'


class TmpLista(models.Model):
    tmp_id = models.CharField(db_column='TMP_ID', primary_key=True, max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMP_LISTA'


class TAfiBiometric(models.Model):
    no_persona = models.CharField(db_column='NO_PERSONA', primary_key=True, max_length=25)  # Field name made lowercase.
    bio_persona = models.CharField(db_column='BIO_PERSONA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bio_estado = models.BooleanField(db_column='BIO_ESTADO', blank=True, null=True)  # Field name made lowercase.
    bio_finger1 = models.BinaryField(db_column='BIO_Finger1', blank=True, null=True)  # Field name made lowercase.
    bio_finger1i = models.BinaryField(db_column='BIO_Finger1I', blank=True, null=True)  # Field name made lowercase.
    bio_finger2 = models.BinaryField(db_column='BIO_Finger2', blank=True, null=True)  # Field name made lowercase.
    bio_finger2i = models.BinaryField(db_column='BIO_Finger2I', blank=True, null=True)  # Field name made lowercase.
    bio_finger3 = models.BinaryField(db_column='BIO_Finger3', blank=True, null=True)  # Field name made lowercase.
    bio_finger3i = models.BinaryField(db_column='BIO_Finger3I', blank=True, null=True)  # Field name made lowercase.
    bio_finger4 = models.BinaryField(db_column='BIO_Finger4', blank=True, null=True)  # Field name made lowercase.
    bio_finger4i = models.BinaryField(db_column='BIO_Finger4I', blank=True, null=True)  # Field name made lowercase.
    bio_finger5 = models.BinaryField(db_column='BIO_Finger5', blank=True, null=True)  # Field name made lowercase.
    bio_finger5i = models.BinaryField(db_column='BIO_Finger5I', blank=True, null=True)  # Field name made lowercase.
    bio_finger6 = models.BinaryField(db_column='BIO_Finger6', blank=True, null=True)  # Field name made lowercase.
    bio_finger6i = models.BinaryField(db_column='BIO_Finger6I', blank=True, null=True)  # Field name made lowercase.
    bio_finger7 = models.BinaryField(db_column='BIO_Finger7', blank=True, null=True)  # Field name made lowercase.
    bio_finger7i = models.BinaryField(db_column='BIO_Finger7I', blank=True, null=True)  # Field name made lowercase.
    bio_finger8 = models.BinaryField(db_column='BIO_Finger8', blank=True, null=True)  # Field name made lowercase.
    bio_finger8i = models.BinaryField(db_column='BIO_Finger8I', blank=True, null=True)  # Field name made lowercase.
    bio_finger9 = models.BinaryField(db_column='BIO_Finger9', blank=True, null=True)  # Field name made lowercase.
    bio_finger9i = models.BinaryField(db_column='BIO_Finger9I', blank=True, null=True)  # Field name made lowercase.
    bio_finger10 = models.BinaryField(db_column='BIO_Finger10', blank=True, null=True)  # Field name made lowercase.
    bio_finger10i = models.BinaryField(db_column='BIO_Finger10I', blank=True, null=True)  # Field name made lowercase.
    bio_smart = models.SmallIntegerField(db_column='BIO_Smart', blank=True, null=True)  # Field name made lowercase.
    bio_foto = models.BinaryField(db_column='BIO_FOTO', blank=True, null=True)  # Field name made lowercase.
    bio_fingerwsq1 = models.BinaryField(db_column='BIO_FINGERWSQ1', blank=True, null=True)  # Field name made lowercase.
    bio_fingerwsq2 = models.BinaryField(db_column='BIO_FINGERWSQ2', blank=True, null=True)  # Field name made lowercase.
    bio_fingerwsq3 = models.BinaryField(db_column='BIO_FINGERWSQ3', blank=True, null=True)  # Field name made lowercase.
    bio_fingerwsq4 = models.BinaryField(db_column='BIO_FINGERWSQ4', blank=True, null=True)  # Field name made lowercase.
    bio_fingerwsq5 = models.BinaryField(db_column='BIO_FINGERWSQ5', blank=True, null=True)  # Field name made lowercase.
    bio_fingerwsq6 = models.BinaryField(db_column='BIO_FINGERWSQ6', blank=True, null=True)  # Field name made lowercase.
    bio_fingerwsq7 = models.BinaryField(db_column='BIO_FINGERWSQ7', blank=True, null=True)  # Field name made lowercase.
    bio_fingerwsq8 = models.BinaryField(db_column='BIO_FINGERWSQ8', blank=True, null=True)  # Field name made lowercase.
    bio_fingerwsq9 = models.BinaryField(db_column='BIO_FINGERWSQ9', blank=True, null=True)  # Field name made lowercase.
    bio_fingerwsq10 = models.BinaryField(db_column='BIO_FINGERWSQ10', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_AFI_BIOMETRIC'


class TBioframeFace(models.Model):
    face_id = models.CharField(db_column='FACE_ID', max_length=25)  # Field name made lowercase.
    face_name = models.CharField(db_column='FACE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    face_foto = models.BinaryField(db_column='FACE_FOTO', blank=True, null=True)  # Field name made lowercase.
    face_min = models.BinaryField(db_column='FACE_MIN', blank=True, null=True)  # Field name made lowercase.
    face_fcrea = models.DateTimeField(db_column='FACE_FCREA', blank=True, null=True)  # Field name made lowercase.
    face_ucrea = models.CharField(db_column='FACE_UCREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    face_smc = models.CharField(db_column='FACE_SMC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    face_flag1 = models.CharField(db_column='FACE_FLAG1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    face_flag2 = models.CharField(db_column='FACE_FLAG2', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_BIOFRAME_FACE'


class VePuerta(models.Model):
    prt_cod = models.CharField(db_column='PRT_COD', max_length=4)  # Field name made lowercase.
    pri_des = models.CharField(db_column='PRI_DES', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pri_loc = models.CharField(db_column='PRI_LOC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pri_p = models.IntegerField(db_column='PRI_P', blank=True, null=True)  # Field name made lowercase.
    pri_area = models.DecimalField(db_column='PRI_AREA', max_digits=10, decimal_places=0)  # Field name made lowercase.
    pri_area1 = models.CharField(db_column='PRI_AREA1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pri_ip = models.CharField(db_column='PRI_IP', max_length=16, blank=True, null=True)  # Field name made lowercase.
    pri_fec = models.DateTimeField(db_column='PRI_FEC', blank=True, null=True)  # Field name made lowercase.
    pri_sta = models.CharField(db_column='PRI_STA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pri_st = models.CharField(db_column='PRI_ST', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pri_pto = models.CharField(db_column='PRI_PTO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    pri_tipo = models.CharField(db_column='PRI_TIPO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pri_virdi = models.CharField(db_column='PRI_VIRDI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pri_ti = models.CharField(db_column='PRI_TI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pri_te = models.CharField(db_column='PRI_TE', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VE_PUERTA'


class Dtproperties(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=255, blank=True, null=True)
    uvalue = models.CharField(max_length=255, blank=True, null=True)
    lvalue = models.BinaryField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'
        unique_together = (('id', 'property'),)


class TblZonamarcaje(models.Model):
    zm_id = models.AutoField(db_column='ZM_ID')  # Field name made lowercase.
    zm_des = models.CharField(db_column='ZM_DES', primary_key=True, max_length=50)  # Field name made lowercase.
    zm_sel = models.DecimalField(db_column='ZM_SEL', max_digits=1, decimal_places=0)  # Field name made lowercase.
    zm_empe = models.IntegerField(db_column='ZM_EMPE', blank=True, null=True)  # Field name made lowercase.
    zm_empe_nom = models.CharField(db_column='ZM_EMPE_NOM', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ZonaMarcaje'
