# -*- coding: utf-8 -*-
u"""GameConfigHolderクラスに対するテストをまとめたモジュール。"""

from unittest import TestCase

from td_utils import GameConfigHolder


class GameConfigHolderTest(TestCase):
    u"""GameConfigHolderクラスに対するテスト。"""

    def test_init(self):
        u"""コンストラクタのテスト。"""
        game_config = GameConfigHolder(
            '/home/kpi-user/kpi_config/game_config/asukazero.yaml'
        )
        self.assertIsInstance(game_config, GameConfigHolder)
