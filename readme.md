# Azure SQL Dedicated Pools Automation

This repository contains scripts to pause and resume Azure SQL Dedicated Pools. These scripts help automate the management of your SQL Pools by leveraging the Azure Management Client.

## Prerequisites

- **Python Version:** 3.8 or higher
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

## Managed Identity in Python

Managed identities provide an identity for applications to use when connecting to resources that support Azure AD authentication. For our script, it is used to authenticate to Azure services without storing credentials in code.

Ensure the following before executing the scripts:

1. Set up Managed Identity on your Azure service where this script will run. You can use either System Assigned or User Assigned Managed Identity.
2. Grant the necessary permissions in the Azure SQL service to the managed identity.

For more details on how to set up and use Managed Identity with Python, refer to [Azure AD's official documentation](https://docs.microsoft.com/azure/active-directory/managed-identities-azure-resources/overview).

## Setup

1. Ensure you have set up Managed Identity on your Azure service where this script will run.
2. Update the following variables in the script to match your setup:
   - `resource_group_name`
   - `server_name`
   - `database_name`
   - `subscription_id`

## Usage

### Configuring a Runbook for Python 3.8 in Automation Account

1. In the Azure portal, navigate to your Automation Account.
2. Under "Process Automation", click on "Runbooks".
3. Click on "+ Add a runbook" and select "Python 3.8" as the type.
4. Name your runbook and provide a description if necessary.
5. Copy and paste the content of the script (either `pause_sql_pool.py` or a resume script if you have one) into the runbook editor.
6. Click on "Test Pane" to test your runbook or "Publish" to save and make it available for scheduling or other triggers.

# Permissions for Managed Identity

The managed identity would typically need the Microsoft.Sql/servers/databases/pause/action and Microsoft.Sql/servers/databases/resume/action permissions in Azure RBAC (Role-Based Access Control). You could assign the following permission (from the most to the least restrictive): 

- `SQL DB Contributor`: This role allows for management of SQL DBs, but not their security-related policies. Given its broad range of permissions, it will include the ability to pause and resume.

- `SQL Server Contributor`: This is a more comprehensive role than the SQL DB Contributor, allowing management of SQL servers and their databases, but not their security-related policies. Again, due to its broad permissions, it would encompass the ability to pause and resume.

- `Contributor`: This is also a very broad role that provides full management rights to the assigned resource except for changing permissions. This would also encompass the ability to pause and resume.

- `Owner`: This is a very broad role that provides full management rights to the assigned resource, which means it can manage everything including pausing and resuming of databases.


## Troubleshooting

If you encounter any issues:

- Ensure your Managed Identity has the right permissions in Azure.
- Check that all required variables in the script have been correctly set.
- Confirm your Python environment has all the necessary packages installed.

## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.
