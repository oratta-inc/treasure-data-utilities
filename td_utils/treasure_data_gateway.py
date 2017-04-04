# -*- coding: utf-8 -*-
u"""TreasureDataGatewayクラスを提供するモジュール。"""


class TreasureDataGateway:
    u"""TreasureDataとのAPI疎通用ラッパー。"""

    @classmethod
    def create(cls, db_name, config_path):
        u"""ファクトリメソッド。"""
        pass

    def __init__(self, db_name, config_dict):
        u"""コンストラクタ。"""
        pass

    def issue_query(query):
        u"""TreasureDataへクエリを発行し、結果をDataFrameクラスとして返す。"""
        pass

    def write_to(table_name, data_frame):
        u"""TreasureData上のテーブルに、データを書き込む。"""
        pass
