# Gemini Search Command

## 概要

このファイルは、Claude AI アシスタントで Gemini CLI ツールを使用したウェブ検索機能の設定を定義しています。
最新の技術情報やドキュメントを効率的に検索するためのガイドラインです。

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

## まとめ

Gemini CLI ツールは、AI駆動コーディングプロジェクトにおいて非常に強力なツールです。
適切な環境チェックとベストプラクティスに従うことで、効率的な開発と高品質なコードの実現が可能になります。

**重要なポイント:**
1. **環境チェックの徹底**: コード実行前に必ず `python utility/check_env.py` を実行
2. **具体的な検索クエリ**: 詳細で具体的なクエリでより良い結果を得る
3. **最新情報の活用**: 年号を含めて最新の情報を取得
4. **セキュリティの確保**: API キーと機密情報の適切な管理
5. **継続的な学習**: 定期的な情報更新とベストプラクティスの習得