# python_changefeed_tablestorage_sample

## このリポジトリの説明

このリポジトリは、Azure Change Feed を使用して Azure Blob Storage の変更を監視し、その変更を Azure Table Storage に書き込む方法を示しています。`REST.http` ファイルを使用してデータを追加すると、Change Feed が発動し、そのデータが Table Storage に追加されます。

## テスト方法

1. **環境のセットアップ:**
   - Python と必要な依存関係がインストールされていることを確認します。仮想環境をセットアップすることをお勧めします。
   - 必要なパッケージをインストールします:
     ```bash
     pip install -r requirements.txt
     ```

2. **Azure サービスの設定:**
   - Azure Blob Storage と Azure Table Storage を設定します。
   - 必要な接続文字列とキーが利用可能であることを確認します。

3. **アプリケーションの実行:**
   - 以下のコマンドでアプリケーションを開始します:
     ```bash
     python main.py
     ```

4. **REST リクエストの実行:**
   - `REST.http` ファイルを使用して、実行中のアプリケーションに HTTP リクエストを送信します。これにより、Blob Storage にデータが追加されます。
   - [VS Code 用 REST クライアント](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) などの HTTP クライアントを使用して、リクエストを実行できます。

5. **データの追加を確認:**
   - Azure Table Storage を確認し、Change Feed によってデータが正しく追加されたことを確認します。
