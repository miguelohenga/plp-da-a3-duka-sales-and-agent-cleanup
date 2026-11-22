import numpy as np
import pandas as pd

# --- Duka Electronics Generator ---
# Note: I am assuming the Duka generator looks like this based on standard PLP assignments. 
# If your portal has a specific code block for Duka, replace this section with it.
np.random.seed(2026)
duka_data = pd.DataFrame({
    'order_id': [f"ORD-{i:04d}" for i in range(1, 1001)],
    'date': pd.date_range("2026-01-01", periods=1000, freq="6H").strftime("%Y-%m-%d"),
    'branch': np.random.choice(["Nairobi", "Mombasa", "Kisumu"], 1000),
    'channel': np.random.choice(["Online", "In-Store"], 1000),
    'product': np.random.choice(["Laptop", "Phone", "TV", "Headphones", "Charger"], 1000),
    'units': np.random.randint(1, 5, 1000),
    'price': np.random.randint(500, 30000, 1000)
})
duka_data['revenue'] = duka_data['units'] * duka_data['price']
duka_data.to_csv("duka_sales.csv", index=False)

# --- Agent Network Generator ---
rng = np.random.default_rng(44)
n = 600

agents = pd.DataFrame({
    "agent_id": [f"AG{i:03d}" for i in range(1, 21)],
    "county": rng.choice(["Nairobi", "Kiambu", "Nakuru", "Mombasa", "Kisumu"], 20),
    "onboarded": pd.date_range("2024-01-01", periods=20, freq="MS").strftime("%Y-%m-%d")
})

txns = pd.DataFrame({
    "txn_id": [f"TX{i:05d}" for i in range(1, n + 1)],
    "agent_id": rng.choice(agents["agent_id"], n),
    "txn_type": rng.choice(["Deposit", "withdrawal", "DEPOSIT", "Withdrawal", "deposit"], n),
    "amount": rng.lognormal(7.5, 0.8, n).round(0).astype(str),
    "txn_date": (pd.to_datetime("2026-03-01") + pd.to_timedelta(rng.integers(0, 60, n), unit="D")).strftime("%Y-%m-%d")
})

idx = rng.choice(n, 30, replace=False)
txns.loc[idx[:15], "amount"] = np.nan
txns.loc[idx[15:20], "amount"] = "N/A"
txns.loc[idx[20:25], "amount"] = "250000"
txns.loc[idx[25:], "txn_date"] = txns.loc[idx[25:], "txn_date"].str.replace("-", "/")

txns = pd.concat([txns, txns.sample(12, random_state=1)], ignore_index=True)
txns.loc[rng.choice(len(txns), 8, replace=False), "agent_id"] = "AG099"

agents.to_csv("agents.csv", index=False)
txns.to_csv("agent_transactions.csv", index=False)
