# 通过输入中文
from PIL import Image,ImageDraw,ImageFont
import avsplit
# 定义屏幕尺寸
OLED = [128,64]
# 定义字号
fontPx = 12  

# 定义偏移量
Xaxis = []
Yaxis = []

line = 1 # 数据行数，默认1行

# 传入的的字符串
inputData = '中文测试功能'

# 计算字符的占位空间
inputDataSize = len(inputData)  #获取字符串长度

inputDataPx =  inputDataSize * fontPx # 获取字符串的总长度

line = (inputDataPx // OLED[0]) + 1  # 将实际长度向下取模除以屏幕宽度然后+1就是实际的行数
inputData = avsplit.avsplit(inputData, line) # 按照行数，自动分割字符串，存入列表
print(line,inputData)

for i in range(line):
    XtempData = (OLED[0] - (len(inputData[i]) * fontPx)) // 2 # 字符串的长度乘以字号等于字符串的总占屏
    Xaxis.append(XtempData)
    if line is 1:
        YtempData =(OLED[1] // 2) - fontPx // 2
        Yaxis.append(YtempData)
    else:
        YtempData =(OLED[1] // line) * i
        Yaxis.append(YtempData)

    


# 创建画布 大小128*64
image = Image.new("L",OLED,'White')

draw = ImageDraw.Draw(image) # 创建绘画对象


fnt = ImageFont.truetype(r'C:\\Windows\\Fonts\\msyhbd.ttc',fontPx) # 字体对象，字体与字号

# draw.text((8,(image.size[1]/2)-fontPx),'妈妈喜欢的',fill='black',font= fnt)
for i in range(line):
    draw.text((Xaxis[i],Yaxis[i]),inputData[i],fill='black',font= fnt)

pixels = image.load() # 二值化操作
for x in range(image.width):
    for y in range(image.height):
        
        if pixels[x, y] > 125:
            pixels[x, y] = 255
        else: 
            pixels[x, y] =0


image.show()

image.save('1.bmp')