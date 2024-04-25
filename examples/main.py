"""
Eternal Return Damage Calculator
Main Example File

Program that attempts to simulate player skill/basic attack damage
"""
from classes.character import Character
from classes.skill import Skill
from formulas.armor import calc_damage
from formulas.auto_attacks import calc_auto_attack_dps, calc_raw_auto_attack_average
from formulas.spells import calc_raw_skill_damage

# Example use case for testing
c1 = Character()
c1.health = 3155
c1.current_health = 3155
c1.defense = 71
c1.skill_amp = 25
c1.attack_power = 346
c1.amp_percent = 1
c1.basic_attack_amp = 1.34
c1.armor_penetration = 0
c1.pen_percent = 0
c1.damage_reduction = 0
c1.extra_attack_power = 0
c1.crit_mult = 1.75
c1.crit_chance = 1
c1.attack_speed = .5

c2 = Character()
c2.health = 1000
c2.current_health = 448
c2.defense = 50
c2.skill_amp = 0
c2.attack_power = 0
c2.amp_percent = 0
c2.basic_attack_amp = 1
c2.armor_penetration = 0
c2.pen_percent = 0
c2.damage_reduction = 0
c2.crit_mult = 1.75

s1 = Skill()
s1.base_damage = 0
s1.amp_scaling = 0
s1.attack_power_scaling = 1
s1.extra_attack_scaling = 0
s1.defense_scaling = 0
s1.health_scaling = 0
s1.enemy_health_scaling = 0
s1.current_health_scaling = 0
s1.isCrit = True

raw = calc_raw_skill_damage(c1, s1, c2)
raw1 = calc_auto_attack_dps(c1)
raw2 = calc_raw_auto_attack_average(c1)
print(raw)
print(calc_damage(c1, c2, raw))
