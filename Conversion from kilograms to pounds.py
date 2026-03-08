# Conversion factors
KG_TO_POUNDS = 2.2
POUNDS_TO_KG = 0.45

print(f"{'Kilograms':<10} {'Pounds':<10} | {'Pounds':<10} {'Kilograms':<10}")
print("-" * 45)

kg = 1
pounds = 20

while kg <= 199 and pounds <= 515:
    kg_to_pounds = kg * KG_TO_POUNDS
    pounds_to_kg = pounds * POUNDS_TO_KG
    print(f"{kg:<10} {kg_to_pounds:<10.2f} | {pounds:<10} {pounds_to_kg:<10.2f}")
    kg += 2
    pounds += 5
