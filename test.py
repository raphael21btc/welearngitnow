def sum_by_raphael(a, b):
    return a + b   # This is the correct implementation


# Egon hat es vielleicht doch geschafft..
c = input(int("Geben Sie einen Wert für C ein:"))
# so ein Nonsense

## lets implement something stupid

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

print ("Guten Morgen!")


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def implement_the_most_stupid_function_on_earth_wie_lang_kann_eine_python_function_sein_frage__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________():
    print("I am stupid")
    return 0
