weight = int(input("请输入您的体重(kg)："))
height = float(input("请输入您的身高(m)："))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("体型偏瘦，多吃点蔬菜、水果、肉类。")
elif bmi < 25:
    print("体型正常。")
    if input("你想找女朋友吗？(y/n)：") in ("y", "Y") or input("你想找男朋友吗？(y/n)：") == "y": #此处后边input语句可能不会执行，因为if条件满足，所以后边的语句不会执行，所以需要将后边的语句放在if语句中
        print("我来帮你！")
    else:
        print("请随时联系我！")
elif bmi < 28:
    print("体型偏胖，多吃点零食、肉类、蔬菜。")
elif bmi < 32:
    print("体型肥胖，建议减肥。")
else:
    print("严重肥胖，建议立即减肥。")  # 前面所述条件都不满足时，执行该语句