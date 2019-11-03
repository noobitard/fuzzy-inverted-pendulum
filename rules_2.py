
angle_rules = dict()
angle_rules[('NL', 'N')] = 'NL'
angle_rules[('NL', 'ZE')] = 'NM'
angle_rules[('NL', 'P')] = 'NS'

angle_rules[('NM', 'N')] = 'NM'
angle_rules[('NM', 'ZE')] = 'NS'
angle_rules[('NM', 'P')] = 'ZE'

angle_rules[('NS', 'N')] = 'NM'
angle_rules[('NS', 'ZE')] = 'NS'
angle_rules[('NS', 'P')] = 'ZE'

angle_rules[('ZE', 'N')] = 'NS'
angle_rules[('ZE', 'ZE')] = 'ZE'
angle_rules[('ZE', 'P')] = 'PS'

angle_rules[('PS', 'N')] = 'ZE'
angle_rules[('PS', 'ZE')] = 'PS'
angle_rules[('PS', 'P')] = 'PM'

angle_rules[('PM', 'N')] = 'ZE'
angle_rules[('PM', 'ZE')] = 'PM'
angle_rules[('PM', 'P')] = 'PM'

angle_rules[('PL', 'N')] = 'PS'
angle_rules[('PL', 'ZE')] = 'PM'
angle_rules[('PL', 'P')] = 'PL'



position_rules = dict()
position_rules[('NL', 'NL')] = 'PL'
position_rules[('NL', 'NM')] = 'PL'
position_rules[('NL', 'NS')] = 'PL'
position_rules[('NL', 'ZE')] = 'PM'
position_rules[('NL', 'PS')] = 'PS'
position_rules[('NL', 'PM')] = 'PS'
position_rules[('NL', 'PL')] = 'ZE'

position_rules[('NM', 'NL')] = 'PL'
position_rules[('NM', 'NM')] = 'PM'
position_rules[('NM', 'NS')] = 'PM'
position_rules[('NM', 'ZE')] = 'PM'
position_rules[('NM', 'PS')] = 'PS'
position_rules[('NM', 'PM')] = 'ZE'
position_rules[('NM', 'PL')] = 'ZE'

position_rules[('NS', 'NL')] = 'PM'
position_rules[('NS', 'NM')] = 'PM'
position_rules[('NS', 'NS')] = 'PS'
position_rules[('NS', 'ZE')] = 'PS'
position_rules[('NS', 'PS')] = 'ZE'
position_rules[('NS', 'PM')] = 'ZE'
position_rules[('NS', 'PL')] = 'NS'

position_rules[('ZE', 'NL')] = 'PS'
position_rules[('ZE', 'NM')] = 'PS'
position_rules[('ZE', 'NS')] = 'ZE'
position_rules[('ZE', 'ZE')] = 'ZE'
position_rules[('ZE', 'PS')] = 'ZE'
position_rules[('ZE', 'PM')] = 'NS'
position_rules[('ZE', 'PL')] = 'NS'

position_rules[('PS', 'NL')] = 'PS'
position_rules[('PS', 'NM')] = 'ZE'
position_rules[('PS', 'NS')] = 'ZE'
position_rules[('PS', 'ZE')] = 'NS'
position_rules[('PS', 'PS')] = 'NS'
position_rules[('PS', 'PM')] = 'NM'
position_rules[('PS', 'PL')] = 'NM'

position_rules[('PM', 'NL')] = 'ZE'
position_rules[('PM', 'NM')] = 'ZE'
position_rules[('PM', 'NS')] = 'NS'
position_rules[('PM', 'ZE')] = 'NM'
position_rules[('PM', 'PS')] = 'NM'
position_rules[('PM', 'PM')] = 'NM'
position_rules[('PM', 'PL')] = 'NL'

position_rules[('PL', 'NL')] = 'ZE'
position_rules[('PL', 'NM')] = 'NS'
position_rules[('PL', 'NS')] = 'NM'
position_rules[('PL', 'ZE')] = 'NM'
position_rules[('PL', 'PS')] = 'NL'
position_rules[('PL', 'PM')] = 'NL'
position_rules[('PL', 'PL')] = 'NL'