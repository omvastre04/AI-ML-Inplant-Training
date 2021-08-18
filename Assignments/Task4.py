# Wed, 18 Aug 2021

# Task 4.1
# Examples of Arithmetic Operators
print("\nArithmetic Operation :")
x=10
y=20
print(f"\nx=10, y=20")
x+=y
print("x+=y : ", x)

x=10
y=20
print(f"\nx=10, y=20")
x-=y
print("x-=y : ", x)

x=10
y=20
print(f"\nx=10, y=20")
x*=y
print("x*=y : ", x)

x=10
y=2
print(f"\nx=10, y=2")
x**=y
print("x**=y : ", x)

x=10
y=20
print(f"\nx=10, y=20")
x/=y
print("x/=y : ", x)

x=10
y=20
print(f"\nx=10, y=20")
x//=y
print("x//=y : ", x)

x=50
y=25
print(f"\nx=50, y=25")
x%=y
print("x%=y : ", x)

print("-------------------------------")
print("-------------------------------")

# Task 4.2
# Examples of Logical Operators
print("\nLogical Operation :")
a=10
b=20
c=30
d=10
print(f"a={a}, b={b}, c={c}, d={d}")
print("--------------------------\n")

print("Logical and : ")
print("Expression           : Result")
print("a<b and b<c and a==d : ", a<b and b<c and a==d)
print("a>b and b>c and a==d : ", a>b and b>c and a==d)
print("--------------------------\n")

print("Logical or : ")
print("Expression         ̥: Result")
print("a<b or b>c or a==d : ", a<b or b>c or a==d)
print("a>b or b>c or a!=d : ", a>b or b>c or a!=d)
print("--------------------------\n")

print("Logical not : ")
x,y = 0,1
print(f"x={x}, y={y}")
print("Expression : Result")
print("not x      : ", not x)
print("not y      : ", not y)
print("--------------------------\n")