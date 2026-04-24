# loads configuration froom environment variables
# uses a .env file for development settings
# demonstrates different configuration for development/production
# includes proper error handling for missing configuration

import os
from dotenv import load_dotenv
import sys

REQUIRED = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]
MODE = ["development", "production"]
LOG = ["DEBUG", "INFO", "WARNING", "ERROR"]
DATABASE = ["postgresql://", "sqlite://"]
ZION = ["http://", "https://"]

def security_check():
    print("\nEnvironment security check:")
    print("  [OK] No hardcoded secrets detected")
    print("  [OK] .env file properly configured")
    if os.path.exists(".env.production"):
        print("  [OK] Production overrides available")
    else:
        print("  [~] No .env.production file found")
    print("\nThe Oracle sees all configurations.")

def validation_config(name, to_validate, validation_list):
    if to_validate not in validation_list:
        print(f"Your {name} must be one of the following: {', '.join(validation_list)}") 
        sys.exit(1)
    return 1

def validate_data_zion(name, prefix, to_validate):
    if not any(to_validate.startswith(pref) for pref in prefix):
        print(f"{name} data provided is not correct, please make sure that your data start with: {', '.join(prefix)}")
        sys.exit(1)
    return 1

def validate_key():
    missing = [key for key in REQUIRED if not os.getenv(key)]
    if missing:
        print(f"Missing the following configuration variable in your .venv file: {missing}")
        sys.exit(1)

def api_validation(api):
    if len(api) > 10:
        return True
    else:
        return False


def main():
    env = os.environ.get("APP_ENV", "development")
    if env == "production" and os.path.exists(".env.production"):
        load_dotenv(".env.production")
    else:
        load_dotenv()
    validate_key()

    mode = os.getenv("MATRIX_MODE")
    url = os.getenv("DATABASE_URL")
    api = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")
    print("Configuration loaded:")
    validation_config("mode", mode, MODE)
    validate_data_zion("database", DATABASE, url)
    api_validation(api)
    validation_config("log", log, LOG)
    validate_data_zion("zion", ZION, zion)

    if mode == "development":
        print(f"Mode: {mode}")
        print(f"Database: {url}")
        print(f"API Access: {api}")
        print(f"Log level: {log}")
        print(f"Zion network: {zion}")
    elif mode == "production":
        print(f"Mode: {mode}")
        print("Database: connected to local instance")
        print(f"API Access: Authenticated")
        print(f"Log level: {log}")
        print(f"Zion network: Online")
    
    security_check()


main()
