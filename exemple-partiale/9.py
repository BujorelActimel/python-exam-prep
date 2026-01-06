minutes_BN = 6548354

hours_BN = minutes_BN // 60

# minutes_BN = minutes_BN - hours_BN * 60
minutes_BN = minutes_BN % 60

print(f"{hours_BN*60+minutes_BN} minutes represent {hours_BN} hours and {minutes_BN} minutes")
