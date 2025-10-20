def find_palindromes(word_list):
    palindromes = []
    
    for word in word_list:
        lower_word = word.lower()
        
        if lower_word == lower_word[::-1]:
            palindromes.append(word)
    
    return palindromes


if __name__ == "__main__":
    print("Kelimeleri virgülle ayırarak girin (örn: level, python, radar)")
    
    try:
        user_input = input("Kelimeler: ")
        

        word_list = [word.strip() for word in user_input.split(",")]
        
        result = find_palindromes(word_list)
        
        if result:
            print(f"palindromikler {result}")
        else:
            print("palindromik kelime yok")
        
    
    
    except Exception as e:
        print(f"\nHata: {e}")