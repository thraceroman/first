from bs4 import BeautifulSoup
import os
import shutil
import zipfile
print("hello world")
path = "C:\\Users\\mlb85\\Desktop\\新建文件夹\\html\\1.html"
pathhtmls = "C:\\Users\\mlb85\\Desktop\\新建文件夹\\html"
pathimages = "C:\\Users\\mlb85\\Desktop\\新建文件夹\\image"
pathepub = "C:\\Users\\mlb85\\Desktop\\原文件"
pathdir = "C:\\Users\\mlb85\\Desktop\\解压后"
pathfins = "C:\\Users\\mlb85\\Desktop\\可读"

print("---------修改格式------------")

for root,dirs,files in os.walk(pathepub):
    for name in files:
        # print(os.path.join(root,name))
        # 解压后的文件夹名字
        zip_path = pathdir + "\\" + name[:-11]
        # print(zip_path)
        zip_file = zipfile.ZipFile(os.path.join(root,name))
        zip_list = zip_file.namelist()
        for f in zip_list:
            zip_file.extract(f,zip_path)
        zip_file.close()
        # 进行以下逻辑操作
        # 找这个文件夹下面的图片张书
        maxfile = os.listdir(zip_path +"\\html")
        max = len(maxfile) - 5
        print(max)
        #建子文件夹
        pathfin = pathfins + "\\" + name[:-11]
        os.mkdir(pathfin)
        # 找对应图片
        for num in range(1,max+1):
            pathhtml = zip_path + "\\html\\" + str(num) + ".html"
            pathimage = zip_path + "\\image"
            soup = open(pathhtml,'r',encoding='utf-8')
            soup1=BeautifulSoup(soup.read(),'lxml')
            page = soup1.img.get("src")
            page1 = page[9:]
            soup.close()
            # print(page1)
            imagepath = pathimage + "\\" + page1
            image = pathfin +"\\" + str(num) +".jpg"
            shutil.copyfile(imagepath,image)
print("----------完毕---------------")


# print("---------找对应图片,这是核心,用epub里面的对应格式,这个只是vol.moe网站的格式----------")
# htmlfile = open(path ,'r',encoding='utf-8')
# htmlhandle = htmlfile.read()
# # print(htmlhandle)
# soup = BeautifulSoup(htmlhandle,'lxml')
# # print(soup)
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.img)
# # print(soup.img.get("src"))
# pag=soup.img.get("src")
# pag1 = pag[9:]
# print(pag1)
# print("---------找图片张书---------")
# maxfile=os.listdir(pathhtmls)
# # print(maxfile)
# # 这里,有个未完成的,就是在这一堆字符串中找到max,而不是用列表长度
# max = len(maxfile)-5
# print(max)
# print("---------改名字,以找到对应顺序的图片重命名的形式----")
# path1 = pathimages+ "\\" + pag1
# print(path1)
# os.walk
# help(os.walk)

# for num in range(1,max+1):
#     pathhtml = pathhtmls + "\\" + str(num) + ".html"
#     soup1=BeautifulSoup(open(pathhtml,'r',encoding='utf-8').read(),'lxml')
#     page = soup1.img.get("src")
#     page1 = page[9:]
#     # print(page1)
#     imagepath = pathimages + "\\" + page1
#     image = "C:\\Users\\mlb85\\Desktop\\新建文件夹2" +"\\" + str(num) +".jpg"
#     shutil.copyfile(imagepath,image)
