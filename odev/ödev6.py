def calculate(operation, *args):

    if len(args) == 0:
        return None
    
    if operation == "topla":
        return sum(args)
    
    elif operation == "çarp":
        result = 1
        for num in args:
            result *= num
        return result
    
    elif operation == "ortalama":
        return sum(args) / len(args)
    
    elif operation == "max":
        return max(args)
    
    elif operation == "min":
        return min(args)
    
    else:
        return None

if __name__ == "__main__":

    print("Mevcut işlemler: topla, çarp, ortalama, max, min")
    print()
    
    try:
        operation = input("İşlem türünü girin: ").strip().lower()
        numbers_input = input("Sayıları boşlukla ayırarak girin: ")
        
        # Sayıları listeye çevir
        numbers = [float(num) for num in numbers_input.split()]
        
        if not numbers:
            print("\nHata: En az bir sayı girmelisiniz!")
        else:
            result = calculate(operation, *numbers)
            
            if result is None:
                print(f" '{operation}' geçersiz bir işlem türü!")
            else:
                print(f"\nSonuç: {operation}({', '.join(map(str, numbers))}) = {result}")
 
    except ValueError:
        print()
    except Exception as e:
        print()