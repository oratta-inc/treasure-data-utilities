# -*- coding: utf-8 -*-
u"""このライブラリで、独自定義する例外をまとめたモジュール。"""


class ConfigError(RuntimeError):
    u"""設定値に関する例外。"""

    pass


class TrivialConfigError(ConfigError):
    u"""些細な設定値に誤りがある場合に、スローする例外。

    ex) 特定のKPIに関する設定値のキーが誤っていた。
    """

    pass


class CrucialConfigError(ConfigError):
    u"""システム全体に影響する設定値が誤っていて、処理続行できない場合にスローする例外。

    ex) DB名のスペルが間違えていて、全てのスクリプトで処理が失敗してしまう。
    """

    pass


class TreasureDataError(OSError):
    u"""TreasureDataとの通信時にスローされる例外。"""

    pass


class TreasureDataConnectionError(TreasureDataError):
    u"""TreasureDataとの通信時にスローされる例外。"""

    pass


class TreasureDataTimeOutError(TreasureDataError):
    u"""TreasureDataとの通信時、規定時間が経過してもレスポンスがない時にスローされる例外。"""

    pass


class TreasureDataQueryError(TreasureDataError):
    u"""TreasureDataに発行したクエリに、誤りがあった場合にスローされる例外。"""

    pass


class DataFrameError(RuntimeError):
    u"""DataFrameに関する例外。"""

    pass


class DataFrameEmptyDataError(DataFrameError):
    u"""DataFrameインスタンスが、空だった場合にスローする例外。"""

    pass


class DataFrameInvalidFormatError(DataFrameError):
    u"""DataFrameインスタンスが、期待しない形式だった場合にスローする例外。"""

    pass
