# Cursor Rules for Career Consulting Seminar Preparation

## 概要

このファイルは、Cursor IDE でのキャリアコンサルティングセミナー準備プロジェクトの開発ルールとベストプラクティスを定義しています。
効率的で高品質なセミナーコンテンツ作成を支援するためのガイドラインです。

---

## ⚠️ 重要な注意事項

### 環境チェックの実行
**このプロジェクトでコンテンツを生成する前に、必ず環境チェックスクリプトを実行してください：**

```bash
# 仮想環境のアクティベート
conda activate career-seminar  # または適切な環境名

# 環境チェックスクリプトの実行
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

---

## プロジェクト構造ガイドライン

### ディレクトリ構成

```
career-consulting-seminar/
├── seminars/                   # セミナー資料
│   ├── templates/             # セミナーテンプレート
│   │   ├── career-transition.md
│   │   ├── leadership-development.md
│   │   └── work-life-balance.md
│   ├── materials/             # セミナー資料
│   │   ├── presentations/     # プレゼンテーション資料
│   │   ├── handouts/          # 配布資料
│   │   └── scripts/           # セミナー台本
│   └── exercises/             # 演習・ワークシート
│       ├── self-assessment/   # 自己評価ツール
│       ├── group-activities/  # グループ活動
│       └── reflection/        # 振り返りシート
├── research/                   # リサーチ資料
│   ├── industry-trends/       # 業界動向
│   ├── case-studies/          # 事例研究
│   └── best-practices/        # ベストプラクティス
├── tools/                      # セミナー用ツール
│   ├── assessment-tools/      # アセスメントツール
│   └── interactive-tools/     # インタラクティブツール
├── utility/                    # ユーティリティツール
│   └── check_env.py           # 環境チェックスクリプト
├── sharing/                    # 共有ツール
│   └── career-content-generator.py    # コンテンツ生成スクリプト
├── requirements.txt            # Python依存関係
└── README.md                   # プロジェクト説明
```

### ファイル命名規則

- **セミナー資料**: ケバブケース（`career-transition-seminar.md`）
- **テンプレート**: ケバブケース（`leadership-development-template.md`）
- **演習**: スネークケース（`self_assessment_worksheet.py`）
- **設定ファイル**: ケバブケース（`seminar-config.yml`）

---

## セミナーコンテンツ作成プロセス

### 1. 環境チェック（必須）

```bash
# 1. 仮想環境のアクティベート
conda activate career-seminar  # または適切な環境名

# 2. 環境チェックスクリプトの実行
python utility/check_env.py

# 3. 依存関係のインストール（必要に応じて）
pip install -r requirements.txt
```

### 2. セミナーコンテンツ作成サイクル

#### 基本サイクル
1. **Research**: テーマに関するリサーチと情報収集
2. **Design**: 参加者ニーズに基づいたコンテンツ設計
3. **Create**: AIツールを活用したコンテンツ作成
4. **Review**: 品質チェックと改善

#### 実装例
```python
# 1. Research: テーマリサーチ
def research_career_trends(topic: str) -> Dict[str, any]:
    """キャリアトレンドのリサーチ"""
    # AIツールを使用して最新情報を収集
    pass

# 2. Design: コンテンツ設計
def design_seminar_content(target_audience: str, duration: int) -> Dict[str, any]:
    """セミナーコンテンツの設計"""
    # 参加者ニーズに基づいた設計
    pass

# 3. Create: コンテンツ作成
def generate_seminar_materials(template: str, theme: str) -> str:
    """セミナー資料の生成"""
    # AIツールを活用した資料作成
    pass

# 4. Review: 品質チェック
def review_content_quality(content: str) -> Dict[str, any]:
    """コンテンツ品質のチェック"""
    # 品質基準に基づく評価
    pass
```

### 3. 継続的改善

- 参加者フィードバックの収集と分析
- コンテンツの定期的な更新
- 最新トレンドの反映

---

## セミナーコンテンツ品質標準

### マークダウン形式

#### 構造化されたコンテンツ
```markdown
# キャリア転換セミナー

## 概要
- 対象者: キャリア転換を検討している方
- 時間: 90分
- 形式: オンライン/対面

## 学習目標
1. キャリア転換の現状理解
2. 自己分析の実施
3. 転換戦略の策定

## コンテンツ構成
### 1. イントロダクション (15分)
- アイスブレイク
- セミナーの目的説明

### 2. キャリア転換の現状 (20分)
- 業界動向
- 成功事例

### 3. 自己分析ワーク (30分)
- 強み・弱み分析
- 価値観の整理

### 4. 戦略策定 (20分)
- アクションプラン作成
- 次のステップ

