def dodawanie(a, b):
    return a+b
def odejmowanie(a, b):
    return a - b
def mnozenie(a, b):
    return a * b
def dzielenie(a, b):
    if b!=0:
        return a / b

sl = {'+':dodawanie, '-':odejmowanie, '*':mnozenie, '/':dzielenie}
aa = float(input('L 1 '))
bb = float(input('L 2 '))
co = str(input("Co będziemy robić? (+ _ * /) "))
w = sl[co](aa, bb)
print(w)


