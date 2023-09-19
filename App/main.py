import math
import yaml

def calculate_trolleys_required_from_yaml(file_path):
    # Maximum parameters for cargo items and trolleys
    max_item_weight = 200.0  # Maximum weight of a single cargo item (in kg)
    max_item_volume = 2.0    # Maximum volume of a single cargo item (in m^3)
    max_trolley_weight = 2000.0  # Maximum weight capacity of a cargo trolley (in kg)

    # Load the cargo manifest from the YAML file
    with open(file_path, 'r') as file:
        cargo_manifest = yaml.safe_load(file)

    total_weight = 0.0
    total_volume = 0.0
    trolley_count = 0

    for item_id, item in cargo_manifest.items():
        item_weight = item['mass']
        item_volume = math.prod(item['volume'])  # Calculate the volume as the product of all dimensions

        # Check if the weight of the current item exceeds the trolley weight limit or is greater than 200 kg
        if item_weight > max_trolley_weight or item_weight > max_item_weight:
            print(f"Warning: Cargo {item_id} in {file_path} cannot be loaded due to excessive weight.")
        # Check if the volume of the current item exceeds the maximum volume
        elif item_volume > max_item_volume:
            print(f"Warning: Cargo {item_id} in {file_path} exceeds the maximum volume limit and cannot be loaded.")
        else:
            total_weight += item_weight

        # Check if the total weight exceeds the trolley weight limit
        if total_weight > max_trolley_weight:
            trolley_count += 1
            total_weight = item_weight
            total_volume = item_volume

    # Check if there are remaining items that require an additional trolley
    if total_weight > 0.0 or total_volume > 0.0:
        trolley_count += 1

    return trolley_count
