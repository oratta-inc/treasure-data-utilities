# -*- coding: utf-8 -*-
u"""KpiConfigHolderクラスに対するテストをまとめたモジュール。"""

from datetime import datetime
from unittest import TestCase

from td_utils import KpiConfigHolder


class KpiConfigHolderTest(TestCase):
    u"""KpiConfigHolderクラスに対するテスト。"""

    def test_init(self):
        u"""コンストラクタのテスト。"""
        config_dict = {
            "kpi_name": "purchase_amount_daily_seg_all"
        }
        sql = 'SELECT * FROM sample_table;'
        start_time = datetime.strptime(
            '2017-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'
        )
        end_time = datetime.strptime(
            '2017-01-02 00:00:00', '%Y-%m-%d %H:%M:%S'
        )

        kpi_config = KpiConfigHolder(config_dict, sql, start_time, end_time)

        self.assertIsInstance(kpi_config, KpiConfigHolder)
