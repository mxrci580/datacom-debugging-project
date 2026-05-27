
import unittest
from process_data import DataProcessor


class TestDataProcessor(unittest.TestCase):

    def test_export_customer_data_with_invalid_structure(self):

        processor = DataProcessor("customers.csv")

        processor.customers = {
            "C001": "INVALID_DATA"
        }

        result = processor.export_customer_data("test.csv", "csv")

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
