from typing import List

from environs import Env

env = Env()
env.read_env()


def get_config_str(name: str, suffix: str, default: str = "") -> str:
    if suffix == "":
        return env.str(name, default)
    return env.str(name + "_" + suffix, default)


def get_config_list(name: str, suffix: str, default: List[str] = []) -> List[str]:
    if suffix == "":
        return env.list(name, default)
    return env.list(name + "_" + suffix, default)
