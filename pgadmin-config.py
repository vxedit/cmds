import os
import sys

# Step 1: Check if in virtual environment and find site-packages path
site_packages_dir = None

# Check sys.path to locate the specific environment’s site-packages directory
for path in sys.path:
    if 'pgadminenv' in path and 'site-packages' in path:
        site_packages_dir = path
        break

if not site_packages_dir:
    print("Couldn't find pgadminenv site-packages directory.")
    exit(1)

# Step 2: Define the path for config_local.py within pgadmin4 directory
pgadmin_config_path = os.path.join(site_packages_dir, 'pgadmin4', 'config_local.py')

# Step 3: Prepare DATA_DIR path and config content
config_content = '''import os
DATA_DIR = os.path.realpath(os.path.expanduser(u'~/.pgadmin/'))
LOG_FILE = os.path.join(DATA_DIR, 'pgadmin4.log')
SQLITE_PATH = os.path.join(DATA_DIR, 'pgadmin4.db')
SESSION_DB_PATH = os.path.join(DATA_DIR, 'sessions')
STORAGE_DIR = os.path.join(DATA_DIR, 'storage')
SERVER_MODE = False
AZURE_CREDENTIAL_CACHE_DIR = os.path.join(DATA_DIR, 'azurecredentialcache')
'''

# Step 5: Write the config file
with open(pgadmin_config_path, 'w') as file:
    file.write(config_content)

print(f"config_local.py has been created at: {pgadmin_config_path}")
