## KPI汎化ツールの開発方針について
==

----

## 1.開発環境のセットアップ
* このプロジェクトでは、python3.5以降を使用する。
* 各開発者・本番環境では、 `pyenv` と `virtualenv` を使い、環境を切り替えられるようにしておくこと。
* また、依存するパッケージは、 `pip` を使って管理すること。
* 各ツールの使い方については、以下に示す。

#### 1.1.pyenvについて
* マシン中のpythonのバージョンを、自在に切り替えられるようにするためのツールである。
* インストールについては、以下の記事を参照すること。
  * [Qiita pyenvとvirtualenvで環境構築](http://qiita.com/Kodaira_/items/feadfef9add468e3a85b)
* 以下のようなコマンドを打つことで、マシン中のpythonのバージョンを、3.5に統一できる(必要な時に、いつでも切り替えできる)。

```
$ pyenv install 3.5.0
$ pyenv global 3.5.0
```

#### 1.2.virtualenvについて
* こちらは、マシン中の環境を自在に切り替えられるようにするためのツールである。環境とは、必要なパッケージが準備済みの、Python実行環境を示す。
* 具体例を挙げると、virtualenvを使えば、以下のような環境をマシン中に併存&切替可能ることが可能になる。
  * データ分析用に、pandasなどのパッケージがインストールされた環境。
  * web開発用に、Djangoに関連するパッケージがインストールされた環境。
* インストールは、同じく以下記事で実施する。
  * [Qiita pyenvとvirtualenvで環境構築](http://qiita.com/Kodaira_/items/feadfef9add468e3a85b)
* 仮想環境の作り方や、切り替えは、以下の記事を参照すること。
  * [Qiita virtualenv 基本的なコマンド使い方メモ](http://qiita.com/th1209/items/84f21a4499548b34ec91)

#### 1.3.pipについて
* pipとは、pythonの依存パッケージ管理ツールである(phpで言うところの、composerと似た役割を持つツール)。
* pipコマンドを使うと、このプロジェクトのrequirements.txtで規定したパッケージを、まとめてインストールすることができる。以下のように実施する。

```
$ pip install -r packages_requirements.txt
```

* 現在インストールしているパッケージは、freezeコマンドで確認できる。

```
$ pip freeze
```

* また、pipはrequirements.txtで依存パッケージを管理することが慣例となっているため、次のようにするだけで、依存パッケージの一覧をバージョン管理できる。

```
$ pip freeze > requirementx.txt
```

----

## 2.開発ルール
* 開発においては、以下のルールを遵守すること。

#### 2.1.修正はプルリクエスト単位にまとめる
* 機能はプルリクエスト単位で発行する。
* プルリクエストのブランチ名規則や記載の粒度は、通常プロジェクトと同じで構わない。

#### 2.2.コーディング規約PEP8に従う
* pythonには、デファクトスタンダードのコーディング規約、[PEP8](https://pep8-ja.readthedocs.io/ja/latest/)が存在する。
* 開発者によって記載がバラつかないよう、PEP8に基づいた記載を心がけること。
* PEP8に対応したチェックツール、flake8を使うことで、規約のチェックを実施することができる。コマンドライン上で、以下のように実行すれば良い。

```
flake8 td_utils/game_config_holder.py
```

* また、開発上やむを得ない警告は、プロジェクト直下のsetup.cfgに追加することで、flake8のチェックを無視できる。
  * ex) D400
      * docstringの末尾はコンマでなければいけないとする規約。
      * 日本メンバーのみの開発では、ほぼ意味が無いため無視している。
* また、IDE PyCharmを使えば、大体のPEP8違反箇所は、警告表示してくれる。

#### 2.3.単体テストを必ず書く
* 機能追加時は、testディレクトリ以下に、必ずテストを記載すること。
* テスト時は、以下のモジュールやパッケージを使うこと。
  * [unittestモジュール](https://docs.python.jp/3/library/unittest.html)
      * python標準の、単体テスト用モジュール。
  * [TestFixtuiresパッケージ](https://testfixtures.readthedocs.io/en/latest/)
      * テストに関するサポート用のパッケージで、「ファイルIO」「ロギング」「日付」など、システム依存や副作用を持つ処理のテストができる。
* 必要に応じて、[Pytest](http://pytest.org/latest-ja/)や[nose](https://nose.readthedocs.io/en/latest/)などのテストフレームワークも導入して構わない。

#### 2.4.CircleCI, Scrutinizerにも注意する
* このプロジェクトでは、他プロジェクトと同様に、CircleCI, Scrutinizerを使用する。
* テストが疎通しなかったり、コードのスコアが低く付いた場合(Cランク以下)は、一旦手を止め、修正やリファクタリングを実施すること。

----

## 3.コーディング規約について
#### 3.1.python
* [PEP8](https://pep8-ja.readthedocs.io/ja/latest/)に従う。
* PEP8に記載がない事項は、現状以下の慣例で実装している。無理に従う必要はないし、「一般的でない」「不合理である」と判断した場合は修正して構わない。
  * メソッド名
      * 基本的に動詞で始める。
          * ex) `def get_or_create():`
      * データをカプセル化し、プロパティ的に扱う場合は名詞でも可。
          * ex) `def db_name():`
  * モジュールの公開規則
      * `__init__.py`で、公開するクラスをimportする。
      * こうする意図は、`td_util/__init__.py` 内のコメントを参照すること。
  * テスト用モジュールの命名規則
      * `test_(対象のモジュール名).py`
        * ex) `test_game_config_holder.py`

#### 3.2.SQL
* SQLは、標準的な規約が存在しないものの、以下の記事に沿った記載を心がけると、読みやすいSQLになる(データベース界隈で有名書籍を多数出版している、ミック氏の記事)。
  * [リレーショナル・データベースの世界 SQLプログラミング作法](http://www.geocities.jp/mickindex/database/db_manner.html)

----

## 4.例外の扱いについて
* 例外はできる限り使い分け、「エラーのレベル分け」や「エラー時の原因究明」がやりやすくなるように心がけること。
* 例外の扱いはまだ明確に決めていないが、少なくとも以下のように扱う予定である。

#### 4.1.例外のレベルを切り分ける
* 「全スクリプトの処理を中止するレベルの例外」と「特定スクリプトだけ中止して、処理続行する例外」に切り分ける。
* 「全スクリプトの処理を中止するレベルの例外」とは、例えば以下のようなケースが該当する。
  * プログラムのロジックにバグがあり、まともに動作しない。
  * 全スクリプトで使う設定値にタイポがあった。
  * 外部サービスが停止していて、後続するスクリプトを実行させても意味がない。
* 「特定スクリプトだけ中止して、処理続行する例外」とは、例えば以下のようなケースが該当する。
  * 特定のKPI取得だけに使う設定値に、タイポがあった。

#### 4.2.標準例外の扱いについて
* pythonの標準例外は、以下のページに一覧化されている。
  * [5. 組み込み例外](https://docs.python.jp/3/library/exceptions.html)
* 以下に、標準例外の例を示す。
  * AttributeError
      * 存在しないプロパティにアクセス。
  * ImportError, ModuleNotFoundError
      * そもそもモジュールがインポートできない。
  * SyntaxError
      * プログラムにタイポがあって、動作しない。
  * TypeError
      * 型の扱いを間違えている。
* ほとんどの標準例外が発生するケースでは、処理を続行しても有益な結果にならない。これらの例外は握りつぶさず、スクリプトの末端で適切なエラーメッセージ、エラーコードを表示するなどすること。また、後続するスクリプトの実行も打ち切って構わないだろう。
* 一部の特殊ケースでしか走らないプログラムで起こる標準例外や、RunTimeErrorやOSErrorなどのやむを得ない例外は、例外をcatchして処理続行しても構わない。

#### 4.3.拡張例外
* td_utilパッケージで提供する例外を以下に示す。
* 必要に応じて、これらの例外を使用したり、例外の追加を行うこと。

```
Exception
├ RunTimeError
  ├ ConfigError                    設定に関するエラー
    ├ TrivialConfigError           特定スクリプトにしか影響のない設定でエラー
    └ CrucialConfigError           全スクリプトに影響のある設定でエラー
  └ DataFrameError                 DataFrameインスタンスに関するエラー
    ├ DataFrameEmptyDataError      DataFrameインスタンスが空
    └ DataFrameInvalidFormatError  DataFrameインスタンスが意図しない形式
└ OSError
  └ TreasureDataError              TreasureDataに関するエラー
    ├ TreasureDataConnectionError  TreasureDataの接続でエラー
    ├ TreasureDataTimeOutError　　　TreasureDataとの通信でタイムアウト
    └ TreasureDataQueryError　　　  TreasureDataに発行したクエリでエラー
```

----

### 5.その他
