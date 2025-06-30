# OpenAI エージェント設定

## ディレクトリ構成

### ソースコード

* **すべてのソースコードは `src/` または `app/` ディレクトリに配置してください。**

  * メインアプリケーション: `src/main.py` または `app/index.js`
  * ユーティリティ関数: `src/utils/` または `app/utils/`
  * API エンドポイント: `src/api/` または `app/api/`
  * データベースモデル: `src/models/` または `app/models/`

### テストファイル

* **すべてのテストファイルは `tests/` ディレクトリに配置してください。**

  * ユニットテスト: `tests/unit/`
  * 結合テスト: `tests/integration/`
  * テストフィクスチャ: `tests/fixtures/`
  * テスト設定: `tests/conftest.py`

### 設定ファイル

* **設定ファイルは `config/` ディレクトリに配置してください。**

  * アプリ設定: `config/settings.json` または `config/config.yaml`
  * 環境変数: `.env`（機密情報用）

### ユーティリティファイル

* **ユーティリティファイルは `utility/` ディレクトリに配置してください。**

  * 環境チェックスクリプト: `utility/check_env.py`
  * ヘルパースクリプト: `utility/` ディレクトリ

## 開発プロセス

### 環境チェック

**このプロジェクトでコードを実行する前に、必ず環境チェックスクリプトを実行してください：**

```bash
# 仮想環境のアクティベート
conda activate py-review  # または適切な環境名

# 環境チェックスクリプトの実行
python utility/check_env.py
```

このスクリプトは以下を確認します：
- ✅ 適切な仮想環境がアクティブか
- ✅ 必要な依存関係がインストールされているか
- ✅ 設定ファイルが存在するか

### Python スクリプト利用

1. プロジェクトディレクトリへ移動
2. 開発用スクリプトを実行

   ```bash
   # テスト実行
   python -m pytest tests/

   # Lint 実行
   flake8 src/ --max-line-length=88

   # フォーマッタ実行
   black src/

   # 型チェック
   mypy src/
   ```

### Docker 環境利用

```bash
# 開発環境起動
docker-compose up -d

# ログ確認
docker-compose logs -f

# サービス停止
docker-compose down
```

### テスト実行

```bash
# すべてのテスト
python -m pytest tests/ -v

# 特定ファイルのテスト
python -m pytest tests/test_main.py

# カバレッジ付き実行
python -m pytest tests/ --cov=src --cov-report=html
```

## 新規コンテンツ追加

### 新機能追加

1. `src/` または `app/` にファイル例 `src/new_feature.py` を作成
2. 基本的なクラス／関数を実装
3. 必要に応じて `config/` に設定を追加
4. 単体テストを作成
5. 適切な結合テストを追加

### 設定追加

1. `config/` 内の設定ファイルを編集

   ```json
   {
     "new_feature": {
       "enabled": true,
       "timeout": 30
     }
   }
   ```
2. 必要に応じて環境変数を設定
3. 設定読み込みを検証

### テスト追加

1. `tests/` にテストファイルを作成
2. 命名規約: `test_<module_name>.py`
3. 適切なテストフレームワーク（pytest, jest 等）を使用
4. 単体テストと結合テストの両方を含める

## コード品質基準

### 言語別ガイドライン

#### Python

* PEP 8 準拠
* インデントは 4 スペース
* クラス／メソッドに docstring を追加
* 適切な型ヒントを使用
* 適切なエラーハンドリングを実装

#### JavaScript / TypeScript

* ESLint・Prettier 設定に従う
* 一貫した命名規則
* 関数に JSDoc コメント
* 型安全のため TypeScript を使用
* 適切なエラーハンドリングを実装

#### Java

* Checkstyle 準拠
* 一貫した命名規則
* JavaDoc コメント追加
* 適切な例外処理
* 適切なデザインパターンを使用

### テスト戦略

* コンポーネント単位のユニットテスト
* ワークフロー全体の結合テスト
* 外部依存をモック
* CI/CD との統合
* 高いテストカバレッジを維持

### パフォーマンス最適化

* 効率的なアルゴリズムを実装
* 必要に応じてキャッシュを導入
* メモリ使用量を最適化
* 不要な処理を削減
* プロファイラでボトルネックを特定

## GitHub Actions CI/CD

### 自動テスト

