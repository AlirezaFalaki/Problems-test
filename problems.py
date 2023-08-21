import math
import cv2
import numpy as np
import matplotlib.pyplot as plt


# question 2 -----------------------------------------------------------------

img = np.load('img.npy') # لود عکس (آرایه نامپای) داده شده توسط سوال
img = img.astype('uint8') # تغییر نوع آرایه به uint8
cv2.imshow('circle', img) # نمایش عکس

canny = cv2.Canny(img,threshold1=150,threshold2=255) #  استفاده از تابع canny ایجاد لبه های دایره برای محاسبه محیط
# cv2.imshow('canny', canny)

# calculate parameters with np.sum() -------------------------------
perimeter = np.sum(canny==255) # محاسبه محیط دایره با شمارش پیکسل های لبه دایره در عکس canny

# محاسبه قطر، شماردن تعداد پیکسل های سفید در ستون های عکس چون نتایج به صورت است آخرین ستون بیشترین تعداد پیکسل سفید را دارا است
diameter = np.sum(img==255,axis=0)[255]
# نمایش نتایچ
print('diameter:',diameter)
print('perimeter:',perimeter)

# شمارش تعداد کل پیکسل های سفید در تصویر که برابر است با مساحت
number_w = np.sum(img==255) # مساحت
print('Area:',number_w)



# ----------------------------------------------------------------------------
# question 1

# ساخت یک سری آرایه های نامپای به منظور پیاده سازی و شبیه سازی اضلاع مربع

x_3 = np.full(fill_value=3,shape=(100,))# آرا یه ۱۰۰ تایی یک بعدی که همه مقادیر آن ۳ است
x_ne3 = np.full(fill_value=-3,shape=(100,)) # آرا یه ۱۰۰ تایی یک بعدی که همه مقادیر آن منفی ۳ است

y_b = np.linspace(-3,3,100) # ایجاد یک آرايه با ۱۰۰ مقدار تصادفی بین ۳ و منفی ۳

# radius -------------
r_right = np.sqrt(x_3**2 + y_b**2) # محاسبه شعاع ضلع سمت راست مربع

r_left = np.sqrt(x_ne3**2 + y_b**2) #ضلع سمت چپ

r_up = np.sqrt(y_b**2 + x_3**2) # ضلع بالا

r_down = np.sqrt(y_b**2 + x_ne3**2) # ضلع  پایین

# teta --------------
teta_right = np.degrees(np.arctan(y_b/(x_3+1e-8))) # محاسبه زاویه تتا برای ضلع سمت راست مربع

teta_left = np.degrees(np.arctan(y_b/(x_ne3+10**-8))) #ضلع سمت چپ مربع

teta_up = np.degrees(np.arctan(x_3/(y_b+10**-8))) #ضلع بالا مربع

teta_down = np.degrees(np.arctan(x_ne3/(y_b+10**-8))) #ضلع پایین مربع

# ایجاد محور مختصات با استفاده از متپلات لیب برای نمایش نتیجه ------

plt.figure(figsize=(8, 8))
plt.subplot(141)

plt.plot(r_right,teta_right) # رسم ضلع سمت راست مربع در مختصات جدید
plt.subplot(142)
plt.plot(r_left,teta_left) # رسم ضلع سمت چپ مربع در مختصات جدید
plt.subplot(143)
plt.plot(r_up,teta_up) # رسم ضلع بالا مربع در مختصات جدید
plt.subplot(144)
plt.plot(r_down,teta_down) # رسم ضلع پایین مربع در مختصات جدید
plt.show()
