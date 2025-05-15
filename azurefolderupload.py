from azure.storage.filedatalake import DataLakeServiceClient
import os

# Azure credentials
account_name = "mayfairproject"
sas_token = "sv=2024-11-04&ss=bfqt&srt=co&sp=rwdlacupyx&se=2025-05-19T15:21:36Z&st=2025-05-05T07:21:36Z&spr=https&sig=25%2FT3LltnjZF2rDlnec%2FQQUA16Q%2BdqxKHcA7%2F4%2FEiFs%3D"  # Replace with new SAS token
container_name = "customer-reviews"  # Verify container exists!
local_folder = "raw_data"
datalake_folder = "raw/reviews"

# Initialize client
service_client = DataLakeServiceClient(
    account_url=f"https://{account_name}.dfs.core.windows.net",
    credential=sas_token
)
file_system_client = service_client.get_file_system_client(container_name)

# Upload files recursively (no manual directory creation)
for root, _, files in os.walk(local_folder):
    for file in files:
        local_path = os.path.join(root, file)
        relative_path = os.path.relpath(local_path, local_folder)
        datalake_path = f"{datalake_folder}/{relative_path}".replace("\\", "/")

        # Upload file directly (directories auto-created)
        with open(local_path, "rb") as data:
            file_client = file_system_client.get_file_client(datalake_path)
            file_client.upload_data(data, overwrite=True)
            print(f"Uploaded: {datalake_path}")