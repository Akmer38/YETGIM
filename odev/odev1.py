def is_prime(number):
   
    if number <= 1:
        return False
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        return False
    
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
    
    return True


# Kullanıcıdan sayı al ve kontrol et
if __name__ == "__main__":
    print()
    
    try:
        number = int(input("Kontrol etmek istediğiniz sayıyı girin: "))
        
        if is_prime(number):
            print(f"\n{number} bir ASAL sayıdır!")
        else:
            print(f"\n{number} asal değildir.")
    
    except ValueError:
        print("\nHata: Lütfen geçerli bir tam sayı girin!")