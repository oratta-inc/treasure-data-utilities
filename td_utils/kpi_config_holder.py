# -*- coding: utf-8 -*-
u"""KpiConfigHolderクラスを提供するモジュール。"""


class KpiConfigHolder:
    u"""1つのKPIに対する設定情報を保持するオブジェクト。

    このオブジェクトは、以下のような情報を保持する。
    * KPIに関する設定情報
    * SQL文字列
    * データを取得する範囲
    """

    @classmethod
    def create(cls, kpi_name, config_path, start_time, end_time):
        u"""ファクトリメソッド。"""
        pass

    def __init__(self, config_dict, raw_sql, start_time, end_time):
        u"""コンストラクタ。"""
        pass

    def sql(self):
        u"""このKPIをTreasureData上で取得するためのSQLを返す。"""
        pass

    def table_name(self):
        u"""このKPIと1対1で対応する、TreasureData上のテーブル名を返す。"""
        pass
