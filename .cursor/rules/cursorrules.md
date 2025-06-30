# Cursor Rules for AI-Driven Coding

## 概要

このファイルは、Cursor IDE での AI駆動コーディングプロジェクトの開発ルールとベストプラクティスを定義しています。
効率的で高品質なコード開発を支援するためのガイドラインです。

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

## プロジェクト構造ガイドライン

### ディレクトリ構成

```
project/
├── src/                    # メインソースコード
│   ├── main.py            # エントリーポイント
│   ├── api/               # API関連
│   ├── models/            # データモデル
│   ├── services/          # ビジネスロジック
│   └── utils/             # ユーティリティ関数
├── tests/                 # テストファイル
│   ├── unit/              # 単体テスト
│   ├── integration/       # 統合テスト
│   └── fixtures/          # テストデータ
├── config/                # 設定ファイル
│   ├── settings.json      # アプリケーション設定
│   └── database.yml       # データベース設定
├── docs/                  # ドキュメント
├── scripts/               # スクリプトファイル
├── utility/               # ユーティリティツール
│   └── check_env.py       # 環境チェックスクリプト
├── requirements.txt       # Python依存関係
├── package.json           # Node.js依存関係
└── README.md              # プロジェクト説明
```

### ファイル命名規則

- **Python**: スネークケース（`user_service.py`）
- **JavaScript**: キャメルケース（`userService.js`）
- **TypeScript**: キャメルケース（`userService.ts`）
- **設定ファイル**: ケバブケース（`database-config.yml`）

---

## 開発プロセス

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
1. **Red**: 失敗するテストを書く
2. **Green**: テストを通す最小限のコードを書く
3. **Refactor**: コードを改善する

#### 実装例
```python
# 1. Red: 失敗するテスト
def test_user_creation():
    user = User("John", "john@example.com")
    assert user.name == "John"
    assert user.email == "john@example.com"

# 2. Green: 最小限の実装
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# 3. Refactor: 改善
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    
    def __str__(self) -> str:
        return f"User(name={self.name}, email={self.email})"
```

### 3. 継続的リファクタリング

- 小さな変更を頻繁に行う
- テストが通ることを確認
- 意味のある名前を使用
- 重複を除去する

---

## コード品質標準

### Python

#### PEP 8 準拠
```python
# 良い例
def calculate_total(items: List[Item]) -> float:
    """Calculate total price of items."""
    return sum(item.price for item in items)

# 悪い例
def calculate_total(items):
    return sum([item.price for item in items])
```

#### 型ヒントの使用
```python
from typing import List, Optional, Dict

def process_data(data: List[Dict[str, any]]) -> Optional[str]:
    """Process data and return result."""
    if not data:
        return None
    return str(len(data))
```

#### エラーハンドリング
```python
import logging
from typing import Optional

def safe_divide(a: float, b: float) -> Optional[float]:
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("Division by zero attempted")
        return None
```

### JavaScript/TypeScript

#### ESLint と Prettier
```typescript
// 良い例
interface User {
  id: number;
  name: string;
  email: string;
}

const createUser = (name: string, email: string): User => ({
  id: Date.now(),
  name,
  email,
});

// 悪い例
const createUser = function(name, email) {
  return {
    id: Date.now(),
    name: name,
    email: email
  }
}
```

#### エラーハンドリング
```typescript
async function fetchUserData(userId: number): Promise<User | null> {
  try {
    const response = await fetch(`/api/users/${userId}`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Failed to fetch user data:', error);
    return null;
  }
}
```

---

## テスト戦略

### 単体テスト

#### Python (pytest)
```python
import pytest
from src.services.user_service import UserService

class TestUserService:
    def test_create_user(self):
        service = UserService()
        user = service.create_user("John", "john@example.com")
        
        assert user.name == "John"
        assert user.email == "john@example.com"
    
    def test_create_user_with_invalid_email(self):
        service = UserService()
        
        with pytest.raises(ValueError):
            service.create_user("John", "invalid-email")
```

