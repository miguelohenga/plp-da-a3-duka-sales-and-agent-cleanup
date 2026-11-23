import pandas as pd
import numpy as np

def clean_agent_data(txns, agents):
    """
    Cleans the agent transaction data and merges it with the agent registry.
    Returns a tuple: (clean_dataframe, cleaning_log_dataframe)
    """
    log = []
    df = txns.copy()

    # 1. Uniqueness (Duplicates)
    initial_rows = len(df)
    df = df.drop_duplicates(subset=['txn_id'], keep='first')
    duplicates_removed = initial_rows - len(df)
    log.append({'issue': 'Duplicates', 'dimension': 'Uniqueness', 'column': 'txn_id', 'rows_affected': duplicates_removed})

    # 2. Consistency (txn_type)
    df['txn_type'] = df['txn_type'].str.strip().str.capitalize()
    
    # 3. Validity & Completeness (Amount)
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    df['amount_imputed'] = df['amount'].isna()
    imputed_count = df['amount_imputed'].sum()
    median_amount = df['amount'].median()
    df['amount'] = df['amount'].fillna(median_amount)
    log.append({'issue': 'Missing amounts', 'dimension': 'Completeness', 'column': 'amount', 'rows_affected': int(imputed_count)})

    # 4. Validity (Dates)
    df['txn_date'] = df['txn_date'].str.replace('/', '-')
    df['txn_date'] = pd.to_datetime(df['txn_date'])

    # 5. Outliers (IQR)
    Q1 = df['amount'].quantile(0.25)
    Q3 = df['amount'].quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + (1.5 * IQR)
    df['is_outlier'] = df['amount'] > upper_bound
    log.append({'issue': 'Outliers', 'dimension': 'Accuracy', 'column': 'amount', 'rows_affected': int(df['is_outlier'].sum())})

    # 6. Merge & Unknown Agents
    merged_df = pd.merge(df, agents, on='agent_id', how='left')
    unknown_count = merged_df['county'].isna().sum()
    merged_df['county'] = merged_df['county'].fillna('Unknown')
    log.append({'issue': 'Unknown agents', 'dimension': 'Integrity', 'column': 'agent_id', 'rows_affected': int(unknown_count)})

    log_df = pd.DataFrame(log)
    return merged_df, log_df
