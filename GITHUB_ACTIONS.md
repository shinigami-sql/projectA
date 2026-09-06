# daily_data_generator.yml

This workflow runs `data_generator.py` on a daily schedule to populate the `plots` table in Supabase with random plot session data, supporting future data models and reporting.

## Schedule
Runs daily at 6:40PM EST (11:40PM UTC). Can also be triggered manually from the Actions tab.

## What it does
1. Spins up a fresh Ubuntu virtual machine on GitHub's servers
2. Checks out the repo code
3. Installs Python 3.10
4. Installs dependencies from requirements.txt
5. Injects DATABASE_URL secret and runs data_generator.py
6. Inserts 250 random plot entries into the Supabase plots table

## Required secrets
DATABASE_URL: Supabase connection string, stored in GitHub repository secrets

## Manual trigger
Go to Actions tab -> Daily Data Generator -> Run workflow
