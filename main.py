from os import path, getenv
from datetime import datetime as date
import json

ENVVAR = 'TIMETABLER_CONFIG_FILE'
CONFIG_FILE = getenv(ENVVAR) or '~/.config/timetabler/config.json'


def json_key_upper(d):
    return {k.upper(): v for k, v in d.items()}


def read_config_file():
    if not path.exists(path.expanduser(CONFIG_FILE)):
        print("Config file does not exist. Create a new one?")
        return
    with open(path.expanduser(CONFIG_FILE), 'r') as f:
        return json_key_upper(json.load(f))


def get_current_short_day_name():
    return date.today().strftime('%a').upper()


def main():
    print("Timetabler")
    timetable = read_config_file()
    print(timetable[get_current_short_day_name()])


if __name__ == '__main__':
    main()
