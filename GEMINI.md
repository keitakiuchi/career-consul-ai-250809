# Gemini ワークスペース設定

このファイルは、AI 主導のコーディング プロジェクトにおけるプロジェクト構造と規約を Gemini が理解できるようにするものです。

## プロジェクト概要

本プロジェクトは AI 主導のコーディングおよび開発のためのテンプレートです。さまざまな AI ツールの設定、開発ワークフロー、そして現代的なソフトウェア開発のベストプラクティスが含まれております。

## 主要ディレクトリ

* `src/` または `app/`：メインのアプリケーションソースコード
* `tests/`：テストファイルおよびテスト設定
* `config/`：各種設定ファイル
* `docs/`：プロジェクトドキュメント
* `scripts/`：ユーティリティスクリプト・自動化ツール
* `workbench/`：実験用コードおよび調査用フォルダ
* `plan/`：プロジェクト計画・ロードマップ文書

## 規約

* プロジェクトに適したプログラミング言語（Python、JavaScript、TypeScript、Java など）を使用
* 言語ごとのスタイルガイドとベストプラクティスを遵守
* 最新の開発ツール・フレームワークを活用
* 包括的なテスト戦略を実装

## 開発手法とベストプラクティス

### テスト駆動開発 (TDD)

**twada 氏推奨のアプローチ**に従います。

#### TDD 基本サイクル

1. **Red**：失敗するテストを書く
2. **Green**：テストを通す最小限のコードを書く
3. **Refactor**：重複排除や可読性向上のためにリファクタリング

#### twada 氏の TDD の特徴

* **テストファースト**：常にテストを先に書く
* **小さなステップ**：小さな変更を積み重ねる
* **意図の明確化**：テストで意図を明瞭に表現
* **継続的リファクタリング**：常にコード改善を意識

#### 実装例

```python
# 1. Red: 失敗するテストを書く
def test_calculator_add_returns_sum():
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
        """2 つの整数を足し算する"""
        return a + b
```

### リファクタリング

**Martin Fowler 氏のアプローチ**を参考にします。

#### リファクタリング原則

1. **小さなステップ**
2. **テスト駆動**
3. **意味のある名前**
4. **重複排除 (DRY)**
5. **単一責任の原則**

#### 推奨テクニック

* **メソッド抽出 (Extract Method)**
* **クラス抽出 (Extract Class)**
* **名前の変更 (Rename)**
* **メソッドの移動 (Move Method)**
* **条件分岐のポリモーフィズム化**

#### AI 主導開発向け例

```python
# リファクタリング前
def process_data(self, data_type, data):
    if data_type == "user":
        # ユーザ処理
        results = self.process_user_data(data)
        self.save_to_database(results, "users")
    elif data_type == "product":
        # 商品処理
        results = self.process_product_data(data)
        self.save_to_database(results, "products")

# リファクタリング後
def process_data(self, data_type, data):
    processor = self.get_processor(data_type)
    results = processor.process(data)
    processor.save(results)

class UserDataProcessor:
    def process(self, data):
        return self.process_user_data(data)
    
    def save(self, results):
        return self.save_to_database(results, "users")
```

### コミット管理

#### コミットのタイミング

* **機能単位**：機能が完了したらコミット
* **テスト単位**：テストが通ったらコミット
* **リファクタ単位**：リファクタ完了時にコミット
* **バグ修正単位**：バグ修正完了時にコミット

#### コミットメッセージ規約

```
<type>(<scope>): <description>

<body>

<footer>
```

* **type**：feat, fix, docs, style, refactor, test, chore
* **scope**：影響範囲 (src, tests, config など)
* **description**：簡潔な変更内容

##### 例

```
feat(src): add user authentication service

- UserAuthService クラスの login/logout 実装
- 認証失敗時のエラーハンドリング追加
- 認証機能のユニットテストを含む

Closes #123
```

### 計画管理

**plan フォルダ**で計画内容と進捗を管理します。

#### 構成例

```
plan/
├── roadmap.md              # 全体ロードマップ
├── current-sprint.md       # 今スプリントの計画
├── completed-tasks.md      # 完了タスク一覧
├── technical-debt.md       # 技術的負債管理
└── milestones/             # マイルストーンごとの計画
    ├── v1.0.0.md
    ├── v1.1.0.md
    └── v2.0.0.md
```

