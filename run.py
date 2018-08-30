# 通过输入中文
from PIL import Image,ImageDraw,ImageFont
# 定义屏幕尺寸
OLED = [128,64]
# 定义字号
fontPx = 16  

# 定义偏移量
Xaxis = 0
Yaxis = 0

line = 1 # 数据行数，默认1行

# 传入的的字符串
inputData = '妈妈喜欢的饺子蘸料'

# 计算字符的占位空间
inputDataSize = len(inputData)  #获取字符串长度

inputDataPx =  inputDataSize * fontPx # 获取字符串的总长度
if (inputDataPx- 128) > 0 :
    # 超长
    print(inputDataPx,'超长')
    # 超过一行的长度需要截断，等于1 2行，等于2 3行
    line = (inputDataPx // OLED[0]) + 1  # 将实际长度向下取模除以屏幕宽度然后+1就是实际的行数
    print(line)
    
    # https://segmentfault.com/q/1010000002615925
    #inputDataSize // line
    #inputDataList.append()
    
else:
    # 不超长
    print(inputDataPx,'不超长')
    line = 1
    # 不超长的情况下，用总屏幕像素减去实际长度，然后除以2取整，获得X轴的偏移量
    Xaxis = (OLED[0] - inputDataPx) // 2    # 总像素-实际长度 除2 向下取模
        


# 创建画布 大小128*64
image = Image.new("L",OLED,'White')

draw = ImageDraw.Draw(image) # 创建绘画对象


fnt = ImageFont.truetype(r'C:\\Windows\\Fonts\\msyhbd.ttc',fontPx) # 字体对象，字体与字号

# draw.text((8,(image.size[1]/2)-fontPx),'妈妈喜欢的',fill='black',font= fnt)
draw.text((Xaxis,(image.size[1]/2)-fontPx),inputData,fill='black',font= fnt)

pixels = image.load()
for x in range(image.width):
    for y in range(image.height):
        
        if pixels[x, y] > 125:
            pixels[x, y] = 255
        else: 
            pixels[x, y] =0

image.show()

image.save('1.bmp')