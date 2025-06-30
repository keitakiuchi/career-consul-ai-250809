# キャリアコンサルティングセミナー準備リポジトリ

このリポジトリは、キャリアコンサルティングに関するセミナーの準備と資料管理のためのプロジェクトです。AIツールを活用して効率的にセミナー資料を作成し、管理するためのテンプレートとルールを提供します。

## 🎯 目的

- **セミナー資料の効率的な作成**: AIツールを活用した資料作成の自動化
- **一貫性のあるコンテンツ**: 複数のセミナーで統一された品質の資料を提供
- **知識の蓄積と共有**: キャリアコンサルティングの知見を体系的に管理
- **参加者体験の向上**: インタラクティブで価値のあるセミナーコンテンツの提供

## 🚀 クイックスタート

### 1. リポジトリのクローン
```bash
git clone https://github.com/your-username/career-consulting-seminar.git
cd career-consulting-seminar
```

### 2. 環境チェック（必須）
```bash
# 仮想環境のアクティベート
conda activate career-seminar  # または適切な環境名

# 環境チェックスクリプトの実行
python utility/check_env.py
```

### 3. 依存関係のインストール
```bash
pip install -r requirements.txt
```

## 📁 プロジェクト構造

```
career-consulting-seminar/
├── .claude/                    # Claude Code CLI設定
│   ├── commands/
│   │   └── career-research.md
│   └── claude.yml
├── .cursor/                    # Cursor設定
│   └── rules/
│       └── cursorrules.md
├── .github/                    # GitHub Actions設定
│   └── workflows/
│       ├── claude.yml
│       └── content-generation.yml
├── utility/                    # ユーティリティツール
│   └── check_env.py           # 環境チェックスクリプト
├── sharing/                    # 共有ツール
│   └── career-content-generator.py    # コンテンツ生成スクリプト
├── seminars/                   # セミナー資料
│   ├── templates/             # セミナーテンプレート
│   ├── materials/             # セミナー資料
│   └── exercises/             # 演習・ワークシート
├── research/                   # リサーチ資料
│   ├── industry-trends/       # 業界動向
│   ├── case-studies/          # 事例研究
│   └── best-practices/        # ベストプラクティス
├── tools/                      # セミナー用ツール
│   ├── assessment-tools/      # アセスメントツール
│   └── interactive-tools/     # インタラクティブツール
├── CLAUDE.md                   # Claude使用ガイド
├── GEMINI.md                   # Gemini使用ガイド
├── AGENTS.md                   # AIエージェント使用ガイド
├── career-consulting-rules.md  # 集約されたルールファイル
├── requirements.txt            # Python依存関係
└── README.md                   # このファイル
```

## ⚠️ 重要な注意事項

### 環境チェックの実行
**このプロジェクトでコンテンツを生成する前に、必ず環境チェックスクリプトを実行してください：**

```bash
python utility/check_env.py
```

このスクリプトは以下を確認します：
- ✅ 適切な仮想環境がアクティブか
- ✅ 必要な依存関係がインストールされているか
- ✅ 設定ファイルが存在するか

### 仮想環境の管理
- **Pythonプロジェクト**: `conda activate career-seminar` または適切な仮想環境
- **Node.jsプロジェクト**: `npm install` で依存関係をインストール
- **環境変数**: APIキーは `.env` ファイルで管理

## 📋 セミナーコンテンツ構成

### セミナーテンプレート
- `seminars/templates/` - 各種セミナーのテンプレート
- `seminars/materials/` - 実際のセミナー資料
- `seminars/exercises/` - 参加者用演習・ワークシート

### リサーチ資料
- `research/industry-trends/` - 業界動向・市場分析
- `research/case-studies/` - 成功事例・失敗事例
- `research/best-practices/` - キャリアコンサルティングのベストプラクティス

### ツール類
- `tools/assessment-tools/` - キャリアアセスメントツール
- `tools/interactive-tools/` - インタラクティブなセミナー用ツール

## 🔄 コンテンツ生成機能

### career-content-generator.py

`sharing/career-content-generator.py`を使用することで、AIを活用してセミナーコンテンツを効率的に生成できます。

```bash
# セミナーコンテンツの生成
python sharing/career-content-generator.py

# 特定のテーマでコンテンツ生成
python sharing/career-content-generator.py --theme "キャリア転換"
```

### 使用方法

1. **コンテンツの生成**:
   ```bash
   cd sharing
   python3 career-content-generator.py
   ```

2. **テーマ別コンテンツ生成**:
   ```bash
   python3 career-content-generator.py --theme "リーダーシップ開発"
   python3 career-content-generator.py --theme "ワークライフバランス"
   ```

## 🛠️ 各AIツールの設定

### Claude Code CLI
- `.claude/claude.yml`でシステムプロンプトとツール設定
- `.claude/commands/career-research.md`でキャリアリサーチ機能
- `CLAUDE.md`で詳細な使用方法

### Cursor
- `.cursor/rules/cursorrules.md`でセミナー資料作成ルールとベストプラクティス
- キャリアコンサルティング固有のコンテンツ作成規約を定義

### GitHub Actions
- `.github/workflows/claude.yml`でCI/CD自動化
- `.github/workflows/content-generation.yml`でコンテンツ生成ワークフロー

### Gemini CLI
- `GEMINI.md`でGemini使用ガイドライン
- キャリアリサーチとコンテンツ生成のベストプラクティス

## 🔧 カスタマイズ

### 新しいセミナーテーマの追加
1. `seminars/templates/`に新しいテンプレートを配置
2. `sharing/career-content-generator.py`を更新して新しいテーマを含める
3. 関連するリサーチ資料を`research/`に追加

### プロジェクト固有の設定
- 各ルールファイルをセミナーの要件に合わせてカスタマイズ
- 環境変数やAPIキーの設定を適切に管理

## 📚 ベストプラクティス

### セミナーコンテンツ作成
- **参加者中心の設計**: 参加者のニーズに基づいたコンテンツ
- **インタラクティブ要素**: 演習・ワークショップの組み込み
- **実践的な内容**: 理論と実践のバランス
- **継続的な改善**: フィードバックに基づくコンテンツ更新

### コンテンツ管理
- **一貫性の維持**: 複数セミナーで統一された品質
- **定期的な更新**: 最新のキャリアトレンドを反映
- **バージョン管理**: コンテンツの変更履歴を追跡

### 環境管理
- **環境チェックの徹底**: コンテンツ生成前に必ず`utility/check_env.py`を実行
- **仮想環境の適切な管理**: プロジェクト固有の環境を使用
- **依存関係の管理**: requirements.txtの定期的な更新

## 🤝 貢献

1. このリポジトリをフォーク
2. 新しいセミナーテーマや改善を提案
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

**注意**: このテンプレートを使用する際は、セミナーの要件に合わせてコンテンツをカスタマイズしてください。また、コンテンツ生成前に必ず環境チェックスクリプトを実行してください。






