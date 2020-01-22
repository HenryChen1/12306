# -*- coding: utf8 -*-
import TickerConfig
from config.urlConf import urls
from myUrllib.httpUtils import HTTPClient

PUSH_SERVER_CHAN_PATH = "https://sc.ftqq.com"


def sendServerChan(msg):
    """
    pushBear微信通知
    :param str: 通知内容 content
    :return:
    """
    if (
        TickerConfig.SERVER_CHAN_CONF["is_server_chan"]
        and TickerConfig.SERVER_CHAN_CONF["secret"].strip() != ""
    ):
        try:
            secret = TickerConfig.SERVER_CHAN_CONF["secret"].strip()
            sendServerChanUrls = urls.get("ServerChan")
            sendServerChanUrls["req_url"] += f'{secret}.send'

            params = {"text": "嘻嘻抢到票了👌", "desp": msg}
            httpClint = HTTPClient(0)
            sendServerChanRsp = httpClint.send(sendServerChanUrls, params=params)
            if sendServerChanRsp.get("errno") == 0:
                print(u"已下发 Server酱 微信通知, 请查收")
            else:
                print(sendServerChanRsp)
        except Exception as e:
            print(u"Server酱 配置有误 {}".format(e))


if __name__ == "__main__":
    sendServerChan(1)
