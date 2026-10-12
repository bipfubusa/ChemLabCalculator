atomic_masses = {
    "H": 1.008,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "Na": 22.990,
    "Cl": 35.45,
    "S": 32.06,
    "Ca": 40.078,
    "Mg": 24.305,
    "K": 39.098,
    "Fe": 55.845
}


def calculate_molar_mass(formula):
    import re

    pattern = r"([A-Z][a-z]?)(\d*)"
    matches = re.findall(pattern, formula)

    if not matches or "".join(
        element + number for element, number in matches
    ) != formula:
        raise ValueError("Invalid chemical formula.")

    total_mass = 0

    for element, number in matches:
        if element not in atomic_masses:
            raise ValueError(f"Unknown element: {element}")

        count = int(number) if number else 1
        total_mass += atomic_masses[element] * count

    return total_mass

print("=" * 35)
print("      CHEMISTRY CALCULATOR")
print("=" * 35)


print("\n1. Calculate molar concentration")
print("2. Calculate dilution")
print("3. Exit")

choice = input("\nChoose an option: ")

if choice == "1":
    try:
        mass = float(input("Enter solute mass (g): "))
        molar_mass = float(input("Enter molar mass (g/mol): "))
        volume = float(input("Enter solution volume (L): "))

        if mass <= 0 or molar_mass <= 0 or volume <= 0:
            print("Error: All values must be positive.")

        else:
            moles = mass / molar_mass
            concentration = moles / volume

            print("\n--- RESULTS ---")
            print(f"Amount of substance: {moles:.4f} mol")
            print(f"Molar concentration: {concentration:.4f} mol/L")

    except ValueError:
        print("Error: Enter valid numbers.")

elif choice == "2":
    try:
        c1 = float(input("Initial concentration (mol/L): "))
        c2 = float(input("Desired concentration (mol/L): "))
        v2 = float(input("Final volume (mL): "))

        if c1 <= 0 or c2 <= 0 or v2 <= 0:
            print("Error: Values must be positive.")

        elif c2 > c1:
            print("Error: Dilution cannot increase concentration.")

        else:
            v1 = (c2 * v2) / c1
            print(f"Stock solution needed: {v1:.2f} mL")
            print(f"Water to add approximately: {v2 - v1:.2f} mL")

    except ValueError:
        print("Error: Enter valid numbers.")

elif choice == "3":
    print("Goodbye!")


else:
    print("Invalid choice.")
