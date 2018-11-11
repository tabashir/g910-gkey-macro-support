
import json
import uinput
import os, sys
import subprocess
import inspect
import pyautogui
from lib.data_mappers import hotkey_type

main_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
config_path = os.path.join(main_dir, "config/config.json")


def execute_writing(string_to_write: str, device):
    # TODO: add support for slovenian layout
    pyautogui.typewrite(string_to_write)

def execute_hotkey(string_for_hotkey: str, device):
    # TODO: add support for slovenian layout
    pyautogui.hotkey(*string_for_hotkey.split("+"))

def execute_command(command):
    subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def resolve_config(key):
    with open(config_path, "r") as f:
        try:
            config = json.load(f)
        except:
            print("\nJSON FILE ERROR, CORRECT JSON!\n")
            exit(1)



    if key not in config.keys():
        return lambda _: None

    key_config : dict = config[key]
    command = key_config.get("hotkey_type","nothing")
    command = hotkey_type.type[command]

    if command == 0:
        return lambda device: execute_writing(key_config["do"], device)
    if command == 1:
        return lambda device: execute_hotkey(key_config["do"], device)
    if command == 2:
        return lambda _: execute_command(key_config["do"])
    if command == -1:
        return lambda _: None





def g1(device):
    resolve_config("g1")(device)

def g2(device):
    resolve_config("g2")(device)


def g3(device):
    resolve_config(inspect.stack()[0][3])(device)


def g4(device):
    resolve_config(inspect.stack()[0][3])(device)


def g5(device):
    resolve_config(inspect.stack()[0][3])(device)


def g6(device):
    resolve_config(inspect.stack()[0][3])(device)


def g7(device):
    resolve_config(inspect.stack()[0][3])(device)


def g8(device):
    resolve_config(inspect.stack()[0][3])(device)


def g9(device):
    resolve_config(inspect.stack()[0][3])(device)
