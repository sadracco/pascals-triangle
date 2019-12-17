import json

with open('config/app_config.json') as config_file:
    app_config = json.load(config_file)

with open('config/triangle_config.json') as config_file:
    triangle_config = json.load(config_file)

if __name__ == '__main__':
    print(app_config['title'])
    print(triangle_config)
