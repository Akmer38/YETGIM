
def fibonacci(n):

    if n == 0:
        return []
    if n == 1:
        return [0]
    
    fib_list = [0, 1]
    
    for i in range(2, n):
        
        next_fib = fib_list[i-1] + fib_list[i-2]
        fib_list.append(next_fib)
    
    return fib_list
if __name__ == "__main__":
    
    try:
        n = int(input("Kaç adet Fibonacci sayısı üretmek istiyorsunuz? "))
        
        if n < 0:
            print("\nHata: Lütfen 0 veya daha büyük bir sayı girin!")
        else:
            result = fibonacci(n)
            
            if result:
                print(f"\nİlk {n} Fibonacci sayısı:")
                print(result)
                print(f"\nToplam: {sum(result)}")
            else:
                print("\nBoş liste döndürüldü (n = 0)")
    
    except ValueError:
        print("\nHata: Lütfen geçerli bir tam sayı girin!")