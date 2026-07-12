#برنامج يقيم نسب الطلاب ويرتبها
fa = float(input ("what is the degree of the student ?\n"))
if fa >= 90 and fa <100:
    print("امتياز")
elif fa >=80 and fa <90:
    print("جيد جدا")
elif fa >=70 and fa <80:
    print("جيد")
elif fa >=50 and fa <70:
    print("مقبول")
else:
    print("ضعيف")