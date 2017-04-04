# -*- coding: utf-8 -*-
u"""TreasureDataをプログラム上で扱う上でのユーティリティ処理を提供するライブラリ。

補足:

* 各モジュールから、必要なクラスを事前にimportしている。
* こうする理由は、以下の2つの理由による。
  1. import時の記載を簡潔にするため。
     NG) from td_util.kpi_config_holder import KpiConfigHolder
     OK) from td_util import KpiConfigHolder
  2. このライブラリ内のモジュール構成を変更した際に、
     import先に修正が及ばないようにするため。
"""

# 各モジュールから、外部に公開するクラスをimportしておく。
from .data_frame_formatter import DataFrameFormatter
from .exceptions import ConfigError
from .exceptions import CrucialConfigError
from .exceptions import DataFrameEmptyDataError
from .exceptions import DataFrameInvalidFormatError
from .exceptions import TreasureDataConnectionError
from .exceptions import TreasureDataError
from .exceptions import TreasureDataQueryError
from .exceptions import TreasureDataTimeOutError
from .exceptions import TrivialConfigError
from .game_config_holder import GameConfigHolder
from .kpi_config_holder import KpiConfigHolder
from .treasure_data_gateway import TreasureDataGateway
