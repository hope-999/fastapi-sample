import json
import re
from json import JSONDecodeError

with open('无映射-工作表1.csv', 'r') as f:
    contents = f.readlines()

result_list = []

with open('cvm-replace-1026-eo_aat_collection_scene_case_api.sql', 'w') as f:
    for content in contents:
        # result = re.findall(r'http?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', content)
        content = content.split(',')[:2]
        # print(content)
        sql_str = f"UPDATE eo_aat_collection_scene_case_api SET caseData = REPLACE ( caseData, '{content[0]}', '{content[1]}');\n"
        print(sql_str)
        f.write(sql_str)
