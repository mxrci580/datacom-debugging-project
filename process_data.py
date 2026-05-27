
import csv
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataProcessor:

    def __init__(self, input_file):
        self.input_file = input_file
        self.customers = {}
        self.transactions = []
        self.reports = {}

    def load_data(self):
        try:
            with open(self.input_file, 'r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    self.customers[row['customer_id']] = {
                        'name': row['name'],
                        'email': row['email'],
                        'join_date': row['join_date'],
                        'total_spent': 0,
                        'transaction_count': 0
                    }

            logger.info(f"Loaded {len(self.customers)} customers")
            return True

        except Exception as e:
            logger.error(f"Error loading customer data: {e}")
            return False

    def process_transactions(self, transaction_file):
        try:
            with open(transaction_file, 'r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    transaction = {
                        'transaction_id': row['transaction_id'],
                        'customer_id': row['customer_id'],
                        'amount': float(row['amount']),
                        'date': row['date'],
                        'category': row['category']
                    }

                    self.transactions.append(transaction)

                    customer = self.customers.get(row['customer_id'])

                    if customer:
                        customer['total_spent'] += float(row['amount'])
                        customer['transaction_count'] += 1

            logger.info(f"Processed {len(self.transactions)} transactions")
            return True

        except Exception as e:
            logger.error(f"Error processing transactions: {e}")
            return False

    def calculate_customer_metrics(self):

        total_revenue = sum(
            transaction['amount'] for transaction in self.transactions
        )

        metrics = {
            'total_customers': len(self.customers),
            'total_transactions': len(self.transactions),
            'total_revenue': total_revenue,
            'average_transaction_value': (
                total_revenue / len(self.transactions)
                if self.transactions else 0
            ),
            'top_customers': sorted(
                self.customers.items(),
                key=lambda x: x[1]['total_spent'],
                reverse=True
            )[:5]
        }

        return metrics

    def export_customer_data(self, output_file, format='csv'):

        try:

            if not self.customers:
                logger.warning("No customer data available for export")
                return False

            if format == 'csv':

                valid_customers = {}

                for customer_id, data in self.customers.items():

                    if isinstance(data, dict):
                        valid_customers[customer_id] = data
                    else:
                        logger.warning(
                            f"Skipping malformed customer record: {customer_id}"
                        )

                if not valid_customers:
                    logger.error("No valid customer records found")
                    return False

                first_customer = next(iter(valid_customers.values()))

                fieldnames = ['customer_id'] + list(first_customer.keys())

                with open(output_file, 'w', newline='') as file:

                    writer = csv.DictWriter(
                        file,
                        fieldnames=fieldnames
                    )

                    writer.writeheader()

                    rows = [
                        {'customer_id': cid, **data}
                        for cid, data in valid_customers.items()
                    ]

                    writer.writerows(rows)

            elif format == 'json':

                with open(output_file, 'w') as file:
                    json.dump(self.customers, file, indent=2)

            else:
                logger.error(f"Unsupported format: {format}")
                return False

            logger.info(f"Exported customer data to {output_file}")
            return True

        except Exception as e:
            logger.error(f"Error exporting data: {e}")
            return False


if __name__ == "__main__":

    processor = DataProcessor("customers.csv")

    processor.load_data()
    processor.process_transactions("transactions.csv")

    metrics = processor.calculate_customer_metrics()

    print(metrics)

    processor.export_customer_data("customer_export.csv")
