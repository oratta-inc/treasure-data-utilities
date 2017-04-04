## 設定ファイルの仕様について
==

----

## 1.ディレクトリ構成

* 任意のパスに、以下の構造を持つ設定ファイル群を作成すること。
* `.sql` 以外の設定ファイルは、 `.yaml` もしくは `.json` のいずれでも構わない。
* 以降で、各設定ファイルについて言及する。

```
(任意のディレクトリ名)/
├ query/
  ├ purchase_amount.sql
  └ ...
├ game_config/
  ├ asukazero.yaml
  ├ bleach.yaml
  └ ...
├ kpi_config/
  ├ seg_all.yaml
  ├ seg_purchase.yaml
  ├ ...
  ├ player_num_seg_all.yaml
  ├ purchase_amount_seg_all.yaml
  └ ...
└ treasure_data.yaml

```

----

## 2.SQLファイルについて

#### 2.1.記載のルール
* このスクリプトで使うSQLは、いわゆるプレースホルダ付きSQLで、 `{}` で指定した変数を設定値で置き換えることができる。
* プレースホルダは必要に応じて追加して構わないが、各SQLは最低限以下のプレースホルダを必ず含むこと。
  * start: データの取得開始日時(タイムスタンプ)
  * end:   データの取得終了日時(タイムスタンプ)
* また、このスクリプトで使うSQLは汎化されたものであり、「取得期間」「ネイティヴゲームか否か」「PC版か否か」といった観点を無視して使いまわせるSQLでなければいけない。
* これを実現するために、以下のカラムで `GROUP BY` を行う必要がある。
  * 日付
  * platform
  * user_agent
* ※ スクリプトの末端で、 `platform` や `user_agent` に応じた集計を行う。そのため、SQLで取得するデータが細かくなりすぎることを気にする必要はない。

#### 2.2.セグメント取得用のクエリ例
* 以下に、課金ユーザセグメントを取得するためのSQLサンプルを示す。
* 次の3点に注意すること。
  * 最初の副問合せでユーザの時間帯毎の課金額を求め、主問い合わせでユーザが最初に課金した時間帯で絞り込んでいる。
  * 日毎にデータを集計する必要があるため、日付(date)の取得も必要。
  * GROUP BYを省略するために、DISTINCTしている。

```sql
-- 時間帯毎に課金者を求める。
WITH sub1 AS
(
SELECT
    DISTINCT
     TD_TIME_FORMAT(floor(time/3600) * 3600, 'yyyy-MM-dd', 'JST') AS date
    ,TD_TIME_FORMAT(floor(time/3600) * 3600, 'yyyy-MM-dd HH:mm:ss', 'JST') AS date_time
    ,platform
    ,user_agent
    ,user_id
FROM
    kpi_variables
WHERE
    TD_TIME_RANGE(time, {start}, {end}, 'JST')
    AND (purchase_amount > 0)
)
-- ユーザが最初に課金した時間帯に絞り込む。
SELECT
    MIN(date_time) AS date_time, platform, user_agent, user_id
FROM
    sub1
GROUP BY
    user_id, date, platform, user_agent
ORDER BY
    date_time, platform, user_agent, user_id
;
```

#### 2.3.通常KPI取得のクエリ例
* 以下に、日毎の課金額を取得するためのSQLサンプルを示す。

