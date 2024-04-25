# Calculate raw skill damage
import math


def calc_raw_skill_damage(caster, skill, target):
    damage = skill.base_damage \
             + math.floor(skill.amp_scaling * math.floor(caster.skill_amp * caster.amp_percent)) \
             + math.floor(skill.attack_power_scaling * caster.attack_power) \
             + math.floor(skill.extra_attack_scaling * caster.extra_attack_power) \
             + math.floor(skill.defense_scaling * caster.defense) \
             + math.floor(skill.health_scaling * caster.health) \
             + math.floor(skill.enemy_health_scaling * target.health) \
             + math.floor(skill.current_health_scaling * target.current_health)

    if skill.isCrit:
        damage = math.floor(damage * caster.crit_mult)

    return damage


def calc_spell_dps_raw(caster, spell):
    output = calc_raw_skill_damage(caster, spell) / (spell.base_cooldown * caster.cooldown_reduction + spell.cast_time)
    return output
