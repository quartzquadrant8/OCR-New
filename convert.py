import requests

# List of packages to update
packages = [
    'aiohappyeyeballs',
    'aiohttp',
    'aiosignal',
    'attrs',
    'Brotli',
    'cachetools',
    'certifi',
    'cffi',
    'charset-normalizer',
    'cryptography',
    'exceptiongroup',
    'frozenlist',
    'google-api-core',
    'google-auth',
    'google-cloud-vision',
    'googleapis-common-protos',
    'googleapis-common-protos',
    'googleapis-common-protos',
    'googleapis-common-protos',
    'h11',
    'h2',
    'hpack',
    'hyperframe',
    'idna',
    'multidict',
    'multidict',
    'multidict',
    'outcome',
    'outcome',
    'outcome',
    'propcache',
    'proto-plus',
    'protobuf',
    'pyasn1',
    'pyasn1_modules',
    'pycparser',
    'pyOpenSSL',
    'pyOpenSSL',
    'PySocks',
    'PySocks',
    'pyu2f',
    'requests',
    'rsa',
    'selenium',
    'selenium',
    'six',
    'sniffio',
    'sortedcontainers',
    'trio',
    'trio-websocket',
    'typing_extensions',
    'urllib3',
    'urllib3',
    'websocket-client',
    'websocket-client',
    'win_inet_pton',
    'wsproto',
    'yarl',
    'yarl',

    # Add more packages as needed
]

# Function to get the latest version of a package from PyPI
def get_latest_version(package_name):
    response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
    if response.status_code == 200:
        data = response.json()
        return data['info']['version']
    return None

# Read the original Requirements.txt file
with open('Requirements.txt', 'r') as file:
    lines = file.readlines()

updated_lines = []

# Process each line and update if necessary
for line in lines:
    for package in packages:
        if line.startswith(package):
            latest_version = get_latest_version(package)
            if latest_version:
                updated_lines.append(f"{package}=={latest_version}\n")
            break
    else:
        updated_lines.append(line)

# Write the updated requirements to a new file
with open('UpdatedRequirements.txt', 'w') as file:
    file.writelines(updated_lines)

# Print the result
for req_str in updated_lines:
    print(req_str)
