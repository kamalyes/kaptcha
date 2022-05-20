import kaptcha

kaptcha.CaptchaPainter(text="Kaptcha", im_x=350).normal.show()

# 字母数字混合型
x, y = kaptcha.Captcha().letter_digit()
print(x, y)
# 数字型
x, y = kaptcha.Captcha().digit()
print(x, y)
# 字母型
x, y = kaptcha.Captcha().letter()
print(x, y)
# 增强
x, y = kaptcha.Captcha(enhance=True).letter_digit()
print(x, y)
# 边缘凸显
x, y = kaptcha.Captcha(edge=True).letter_digit()
print(x, y)
# 浮雕效果
x, y = kaptcha.Captcha(emboss=True).letter_digit()
print(x, y)
# 轮廓
x, y = kaptcha.Captcha(contour=True).letter_digit()
print(x, y)
# gif动态图
x, y = kaptcha.Captcha(gif=True, width=300).letter_digit()
print(x, y)
