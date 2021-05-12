a=input("Enter a Number:")
if a.isnumeric(): print(type(int(a)))
elif len(a)>2 and "." in a and not a.endswith(".") and not a.startswith("."): print(type(float(a)))
elif len(a)>1 and "j" in a: print(type(complex(a)))
else: print(type(str(a)))

