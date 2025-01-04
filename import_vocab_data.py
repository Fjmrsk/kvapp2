import os
import django

# プロジェクトの設定をロード
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kvapp.settings')
django.setup()

from vocabulary.models import Vocabulary

# 登録したいデータ
vocab_data = [
    {"korean_word": "안녕하세요", "english_translation": "Hello", "example_sentence": "안녕하세요! 만나서 반갑습니다."},
    {"korean_word": "감사합니다", "english_translation": "Thank you", "example_sentence": "도와주셔서 감사합니다."},
    # 他の単語を追加
]

# データをデータベースに登録
for data in vocab_data:
    Vocabulary.objects.create(**data)

print("単語の登録が完了しました！")