#### 管理ルール

* **定期更新**：週次で進捗を更新
* **明確な目標**：各タスクに完了基準を設定
* **優先順位付け**：タスクに優先度を設定
* **見積もり**：作業量を見積もる

##### 例

```markdown
# plan/current-sprint.md

## 今スプリントの目標
- ユーザ認証システムの完成
- API 連携の実装開始
- エラーハンドリング機能の改善

## タスクリスト
- [ ] 認証エラー処理の改善
- [ ] API クライアントの基本実装
- [ ] データベースクエリの最適化
- [ ] テストカバレッジ向上

## 完了基準
- すべてのタスクが完了
- テストカバレッジ 80％ 以上
- コードレビュー完了
```

### 実験的実行

**workbench フォルダ**で実験用スクリプトと結果を管理します。

#### 構成例

```
workbench/
├── scripts/                # 実験スクリプト
│   ├── test_new_feature.py
│   ├── experiment_ai_integration.py
│   └── benchmark_performance.py
├── results/                # 実行結果
│   ├── test_outputs/
│   ├── performance_logs/
│   └── error_logs/
├── data/                   # 実験データ
│   ├── sample_data.json
│   └── test_config.yaml
└── README.md               # ワークベンチ利用ガイド
```

#### 実行ルール

* **分離**：本番コードと実験コードを明確に分離
* **記録**：常に結果・ログを保存
* **再現性**：再現可能な形で記録
* **クリーンアップ**：不要ファイルは削除

#### スクリプト命名

```
test_<feature>_<purpose>.py
experiment_<content>_<date>.py
benchmark_<target>_<condition>.py
```

##### 例

```python
# workbench/scripts/test_ai_integration.py
import time
import requests
import json
from datetime import datetime

def test_ai_api_integration():
    """AI API 連携のパフォーマンスをテスト"""
    start_time = datetime.now()
    results = []
    
    for i in range(10):
        try:
            # AI サービスへの API コール
            response = requests.post("https://api.openai.com/v1/chat/completions")
            results.append({
                'request': i,
                'status': response.status_code,
                'timestamp': datetime.now()
            })
            time.sleep(0.1)  # レート制限
        except Exception as e:
            results.append({
                'request': i,
                'error': str(e),
                'timestamp': datetime.now()
            })
    
    # 結果を保存
    with open('workbench/results/ai_integration_test.json', 'w') as f:
        json.dump(results, f, default=str)

if __name__ == "__main__":
    test_ai_api_integration()
```

## AI ツール統合

### Claude AI Assistant

* Issue や Pull Request で `@claude` を使用して自動支援
* プロジェクト固有の動作は `.claude/claude.yml` で設定
* GitHub Actions と連携して CI/CD 自動化

### Codex TDD ワークフロー

* Issue タイトルで `@codex` を利用し TDD を推進
* 品質チェック付きの自動コード生成
* すべての新機能で TDD 原則を遵守

### Gemini Search

* `gemini --prompt 'WebSearch: <query>'` でウェブ検索
* 新技術・ベストプラクティスのリサーチ
* 技術的課題の解決策を探索

## ベストプラクティス

### コード品質

* 言語別スタイルガイド遵守
* 包括的なテスト実装
* 静的解析ツール使用
* 高いテストカバレッジ維持

### セキュリティ

* 機密情報をコミットしない
* 環境変数で設定を管理
* 適切な入力バリデーション
* セキュリティベストプラクティス遵守

### パフォーマンス

* プロファイリングでボトルネック特定
* 適切なデータ構造を選択
* 必要に応じてキャッシュを活用
* リソース使用状況を監視

### ドキュメンテーション

* README を最新状態に保つ
* API エンドポイントをドキュメント化
* インラインコードコメントを維持
* ユーザーガイド・チュートリアルを作成

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

## Gemini CLI ツールの概要

### 目的
- **ウェブ検索機能**: 最新の技術情報やドキュメントの検索
- **コード生成支援**: AI駆動でのコード生成と改善
- **開発効率化**: 開発プロセスの自動化と最適化

### 特徴
- **リアルタイム検索**: 最新の情報にアクセス
- **多言語対応**: 様々なプログラミング言語をサポート
- **コンテキスト理解**: プロジェクトの文脈を理解した提案
- **統合開発**: 他のAIツールとの連携

