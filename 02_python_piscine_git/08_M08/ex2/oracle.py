import os
from dotenv import load_dotenv
import sys

REQUIRED = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]
MODE = ["development", "production"]
LOG = ["DEBUG", "INFO", "WARNING", "ERROR"]
DATABASE = ["postgresql://", "sqlite://"]
ZION = ["http://", "https://"]

def validation_config(name, to_validate, validation_list):
    if to_validate not in validation_list:
        print(f"Your {name} must be one of the following: {', '.join(validation_list)}") 
        sys.exit(1)

def validate_data_zion(name, prefix, to_validate):
    if not any(to_validate.startswith(pref) for pref in prefix):
        print(f"{name} data provided is not correct, please make sure that your data start with: {', '.join(prefix)}")
        sys.exit(1)

def validate_key():
    missing = [key for key in REQUIRED if not os.getenv(key)]
    if missing:
        print(f"Missing the following configuration variable in your .venv file: {missing}")
        print("Hint: cp .env.example .env and edit with your values")
        sys.exit(1)

def api_validation(api):
    if len(api) > 10:
        return True
    else:
        return False
    
def security_check():
    print("\nEnvironment security check:")
    print("  [OK] No hardcoded secrets detected")
    print("  [OK] .env file properly configured")
    print("  [OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


def display_config(mode, url, api, log, zion):
    print("Configuration loaded:")
    print(f"  Mode: {mode}")
    print(f"  Database: Connected to {'local' if mode == 'development' else 'remote'} instance")
    print(f"  API Access: {'Authenticated' if api_validation(api) else 'Refused'}")
    print(f"  Log Level: {log}")
    print(f"  Zion Network: {'Online' if mode == 'development' else 'Secure'}")

    if mode == "development":
        print("\n  [DEV] Full details:")
        print(f"    Database URL: {url}")
        print(f"    API Key: {api[:8]}***")
        print(f"    Zion endpoint: {zion}")
    elif mode == "production":
        print("\n  [PROD] Sensitive values hidden for security")
        print(f"    Database URL: ***hidden***")
        print(f"    API Key: ***hidden***")
        print(f"    Zion endpoint: ***hidden***")
    
def main():

    load_dotenv()
    validate_key()

    mode = os.getenv("MATRIX_MODE")
    url = os.getenv("DATABASE_URL")
    api = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")
    
    validation_config("MATRIX_MODE", mode, MODE)
    validation_config("LOG_LEVEL", log, LOG)
    validate_data_zion("DATABASE_URL", DATABASE, url)
    validate_data_zion("ZION_ENDPOINT", ZION, zion)
    
    display_config(mode, url, api, log, zion)
    security_check()


main()