```sql
--全ユーザの課金情報
WITH sub1 AS
(
SELECT
     TD_TIME_FORMAT(time, 'yyyy-MM-dd','JST') AS date_time
    ,platform
    ,user_agent
    ,user_id
    ,COALESCE(SUM(paid_column), 0) AS purchase_amount
FROM
    kpi_variables
WHERE
    TD_TIME_RANGE(time, {start}, {end}, 'JST')
    -- 以下プレースホルダは、有償・無償の切り替え用。
    AND {paid_condition}
GROUP BY
     user_id
    ,TD_TIME_FORMAT(time, 'yyyy-MM-dd','JST')
    ,platform
    ,user_agent
ORDER BY
    date_time ,platform ,user_agent ,user_id
)
--セグメントユーザ一覧取得
, sub2 AS
(
SELECT
     TD_TIME_FORMAT(TD_TIME_PARSE(date_time, 'JST'), 'yyyy-MM-dd','JST') AS date_time
    ,platform
    ,user_agent
FROM
    {seg_table}
WHERE
    TD_TIME_RANGE(TD_TIME_PARSE(date_time, 'JST'), {start}, {end}, 'JST')
GROUP BY
     user_id
    ,TD_TIME_FORMAT(TD_TIME_PARSE(date_time, 'JST'), 'yyyy-MM-dd','JST')
    ,platform
    ,user_agent
ORDER BY
     date_time ,platform ,user_agent ,user_id
)
-- 対象セグメントの課金額取得
-- (全ユーザの課金情報と、対象セグメントの一覧でINNER JOIN)
SELECT
     sub1.date_time
    ,sub1.platform
    ,sub1.user_agent
    ,COALESCE(SUM(sub1.purchase_amount), 0) AS purchase_amount
FROM
    sub1
INNER JOIN
    sub2
ON
    sub1.date_time = sub2.date_time
    AND sub1.platform = sub2.platform
    AND sub1.user_agent = sub2.user_agent
    AND sub1.user_id = sub2.user_id
GROUP BY
     sub1.date_time
    ,sub1.platform
    ,sub1.user_agent
ORDER BY
     sub1.date_time, sub1.platform, sub1.user_agent
;
```

----

### 2. ゲーム用の設定ファイルについて

* 名称は、`(db名).yaml` or `(db名).json` とする。
* 以下キーを持つ。
  * db_name
    * TreasureData上のDB名を指定する。
  * platforms
    * このタイトルがサポートするプラットフォームの一覧を指定する。
  * user_agents
    * このタイトルがサポートするユーザーエージェントの一覧を指定する。
  * game_type
    * このタイトルのゲームの種類を指定する。
    * 値は、'browser'か'native'のいずれか。
* 以下に、アスカ零での設定例を示す。

```yaml
db_name: 'asukazero'
platforms:
    - 'semi-native'
user_agents:
    - 0
    - 1
game_type: 'native'
```

* 以下に、クロリスガーデンでの設定例を示す。

```yaml
db_name: 'chloris'
platforms:
    - 'ameba'
    - 'dgame'
    - 'gree'
    - 'mbga'
    - 'mixi'
    - 'mobcast'
    - 'yamada'
user_agents:
    - 'FP'
    - 'SP'
    - 'PC'
game_type: 'browser'
```

----

### 3. KPI用の設定ファイルについて

* 名称は、(テーブル名).yaml or (テーブル名).jsonとする。
* 最低限、以下のキーを持つ。
  * table_name
    * このKPIのテーブル名。この名称で、TreasureData上に対応するテーブルが存在していること。
  * column_def
    * このKPIのカラムと、そのデフォルト値についての定義。
  * fill_columns
    * データの歯抜けを行うカラムをまとめた配列。
    * もしこのカラムで規定したデータが1件も無かった場合、デフォルト値でデータの穴埋めが行われる。
  * sum_columns
    * データを集計したいカラムをまとめた配列。このカラムを指定した場合、スクリプトの末端で、データの集計が行われる。
* 必要に応じて、追加のキー設定も行ってよい(SQL側に、対応するプレースホルダを用意すること)。例えば、以下のようなキーが挙げられる。
  * seg_table
    * どのセグメントのユーザと結びつくかを指定する。
  * paid_condition
    * 有償か無償かを切り分ける。


* 以下に、DAUでの設定例を示す。

```yaml
table_name: 'purchase_amount_seg_all'
column_def:
    - date_time: '%Y-%m-%d %H:%M:%S'
    - platform: ''
    - user_agent: ''
    - purchase_amount: 0
sum_columns: 'user_agent'
seg_table: 'seg_all'
paid_condition: 'purchase_amount > 0'
```

----

### 4. TreasureData用の設定ファイルについて

* 名称は、treasure_data.yaml or treasure_data.jsonとする。
* 以下キーを持つ。
  * api_key
      * TreasureDataへ接続する際の、API KEY。
  * end_point
      * TreasureDataのエンドポイントを指定する。
  * query_type
      * TreasureDataへ発行するクエリの種類。
      * 値は、'presto'か'hive'のいずれか。
* 以下に、設定例を示す。

```yaml
api_key: 'xxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
end_point: 'https://ybi.jp-east.idcfcloud.com'
query_type: 'presto'
```
