import os
import sys

from util.BiliRequest import BiliRequest
from util.KVDatabase import KVDatabase


# 创建通知器实例

# 获取图标文件的路径
def get_application_path():
    if getattr(sys, "frozen", False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))

    return application_path


def get_application_tmp_path():
    os.makedirs(os.path.join(get_application_path(), "tmp"), exist_ok=True)
    return os.path.join(get_application_path(), "tmp")


configDB = KVDatabase(os.path.join(get_application_tmp_path(), "config.json"))
if not configDB.contains("cookie_path"):
    configDB.insert("cookie_path", os.path.join(get_application_tmp_path(), "cookies.json"))
issue_please_text = " (如果还无法解决, 请提交issue到仓库, 十分感谢)"
main_request = BiliRequest(cookies_config_path=configDB.get("cookie_path"))

global_cookieManager = main_request.cookieManager
sleep_seconds = 1
