# Template Vibe Coding - AI駆動コーディングテンプレート

このリポジトリは、vibe-codingやai-driven-codingを始めるためのテンプレートレポジトリです。最新の知見に基づいて汎用的なルールファイルを貯蔵し、他のプロジェクトで再利用できるように設計されています。

## 🎯 目的

- **AI駆動コーディングの標準化**: 様々なAIツール向けのルールファイルを一元管理
- **プロジェクト間の一貫性**: 複数のプロジェクトで同じルールセットを共有
- **効率的な開発**: ルールファイルの自動集約と更新機能

## 🚀 クイックスタート

### 1. リポジトリのクローン
```bash
git clone https://github.com/your-username/template-vibe-coding.git
cd template-vibe-coding
```

### 2. 環境チェック（必須）
```bash
# 仮想環境のアクティベート
conda activate py-review  # または適切な環境名

# 環境チェックスクリプトの実行
python utility/check_env.py
```

### 3. 依存関係のインストール
```bash
pip install -r requirements.txt
```

## 📁 プロジェクト構造

```
template-vibe-coding/
├── .claude/                    # Claude Code CLI設定
│   ├── commands/
│   │   └── gemini-search.md
│   └── claude.yml
├── .cursor/                    # Cursor設定
│   └── rules/
│       └── cursorrules.md
├── .github/                    # GitHub Actions設定
│   └── workflows/
│       ├── claude.yml
│       └── codex-tdd.yml
├── utility/                    # ユーティリティツール
│   └── check_env.py           # 環境チェックスクリプト
├── sharing/                    # 共有ツール
│   └── ai-driven-coding.py    # ルールファイル集約スクリプト
├── workbench/                  # 実験用ワークスペース
├── plan/                       # プロジェクト計画
├── results/                    # 実行結果
├── CLAUDE.md                   # Claude使用ガイド
├── GEMINI.md                   # Gemini使用ガイド
├── AGENTS.md                   # AIエージェント使用ガイド
├── ai-driven-coding.md         # 集約されたルールファイル
├── requirements.txt            # Python依存関係
└── README.md                   # このファイル
```

## ⚠️ 重要な注意事項

### 環境チェックの実行
**このプロジェクトでコードを実行する前に、必ず環境チェックスクリプトを実行してください：**

```bash
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

## 📋 ルールファイル構成

### Claude Code CLI用
- `.claude/commands/gemini-search.md` - Gemini検索コマンド設定
- `.claude/claude.yml` - Claude AIアシスタント設定
- `CLAUDE.md` - Claude使用ガイドライン

### Claude Code GitHub Actions用
- `.github/workflows/claude.yml` - GitHub Actions CI/CD設定

### OpenAI Codex用
- `.github/workflows/codex-tdd.yml` - TDDワークフロー設定
- `AGENTS.md` - AIエージェント使用ガイドライン

### Gemini CLI用
- `GEMINI.md` - Gemini使用ガイドライン

### Cursor用
- `.cursor/rules/cursorrules.md` - Cursor開発ルール

## 🔄 ルールファイル集約機能

### ai-driven-coding.py

`sharing/ai-driven-coding.py`を使用することで、このリポジトリのルールファイルを`ai-driven-coding.md`に集約し、他のリポジトリで参照できます。

```bash
# ルールファイルの集約
python sharing/ai-driven-coding.py

# 生成されたai-driven-coding.mdを他のプロジェクトで使用
```

### 使用方法

1. **ルールファイルの集約**:
   ```bash
   cd sharing
   python3 ai-driven-coding.py
   ```

2. **他のプロジェクトでの参照**:
   - 生成された`ai-driven-coding.md`を他のリポジトリにコピー
   - 各AIツールの設定ファイルで参照

## 🛠️ 各AIツールの設定

### Claude Code CLI
- `.claude/claude.yml`でシステムプロンプトとツール設定
- `.claude/commands/gemini-search.md`でGemini検索機能
- `CLAUDE.md`で詳細な使用方法

### Cursor
- `.cursor/rules/cursorrules.md`で開発ルールとベストプラクティス
- プロジェクト固有のコーディング規約を定義

### GitHub Actions
- `.github/workflows/claude.yml`でCI/CD自動化
- `.github/workflows/codex-tdd.yml`でTDDワークフロー

### Gemini CLI
- `GEMINI.md`でGemini使用ガイドライン
- ウェブ検索とコード生成のベストプラクティス

## 🔧 カスタマイズ

### 新しいルールファイルの追加
1. 適切なディレクトリにルールファイルを配置
2. `sharing/ai-driven-coding.py`を更新して新しいファイルを含める
3. ルールファイルを集約して`ai-driven-coding.md`を更新

### プロジェクト固有の設定
- 各ルールファイルをプロジェクトの要件に合わせてカスタマイズ
- 環境変数やAPIキーの設定を適切に管理

## 📚 ベストプラクティス

### AI駆動コーディング
- **テスト駆動開発**: TDDサイクルを徹底
- **継続的リファクタリング**: コードの品質を常に改善
- **適切なコミット管理**: 機能単位でのコミット
- **実験的実行**: workbenchディレクトリでの試行錯誤

### ルールファイル管理
- **一貫性の維持**: 複数プロジェクトで同じルールセットを使用
- **定期的な更新**: 最新のベストプラクティスを反映
- **バージョン管理**: ルールファイルの変更履歴を追跡

### 環境管理
- **環境チェックの徹底**: コード実行前に必ず`utility/check_env.py`を実行
- **仮想環境の適切な管理**: プロジェクト固有の環境を使用
- **依存関係の管理**: requirements.txtの定期的な更新

## 🤝 貢献

1. このリポジトリをフォーク
2. 新しいルールファイルや改善を提案
3. プルリクエストを作成
4. レビューとマージ

## 📄 ライセンス

このプロジェクトは既存のLICENSEファイルに従います。

## 🔗 関連リンク

- [Claude Code CLI](https://claude.ai/)
- [Cursor](https://cursor.sh/)
- [Gemini](https://gemini.google.com/)
- [GitHub Actions](https://github.com/features/actions)

---

**注意**: このテンプレートを使用する際は、プロジェクトの要件に合わせてルールファイルをカスタマイズしてください。また、コード実行前に必ず環境チェックスクリプトを実行してください。