### 5. まとめ (5分)
- 振り返り
- 質疑応答
```

#### インタラクティブ要素
```markdown
## 演習: 自己分析ワークシート

### ステップ1: 強みの分析
以下の質問に答えてください：

1. あなたが最も得意としていることは何ですか？
   - [ ] コミュニケーション
   - [ ] 問題解決
   - [ ] リーダーシップ
   - [ ] その他: _________

2. 周囲の人からよく褒められることは何ですか？
   _________________________________

### ステップ2: 価値観の整理
重要度を1-5で評価してください：

- 仕事の安定性: [1] [2] [3] [4] [5]
- 創造性の発揮: [1] [2] [3] [4] [5]
- 社会貢献: [1] [2] [3] [4] [5]
- 収入: [1] [2] [3] [4] [5]
```

### Pythonスクリプト

#### アセスメントツール
```python
from typing import Dict, List, Optional
import json
import datetime

class CareerAssessment:
    """キャリアアセスメントツール"""
    
    def __init__(self):
        self.questions = self._load_questions()
        self.results = {}
    
    def _load_questions(self) -> Dict[str, List[str]]:
        """アセスメント質問の読み込み"""
        return {
            "strengths": [
                "あなたの強みは何ですか？",
                "周囲から評価される能力は？",
                "自信を持ってできることは？"
            ],
            "values": [
                "仕事で最も重視することは？",
                "理想的な職場環境は？",
                "キャリアで達成したいことは？"
            ],
            "interests": [
                "興味のある業界は？",
                "好きな仕事の種類は？",
                "学びたいスキルは？"
            ]
        }
    
    def conduct_assessment(self, participant_id: str) -> Dict[str, any]:
        """アセスメントの実施"""
        results = {
            "participant_id": participant_id,
            "date": datetime.datetime.now().isoformat(),
            "answers": {},
            "analysis": {}
        }
        
        # 各カテゴリの質問に回答
        for category, questions in self.questions.items():
            results["answers"][category] = {}
            for question in questions:
                # 実際の実装では、ユーザー入力を受け取る
                results["answers"][category][question] = "サンプル回答"
        
        # 結果の分析
        results["analysis"] = self._analyze_results(results["answers"])
        
        return results
    
    def _analyze_results(self, answers: Dict[str, any]) -> Dict[str, any]:
        """回答結果の分析"""
        analysis = {
            "strength_areas": [],
            "value_priorities": [],
            "career_suggestions": []
        }
        
        # 分析ロジックの実装
        # 実際の実装では、より詳細な分析を行う
        
        return analysis
    
    def generate_report(self, assessment_results: Dict[str, any]) -> str:
        """アセスメントレポートの生成"""
        report = f"""
# キャリアアセスメントレポート

## 参加者情報
- ID: {assessment_results['participant_id']}
- 実施日: {assessment_results['date']}

## 分析結果

### 強みエリア
{chr(10).join(f"- {area}" for area in assessment_results['analysis']['strength_areas'])}

### 価値観の優先順位
{chr(10).join(f"- {priority}" for priority in assessment_results['analysis']['value_priorities'])}

### キャリア提案
{chr(10).join(f"- {suggestion}" for suggestion in assessment_results['analysis']['career_suggestions'])}

## 次のステップ
1. 強みを活かしたキャリアパスの検討
2. 価値観に合った職場環境の調査
3. 必要なスキルの習得計画の策定
        """
        
        return report
```

#### コンテンツ生成ツール
```python
import openai
from typing import Dict, List, Optional
import json

class SeminarContentGenerator:
    """セミナーコンテンツ生成ツール"""
    
    def __init__(self, api_key: str):
        openai.api_key = api_key
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict[str, str]:
        """セミナーテンプレートの読み込み"""
        return {
            "career_transition": """
# {title}

## 概要
- 対象者: {target_audience}
- 時間: {duration}分
- 形式: {format}

## 学習目標
{learning_objectives}

## コンテンツ構成
{content_structure}

## 演習・ワーク
{exercises}
            """,
            "leadership_development": """
# {title}

## 概要
- 対象者: {target_audience}
- 時間: {duration}分
- 形式: {format}

## 学習目標
{learning_objectives}

## コンテンツ構成
{content_structure}

## リーダーシップ演習
{leadership_exercises}
            """
        }
    
    def generate_seminar_content(self, 
                                theme: str, 
                                target_audience: str,
                                duration: int,
                                format_type: str = "オンライン") -> str:
        """セミナーコンテンツの生成"""
        
        # AIを使用してコンテンツを生成
        prompt = f"""
        キャリアコンサルティングセミナーのコンテンツを作成してください。
        
        テーマ: {theme}
        対象者: {target_audience}
        時間: {duration}分
        形式: {format_type}
        
        以下の要素を含めてください：
        1. 学習目標（3-5個）
        2. コンテンツ構成（時間配分付き）
        3. インタラクティブな演習・ワーク
        4. 実践的なアクションプラン
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "あなたは経験豊富なキャリアコンサルタントです。"},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"コンテンツ生成中にエラーが発生しました: {str(e)}"
    
    def create_exercise_worksheet(self, theme: str, exercise_type: str) -> str:
        """演習ワークシートの作成"""
        
        exercise_templates = {
            "self_assessment": """