## 使用方法

### 基本的な検索コマンド

```bash
# 基本的な検索
gemini --prompt "WebSearch: <検索クエリ>"

# 技術的な検索例
gemini --prompt "WebSearch: Python async programming best practices 2024"
gemini --prompt "WebSearch: React hooks performance optimization"
gemini --prompt "WebSearch: Docker containerization best practices"
```

### 開発関連の検索例

#### 1. 技術トレンドの調査
```bash
# 最新の開発トレンド
gemini --prompt "WebSearch: latest Python development trends 2024"
gemini --prompt "WebSearch: JavaScript framework comparison 2024"
gemini --prompt "WebSearch: cloud computing trends 2024"
```

#### 2. ベストプラクティスの検索
```bash
# コーディング規約
gemini --prompt "WebSearch: Python PEP 8 style guide"
gemini --prompt "WebSearch: JavaScript ES6+ best practices"
gemini --prompt "WebSearch: Git workflow best practices"
```

#### 3. API・ライブラリの調査
```bash
# APIドキュメント
gemini --prompt "WebSearch: OpenAI API documentation"
gemini --prompt "WebSearch: FastAPI tutorial examples"
gemini --prompt "WebSearch: React hooks documentation"
```

#### 4. 問題解決の検索
```bash
# エラー解決
gemini --prompt "WebSearch: Python ModuleNotFoundError solutions"
gemini --prompt "WebSearch: JavaScript CORS error handling"
gemini --prompt "WebSearch: Docker build failed troubleshooting"
```

#### 5. 自動化技術の調査
```bash
# テスト自動化
gemini --prompt "WebSearch: Selenium web automation best practices"
gemini --prompt "WebSearch: pytest testing framework examples"
gemini --prompt "WebSearch: GitHub Actions CI/CD examples"
```

## 開発ワークフローとの統合

### 1. プロジェクト初期化時

```bash
# プロジェクトテンプレートの検索
gemini --prompt "WebSearch: Python project structure best practices"
gemini --prompt "WebSearch: React project setup guide 2024"
gemini --prompt "WebSearch: microservices architecture patterns"
```

### 2. 新機能開発時

```bash
# 技術選定
gemini --prompt "WebSearch: Python web framework comparison 2024"
gemini --prompt "WebSearch: database ORM comparison Python"
gemini --prompt "WebSearch: authentication libraries Python"
```

### 3. パフォーマンス最適化時

```bash
# 最適化手法
gemini --prompt "WebSearch: Python performance optimization techniques"
gemini --prompt "WebSearch: React performance optimization 2024"
gemini --prompt "WebSearch: database query optimization strategies"
```

### 4. セキュリティ強化時

```bash
# セキュリティベストプラクティス
gemini --prompt "WebSearch: web application security best practices 2024"
gemini --prompt "WebSearch: API security authentication methods"
gemini --prompt "WebSearch: OWASP top 10 2024"
```

## 検索クエリの最適化

### 効果的なクエリ作成のコツ

#### 1. 具体的で詳細なクエリ
```bash
# 良い例
gemini --prompt "WebSearch: Python async programming with asyncio examples 2024"

# 悪い例
gemini --prompt "WebSearch: Python async"
```

#### 2. 年号を含める
```bash
# 最新情報を取得
gemini --prompt "WebSearch: React hooks best practices 2024"
gemini --prompt "WebSearch: Python type hints tutorial 2024"
```

#### 3. 特定の技術スタックを指定
```bash
# 具体的な技術を指定
gemini --prompt "WebSearch: FastAPI with PostgreSQL integration examples"
gemini --prompt "WebSearch: React with TypeScript setup guide"
```

#### 4. 問題解決に特化
```bash
# エラー解決に特化
gemini --prompt "WebSearch: Python ModuleNotFoundError virtual environment solutions"
gemini --prompt "WebSearch: Docker permission denied error solutions"
```

## 環境チェックとセットアップ

### 1. 環境チェック（必須）

```bash
# 1. 仮想環境のアクティベート
conda activate py-review  # または適切な環境名

# 2. 環境チェックスクリプトの実行
python utility/check_env.py

# 3. 依存関係のインストール（必要に応じて）
pip install -r requirements.txt
```

### 2. Gemini CLI の設定

