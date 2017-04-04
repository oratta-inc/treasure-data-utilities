# -*- coding: utf-8 -*-
u"""GameConfigHolderクラスを提供するモジュール。"""


class GameConfigHolder:
    u"""特定ゲームタイトルの設定情報を保持するクラス。"""

    def __init__(self, config_path):
        u"""コンストラクタ。"""
        pass

    def db_name(self):
        u"""このタイトルが対応するDB名を返す。"""
        pass

    def platforms(self):
        u"""このタイトルが対応するプラットフォームをタプルで返す。"""
        pass
