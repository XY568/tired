
from PIL import Image
from pylab import show
pil_im = Image.open('图片4.jpg')



#裁剪指定区域
box = (100,100,400,400)
region = pil_im.crop(box)

#将裁剪的区域放回
region = region.transpose(Image.ROTATE_180)
pil_im.paste(region,box)
pil_im.show()




from PIL import Image
from pylab import *
# 读取图像到数组中
im = array(Image.open('图片4.jpg').convert('L'))
# 新建一个图像
figure()
# 不使用颜色信息
gray()
# 在原点的左上角显示轮廓图像
contour(im, origin='image')
axis('equal')
axis('off')
figure()
hist(im.flatten(),128)
show()

from PIL import Image
from pylab import *
im = array(Image.open('图片2.jpg'))
imshow(im)
print ('Please click 3 points')
x = ginput(3)
print( 'you clicked:',x)
show()


from PIL import Image
from pylab import *
im = array(Image.open('图片3.jpg'))
print (im.shape, im.dtype)
im = array(Image.open('图片1.jpg').convert('L'),'f')
print (im.shape, im.dtype)



def imresize(im,sz):
    """ 使用 PIL 对象重新定义图像数组的大小 """
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))


#直方图均衡化
def histeq(im,nbr_bins=256):
 """ 对一幅灰度图像进行直方图均衡化 """
 # 计算图像的直方图
 imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
 cdf = imhist.cumsum() # cumulative distribution function
 cdf = 255 * cdf / cdf[-1] # 归一化
 # 使用累积分布函数的线性插值，计算新的像素值
 im2 = interp(im.flatten(),bins[:-1],cdf)
 return im2.reshape(im.shape), cdf

#函数计算平均图像
def compute_average(imlist): 
 """ 计算图像列表的平均图像 """
 # 打开第一幅图像，将其存储在浮点型数组中
 averageim = array(Image.open(imlist[0]), 'f')
 for imname in imlist[1:]:
    try:
        averageim += array(Image.open(imname))
    except:
        print (imname + '...skipped')
 averageim /= len(imlist)
 # 返回 uint8 类型的平均图像
 return array(averageim, 'uint8')
 
from PIL import Image
from numpy import *
im = array(Image.open('图片1.jpg').convert('L'))
im2,cdf = imtools.histeq(im)
show()


from PIL import Image
from numpy import *
from pylab import *
import pca
im = array(Image.open(imlist[0])) # 打开一幅图像，获取其大小
m,n = im.shape[0:2] # 获取图像的大小
imnbr = len(imlist) # 获取图像的数目
# 创建矩阵，保存所有压平后的图像数据
immatrix = array([array(Image.open(im)).flatten()
 for im in imlist],'f')
# 执行 PCA 操作
V,S,immean = pca.pca(immatrix)
# 显示一些图像（均值图像和前 7 个模式）
figure()
gray()
subplot(2,4,1) 
imshow(immean.reshape(m,n))
for i in range(7):
 subplot(2,4,i+2)
 imshow(V[i].reshape(m,n))
show()





from PIL import Image
from numpy import *
im = array(Image.open('图片1.jpg').convert('L'))
im3 = (100.0/255) * im + 100 # 将图像像素值变换到 100...200 区间
print (int(im3.min()), int(im3.max()))

#图像数据
from PIL import Image
from numpy import *
im = array(Image.open('图片1.jpg'))
print (im.shape, im.dtype)
im = array(Image.open('图片1.jpg').convert('L'),'f')
print (im.shape, im.dtype)