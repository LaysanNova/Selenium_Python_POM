from dotenv import load_dotenv
import os


def load_env(env_name):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    env_path = os.path.join(root_dir, 'config', f'.env.{env_name}')

    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path)
    else:
        print(f"No .env file found for {env_name}. Using environment variables.")