#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
allCheck=True
def leftFormula (x,y,z):
    return not(x or y or z)
def rightFormula(x,y,z):
    return (not(x) and not(y) and not(z))
print('X    Y    Z     ¬(X ⋁ Y ⋁ Z)     ¬X ⋀ ¬Y ⋀ ¬Z     ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
for x in [False,True]:
    for y in [False,True]:
        for z in [False,True]:
            print(f'{x:1}{y:5}{z:5}{leftFormula (x,y,z):12}{rightFormula(x,y,z):18}{leftFormula (x,y,z)==rightFormula(x,y,z):25}')
            if not(leftFormula (x,y,z)==rightFormula(x,y,z)):
                allCheck=False
if allCheck:
    print ('Тождество верно')
else:
    print('Тождество неверно')