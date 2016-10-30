# RFC 7230

**Points : 50**
**Solves : 533**


##Description:

	Get just basic information from this server (ctf.ekoparty.org).

## Write-up
See protocol [RFC 7230](https://tools.ietf.org/html/rfc7230) is Hypertext Transfer Protocol (HTTP)
Use [Burp Suite](https://portswigger.net/burp/) catch packet, then can found the flag in the header
![](http://i.imgur.com/fo8hXAA.jpg)
The flag is `EKO{this_is_my_great_server}`