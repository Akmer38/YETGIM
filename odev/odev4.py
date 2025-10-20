def intersection(list1, list2):
    result = list(set(list1) & set(list2))
    
    return result

def intersection_alternative(list1, list2):

    result = []
    
    for item in list1:
    
        if item in list2 and item not in result:
            result.append(item)
    
    return result


if __name__ == "__main__":
    try:
        print("İlk listeyi virgülle ayırarak girin:")
        input1 = input("Liste 1: ")
        list1 = [item.strip() for item in input1.split(",")]
        
        try:
            list1 = [int(item) for item in list1]
        except ValueError:
            pass 
        
        print("\nİkinci listeyi virgülle ayırarak girin:")
        input2 = input("Liste 2: ")
        list2 = [item.strip() for item in input2.split(",")]
        
        try:
            list2 = [int(item) for item in list2]
        except ValueError:
            pass  
        result = intersection(list1, list2)
        
        print(f"\nListe 1: {list1}")
        print(f"Liste 2: {list2}")
        print(f"Kesişim: {result}")
        
        if not result:
            print("(Ortak eleman bulunamadı)")
        
    except Exception as e:
        print(f"\nHata: {e}")