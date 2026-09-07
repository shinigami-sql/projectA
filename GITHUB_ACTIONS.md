# projecta_daily_data_generator.yml

This workflow runs `data_generator.py` on a daily schedule to populate the `plots` table in Supabase with random plot session data, supporting future data models and reporting.

## Schedule
Runs 4 times daily at 6AM, 12PM, 6PM and 11:40PM UTC. Each run generates a random number of entries between 1 and 25 for more realistic data distribution. Can also be triggered manually from the Actions tab.

## What it does
1. Spins up a fresh Ubuntu virtual machine on GitHub's servers
2. Injects DATABASE_URL secret as a job-level environment variable, available before any steps run
3. Checks out the repo code
4. Installs Python 3.10
5. Installs dependencies from requirements.txt
6. Runs data_generator.py, inserts 1 to 25 random plot entries into the Supabase plots table

## Required secrets
DATABASE_URL: Supabase session pooler connection string using IPv4, stored in GitHub repository secrets

## Manual trigger
Go to Actions tab -> ProjectA Daily Data Generator -> Run workflow