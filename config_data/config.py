from environs import Env
from dataclasses import dataclass


@dataclass
class TGBot:
    token: str
    admin_ids: list[int]


@dataclass
class NASA:
    api_key: str


@dataclass
class Config:
    tg_bot: TGBot
    nasa: NASA


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TGBot(token=env('BOT_TOKEN'),
                               admin_ids=[int(admin_id) for admin_id in env.list('ADMIN_IDS')]),
                  nasa=NASA(api_key=env('NASA_API_KEY')))
# use code below for test your config
# print('BOT_TOKEN:', config.tg_bot.token)
# print('ADMIN_IDS:', config.tg_bot.admin_ids)
# print('NASA_API_KEY:', config.nasa.api_key)
