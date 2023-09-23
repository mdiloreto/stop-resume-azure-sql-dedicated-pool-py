# Azure SQL Dedicated Pools Automation

This repository contains scripts to pause and resume Azure SQL Dedicated Pools. These scripts are intended to help automate the management of your SQL Pools by leveraging the Azure Management Client.

## Prerequisites

- **Python Version:** 3.6 or higher
- An active Azure subscription
- Permissions to manage Azure SQL Dedicated Pools

## Dependencies

To run the provided scripts, you need to install the following Python packages:

\```bash
azure-identity
azure-mgmt-sql
azure-core
\```

You can install these using pip:

\```bash
pip install azure-identity azure-mgmt-sql azure-core
\```

## Setup

Before executing the scripts:

1. Ensure you have set up Managed Identity on your Azure service where this script will run.
2. Update the following variables in the script to match your setup:
   - `resource_group_name`
   - `server_name`
   - `database_name`
   - `subscription_id`

## Usage

### To pause the SQL Pool:

Run the script `pause_sql_pool.py`:

\```bash
python pause_sql_pool.py
\```

### To resume the SQL Pool:

Run the script `resume_sql_pool.py` (assuming you have a similar script for resuming):

\```bash
python resume_sql_pool.py
\```

## Troubleshooting

If you encounter any issues, verify that:

- Your Managed Identity has the right permissions in Azure.
- You have correctly set up all the required variables in the script.
- Your Python environment has all the necessary packages installed.

## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## License

[MIT License](LICENSE)
