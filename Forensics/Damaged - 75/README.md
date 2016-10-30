# Damaged

**Points : 75**
**Solves : 243**

##Description:

	All you have to do is to see this damaged image!
[Attachment](for75_165560e4a08b23f7.zip)


## Write-up
This is a BMP damage image, then I open it with Hex edit,

![](http://i.imgur.com/uHaOdZz.jpg)

I found it must lost its header, after I refrence the BMP header format[[1]](http://www.pcschool.com.tw/campus/share/lib/160/)[[2]](https://en.wikipedia.org/wiki/BMP_file_format)

it's samply to recovery this images.

![](http://i.imgur.com/K6iemAi.jpg)

The flag is `EKO{b1tm4p_r3c}`