height = input("Your height?")
weight = input("Your weight?")

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)


print(bmi_as_int)