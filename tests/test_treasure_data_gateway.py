# -*- coding: utf-8 -*-
u"""TreasureDataGatewayクラスに対するテストをまとめたモジュール。"""

from unittest import TestCase

from td_utils import TreasureDataGateway


class TreasureDataGatewayTest(TestCase):
    u"""KpiConfigHolderクラスに対するテスト。"""

    def test_init(self):
        u"""コンストラクタのテスト。"""
        db_name = 'asuka_zero'
        config_dict = {
            "api_key": "xxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "end_point": "https://ybi.jp-east.idcfcloud.com",
            "query_type": "presto",
        }
        kpi_config = TreasureDataGateway(db_name, config_dict)

        self.assertIsInstance(kpi_config, TreasureDataGateway)