#### JavaScript (Jest)
```javascript
import { UserService } from '../src/services/userService';

describe('UserService', () => {
  let userService;

  beforeEach(() => {
    userService = new UserService();
  });

  test('should create user with valid data', () => {
    const user = userService.createUser('John', 'john@example.com');
    
    expect(user.name).toBe('John');
    expect(user.email).toBe('john@example.com');
  });

  test('should throw error for invalid email', () => {
    expect(() => {
      userService.createUser('John', 'invalid-email');
    }).toThrow('Invalid email format');
  });
});
```

### 統合テスト

```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_user_endpoint():
    response = client.post(
        "/users/",
        json={"name": "John", "email": "john@example.com"}
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John"
    assert data["email"] == "john@example.com"
```

---

## パフォーマンス最適化

### アルゴリズムの選択

```python
# 良い例: O(n) の時間複雑度
def find_duplicates(items: List[int]) -> List[int]:
    seen = set()
    duplicates = set()
    
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

# 悪い例: O(n²) の時間複雑度
def find_duplicates_slow(items: List[int]) -> List[int]:
    duplicates = []
    for i, item in enumerate(items):
        if item in items[i+1:]:
            duplicates.append(item)
    return duplicates
```

### キャッシュ機能

```python
from functools import lru_cache
import time

@lru_cache(maxsize=128)
def expensive_calculation(n: int) -> int:
    """Expensive calculation with caching."""
    time.sleep(1)  # シミュレーション
    return n * n

# 使用例
result1 = expensive_calculation(5)  # 1秒かかる
result2 = expensive_calculation(5)  # キャッシュから即座に取得
```

### メモリ最適化

```python
# 良い例: ジェネレータを使用
def process_large_file(filename: str):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

# 悪い例: 全行をメモリに読み込み
def process_large_file_bad(filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()  # 全行をメモリに読み込み
        return [line.strip() for line in lines]
```

---

## セキュリティベストプラクティス

### 入力値の検証

```python
import re
from typing import Optional

def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def sanitize_input(user_input: str) -> str:
    """Sanitize user input."""
    # HTMLエスケープ
    import html
    return html.escape(user_input.strip())
```

### 環境変数の管理

```python
import os
from dotenv import load_dotenv

load_dotenv()

# 環境変数から設定を取得
DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    raise ValueError("API_KEY environment variable is required")
```

### パスワードハッシュ化

```python
import bcrypt

def hash_password(password: str) -> str:
    """Hash password using bcrypt."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """Verify password against hash."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
```

---

## エラーハンドリングとログ

### ログ設定

```python
import logging
import sys

def setup_logging():
    """Setup logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )

logger = logging.getLogger(__name__)
```

### 例外処理

```python
class CustomException(Exception):
    """Custom exception for application errors."""
    pass

def process_data(data: dict) -> dict:
    """Process data with proper error handling."""
    try:
        if not data:
            raise CustomException("Data cannot be empty")
        
        result = perform_processing(data)
        logger.info("Data processed successfully")
        return result
        
    except CustomException as e:
        logger.error(f"Custom error: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise CustomException(f"Processing failed: {str(e)}")
```

---

## ドキュメントとコメント

### ドキュメント文字列

```python
def calculate_discount(price: float, discount_rate: float) -> float:
    """
    Calculate discounted price.
    
    Args:
        price: Original price
        discount_rate: Discount rate as decimal (e.g., 0.1 for 10%)
    
    Returns:
        Discounted price
    
    Raises:
        ValueError: If discount_rate is negative or greater than 1
    
    Example:
        >>> calculate_discount(100.0, 0.1)
        90.0
    """
    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1")
    
    return price * (1 - discount_rate)
```

### インラインコメント

