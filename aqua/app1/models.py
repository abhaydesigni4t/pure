from django.db import models

class Model1(models.Model):
    device_id = models.CharField(max_length=100,unique=True)
    feed_low_level_switch = models.BooleanField(default=False) # feed_tank_low_level_switch
    product_high_high_level_switch = models.BooleanField(default=False) # product_tank_high_high_level_switch
    product_high_level_switch = models.BooleanField(default=False) # product_tank_high_level_switch
    feed_low_pressure_switch = models.BooleanField(default=False) 
    system_high_pressure_switch = models.BooleanField(default=False) 
    pre_treatment_interlock = models.BooleanField(default=False)
    remote_run = models.BooleanField(default=False)
    chemical_switch1 = models.BooleanField(default=False) # chemical_low_level_switch_1
    chemical_switch2 = models.BooleanField(default=False) # chemical_low_level_switch_2
    chemical_switch3 = models.BooleanField(default=False) # chemical_low_level_switch_3
    chemical_switch4 = models.BooleanField(default=False) # chemical_low_level_switch_4
    chemical_switch5 = models.BooleanField(default=False) # chemical_low_level_switch_5

    permeate_flow = models.FloatField(null=True, blank=True)
    reject_flow = models.FloatField(null=True, blank=True)
    recirculation_flow = models.FloatField(null=True, blank=True)
    feed_flow = models.FloatField(null=True, blank=True)
    permeate_conductivity = models.FloatField(null=True, blank=True)
    feed_conductivity = models.FloatField(null=True, blank=True)
    pre_filter_pressure = models.FloatField(null=True, blank=True)  
    post_filter_pressure = models.FloatField(null=True, blank=True) 
    system_pressure = models.FloatField(null=True, blank=True)
    interstage_pressure = models.FloatField(null=True, blank=True)
    reject_pressure = models.FloatField(null=True, blank=True)
    feed_orp = models.FloatField(null=True, blank=True)
    feed_ph = models.FloatField(null=True, blank=True)
    product_ph = models.FloatField(null=True, blank=True)

    feed_inlet_valve = models.BooleanField(default=False)
    flush_valve = models.BooleanField(default=False)
    bypass_valve = models.BooleanField(default=False)
    divert_valve = models.BooleanField(default=False)
    feed_pump = models.BooleanField(default=False)
    high_pressure_pump = models.BooleanField(default=False)
    chemical_tank1 = models.BooleanField(default=False) # chemical_tank_1
    chemical_tank2 = models.BooleanField(default=False) # chemical_tank_2
    chemical_tank3 = models.BooleanField(default=False) # chemical_tank_3
    chemical_tank4 = models.BooleanField(default=False) # chemical_tank_4
    chemical_tank5 = models.BooleanField(default=False) # chemical_tank_5
    system_running = models.BooleanField(default=False)
    fault_active = models.BooleanField(default=False)

    def __str__(self):
        return self.device_id