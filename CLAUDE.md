# CLAUDE.md

## 概要

本ドキュメントは、AI駆動コーディングプロジェクトにおける Claude AI アシスタントの設定・活用方法を整理したものです。
GitHub Actions による CI/CD と Claude AI アシスタントを組み合わせることで、効率的な開発とコード品質の向上を図ります。

---

## ⚠️ 重要な注意事項

### 環境チェックの実行
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

### 仮想環境の管理
- **Pythonプロジェクト**: `conda activate py-review` または適切な仮想環境
- **Node.jsプロジェクト**: `npm install` で依存関係をインストール
- **環境変数**: APIキーは `.env` ファイルで管理

---

## 設定ファイルの役割と責務

### .github/workflows/claude.yml：GitHub Actions の設定

#### 目的

- プロジェクトのテストを自動化
- 依存関係のインストールと検証
- Claude AI アシスタントの統合
- コード品質チェック（linting, formatting）の実行

#### 変更が必要となるタイミング

- 依存関係の変更
- 新しい機能の追加
- テスト条件やトリガーの変更
- コード品質標準の更新

---

### .claude/claude.yml：Claude AI アシスタントの設定

#### 目的

- Claude セッション中に適用されるルールの定義（system_prompt）
- プロジェクト構造の理解を支援
- 使用可能なコマンド（allowed_tools）の制限
- パフォーマンス最適化と品質保証のガイドライン

#### 変更が必要となるタイミング

- ディレクトリ構造やファイル配置ルールの変更
- 使用ツールや応答テンプレートの更新
- Claude の動作チューニング
- 新しい機能やベストプラクティスの追加

---

## プロジェクト構造ガイドライン

### ソースコードファイル

- メインソースコード: `src/` または `app/` ディレクトリ
- 設定ファイル: `config/` ディレクトリ
- スクリプト: `scripts/` ディレクトリ
- ドキュメント: `docs/` ディレクトリ
- ユーティリティ: `utility/` ディレクトリ

### テストファイル

- すべて `tests/` ディレクトリに保存すること
- 単体テスト: `tests/unit/`
- 統合テスト: `tests/integration/`
- テストデータ: `tests/fixtures/`

### 設定ファイル

- アプリケーション設定: `config/` ディレクトリ
- 環境変数: `.env`（機密情報用）
- Docker設定: `Dockerfile`, `docker-compose.yml`

---

## 開発プロセスガイドライン

### 1. 環境チェック（必須）

```bash
# 1. 仮想環境のアクティベート
conda activate py-review  # または適切な環境名

# 2. 環境チェックスクリプトの実行
python utility/check_env.py

# 3. 依存関係のインストール（必要に応じて）
pip install -r requirements.txt
```

### 2. テスト駆動開発（TDD）

#### 基本サイクル

```bash
# 1. Red: 失敗するテストを書く
# 2. Green: テストを通す最小限のコードを書く
# 3. Refactor: コードを改善する
```

#### 実装例

```python
# 1. Red: 失敗するテスト
def test_calculate_total():
    calculator = Calculator()
    result = calculator.add(2, 3)
    assert result == 5

# 2. Green: 最小限の実装
class Calculator:
    def add(self, a, b):
        return a + b

# 3. Refactor: 改善
class Calculator:
    def add(self, a: int, b: int) -> int:
        """Add two numbers"""
        return a + b
```

### 3. 継続的リファクタリング

- 小さな変更を頻繁に行う
- テストが通ることを確認
- 意味のある名前を使用
- 重複を除去する

---

## コード記述規約

### 言語別の考慮事項

- **Python**: PEP 8ガイドライン、型ヒント、docstring
- **JavaScript**: ESLint、Prettier、JSDoc
- **TypeScript**: 型定義、ESLint、Prettier
- **Java**: Checkstyle、JUnit、JavaDoc

### コードスタイル

- 一貫したインデント（言語に応じて）
- 関連するメソッド/関数のグループ化
- 適切なコメント/docstring
- 言語固有のコーディング規約に従う
- 型ヒントの使用（可能な場合）

### エラーハンドリング

- 適切な例外処理の実装
- ログ出力の追加
- リトライ機能の実装
- ユーザーフレンドリーなエラーメッセージ

### テスト戦略

- 単体テストの作成
- 統合テストの実装
- モックオブジェクトの活用
- CI/CDパイプラインでの自動テスト

---

## Claude AI アシスタントによる支援

### 機能開発

- 新しい機能の実装
- 既存機能の改善・修正
- エラーハンドリングの実装
- パフォーマンス最適化

### 設定管理

- 設定ファイルの作成・更新
- 環境変数の設定
- 依存関係の管理

### ベストプラクティス

- 開発効率化に関するアドバイス
- アルゴリズムの改善
- 一貫したコードスタイルの維持
- セキュリティベストプラクティスの実装

### パフォーマンス最適化

- 効率的なアルゴリズムの選択
- キャッシュ機能の追加
- メモリ使用量の最適化
- 不要な処理の削減

---

## Gemini Search の使用方法

### 概要

`gemini` は Google Gemini CLI ツールで、ウェブ検索機能を提供します。**ウェブ検索が必要な場合、組み込みの `Web_Search` ツールの代わりにこのコマンドを使用する必要があります。**

### 使用方法

ウェブ検索は Task Tool 経由で `gemini --prompt` コマンドを使用して実行します：

```bash
gemini --prompt 'WebSearch: <query>'
```

### 実行例

```bash
# 最新の開発トレンドを検索
gemini --prompt "WebSearch: latest Python development trends 2024"

# ベストプラクティスを検索
gemini --prompt "WebSearch: GitHub Actions best practices"

# APIドキュメントを検索
gemini --prompt "WebSearch: OpenAI API documentation"

# 自動化技術を検索
gemini --prompt "WebSearch: Selenium web automation best practices"

# プロジェクトテンプレートを検索
gemini --prompt "WebSearch: AI-driven coding templates"
```

### 重要な注意事項

- **常に `gemini --prompt` を使用し、組み込みのWeb_Searchツールは使用しない**
- **クエリの前に "WebSearch: " を付ける**
- **Task Toolを使用してコマンドを実行する**
- **具体的で詳細な検索クエリを提供してより良い結果を得る**

### 開発ワークフローとの統合

- 新しい技術やAPIの調査にGemini Searchを使用
- 最新の開発ツールやライブラリの検索
- 技術的な問題やエラーの解決策を検索
- コード最適化のベストプラクティスを調査
- プロジェクトの参考資料や例を検索
