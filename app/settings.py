"""
-------------------------------------------------
  Description :
  Author :    @zhuang_wu
  Time : 2024/3/5 17:42
-------------------------------------------------

host=fortress.tech.xiaoe-tools.com
port=33061
user=72f3b606-3d54-47a1-a8c7-c6fde54028ae
password=GFIiuykHpA0Fs4Fy
db=information_schema
charset=utf8
phone=15818362202
"""
import os

# --------------------------- MySQL -------------------------

MYSQL_MAX_SHARED = int(os.getenv('MYSQL_MAX_SHARED', 10))
MYSQL_MAX_CONNECTIONS = int(os.getenv('MYSQL_MAX_CONNECTIONS', 20))
MYSQL_HOST = os.getenv("MYSQL_HOST", "fortress.tech.xiaoe-tools.com")
MYSQL_PORT = os.getenv("MYSQL_PORT", "33061")
MYSQL_USER = os.getenv("MYSQL_USER", "72f3b606-3d54-47a1-a8c7-c6fde54028ae")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "GFIiuykHpA0Fs4Fy")
MYSQL_DB = os.getenv("MYSQL_DB", "information_schema")
MYSQL_CHARSET = os.getenv("MYSQL_CHARSET", "utf8")

XIAOE_TESTING_PLATFORM_MYSQL_HOST = "127.0.0.1"
XIAOE_TESTING_PLATFORM_MYSQL_PORT = "3307"
XIAOE_TESTING_PLATFORM_MYSQL_USER = "root"
XIAOE_TESTING_PLATFORM_MYSQL_PASSWORD = "xiaoe123"
XIAOE_TESTING_PLATFORM_MYSQL_DB = "xiaoe_testing_platform"
# XIAOE_TESTING_PLATFORM_MYSQL_HOST = "sh-cdb-test-platform-rw.xiaoe-conf.com"
# XIAOE_TESTING_PLATFORM_MYSQL_PORT = "3306"
# XIAOE_TESTING_PLATFORM_MYSQL_USER = "code_viewer"
# XIAOE_TESTING_PLATFORM_MYSQL_PASSWORD = "cORpi7MUpTzniaj8"
# XIAOE_TESTING_PLATFORM_MYSQL_DB = "xiaoe_testing_platform"

# --------------------------- User -------------------------
# 超级权益：15818362202
# 无权益：15626109422
USER_PHONE = os.getenv(
    "USER_PHONE",
    [
        {"phone": 15818362202, "is_buy": "true"},
        {"phone": 15626109422, "is_buy": "false"}
    ]
)

# --------------------------- 线程 -------------------------
THREAD_MAX_WORKERS = int(os.getenv("THREAD_MAX_WORKERS", 10))

# --------------------------- 进程 -------------------------
PROCESS_POOL_SIZE = int(os.getenv("PROCESS_POOL_SIZE", 8))


# ---------------------- logging ------------------------------
LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'DEBUG')
# 最大保留文件数
LOGGING_MAX_COUNT = os.getenv('LOGGING_MAX_COUNT', 5)
# 最大文件大小
LOGGING_MAX_SIZE = os.getenv('LOGGING_MAX_SIZE', 10)
# 定义日志文件的名称
LOG_FILE = os.getenv('LOG_FILE', "../xiaoe_banned_resource.log")

# --------------------------- 任务链接数量 -------------------------
URL_NUMBER = int(os.getenv("URL_NUMBER", -1))

WEWORK_KEY = os.getenv("WEWORK_KEY", "09b5a5e0-9cd1-4f33-9caa-88c81e1b6aa0")
# WEWORK_KEY = os.getenv("WEWORK_KEY", "b6083ac8-1a2f-49d9-bce0-d34102e0b03c")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 5000))

# ---------------------- Redis ---------------------------------
RDB_HOST = os.getenv('RDB_HOST', 'sh-redis-test-platform-standard.xiaoe-conf.com')
RDB_PASSWORD = os.getenv('RDB_PASSWORD', 'oXjFzTuH8PKkZFqe')
RDB_PORT = int(os.getenv('RDB_PORT', 6379))

# ---------------------- 队列 ---------------------------------
QUEUE_MAX_SIZE = int(os.getenv('QUEUE_MAX_SIZE', 1000))
