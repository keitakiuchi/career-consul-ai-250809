#!/usr/bin/env python3
"""
AI-Driven Coding Rules Aggregator

このスクリプトは、template-vibe-codingリポジトリのルールファイルを集約し、
ai-driven-coding.mdファイルを生成します。生成されたファイルは他のプロジェクトで
参照して使用できます。
"""

import os
import glob
from pathlib import Path
from datetime import datetime

class RulesAggregator:
    def __init__(self, root_dir=".."):
        self.root_dir = Path(root_dir)
        self.output_file = "ai-driven-coding.md"
        self.rules_files = {
            "Claude Code CLI": [
                ".claude/commands/gemini-search.md",
                ".claude/claude.yml",
                "CLAUDE.md"
            ],
            "Claude Code GitHub Actions": [
                ".github/workflows/claude.yml"
            ],
            "OpenAI Codex": [
                ".github/workflows/codex-tdd.yml",
                "AGENTS.md"
            ],
            "Gemini CLI": [
                "GEMINI.md"
            ],
            "Cursor": [
                ".cursor/rules/cursorrules.md"
            ]
        }
    
    def read_file_content(self, file_path):
        """ファイルの内容を読み込む"""
        full_path = self.root_dir / file_path
        if not full_path.exists():
            return f"# {file_path}\n\n**ファイルが見つかりません: {file_path}**\n"
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return f"# {file_path}\n\n{content}\n"
        except Exception as e:
            return f"# {file_path}\n\n**ファイル読み込みエラー: {e}**\n"
    
    def generate_header(self):
        """ヘッダー部分を生成"""
        return f"""# AI-Driven Coding Rules

このファイルは、template-vibe-codingリポジトリから自動生成されたAI駆動コーディングのルール集約ファイルです。

## 生成日時
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 概要
このファイルには、様々なAIツール向けのルールファイルが含まれています：
- Claude Code CLI
- Claude Code GitHub Actions  
- OpenAI Codex
- Gemini CLI
- Cursor

## 使用方法
1. このファイルをプロジェクトのルートディレクトリに配置
2. 各AIツールの設定ファイルで参照
3. プロジェクトの要件に合わせてカスタマイズ

---

"""
    
    def aggregate_rules(self):
        """ルールファイルを集約"""
        content = self.generate_header()
        
        for category, files in self.rules_files.items():
            content += f"## {category}\n\n"
            
            for file_path in files:
                content += self.read_file_content(file_path)
                content += "\n---\n\n"
        
        return content
    
    def save_output(self, content):
        """出力ファイルを保存"""
        output_path = Path(self.output_file)
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {output_path} を生成しました")
            return True
        except Exception as e:
            print(f"❌ ファイル保存エラー: {e}")
            return False
    
    def run(self):
        """メイン実行関数"""
        print("🔄 ルールファイルを集約中...")
        
        # ルールファイルの存在確認
        missing_files = []
        for category, files in self.rules_files.items():
            for file_path in files:
                if not (self.root_dir / file_path).exists():
                    missing_files.append(file_path)
        
        if missing_files:
            print("⚠️ 以下のファイルが見つかりません:")
            for file_path in missing_files:
                print(f"  - {file_path}")
            print()
        
        # ルールファイルを集約
        content = self.aggregate_rules()
        
        # 出力ファイルを保存
        if self.save_output(content):
            print(f"📊 集約完了:")
            total_files = sum(len(files) for files in self.rules_files.values())
            print(f"  - 処理したファイル数: {total_files}")
            print(f"  - 出力ファイル: {self.output_file}")
            print(f"  - ファイルサイズ: {len(content)} 文字")
        else:
            print("❌ 集約に失敗しました")

def main():
    """メイン関数"""
    print("🚀 AI-Driven Coding Rules Aggregator")
    print("=" * 50)
    
    aggregator = RulesAggregator()
    aggregator.run()
    
    print("\n📝 次のステップ:")
    print("1. 生成された ai-driven-coding.md を確認")
    print("2. 他のプロジェクトで使用する場合はコピー")
    print("3. 必要に応じてプロジェクト固有の設定を追加")

if __name__ == "__main__":
    main()
