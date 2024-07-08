import os
from pathlib import Path

from dotenv import load_dotenv


def load_env_variables(env_file):
    if os.path.exists(env_file):
        load_dotenv(env_file, override=True)
    else:
        raise FileNotFoundError(f"{env_file} does not exist.")


# 读取环境变量
if os.getenv("APP_ENV") == "production":
    env_path = "/app/.env.production"
    print(f"开始加载环境变量：APP_ENV={os.getenv('APP_ENV')}, PATH={env_path}")
    load_env_variables(env_path)

if os.getenv("APP_ENV") == "development" or not os.getenv("APP_ENV"):
    env_path = Path(os.getcwd()).joinpath(".env.dev")
    print(f"开始加载环境变量：APP_ENV={os.getenv('APP_ENV')}, PATH={env_path}")
    load_env_variables(env_path)

if os.getenv("APP_ENV") == "test":
    env_path = Path(os.getcwd()).joinpath(".env.test")
    print(f"开始加载环境变量：APP_ENV={os.getenv('APP_ENV')}, PATH={env_path}")
    load_env_variables(env_path)

print(f"[main] 环境变量加载完成: environ_items={os.environ.items()}")