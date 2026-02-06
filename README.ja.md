# デジタルカーリング用新クライアント
これはデジタルカーリング用の新しいクライアントです。

## 言語
- 英語（デフォルト）: [README.md](./README.md)
- 日本語           : [README.ja.md](./README.ja.md)

## requirements.txt のインストール
```bash
pip install -r requirements.txt
```
このリポジトリは将来的に pypi で公開する予定ですが、現在は以下を使用してください。

```Bash
pip install .
```

## 使い方
ユーザーデータの準備
試合を行うためには、各ユーザーがサーバー側に登録されている必要があります。 例:

```
MATCH_USER_NAME="user"
PASS_WORD="password"
```
今回の試用段階では、ユーザーが登録されているデータベースがサーバー側で共有されているため、すぐに（ユーザー同士で）対戦が可能だと思います。 （本番環境では、ユーザー名とパスワードが事前に配布され、ユーザーはサーバーに登録されます。）

既に登録済みのユーザー名とパスワードは、この共有リポジトリの .env ファイルに記載されていますのでご注意ください。

## 試合の作成
### 試合設定ファイル
"src.setting.json" ファイルに、standard_end_count（標準エンド数）、time_limits（制限時間）、使用する simulator（シミュレータ）、applied_rule（適用ルール）など、試合に必要な情報を記述してください。 

game_mode には **standard** または **mixed_doubles** を入れてください。
- standardを選択した場合
4人制での対戦が開始されます。この場合は、**applied_rule**には
    - five_lock_rule
    - no_tick_rule
のいずれかを選択してください。
- mixed_doublesを選択した場合
ミックスダブルスに対応した対戦が開始されます。この場合は**applied_rule**には
    - modified_fgz
    を選択してください

(現在、利用可能なシミュレータは "fcv1" のみですので、他のシミュレータでは対戦できません。)

### 試合作成
setting.json の設定が完了したら、以下のコマンドを入力してください。

```Bash
cd src
python match_maker.py
```
上記のコマンドは、新しい試合を開始したいときに入力してください。

これで match_id.json に match_id が保存されます。

## クライアントをサーバーに接続
実際に相互に対戦できるように、client0 と client1 というフォルダを用意しました。（配布する際は、client0 と client1 フォルダを削除した上で、別リポジトリにテンプレートとして作成するsample_client.py を参照してください。）

その試合でプレイするプレイヤーの設定は、"client0.team0_config.json" および "client1.team1_config.json" で行えます。 また、大会と同じ設定でプレイする場合は、以下のように設定してください。

```Markdown
"use_default_config": true
```
独自のチームを作成したい場合は、以下のようにします。

```Markdown
"use_default_config": flase
```
上記の設定が完了したら、以下のコマンドを入力してクライアントをサーバーに接続してください。

```Bash
cd client0
python client.py
```
その後、別のターミナルを開き、以下を実行します。

```Bash
cd client1
python client.py
```
これらのコマンドで接続を確認できると思います。