# 自己分析ワークシート

## ステップ1: 強みの分析
1. あなたの強みを3つ挙げてください
   - 強み1: _________________
   - 強み2: _________________
   - 強み3: _________________

2. その強みをどのように活かしたいですか？
   _________________________________

## ステップ2: 価値観の整理
重要度を1-5で評価してください：

- 仕事の安定性: [1] [2] [3] [4] [5]
- 創造性の発揮: [1] [2] [3] [4] [5]
- 社会貢献: [1] [2] [3] [4] [5]
- 収入: [1] [2] [3] [4] [5]
- ワークライフバランス: [1] [2] [3] [4] [5]

## ステップ3: 理想のキャリア
あなたの理想とするキャリアについて具体的に書いてください：

_________________________________
_________________________________
_________________________________
            """,
            "goal_setting": """
# 目標設定ワークシート

## 短期目標（3ヶ月以内）
1. _________________
2. _________________
3. _________________

## 中期目標（1年以内）
1. _________________
2. _________________
3. _________________

## 長期目標（3-5年）
1. _________________
2. _________________
3. _________________

## アクションプラン
各目標に対して具体的な行動計画を立ててください：

### 短期目標1のアクションプラン
- 週1回: _________________
- 月1回: _________________
- 毎日: _________________
            """
        }
        
        return exercise_templates.get(exercise_type, "演習テンプレートが見つかりません")
```

### JavaScript/TypeScript

#### インタラクティブツール
```typescript
interface SeminarParticipant {
  id: string;
  name: string;
  email: string;
  role: string;
  experience: number;
  goals: string[];
}

interface SeminarSession {
  id: string;
  title: string;
  theme: string;
  participants: SeminarParticipant[];
  startTime: Date;
  endTime: Date;
  materials: string[];
}

class InteractiveSeminarTool {
  private participants: SeminarParticipant[] = [];
  private currentSession: SeminarSession | null = null;

  constructor() {
    this.initializeTool();
  }

  private initializeTool(): void {
    // ツールの初期化
    console.log('インタラクティブセミナーツールを初期化しました');
  }

  public createSession(title: string, theme: string): SeminarSession {
    const session: SeminarSession = {
      id: this.generateSessionId(),
      title,
      theme,
      participants: [],
      startTime: new Date(),
      endTime: new Date(Date.now() + 90 * 60 * 1000), // 90分後
      materials: []
    };

    this.currentSession = session;
    return session;
  }

  public addParticipant(participant: Omit<SeminarParticipant, 'id'>): string {
    const newParticipant: SeminarParticipant = {
      ...participant,
      id: this.generateParticipantId()
    };

    this.participants.push(newParticipant);
    
    if (this.currentSession) {
      this.currentSession.participants.push(newParticipant);
    }

    return newParticipant.id;
  }

  public conductPoll(question: string, options: string[]): Promise<Map<string, number>> {
    return new Promise((resolve) => {
      // 実際の実装では、リアルタイム投票機能を実装
      const results = new Map<string, number>();
      options.forEach(option => results.set(option, Math.floor(Math.random() * 10)));
      
      setTimeout(() => resolve(results), 3000);
    });
  }

  public generateSessionReport(): string {
    if (!this.currentSession) {
      return 'アクティブなセッションがありません';
    }

    return `
# セミナーレポート

## セッション情報
- タイトル: ${this.currentSession.title}
- テーマ: ${this.currentSession.theme}
- 参加者数: ${this.currentSession.participants.length}名
- 実施時間: ${this.currentSession.startTime.toLocaleString()} - ${this.currentSession.endTime.toLocaleString()}

## 参加者分析
${this.analyzeParticipants()}

## フィードバックサマリー
${this.generateFeedbackSummary()}
    `;
  }

  private analyzeParticipants(): string {
    const roles = this.currentSession?.participants.map(p => p.role) || [];
    const roleCount = roles.reduce((acc, role) => {
      acc[role] = (acc[role] || 0) + 1;
      return acc;
    }, {} as Record<string, number>);

    return Object.entries(roleCount)
      .map(([role, count]) => `- ${role}: ${count}名`)
      .join('\n');
  }

  private generateFeedbackSummary(): string {
    // 実際の実装では、参加者からのフィードバックを分析
    return `
- 満足度: 4.2/5.0
- 最も評価された点: 実践的な演習
- 改善点: より多くの事例紹介
- 次回への要望: 業界別のキャリアパス
    `;
  }

  private generateSessionId(): string {
    return `session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }

  private generateParticipantId(): string {
    return `participant_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }
}

// 使用例
const seminarTool = new InteractiveSeminarTool();
const session = seminarTool.createSession('キャリア転換セミナー', 'キャリア開発');

seminarTool.addParticipant({
  name: '田中太郎',
  email: 'tanaka@example.com',
  role: 'エンジニア',
  experience: 5,
  goals: ['マネジメント職への転向', '新しい技術の習得']
});

// 投票の実施
seminarTool.conductPoll('最も関心のあるキャリアパスは？', [
  '技術スペシャリスト',
  'マネージャー',
  'コンサルタント',
  '起業'
]).then(results => {
  console.log('投票結果:', results);
});
```

---

## セミナーコンテンツ作成のベストプラクティス

### コンテンツ設計
- **参加者中心**: 対象者のニーズとレベルに合わせた設計
- **インタラクティブ**: 受動的な講義ではなく、参加型の要素を重視
- **実践的**: 理論だけでなく、具体的なアクションにつながる内容
- **段階的**: 基礎から応用へと段階的に学習できる構成

### 資料作成
- **視覚的**: 図表やグラフを効果的に活用
- **簡潔**: 1スライド1メッセージの原則
- **一貫性**: デザインとメッセージの一貫性を保つ
- **アクセシビリティ**: 様々な参加者に対応できる配慮

### 演習・ワーク設計
- **目的明確**: 各演習の目的と期待される成果を明確化
- **時間管理**: 適切な時間配分と進行管理
- **グループ活用**: 個人ワークとグループワークのバランス
- **振り返り**: 演習後の振り返り時間の確保

### 品質管理
- **レビュー**: 複数人での内容レビュー
- **テスト**: 実際の参加者でのテスト実施
- **改善**: フィードバックに基づく継続的改善
- **更新**: 最新情報の定期的な反映

---

## 環境管理

### 依存関係の管理
```bash
# 新しいパッケージの追加
pip install package-name
pip freeze > requirements.txt

# 環境の再構築
pip install -r requirements.txt
```

### 環境変数の管理
```bash
# .envファイルの作成
echo "OPENAI_API_KEY=your-api-key" > .env
echo "SEMINAR_CONFIG_PATH=./config" >> .env
```

### バージョン管理
```bash
# 変更のコミット
git add .
git commit -m "セミナーコンテンツの更新: キャリア転換テーマ"

# ブランチ管理
git checkout -b feature/new-seminar-theme
git merge feature/new-seminar-theme
```

---

## トラブルシューティング

### よくある問題と解決方法

#### 1. APIキーの問題
```bash
# 環境変数の確認
echo $OPENAI_API_KEY

# .envファイルの確認
cat .env
```

#### 2. 依存関係の問題
```bash
# 仮想環境の確認
conda info --envs

# パッケージの再インストール
pip install --force-reinstall -r requirements.txt
```

#### 3. ファイルパスの問題
```python
import os
import pathlib

# 絶対パスの取得
current_dir = pathlib.Path(__file__).parent.absolute()
config_path = current_dir / "config" / "seminar-config.yml"

# ファイルの存在確認
if config_path.exists():
    print(f"設定ファイルが見つかりました: {config_path}")
else:
    print(f"設定ファイルが見つかりません: {config_path}")
```

---

## 参考資料

### キャリアコンサルティング関連
- [キャリアコンサルティング協会](https://www.career-cc.org/)
- [厚生労働省 キャリアコンサルティング](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/koyou/career_consulting/)
- [キャリア教育・進路指導に関する総合的調査研究](https://www.mext.go.jp/a_menu/shotou/career/)

### AIツール関連
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Claude API Documentation](https://docs.anthropic.com/)
- [Gemini API Documentation](https://ai.google.dev/docs)

### セミナー運営関連
- [オンラインセミナーのベストプラクティス](https://example.com)
- [参加者エンゲージメント向上のコツ](https://example.com)
- [効果的なプレゼンテーション技法](https://example.com)

---

**注意**: このルールファイルは、キャリアコンサルティングセミナーの準備に特化しています。セミナーの目的や対象者に応じて、適切にカスタマイズしてください。 