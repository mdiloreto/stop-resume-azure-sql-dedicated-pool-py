from azure.identity import ManagedIdentityCredential
from azure.mgmt.sql import SqlManagementClient
from azure.core.polling import LROPoller

resource_group_name = ''
server_name = ''
database_name = ''
subscription_id = ''

credentials = ManagedIdentityCredential()
sql_client = SqlManagementClient(credentials, subscription_id)

def resume_sql_pool(resource_group_name, server_name, database_name):
    poller = sql_client.databases.begin_resume(resource_group_name, server_name, database_name)
    # Wait for the operation to complete
    poller.result()

try:
    database = sql_client.databases.get(resource_group_name, server_name, database_name)
    if database.status == 'Paused':
        resume_sql_pool(resource_group_name, server_name, database_name)
    else:
        print(f"Database status: {database.status}")

except Exception as e:
    print(f"An error occurred: {e}")