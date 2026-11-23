# Duka Sales and Agent Network Cleanup

## Project Summary
This repository contains two data analytics engagements for a Nairobi consultancy. 
**Engagement 1 (Duka Electronics):** Explored sales data to prepare for a half-year review, calculating revenue, ranking branches, and building an Excel summary.
**Engagement 2 (Mobile Money Agent Network):** Audited and cleaned unreliable legacy transaction data, resolving issues across six data quality dimensions, and produced summary tables merged with the agent registry.

## How to Run
You can regenerate the raw data by running `generate_data.py`. 
To view the analysis, open the notebooks in Google Colab:
*   [Open Duka Sales Notebook in Colab](https://colab.research.google.com/drive/1vxUw7SMIz8OcqEe7TQtFI7J1m9NwrH31?usp=sharing)
*   [Open Agent Cleanup Notebook in Colab](https://colab.research.google.com/drive/1iwo-mhV7o-5ce3wkRM4xVyzK-GGyrP-7?usp=sharing)

## Duka Executive Summary
*   Duka Electronics generated a total revenue of KES37947789 across 1000 orders.
*   The Mombasa branch was the top performer, generating KES  12990627 in revenue.
*   Tvs were the highest revenue-generating product, bringing in KES 8291880 .
*   Weekend orders have an average revenue of KES 37201.704861 , compared to KES 38249.575843 on weekdays.
*   The best performing month was July with KES 5,002,499 in revenue, which was 319.81% higher than September.

      ## Agent Network Row Count
*   **Before Cleaning:** 612 rows (including duplicates)
*   **After Cleaning:** 600 rows (after dropping 12 duplicates)
