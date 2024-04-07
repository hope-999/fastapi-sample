"""
-------------------------------------------------
  Description :
  Author :    @zhuang_wu
  Time : 2024/3/6 10:33
-------------------------------------------------
"""
import logging
import os
from logging.handlers import RotatingFileHandler

from app.settings import LOGGING_LEVEL, LOG_FILE, LOGGING_MAX_SIZE, LOGGING_MAX_COUNT

# 创建一个logger对象，用于记录日志
logger = logging.getLogger(__name__)
# 设置日志的级别，可以根据需要修改
logger.setLevel(LOGGING_LEVEL)

# 创建一个RotatingFileHandler对象，用于将日志写入文件，并实现文件大小分割
file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=int(LOGGING_MAX_SIZE) * 1024 * 1024,
    backupCount=int(LOGGING_MAX_COUNT)
)
console_handler = logging.StreamHandler()
# 设置日志的格式，可以根据需要修改
formatter = logging.Formatter(
    '%(asctime)s '
    '%(filename)s:%(lineno)d '
    '%(processName)s '
    '%(threadName)s '
    '%(levelname)s '
    '%(message)s'
)
# 将格式应用到handler对象上
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
# 将handler对象添加到logger对象上
logger.addHandler(file_handler)
logger.addHandler(console_handler)