```python
# 良い例: なぜこの処理が必要かを説明
def process_payment(amount: float, currency: str) -> bool:
    # 通貨がUSDでない場合は変換が必要
    if currency != 'USD':
        amount = convert_currency(amount, currency, 'USD')
    
    # 決済処理を実行
    return payment_gateway.process(amount)

# 悪い例: 何をしているかだけを説明
def process_payment(amount: float, currency: str) -> bool:
    # 通貨を変換
    if currency != 'USD':
        amount = convert_currency(amount, currency, 'USD')
    
    # 決済を処理
    return payment_gateway.process(amount)
```

---

## コミット管理

### コミットメッセージの規約

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

#### タイプ
- `feat`: 新機能
- `fix`: バグ修正
- `docs`: ドキュメント更新
- `style`: コードスタイル修正
- `refactor`: リファクタリング
- `test`: テスト追加・修正
- `chore`: その他の変更

#### 例
```
feat(user): add user authentication system

- Implement JWT token authentication
- Add user registration and login endpoints
- Include password hashing with bcrypt

Closes #123
```

### ブランチ戦略

```
main
├── develop
│   ├── feature/user-auth
│   ├── feature/payment-system
│   └── hotfix/security-patch
└── release/v1.0.0
```

---

## 継続的インテグレーション

### GitHub Actions 設定

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        python -m pytest tests/ --cov=src
    
    - name: Run linting
      run: |
        flake8 src/ --max-line-length=88
        black --check src/
```

---

## ベストプラクティスまとめ

### 開発効率化
1. **環境チェックの徹底**: コード実行前に必ず `python utility/check_env.py` を実行
2. **TDDサイクルの実践**: Red-Green-Refactor
3. **継続的リファクタリング**: 小さな変更を頻繁に
4. **適切なテスト戦略**: 単体・統合テストの実装

### コード品質
1. **言語固有の規約**: PEP 8, ESLint等の準拠
2. **型ヒントの使用**: 可能な限り型を明示
3. **エラーハンドリング**: 適切な例外処理
4. **ドキュメント**: 明確なdocstringとコメント

### セキュリティ
1. **入力値の検証**: すべてのユーザー入力を検証
2. **環境変数の管理**: 機密情報の適切な管理
3. **パスワードハッシュ化**: セキュアな認証
4. **定期的なセキュリティ監査**: 脆弱性の早期発見

### パフォーマンス
1. **効率的なアルゴリズム**: 適切なデータ構造の選択
2. **キャッシュ機能**: 重い処理の結果をキャッシュ
3. **メモリ最適化**: ジェネレータ等の活用
4. **プロファイリング**: ボトルネックの特定

---

## トラブルシューティング

### よくある問題と解決方法

#### 1. 環境の問題
```bash
# 環境チェックスクリプトを実行
python utility/check_env.py

# 仮想環境を再作成
conda create -n py-review python=3.9
conda activate py-review
pip install -r requirements.txt
```

#### 2. テストが失敗する場合
```bash
# テストを個別に実行
python -m pytest tests/test_specific.py -v

# デバッグモードで実行
python -m pytest tests/ -s -v
```

#### 3. 依存関係の問題
```bash
# 依存関係を更新
pip install --upgrade -r requirements.txt

# キャッシュをクリア
pip cache purge
```

---

## まとめ

このルールセットに従うことで、効率的で高品質なAI駆動コーディングが実現できます。
重要なポイントは以下の通りです：

1. **環境チェックの徹底**: コード実行前に必ず `python utility/check_env.py` を実行
2. **TDDサイクルの実践**: テスト駆動開発の徹底
3. **継続的リファクタリング**: コード品質の維持
4. **セキュリティの確保**: 適切なセキュリティ対策
5. **パフォーマンスの最適化**: 効率的なコードの実装
6. **適切なドキュメント**: 保守性の向上

これらのガイドラインを守ることで、チーム全体の開発効率とコード品質が向上します。 