```bash
# Gemini CLI のインストール確認
gemini --version

# API キーの設定
export GEMINI_API_KEY="your-api-key-here"

# 設定の確認
gemini --help
```

### 3. 統合テスト

```bash
# 基本的な検索テスト
gemini --prompt "WebSearch: Python programming"

# 結果の確認
echo "検索結果を確認してください"
```

## ベストプラクティス

### 1. 検索戦略

#### 段階的な検索
```bash
# 1. 概要を把握
gemini --prompt "WebSearch: Python async programming overview"

# 2. 詳細を調査
gemini --prompt "WebSearch: Python asyncio detailed tutorial"

# 3. 実装例を検索
gemini --prompt "WebSearch: Python async web server examples"
```

#### 複数視点からの検索
```bash
# 異なる観点から検索
gemini --prompt "WebSearch: Python async programming benefits"
gemini --prompt "WebSearch: Python async programming challenges"
gemini --prompt "WebSearch: Python async vs threading comparison"
```

### 2. 情報の整理

#### 検索結果の記録
- 重要な情報をメモに記録
- 参考URLをブックマーク
- コード例を保存

#### 情報の検証
- 複数のソースで情報を確認
- 公式ドキュメントを優先
- 最新の情報を確認

### 3. 開発効率化

#### 定期的な情報更新
```bash
# 週次での技術トレンド確認
gemini --prompt "WebSearch: Python development trends this week"
gemini --prompt "WebSearch: JavaScript ecosystem updates"
```

#### プロジェクト固有の検索
```bash
# プロジェクトに関連する検索
gemini --prompt "WebSearch: <プロジェクト名> best practices"
gemini --prompt "WebSearch: <使用技術> integration examples"
```

## トラブルシューティング

### よくある問題と解決方法

#### 1. 検索結果が不適切な場合
```bash
# クエリをより具体的にする
gemini --prompt "WebSearch: Python async programming with asyncio library examples 2024"

# 年号を追加
gemini --prompt "WebSearch: React hooks tutorial 2024"
```

#### 2. API エラーが発生する場合
```bash
# API キーの確認
echo $GEMINI_API_KEY

# 環境変数の再設定
export GEMINI_API_KEY="your-api-key-here"
```

#### 3. 検索結果が古い場合
```bash
# 年号を明示的に指定
gemini --prompt "WebSearch: Python async programming 2024"

# 最新のキーワードを追加
gemini --prompt "WebSearch: Python async programming latest updates"
```

## セキュリティとプライバシー

### 1. API キーの管理

```bash
# 環境変数での管理（推奨）
export GEMINI_API_KEY="your-api-key-here"

# .env ファイルでの管理
echo "GEMINI_API_KEY=your-api-key-here" >> .env
```

### 2. 機密情報の保護

- API キーをGitにコミットしない
- 環境変数で機密情報を管理
- 定期的にAPI キーを更新

### 3. 検索履歴の管理

- 機密情報を含む検索を避ける
- 検索履歴を定期的にクリア
- プライバシー設定を確認

## 今後の拡張予定

### 1. 機能拡張

- **多言語検索**: 日本語での検索対応
- **コード生成**: 検索結果に基づくコード生成
- **統合開発**: 他のAIツールとの連携強化

### 2. パフォーマンス改善

- **検索速度**: 高速化とキャッシュ機能
- **結果精度**: より関連性の高い結果の提供
- **ユーザビリティ**: 使いやすいインターフェース

### 3. 開発者体験の向上

- **自動化**: 開発プロセスの自動化
- **テンプレート**: よく使う検索パターンのテンプレート化
- **学習機能**: 使用パターンに基づく提案機能

## まとめ

Gemini CLI ツールは、AI駆動コーディングプロジェクトにおいて非常に強力なツールです。
適切な環境チェックとベストプラクティスに従うことで、効率的な開発と高品質なコードの実現が可能になります。

**重要なポイント:**
1. **環境チェックの徹底**: コード実行前に必ず `python utility/check_env.py` を実行
2. **具体的な検索クエリ**: 詳細で具体的なクエリでより良い結果を得る
3. **最新情報の活用**: 年号を含めて最新の情報を取得
4. **セキュリティの確保**: API キーと機密情報の適切な管理
5. **継続的な学習**: 定期的な情報更新とベストプラクティスの習得