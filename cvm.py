import json

with open('cvm-pri.txt', 'r') as f:
    contents = f.readlines()

# print(contents)

for content in contents:
    content = json.loads(content)
    # print(f'content={content}')
    # print(content[0]['paramValue'])
    for i in content:
        # print(i)
        # print(i.get('paramValue'))
        param_value = i.get('paramValue')

        if param_value and isinstance(param_value, str) and param_value.startswith('http://sh-lb'):
            print(param_value)
        else:
            pass
            # print(f'错误：{param_value}\n')
