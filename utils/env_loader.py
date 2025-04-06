from dotenv import load_dotenv
import os


def load_env(env_name):
    env_path = f'config/.env.{env_name}'

    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path)
    else:
        print(f"No .env file found for {env_name}. Using environment variables.")