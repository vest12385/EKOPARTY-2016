# Ultra baby

**Points : 25**
**Solves : 261**


##Description:

	Reach the flag function!
	
	nc 9a958a70ea8697789e52027dc12d7fe98cad7833.ctf.site 55000

[Attachment](pwn25_5ae6e58885e7cd75.zip)

## Write-up
Use IDA pro disassembly, our target is reach flag function, this program first point function `Bye` base address to RBP-8, then show "Welcome, give me you best shot", then read your input from stdin, the the end call RBP-8(`Bye` function).

![](http://i.imgur.com/HRg4L9o.jpg)

The vulnerabilit is in read buffer size, the read buffer size is 19h, it may lay over first bytes of `Bye` funcion.
![](http://i.imgur.com/Xkxk9bR.jpg)

In stack ( assign `Bye` base address to rbp-8 )

\------------------   <--- rsp (rbp - 20h)

|  ?? ?? ?? ?? | 

\------------------

|  ?? ?? ?? ?? | 

\------------------

|  ?? ?? ?? ?? | 

\------------------

|  ?? ?? ?? ?? | 

\------------------

|  ?? ?? ?? ?? | 

\------------------

|  ?? ?? ?? ?? | 

\------------------  <--- rbp - 8

|  E0 07 00 00 |

\------------------

|  00 00 00 00 |

\------------------  <--- rbp


In stack ( read [payload](code) from stdin )

![](http://i.imgur.com/HhZDk9n.jpg)

\------------------   <--- rsp (rbp - 20h)

|  61 61 61 61 |

\------------------

|  61 61 61 61 |

\------------------

|  61 61 61 61 |

\------------------

|  61 61 61 61 |

\------------------

|  61 61 61 61 |

\------------------

|  61 61 61 61 |

\------------------  <--- rbp - 8

|  `F3` 07 00 00 | <-- `Bye` funciont base address first byte has been over lay

\------------------

|  00 00 00 00 |

\------------------  <--- rbp


![](http://i.imgur.com/bwwQluV.jpg)
The flage is `EKO{Welcome_to_pwning_challs_2k16}`