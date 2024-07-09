from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QSpinBox, QLabel, QVBoxLayout


def addTab3(self):
    self.tab3 = QWidget()
    self.addTab(self.tab3, "Detailed Editor")
    self.tab1.setStyleSheet("""
    """)
    main_layout = QGridLayout()
    layout = QGridLayout()

    section1_label = QLabel("Player Character")
    main_layout.addWidget(section1_label, 0, 0, 1, 1)

    # Health
    health_text = QLabel("Health")
    health_text.setAlignment(Qt.AlignmentFlag.AlignRight)
    layout.addWidget(health_text, 0, 0, 1, 1)
    spin_box_health = QSpinBox()
    spin_box_health.setMinimum(0)
    spin_box_health.setMaximum(9999)
    layout.addWidget(spin_box_health, 0, 1, 1, 1)
    spin_box_health.setStyleSheet("""
    """)

    # Defense
    defense_text = QLabel("Defense")
    defense_text.setAlignment(Qt.AlignmentFlag.AlignRight)
    layout.addWidget(defense_text, 0, 2, 1, 1)
    spin_box_defense = QSpinBox()
    spin_box_defense.setMinimum(0)
    spin_box_defense.setMaximum(999)
    spin_box_defense.setStyleSheet("""
    """)
    layout.addWidget(spin_box_defense, 0, 3, 1, 1)

    # Skill Amp
    skill_amp_text = QLabel("Skill Amp")
    skill_amp_text.setAlignment(Qt.AlignmentFlag.AlignRight)
    layout.addWidget(skill_amp_text, 0, 4, 1, 1)
    spin_box_skill_amp = QSpinBox()
    spin_box_skill_amp.setMinimum(0)
    spin_box_skill_amp.setMaximum(9999)
    spin_box_skill_amp.setStyleSheet("""
        """)
    layout.addWidget(spin_box_skill_amp, 0, 5, 1, 1)

    # Attack Power
    attack_text = QLabel("Attack Power")
    attack_text.setAlignment(Qt.AlignmentFlag.AlignRight)
    layout.addWidget(attack_text, 0, 6, 1, 1)
    spin_box_attack_power = QSpinBox()
    spin_box_attack_power.setMinimum(0)
    spin_box_attack_power.setMaximum(9999)
    spin_box_attack_power.setStyleSheet("""
        """)
    layout.addWidget(spin_box_attack_power, 0, 7, 1, 1)

    # Armor Pen
    armor_pen_text = QLabel("Armor Pen")
    armor_pen_text.setAlignment(Qt.AlignmentFlag.AlignRight)
    layout.addWidget(armor_pen_text, 0, 8, 1, 1)
    spin_box_armor_pen = QSpinBox()
    spin_box_armor_pen.setMinimum(0)
    spin_box_armor_pen.setMaximum(9999)
    spin_box_armor_pen.setStyleSheet("""
        """)
    layout.addWidget(spin_box_armor_pen, 0, 9, 1, 1)

    # Percent Armor Pen
    percent_pen_text = QLabel("Percent Pen")
    percent_pen_text.setAlignment(Qt.AlignmentFlag.AlignRight)
    layout.addWidget(percent_pen_text, 1, 0, 1, 1)
    spin_box_percent_pen = QSpinBox()
    spin_box_percent_pen.setMinimum(0)
    spin_box_percent_pen.setMaximum(9999)
    spin_box_percent_pen.setStyleSheet("""
        """)
    spin_box_percent_pen.setSuffix("%")
    layout.addWidget(spin_box_percent_pen, 1, 1, 1, 1)

    # Crit Chance
    crit_chance_text = QLabel("Crit Chance")
    crit_chance_text.setAlignment(Qt.AlignmentFlag.AlignRight)
    layout.addWidget(crit_chance_text, 1, 2, 1, 1)
    spin_box_crit_chance = QSpinBox()
    spin_box_crit_chance.setMinimum(0)
    spin_box_crit_chance.setMaximum(100)
    spin_box_crit_chance.setStyleSheet("""
        """)
    spin_box_crit_chance.setSuffix("%")
    layout.addWidget(spin_box_crit_chance, 1, 3, 1, 1)

    # Crit Damage
    crit_damage_text = QLabel("Crit Damage")
    crit_damage_text.setAlignment(Qt.AlignmentFlag.AlignRight)
    layout.addWidget(crit_damage_text, 1, 4, 1, 1)
    spin_box_crit_damage = QSpinBox()
    spin_box_crit_damage.setMinimum(175)
    spin_box_crit_damage.setMaximum(9999)
    spin_box_crit_damage.setStyleSheet("""
        """)
    spin_box_crit_damage.setSuffix("%")
    layout.addWidget(spin_box_crit_damage, 1, 5, 1, 1)

    # Percent Amp Percent
    percent_amp_text = QLabel("Amp Percent")
    percent_amp_text.setAlignment(Qt.AlignmentFlag.AlignRight)
    layout.addWidget(percent_amp_text, 1, 6, 1, 1)
    spin_box_percent_amp = QSpinBox()
    spin_box_percent_amp.setMinimum(0)
    spin_box_percent_amp.setMaximum(9999)
    spin_box_percent_amp.setStyleSheet("""
        """)
    spin_box_percent_amp.setSuffix("%")
    layout.addWidget(spin_box_percent_amp, 1, 7, 1, 1)

    # Percent Amp Percent
    basic_attack_amp_text = QLabel("Basic Attack Amp")
    basic_attack_amp_text.setAlignment(Qt.AlignmentFlag.AlignRight)
    layout.addWidget(basic_attack_amp_text, 1, 8, 1, 1)
    spin_box_basic_attack_amp = QSpinBox()
    spin_box_basic_attack_amp.setMinimum(0)
    spin_box_basic_attack_amp.setMaximum(9999)
    spin_box_basic_attack_amp.setStyleSheet("""
        """)
    spin_box_basic_attack_amp.setSuffix("%")
    layout.addWidget(spin_box_basic_attack_amp, 1, 9, 1, 1)

    main_layout.addLayout(layout, 1, 0, 3, 1)

    # Skill Layout
    layout2 = QGridLayout()
    section2_label = QLabel("Player Skill")
    main_layout.addWidget(section2_label, 4, 0, 1, 1)

    # Base Damage
    basic_damage_text = QLabel("Base Damage")
    basic_damage_text.setAlignment(Qt.AlignmentFlag.AlignRight)
    layout2.addWidget(basic_damage_text, 0, 0, 1, 1)
    spin_box_basic_damage = QSpinBox()
    spin_box_basic_damage.setMinimum(1)
    spin_box_basic_damage.setMaximum(9999)
    spin_box_basic_damage.setStyleSheet("""
        """)
    layout2.addWidget(spin_box_basic_damage, 0, 1, 1, 1)

    # Amp Scaling
    amp_scaling_text = QLabel("Amp Scaling")
    amp_scaling_text.setAlignment(Qt.AlignmentFlag.AlignRight)
    layout2.addWidget(amp_scaling_text, 0, 2, 1, 1)
    spin_box_amp_scaling = QSpinBox()
    spin_box_amp_scaling.setMinimum(0)
    spin_box_amp_scaling.setMaximum(9999)
    spin_box_amp_scaling.setStyleSheet("""
        """)
    spin_box_amp_scaling.setSuffix("%")
    layout2.addWidget(spin_box_amp_scaling, 0, 3, 1, 1)

    # Attack Power Scaling
    attack_scaling_text = QLabel("Attack Scaling")
    attack_scaling_text.setAlignment(Qt.AlignmentFlag.AlignRight)
    layout2.addWidget(attack_scaling_text, 0, 4, 1, 1)
    spin_box_attack_scaling = QSpinBox()
    spin_box_attack_scaling.setMinimum(0)
    spin_box_attack_scaling.setMaximum(9999)
    spin_box_attack_scaling.setStyleSheet("""
        """)
    spin_box_attack_scaling.setSuffix("%")
    layout2.addWidget(spin_box_attack_scaling, 0, 5, 1, 1)

    # Extra Attack Scaling
    extra_attack_scaling_text = QLabel("Extra Attack Scaling")
    extra_attack_scaling_text.setAlignment(Qt.AlignmentFlag.AlignRight)
    layout2.addWidget(extra_attack_scaling_text, 0, 6, 1, 1)
    spin_box_extra_attack_scaling = QSpinBox()
    spin_box_extra_attack_scaling.setMinimum(0)
    spin_box_extra_attack_scaling.setMaximum(9999)
    spin_box_extra_attack_scaling.setStyleSheet("""
        """)
    spin_box_extra_attack_scaling.setSuffix("%")
    layout2.addWidget(spin_box_extra_attack_scaling, 0, 7, 1, 1)

    main_layout.addLayout(layout2, 4, 0, 3, 1)

    self.tab3.setLayout(main_layout)
