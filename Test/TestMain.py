import unittest
from App.main import calculate_trolleys_required_from_yaml


class TestCalculateTrolleysRequired(unittest.TestCase):
    def test_valid_cargo(self):
        cargo_yaml_file = '../valid_cargo.yaml'
        trolley_count = calculate_trolleys_required_from_yaml(cargo_yaml_file)
        self.assertEqual(trolley_count, 1)

    def test_zero_weight(self):
        cargo_yaml_file = '../zero_weight.yaml'
        trolley_count = calculate_trolleys_required_from_yaml(cargo_yaml_file)
        self.assertEqual(trolley_count, 0)

    def test_excessive_volume(self):
        cargo_yaml_file = '../excessive_volume.yaml'
        trolley_count = calculate_trolleys_required_from_yaml(cargo_yaml_file)
        self.assertEqual(trolley_count, 1)

    def test_excessive_weight(self):
        cargo_yaml_file = '../excessive_weight.yaml'
        trolley_count = calculate_trolleys_required_from_yaml(cargo_yaml_file)
        self.assertEqual(trolley_count, 2)

if __name__ == '__main__':
    unittest.main()
