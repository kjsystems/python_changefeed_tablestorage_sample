# python_changefeed_tablestorage_sample

## このリポジトリの説明

このリポジトリは、Cosmos DB の Change Feed を使用して Cosmos DB に追加されたデータを Azure Table Storage に書き込む方法を示しています。`REST.http` ファイルを使用してデータを追加すると、Change Feed が発動し、そのデータが Table Storage に追加されます。

## 実行方法

1. **環境のセットアップ**:
   - `.devcontainer` を使用するか、Codespaces で実行します。
   - 環境変数を設定します:
     - `local.settings.sample.json` を `local.settings.json` にリネームします。
     - `local.settings.json` に `COSMOS_CONNECTION` と `STORAGE_CONNECTION` を設定します。

2. **デバッグ**:
   - デバッグモード（F5）でアプリケーションを実行します。

3. **REST リクエストの実行**:
   - `REST.http` ファイルを使用して、実行中のアプリケーションに HTTP リクエストを送信します。これにより、Cosmos DB にデータが追加されます。

4. **データの追加を確認**:
   - Cosmos DB にデータが追加され、Change Feed がトリガーされて Azure Table Storage にデータが追加されることを確認します。
