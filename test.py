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