* `main` ブランチへのプッシュで自動テスト実行
* ワークフロー定義: `.github/workflows/claude.yml`
* 依存関係のインストールとテストを自動化
* コード品質チェック（Lint・フォーマッタ）実行

### Claude AI 連携

* Issue コメントに `@claude` で自動コード生成
* Pull Request レビューに `@claude` で支援
* 設定ファイル: `.claude/claude.yml`

### Codex TDD 連携

* タイトルに `@codex` を含む Issue で TDD ワークフロー起動
* ワークフロー定義: `.github/workflows/codex-tdd.yml`
* 品質チェック付き自動コード生成

## Gemini Search 連携

### 概要

`gemini` は Google Gemini CLI で、ウェブ検索を提供します。**組み込みの Web\_Search ツールではなく、必ず本コマンドを使用してください。**

### 使い方

Task Tool から次の形式で実行します。

```bash
gemini --prompt 'WebSearch: <query>'
```

### 例

```bash
# 開発トレンド検索
gemini --prompt "WebSearch: latest Python development trends 2024"

# ベストプラクティス検索
gemini --prompt "WebSearch: GitHub Actions best practices"

# API ドキュメント検索
gemini --prompt "WebSearch: OpenAI API documentation"
```

### 重要事項

* **必ず `gemini --prompt` を使用**
* **クエリは `WebSearch: ` で始める**
* **Task Tool で実行**
* **具体的で詳細なクエリを提供**

### 開発ワークフローへの統合

* 新技術や API のリサーチ
* 最新ツール・ライブラリの検索
* 技術的課題の解決策を調査
* コード最適化のベストプラクティスを検索
* 参考プロジェクト・サンプルを検索

## 設定ファイル

### VS Code / Cursor 設定

* `.cursor/rules/cursorrules.md` に AI 主導開発ガイドライン
* ファイル構成ルールとベストプラクティスを定義

### Docker 設定

* `Dockerfile` : 開発環境セットアップ
* `docker-compose.yml` : コンテナ全体構成

## AI アシスタント設定

### `.claude/claude.yml`

* プロジェクト構造理解のためのシステムプロンプト
* 使用ツールと実行パラメータを定義
* コンテキストに応じた支援を実現

### `.cursor/rules/cursorrules.md`

* AI ツールを用いた開発ガイドライン
* ファイル構成ルールとベストプラクティスを定義

## ベストプラクティス

### 言語別考慮事項

* **Python**: 仮想環境とパッケージ管理を適切に扱う
* **JavaScript/Node.js**: 適切なパッケージマネージャ・ロックファイルを使用
* **Java**: Maven/Gradle 規約と依存管理を遵守
* **Go**: モジュール管理と vendor 依存を適切に扱う

### ファイル命名

* 説明的かつ小文字の名前を使用
* 単語区切りはアンダースコアまたはハイフン
* 簡潔ながら内容がわかる名前
* 言語固有の規約に従う

### コードスタイル

* 一貫したインデント・フォーマット
* 関連する関数／クラスをまとめる
* 適切なコメント・ドキュメントを追加
* 言語別スタイルガイドを遵守

### セキュリティベストプラクティス

* 機密情報をコミットしない
* 設定は環境変数で管理
* 適切な入力バリデーション
* OWASP ガイドラインを遵守
* 定期的なセキュリティ監査と更新

### パフォーマンスベストプラクティス

* プロファイルしてボトルネック特定
* 適切なデータ構造・アルゴリズムを選択
* キャッシュを必要に応じて導入
* データベースクエリを最適化
* リソース使用状況を監視

## 開発ワークフロー

### 1. 機能開発

* main からフィーチャーブランチを作成
* テスト付きで実装
* ローカルで品質チェック
* プルリクエスト作成
* コードレビュー
* main へマージ

### 2. テスト戦略

* 実装前にテストを書く（TDD）
* 高いテストカバレッジを維持
* 適切なテストフレームワークを使用
* CI/CD で継続的テスト

### 3. コードレビュー

* 機能を確認
* セキュリティをチェック
* パフォーマンス影響を確認
* ドキュメント更新を確認
* テストカバレッジを検証

### 4. デプロイメント

* 自動デプロイパイプラインを使用
* ブルーグリーンデプロイを実施
* アプリケーションヘルスを監視
* ロールバック手順を用意
* 環境別設定を管理