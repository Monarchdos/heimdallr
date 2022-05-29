# -*- coding:utf-8 -*-
import json

import requests

from env import get_env
from exception import WecomException

from .base import Channel, Message


class WecomMessage(Message):
    def __init__(self, title: str, body: str):
        super().__init__(title, body)


class WecomWebhook(Channel):
    def __init__(self, message: WecomMessage):
        super().__init__(message, name="wecom webhook")
        self.base_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key="
        self.key = ""
        self.get_credential()

    def compose_message(self) -> str:
        msg = {
            "msgtype": "text",
            "text": {"content": f"{self.message.title}\n{self.message.body}"},
        }
        return json.dumps(msg)

    def send(self):
        super().send()
        url = f"{self.base_url}{self.key}"
        rs = requests.post(
            url,
            data=self.compose_message(),
            headers={"Content-Type": "application/json"},
        )
        rs = json.loads(rs.text)
        if rs["errcode"] == 0:
            return True, rs["errmsg"]
        return True, rs["errmsg"]

    def get_credential(self):
        env = get_env()
        self.key = env.wecom_webhook_key


class WecomApp(Channel):
    def __init__(self, message: WecomMessage):
        super().__init__(message, name="wecom app")
        self.base_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="
        self.access_token = ""
        self.agent_id = ""
        self.get_credential()

    def compose_message(self) -> str:
        msg = {
            "touser": "@all",
            "msgtype": "text",
            "agentid": self.agent_id,
            "text": {"content": f"{self.message.title}\n{self.message.body}"},
            "safe": 0,
        }
        return json.dumps(msg)

    def send(self):
        msg = self.compose_message()
        url = f"{self.base_url}{self.access_token}"
        rs = requests.post(
            url,
            data=msg,
            headers={"Content-Type": "application/json"},
        )
        rs = json.loads(rs.text)
        if rs["errcode"] == 0:
            return True, rs["errmsg"]
        return False, rs["errmsg"]

    def get_credential(self):
        env = get_env()
        self.agent_id = env.wecom_agent_id
        corp_id, secret = env.wecom_corp_id, env.wecom_secret
        auth_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={secret}"
        rs = requests.get(auth_url)
        rs = json.loads(rs.text)
        if rs["errcode"] == 0:
            self.access_token = rs["access_token"]
        else:
            raise WecomException(f"Failed to get access token: {rs['errmsg']}")