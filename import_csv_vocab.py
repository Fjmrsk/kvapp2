import os
import csv
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kvapp.settings')
django.setup()

from vocabulary.models import Vocabulary

with open('vocab_data.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    print("ヘッダー名:", reader.fieldnames)  # ヘッダー名を出力して確認
    for row in reader:
        Vocabulary.objects.create(
            korean_word=row['korean_word'],
            english_translation=row['english_translation'],
            example_sentence=row['example_sentence']
        )


print("CSVファイルから単語を登録しました！")
