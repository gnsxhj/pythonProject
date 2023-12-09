#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding=utf-8

## 给照片添加水印
#from PIL import Image
#from PIL import ImageFont
#from PIL import ImageDraw
#
#def watermark_Image(img_path, output_path, text, pos):
#    img = Image.open(img_path)
#    drawing = ImageDraw.Draw(img)
#    black = (250,250,200)
#    drawing.text(pos, text, fill=black)
#    img.show()
#    img.save(output_path)
#
#img = './materials/1.png'
#
#watermark_Image(img,'watermarked_1.png', 'Linhan Xu', pos=(20,20))
#
## 检测文本文件的相似性
#from difflib import SequenceMatcher
#
#def file_similarity_checker(f1, f2):
#    with open(f1, errors="ignore") as file1, open(f2, errors="ignore") as file2:
#        f1_data = file1.read()
#        f2_data = file2.read()
#        checking = SequenceMatcher(None, f1_data, f2_data).ratio()
#        print(f"These two files are {checking*100} % similar.")
#
#file_1 = './materials/1.ses'
#file_2 = './materials/2.ses'
#
#file_similarity_checker(file_1, file_2)
#
##生成二维码
#import qrcode
#from PIL import Image
#from pyzbar.pyzbar import decode
#
#def Generate_qrcode(data):
#    qr = qrcode.QRCode(
#        version=1,
#        error_correction=qrcode.constants.ERROR_CORRECT_L,
#        box_size=10,
#        border=4,
#    )
#    qr.add_data(data)
#    qr.make(fit=True)
#    image = qr.make_image(fill_color="black", black_color="white")
#    image.save("./materials/qrcode.png")
#
#Generate_qrcode("XuXiaohan")
#
#def Decode_Qrcode(file_name):
#    result = decode(Image.open(file_name))
#    print("Data: ", result[0][0].decode())
#
#Decode_Qrcode("./materials/qrcode.png")
#
## 测试网速
#from speedtest import Speedtest
#
#def Testing_Speed(net):
#    download = net.download()
#    upload = net.upload()
#    print(f'the speed of download: {download/(1024*1024)} Mbps')
#    print(f'the speed of upload: {upload/(1024 * 1024)} Mbps')
#    print('start testing the speed of net ...')
#
#net = Speedtest()
#Testing_Speed(net)
#
