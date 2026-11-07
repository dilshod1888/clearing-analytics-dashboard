"""Generate synthetic clearing transactions for portfolio use."""
import csv, random
from datetime import datetime, timedelta

SYSTEMS = ["HUMO", "UZCARD", "WAY4"]
CHANNELS = ["POS", "ATM", "EPOS", "TRANSFER"]
TYPES = ["PAYMENT", "CASH_WITHDRAWAL", "P2P", "REFUND"]

def generate(rows=50000, output="data/synthetic_clearing_transactions.csv"):
    start = datetime(2026, 1, 1)
    with open(output, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["transaction_id","transaction_date","payment_system","direction","channel","transaction_type","amount","commission","reconciliation_status"])
        for i in range(1, rows + 1):
            dt = start + timedelta(minutes=random.randint(0, 60*24*300))
            amount = round(random.uniform(10000, 5000000), 2)
            writer.writerow([
                f"CL{i:08d}", dt.strftime("%Y-%m-%d %H:%M:%S"),
                random.choice(SYSTEMS), random.choice(["INCOMING","OUTGOING"]),
                random.choice(CHANNELS), random.choice(TYPES), amount,
                round(amount * random.uniform(0.001, 0.008), 2),
                "MATCHED" if random.random() < 0.985 else "EXCEPTION"
            ])

if __name__ == "__main__":
    generate()
