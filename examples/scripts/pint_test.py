from pint import UnitRegistry

ureg = UnitRegistry()

# List of common Pint code variations for Wh/L
unit_strings = [
    "Wh / L",
    "Wh / liter",
    "W * h / L",
    "watt * hour / liter",
    "watt hour / liter",
    "watt_hour / liter",   # less common, sometimes used in code
    "watt * hour * liter ** -1",
    "Wh * L ** -1",
    "W*h/L",
    "Wh·L⁻¹",
    "W.h/L",
    "W m⁻²",
    "mA·h·g⁻¹"
]

print("Testing Pint compatibility for Wh/L unit strings:\n")

for unit_str in unit_strings:
    try:
        unit = ureg(unit_str)
        print(f"✅ Accepted: '{unit_str}'  -->  {unit:~P}")
    except Exception as e:
        print(f"❌ Rejected: '{unit_str}'  -->  {e}")
