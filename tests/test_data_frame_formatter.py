# -*- coding: utf-8 -*-
u"""DataFrameFormatterクラスに対するテストをまとめたモジュール。"""

from unittest import TestCase

from td_utils import DataFrameFormatter


class DataFrameFormatterTest(TestCase):
    u"""GameConfigHolderクラスに対するテスト。"""

    def test_init(self):
        u"""コンストラクタのテスト。"""
        game_config = DataFrameFormatter()
        self.assertIsInstance(game_config, DataFrameFormatter)
