# 安装OpenCV和Streamlit，并开发第一个CV应用

# 安装OpenCV和Streamlit

打开电脑的终端(terminal)，输入：

```python
pip3 install opencv-python
```

安装OpenCV。

输入：

```python
pip install streamlit
```

安装streamlit。

创建一个hello.py文件，然后我们可以通过下段脚本来检查我们是否已安装了这OpenCV库。

```python
import cv2 as cv
img = cv.imread("图片路径")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window
```

若运行正常，脚本应打开一个窗口并显示图片路径中的图片文件。

我们可以通过以下命令检查streamlit的安装。

```python
streamlit hello
```

若运行正常，应该自动弹出以下界面：

![Untitled](%E5%AE%89%E8%A3%85OpenCV%E5%92%8CStreamlit%EF%BC%8C%E5%B9%B6%E5%BC%80%E5%8F%91%E7%AC%AC%E4%B8%80%E4%B8%AACV%E5%BA%94%E7%94%A8%203511d6d1ee894502821ff3aba1dfd5a3/Untitled.png)

# 图片上传器

我们的第一个网页应用是一个图片上传应用。用户可以上传一张图片，上传后我们的应用可以显示这张图片。除此之外，我们将应用openCV的灰度函数使应用可以得到图片后输出该照片的黑白版。

完成品图：

![Untitled](%E5%AE%89%E8%A3%85OpenCV%E5%92%8CStreamlit%EF%BC%8C%E5%B9%B6%E5%BC%80%E5%8F%91%E7%AC%AC%E4%B8%80%E4%B8%AACV%E5%BA%94%E7%94%A8%203511d6d1ee894502821ff3aba1dfd5a3/Untitled%201.png)

我们的程序结构如下：

- main函数：包含所有UI以及图像处理逻辑。
- if _  _*name*_ _ == “__ main __”语句 ：用于测试main函数。

我们首先导入我们的所有需要的库：

```python
import streamlit as stl
import cv2
import numpy as np
from PIL import Image
```

在这其中，streamlit和cv2（opencv）我们都已经介绍过了。numpy是python常用的线性代数计算库，而PIL则是python的图像操作库。对于Numpy，我们需要在终端输入：

```python
pip install numpy
```

之后我们开始定义我们的主函数：

```python
def main():
    stl.title("First Streamlit Demo")
    stl.subheader("By Astropower")
    stl.text("A simple image uploader.")
```

这段代码描述的就是网页的前三行文本，title、subheader和text表示为不同的字体渲染。

然后我们需要使用streamlit自带的file_uploader函数来获取图片文件。

```python
image_file = stl.file_uploader("Upload your picture",type=["jpg","png","jpeg"])
```

我们将上传的文件存储在了image_file变量中，以便我们后面继续操作。

我们还需要检测image_file是否为空，如果为空但不检测，我们的程序会无法正常运行。

```python
if not image_file:
		return None
```

之后我们用Image将图片打开，并用np.array将它转换为numpy数组以方便操作。

```python
o_img = Image.open(image_file)
o_img = np.array(o_img)
```

之后我们可以利用streamlit的image函数，将图片渲染在网页上面。

```python
stl.text("Original Image:")
stl.image([o_img])
```

我们就得到了最简单的图片上传器原型。

同时，我们可以使用cv2的灰度函数，将得到的图片（numpy数组）转换为灰度图片。然后将其一起渲染在网页上。

```python
trans_img = cv2.cvtColor(o_img,cv2.COLOR_BGR2GRAY)
stl.text("Gray Image:")
stl.image([trans_img])
```

最后我们只需要将main函数扔到if __ name **=="**__ **main __:**"语句中，就完成了第一个程序。

# 运行

与普通的python脚本不一样，streamlit需要使用：

```python
streamlit run filename.py
```

进行运行。

![Untitled](%E5%AE%89%E8%A3%85OpenCV%E5%92%8CStreamlit%EF%BC%8C%E5%B9%B6%E5%BC%80%E5%8F%91%E7%AC%AC%E4%B8%80%E4%B8%AACV%E5%BA%94%E7%94%A8%203511d6d1ee894502821ff3aba1dfd5a3/Untitled%202.png)

![Untitled](%E5%AE%89%E8%A3%85OpenCV%E5%92%8CStreamlit%EF%BC%8C%E5%B9%B6%E5%BC%80%E5%8F%91%E7%AC%AC%E4%B8%80%E4%B8%AACV%E5%BA%94%E7%94%A8%203511d6d1ee894502821ff3aba1dfd5a3/Untitled%203.png)

# 完整代码

```python
import streamlit as stl
import cv2
import numpy as np
from PIL import Image

def main():
    stl.title("First Streamlit Demo")
    stl.subheader("By Astropower")
    stl.text("A simple image uploader.")

    image_file = stl.file_uploader("Upload your picture",type=["jpg","png","jpeg"])
    if not image_file:
        return None
    o_img = Image.open(image_file)
    o_img = np.array(o_img)
    # image 
    trans_img = cv2.cvtColor(o_img,cv2.COLOR_BGR2GRAY)
    stl.text("Original Image:")
    stl.image([o_img])
    stl.text("Gray Image:")
    stl.image([trans_img])

if __name__=="__main__":
    main()
```

# Github链接：

[HarryLu0708/LearnCV: A misc set of openCV scripts. (github.com)](https://github.com/HarryLu0708/LearnCV)

BasicImageOperations → StlDemo.py