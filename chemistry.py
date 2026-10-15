import re

atomic_masses = {
    "H": 1.008,
    "C": 12.011,
    "Al": 26.982,
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
    if not formula:
        raise ValueError("Chemical formula cannot be empty.")

    tokens = re.findall(r"[A-Z][a-z]?|\d+|[()]", formula)

    if "".join(tokens) != formula:
        raise ValueError("Invalid chemical formula.")

    position = 0

    def parse_group():
        nonlocal position
        total_mass = 0

        while position < len(tokens):
            token = tokens[position]

            if token == ")":
                break

            if token == "(":
                position += 1
                group_mass = parse_group()

                if position >= len(tokens) or tokens[position] != ")":
                    raise ValueError("Unmatched opening parenthesis.")

                position += 1
                multiplier = 1

                if position < len(tokens) and tokens[position].isdigit():
                    multiplier = int(tokens[position])
                    position += 1

                if multiplier < 1:
                    raise ValueError("Multipliers must be positive.")

                total_mass += group_mass * multiplier

            elif token.isdigit():
                raise ValueError("Unexpected number in formula.")

            else:
                element = token
                position += 1

                if element not in atomic_masses:
                    raise ValueError(f"Unknown element: {element}")

                count = 1

                if position < len(tokens) and tokens[position].isdigit():
                    count = int(tokens[position])
                    position += 1

                if count < 1:
                    raise ValueError("Atom counts must be positive.")

                total_mass += atomic_masses[element] * count

        return total_mass

    total_mass = parse_group()

    if position != len(tokens):
        if tokens[position] == ")":
            raise ValueError("Unmatched closing parenthesis.")
        raise ValueError("Invalid chemical formula.")

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
