#!/usr/bin/env python3
"""
環境チェックスクリプト
このプロジェクトでPythonコードを実行する前に、必ずこのスクリプトを実行してください。
"""

import sys
import subprocess
import os
import re
from pathlib import Path

def parse_requirements(requirements_file: str) -> list:
    """requirements.txtファイルを解析してパッケージ名のリストを取得"""
    packages = []
    
    try:
        with open(requirements_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # コメント行と空行をスキップ
                if not line or line.startswith('#'):
                    continue
                
                # パッケージ名を抽出（バージョン指定を除去）
                # 例: "requests>=2.31.0" -> "requests"
                package_name = re.split(r'[<>=!~]', line)[0].strip()
                if package_name:
                    packages.append(package_name)
                    
    except FileNotFoundError:
        print(f"❌ エラー: {requirements_file} が見つかりません")
        return []
    except Exception as e:
        print(f"❌ エラー: {requirements_file} の解析に失敗: {e}")
        return []
    
    return packages

def check_conda_env():
    """conda環境の確認"""
    print("🔍 conda環境をチェック中...")
    
    env_name = os.environ.get('CONDA_DEFAULT_ENV')
    if not env_name:
        print("❌ エラー: conda環境がアクティブではありません")
        print("実行してください: conda activate py-review")
        return False
    
    if env_name != 'py-review':
        print(f"❌ エラー: 現在の環境は '{env_name}' です")
        print("実行してください: conda activate py-review")
        return False
    
    print("✅ py-review環境がアクティブです")
    return True

def check_dependencies():
    """依存関係の確認"""
    print("🔍 依存関係をチェック中...")
    
    # requirements.txtからパッケージリストを動的に取得
    requirements_file = "requirements.txt"
    required_packages = parse_requirements(requirements_file)
    
    if not required_packages:
        print(f"❌ エラー: {requirements_file} からパッケージリストを取得できませんでした")
        return False
    
    print(f"📦 チェック対象パッケージ数: {len(required_packages)}")
    
    missing_packages = []
    
    for package in required_packages:
        try:
            # パッケージ名の正規化（ハイフンをアンダースコアに変換）
            import_name = package.replace('-', '_')
            
            # 特殊なインポート名の処理
            if package == 'python-dateutil':
                import dateutil
            elif package == 'python-dotenv':
                import dotenv
            elif package == 'typing-extensions':
                import typing_extensions
            elif package == 'pyyaml':
                import yaml
            else:
                __import__(import_name)
                
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ 不足している依存関係: {', '.join(missing_packages)}")
        print("実行してください: pip install -r requirements.txt")
        return False
    
    print("✅ 主要な依存関係がインストールされています")
    return True

def check_requirements_files():
    """requirements.txtファイルの存在確認"""
    print("🔍 requirements.txtファイルをチェック中...")
    
    root_req = Path("requirements.txt")
    
    if not root_req.exists():
        print("⚠️ 警告: ルートのrequirements.txtが見つかりません")
        return False
    
    print("✅ requirements.txtファイルが存在します")
    return True

def main():
    """メイン関数"""
    print("🚀 環境チェックを開始します...")
    print("=" * 50)
    
    env_ok = check_conda_env()
    print()
    
    req_files_ok = check_requirements_files()
    print()
    
    deps_ok = check_dependencies()
    print()
    
    print("=" * 50)
    
    if env_ok and deps_ok and req_files_ok:
        print("🎉 環境チェック完了！実行準備OK")
        print("✅ 仮想環境: py-review")
        print("✅ 依存関係: インストール済み")
        print("✅ 設定ファイル: 存在確認済み")
        sys.exit(0)
    else:
        print("⚠️ 環境に問題があります。上記の指示に従って修正してください")
        print()
        print("📋 修正手順:")
        print("1. conda activate py-review")
        print("2. pip install -r requirements.txt")
        print("3. python check_env.py  # 再チェック")
        sys.exit(1)

if __name__ == "__main__":
    main() 