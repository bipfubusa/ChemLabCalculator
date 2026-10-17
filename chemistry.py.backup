import re

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


def calculate_concentration(mass, molar_mass, volume):
    if mass <= 0 or molar_mass <= 0 or volume <= 0:
        raise ValueError("All values must be positive.")

    moles = mass / molar_mass
    concentration = moles / volume

    return moles, concentration


def calculate_dilution(c1, c2, v2):
    if c1 <= 0 or c2 <= 0 or v2 <= 0:
        raise ValueError("All values must be positive.")

    if c2 > c1:
        raise ValueError(
            "The final concentration cannot exceed the initial concentration."
        )

    v1 = (c2 * v2) / c1
    water = v2 - v1

    return v1, water
