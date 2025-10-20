import re
from collections import Counter


def analyze_text(text):
    if not text or text.strip() == "":
        return {
            "char_count": 0,
            "word_count": 0,
            "sentence_count": 0,
            "most_common_word": None,
            "average_word_length": 0.0
        }
    
    char_count = len(text)
    
    # Noktalama işaretlerini kaldır ve kelimelere ayır
    words = re.findall(r'\b[a-zA-ZçğıöşüÇĞİÖŞÜ]+\b', text.lower())
    word_count = len(words)
    
    
    sentences = re.split(r'[.!?]+', text)
    
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(sentences)
    
    if words:
        word_freq = Counter(words)
        most_common_word = word_freq.most_common(1)[0][0]
    else:
        most_common_word = None
    
    if words:
        total_length = sum(len(word) for word in words)
        average_word_length = round(total_length / len(words), 2)
    else:
        average_word_length = 0.0
    
    return {
        "char_count": char_count,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "most_common_word": most_common_word,
        "average_word_length": average_word_length
    }

if __name__ == "__main__":
    print("metin girin")    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    text = "\n".join(lines)
    
    if not text.strip():
        print()
    else:
        result = analyze_text(text)
        
        print(f"Toplam Karakter Sayısı: {result['char_count']}")
        print(f"Toplam Kelime Sayısı: {result['word_count']}")
        print(f"Toplam Cümle Sayısı: {result['sentence_count']}")
        print(f"En Sık Geçen Kelime: {result['most_common_word']}")
        print(f"Ortalama Kelime Uzunluğu: {result['average_word_length']}")
    
  