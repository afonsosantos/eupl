import json
import pathlib
import platform

import psutil
import requests
from riposte import Riposte

from config import *

eupl = Riposte(banner=BANNER, prompt=PROMPT)

MEMORY = []


@eupl.command('ver')
def ver_func():
    eupl.status('Version {}'.format(VERSION))


@eupl.command('exit')
def exit_func():
    eupl.success('Goodbye!\n')
    exit()


@eupl.command('add')
def add_func(x: int, y: int):
    result = f'{x} + {y} = {x + y}'
    MEMORY.append(result)
    eupl.success(result)


@eupl.command('mult')
def multiply_func(x: int, y: int):
    result = f"{x} * {y} = {x * y}"
    MEMORY.append(result)
    eupl.success(result)


@eupl.command('mem')
def memory_func():
    for entry in MEMORY:
        eupl.print(entry)


@eupl.command('say')
def say_func(msg: str):
    eupl.success(msg)


@eupl.command('info')
def info_func():
    eupl.success("OS: {}".format(platform.system()))
    eupl.success("CPU: {} ({})".format(
        platform.processor(), platform.machine()))
    eupl.success("RAM: {} MB".format(psutil.virtual_memory()[0] >> 20))


@eupl.command('bin')
def bin_func(num: int):
    eupl.success(bin(num))


@eupl.command('get')
def post_func(url: str, file_name: str):
    r = requests.get(url=url)
    with open('{}.txt'.format(file_name), 'w') as file:
        json.dump(r.json(), file)
    eupl.success('Data from GET request dumped in {}'.format(
        pathlib.Path(__file__).parent.absolute()))


@eupl.command('man')
def man_func(cmd: str):
    for command, desc in MANUAL.items():
        if cmd in command:
            eupl.success('{} - {}'.format(command, desc))

# ADD HERE


@eupl.command('cmd')
def cmd_func():
    for command in COMMANDS:
        eupl.success(command)


eupl.run()
