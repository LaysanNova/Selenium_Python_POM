from dotenv import load_dotenv
import os

def load_env(env_name):
    env_path = f'config/.env.{env_name}'
    if not os.path.exists(env_path):
        raise FileNotFoundError(f"{env_path} not found")
    load_dotenv(dotenv_path=env_path)