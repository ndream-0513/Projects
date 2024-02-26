from django.db import models

class LogApp(models.Model):
    client_mac = models.CharField(max_length=17, blank=True, null=True)
    app_name = models.CharField(max_length=64, blank=True, null=True)
    start_time = models.BigIntegerField(blank=True, null=True)
    end_time = models.BigIntegerField(blank=True, null=True)
    host = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_app'
        verbose_name = '应用日志'
        verbose_name_plural = '应用日志'


class LogDns(models.Model):
    type = models.IntegerField(blank=True, null=True)
    client_mac = models.CharField(max_length=17, blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    rdata = models.CharField(max_length=255, blank=True, null=True)
    time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_dns'
        verbose_name = 'DNS日志'
        verbose_name_plural = 'DNS日志'


class LogNetflow(models.Model):
    client_mac = models.CharField(max_length=17, blank=True, null=True)
    ip_src = models.CharField(max_length=15, blank=True, null=True)
    ip_dst = models.CharField(max_length=15, blank=True, null=True)
    port_src = models.IntegerField(blank=True, null=True)
    port_dst = models.IntegerField(blank=True, null=True)
    time_start = models.BigIntegerField(blank=True, null=True)
    time_end = models.BigIntegerField(blank=True, null=True)
    len = models.IntegerField(blank=True, null=True)
    pkt_list = models.TextField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_netflow'
        verbose_name = 'TCP/UDP日志'
        verbose_name_plural = 'TCP/UDP日志'
