import math


# Calculate raw auto attack damage
def calc_raw_auto_attack(caster, is_crit=False):
    damage = caster.attack_power
    if is_crit:
        damage = math.floor(damage * caster.crit_mult)
    damage = math.floor(damage * caster.basic_attack_amp)
    return damage


# Calculate the average auto attack damage based on crit change and crit damage
def calc_raw_auto_attack_average(caster):
    damage = math.floor(math.floor(caster.attack_power * (
            caster.crit_mult * caster.crit_chance - caster.crit_chance + 1)) * caster.basic_attack_amp)
    return damage


# Unique formula when using rifles
def calc_raw_auto_attack_rifle(caster, is_crit=False):
    shot1 = math.floor(caster.attack_power * .45)
    shot2 = math.floor(caster.attack_power * .3)

    if is_crit:
        shot1 = math.floor(shot1 * caster.crit_mult)
        shot2 = math.floor(shot2 * caster.crit_mult)

    damage = math.floor(shot1 * caster.basic_attack_amp) \
             + math.floor(shot2 * caster.basic_attack_amp) \
             + math.floor(shot2 * caster.basic_attack_amp)
    return damage


# Calculate auto attack DPS using attack speed
def calc_auto_attack_dps(caster):
    return calc_raw_auto_attack_average(caster) * caster.attack_speed
