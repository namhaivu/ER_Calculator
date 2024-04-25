# Calculate damage after considering the target's armor
# the 'damage' param should be a number (int) that is the raw damage
import math


def calc_damage(caster, target, damage):
    output = math.floor(
        (damage * (100 / (100 + (target.defense * (1 - caster.pen_percent)) - caster.armor_penetration)))
        * (1 + target.damage_increase - target.damage_reduction))
    return output
