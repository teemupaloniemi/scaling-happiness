# Cyber Security Base 2024 Course Project

## Why?

This program is created as a part of the Cyber Security Base 2024 -course. The main reason being the identification and demonstration of OWASP Top 10 security vulnerabilities in a typical web application.  

## Usage

###  Running the program

0. Clone the reository and move to project directory: `git clone <repository_url_goes here>` and `cd scaling-happiness/project` 
1. Install required packages using `pip3 install -r requirements.txt`
2. Create a superuser by running `python3 manage.py createsuperuser`
3. Run the server: `python3 manage.py runserver` (or `python3 manage.py runsslserver --certificate cert.pem --key key.pem` for encrypted version)
  - If sslserver is run you must give a PEM pass phrase which is `cybermooc`
3. Test each vulnerability by setting `PATCHN = False` in the `project/med/views.py`-file. 
4. Test encrypted messaging using tcpdump. (I have included sample run results in `project/ssl.txt` and `project/nossl.txt` )

## Vulnerabilities:

### 0. Injection

Client side data is not validated and quering others data is possible. 

Fix: We infer the user id from the request and therefore it is not given by user. 

### 1. Loggin

The program did not log any activity and therefore finding the previous vulnerability (1. Injection) was hard to identify. 

Fix: We created logging for the program. 

### 2. Broken access control

The previous change introduced a vulnerability that allowed anyone with the right request to see the program logs. 

Fix: We added a check to verify that logs are only visible to the admin users. 

### 3. Data encryption 

When looging in or fetching the user data attackers in the middle can read the data and therefore if not properly encrypted the data might be vulnerable.
Below is an example of logging in with and without using ssl encryption. We can see that in the first case the user password is clearly visible.  

Logging in while not using ssl encryption:

```
  1 18:13:59.964723 IP 127.0.0.1.36814 > 127.0.0.1.8000: Flags [.], ack 3026237152, win 512, options [nop,nop,TS val 1018466529 ecr 1018456525], length 0
  2         0x0000:  4500 0034 6764 4000 4006 d55d 7f00 0001  E..4gd@.@..]....
  3         0x0010:  7f00 0001 8fce 1f40 b525 8f89 b460 b6e0  .......@.%...`..
  4         0x0020:  8010 0200 fe28 0000 0101 080a 3cb4 90e1  .....(......<...
  5         0x0030:  3cb4 69cd                                <.i.
  6 18:13:59.964731 IP 127.0.0.1.8000 > 127.0.0.1.36814: Flags [.], ack 1, win 512, options [nop,nop,TS val 1018466529 ecr 1018456525], length 0
  7         0x0000:  4500 0034 b6f5 4000 4006 85cc 7f00 0001  E..4..@.@.......
  8         0x0010:  7f00 0001 1f40 8fce b460 b6e0 b525 8f8a  .....@...`...%..
  9         0x0020:  8010 0200 fe28 0000 0101 080a 3cb4 90e1  .....(......<...
 10         0x0030:  3cb4 69cd                                <.i.
 11 18:14:02.373374 IP 127.0.0.1.36814 > 127.0.0.1.8000: Flags [P.], seq 1:763, ack 1, win 512, options [nop,nop,TS val 1018468937 ecr 1018466529], length 762
 12         0x0000:  4500 032e 6765 4000 4006 d262 7f00 0001  E...ge@.@..b....
 13         0x0010:  7f00 0001 8fce 1f40 b525 8f8a b460 b6e0  .......@.%...`..
 14         0x0020:  8018 0200 0123 0000 0101 080a 3cb4 9a49  .....#......<..I
 15         0x0030:  3cb4 90e1 504f 5354 202f 6c6f 6769 6e2f  <...POST./login/
 16         0x0040:  2048 5454 502f 312e 310d 0a48 6f73 743a  .HTTP/1.1..Host:
 17         0x0050:  206c 6f63 616c 686f 7374 3a38 3030 300d  .localhost:8000.
 18         0x0060:  0a55 7365 722d 4167 656e 743a 204d 6f7a  .User-Agent:.Moz
 19         0x0070:  696c 6c61 2f35 2e30 2028 5831 313b 2055  illa/5.0.(X11;.U
 20         0x0080:  6275 6e74 753b 204c 696e 7578 2078 3836  buntu;.Linux.x86
 21         0x0090:  5f36 343b 2072 763a 3132 342e 3029 2047  _64;.rv:124.0).G
 22         0x00a0:  6563 6b6f 2f32 3031 3030 3130 3120 4669  ecko/20100101.Fi
 23         0x00b0:  7265 666f 782f 3132 342e 300d 0a41 6363  refox/124.0..Acc
 24         0x00c0:  6570 743a 2074 6578 742f 6874 6d6c 2c61  ept:.text/html,a
 25         0x00d0:  7070 6c69 6361 7469 6f6e 2f78 6874 6d6c  pplication/xhtml
 26         0x00e0:  2b78 6d6c 2c61 7070 6c69 6361 7469 6f6e  +xml,application
 27         0x00f0:  2f78 6d6c 3b71 3d30 2e39 2c69 6d61 6765  /xml;q=0.9,image
 28         0x0100:  2f61 7669 662c 696d 6167 652f 7765 6270  /avif,image/webp
 29         0x0110:  2c2a 2f2a 3b71 3d30 2e38 0d0a 4163 6365  ,*/*;q=0.8..Acce
 30         0x0120:  7074 2d4c 616e 6775 6167 653a 2065 6e2d  pt-Language:.en-
 31         0x0130:  5553 2c65 6e3b 713d 302e 350d 0a41 6363  US,en;q=0.5..Acc
 32         0x0140:  6570 742d 456e 636f 6469 6e67 3a20 677a  ept-Encoding:.gz
 33         0x0150:  6970 2c20 6465 666c 6174 652c 2062 720d  ip,.deflate,.br.
 34         0x0160:  0a52 6566 6572 6572 3a20 6874 7470 3a2f  .Referer:.http:/
 35         0x0170:  2f6c 6f63 616c 686f 7374 3a38 3030 302f  /localhost:8000/
 36         0x0180:  0d0a 436f 6e74 656e 742d 5479 7065 3a20  ..Content-Type:.
 37         0x0190:  6170 706c 6963 6174 696f 6e2f 782d 7777  application/x-ww
 38         0x01a0:  772d 666f 726d 2d75 726c 656e 636f 6465  w-form-urlencode
 39         0x01b0:  640d 0a43 6f6e 7465 6e74 2d4c 656e 6774  d..Content-Lengt
 40         0x01c0:  683a 2031 3138 0d0a 4f72 6967 696e 3a20  h:.118..Origin:.
 41         0x01d0:  6874 7470 3a2f 2f6c 6f63 616c 686f 7374  http://localhost
 42         0x01e0:  3a38 3030 300d 0a43 6f6e 6e65 6374 696f  :8000..Connectio
 43         0x01f0:  6e3a 206b 6565 702d 616c 6976 650d 0a43  n:.keep-alive..C
 44         0x0200:  6f6f 6b69 653a 2063 7372 6674 6f6b 656e  ookie:.csrftoken
 45         0x0210:  3d6c 676c 664b 7877 7130 3376 3855 3247  =lglfKxwq03v8U2G
 46         0x0220:  5070 3571 4339 4167 644c 464c 504a 6f4a  Pp5qC9AgdLFLPJoJ
 47         0x0230:  670d 0a55 7067 7261 6465 2d49 6e73 6563  g..Upgrade-Insec
 48         0x0240:  7572 652d 5265 7175 6573 7473 3a20 310d  ure-Requests:.1.
 49         0x0250:  0a53 6563 2d46 6574 6368 2d44 6573 743a  .Sec-Fetch-Dest:
 50         0x0260:  2064 6f63 756d 656e 740d 0a53 6563 2d46  .document..Sec-F
 51         0x0270:  6574 6368 2d4d 6f64 653a 206e 6176 6967  etch-Mode:.navig
 52         0x0280:  6174 650d 0a53 6563 2d46 6574 6368 2d53  ate..Sec-Fetch-S
 53         0x0290:  6974 653a 2073 616d 652d 6f72 6967 696e  ite:.same-origin
 54         0x02a0:  0d0a 5365 632d 4665 7463 682d 5573 6572  ..Sec-Fetch-User
 55         0x02b0:  3a20 3f31 0d0a 0d0a 6373 7266 6d69 6464  :.?1....csrfmidd
 56         0x02c0:  6c65 7761 7265 746f 6b65 6e3d 6c33 766d  lewaretoken=l3vm
 57         0x02d0:  4345 3671 324a 6453 3471 6668 5050 7547  CE6q2JdS4qfhPPuG
 58         0x02e0:  376d 4f51 506e 6469 4857 7374 7739 4772  7mOQPndiHWstw9Gr
 59         0x02f0:  6331 7347 5343 7951 4f69 4c57 344b 4b38  c1sGSCyQOiLW4KK8
 60         0x0300:  364d 5554 7153 4f58 6761 317a 2675 7365  6MUTqSOXga1z&use
 61         0x0310:  726e 616d 653d 626f 6226 7061 7373 776f  rname=bob&passwo
 62         0x0320:  7264 3d73 7175 6172 6570 616e 7473       rd=squarepants
```
  
Logging in while using ssl encryption:

```
  1 18:15:08.040860 IP 127.0.0.1.33464 > 127.0.0.1.8000: Flags [.], ack 183654860, win 512, options [nop,nop,TS val 1018534605 ecr 1018524493], length 0
  2         0x0000:  4500 0034 26d5 4000 4006 15ed 7f00 0001  E..4&.@.@.......
  3         0x0010:  7f00 0001 82b8 1f40 13e6 7651 0af2 59cc  .......@..vQ..Y. 
  4         0x0020:  8010 0200 fe28 0000 0101 080a 3cb5 9acd  .....(......<...
  5         0x0030:  3cb5 734d                                <.sM
  6 18:15:08.040871 IP 127.0.0.1.8000 > 127.0.0.1.33464: Flags [.], ack 1, win 512, options [nop,nop,TS val 1018534605 ecr 1018524493], length 0
  7         0x0000:  4500 0034 5894 4000 4006 e42d 7f00 0001  E..4X.@.@..-....
  8         0x0010:  7f00 0001 1f40 82b8 0af2 59cc 13e6 7652  .....@....Y...vR
  9         0x0020:  8010 0200 fe28 0000 0101 080a 3cb5 9acd  .....(......<...
 10         0x0030:  3cb5 734d                                <.sM
 11 18:15:16.729410 IP 127.0.0.1.33464 > 127.0.0.1.8000: Flags [P.], seq 1:787, ack 1, win 512, options [nop,nop,TS val 1018543294 ecr 1018534605], length 786 
 12         0x0000:  4500 0346 26d6 4000 4006 12da 7f00 0001  E..F&.@.@.......
 13         0x0010:  7f00 0001 82b8 1f40 13e6 7652 0af2 59cc  .......@..vR..Y.
 14         0x0020:  8018 0200 013b 0000 0101 080a 3cb5 bcbe  .....;......<...
 15         0x0030:  3cb5 9acd 1703 0303 0d45 0188 1914 2dbb  <........E....-.
 16         0x0040:  73ae d1e2 2ab0 a2af baaa f8b8 3658 8952  s...*.......6X.R
 17         0x0050:  72b2 b45f 073b 00a0 c467 e128 880e 581b  r.._.;...g.(..X.
 18         0x0060:  2084 8326 48f1 1e74 7546 6d9b 49a3 f151  ...&H..tuFm.I..Q
 19         0x0070:  4de7 dd16 d2a8 972e e0ed 8a96 8946 85bc  M............F..
 20         0x0080:  8dfd 9c71 d073 c0ec 2f6a 58d6 ffd4 88e1  ...q.s../jX.....
 21         0x0090:  7842 3214 a424 7aa8 8e6c 2994 acd1 9e3c  xB2..$z..l)....<
 22         0x00a0:  01ed ed5e 5179 54b0 f36d 9f22 b98f 1920  ...^QyT..m."....
 23         0x00b0:  6563 ea0d bd15 61b5 7bb0 a9b5 5872 bf11  ec....a.{...Xr..
 24         0x00c0:  34f1 f50b 2d8e ad97 1f40 3bb0 6aff 1d70  4...-....@;.j..p
 25         0x00d0:  1c69 ce1e 2197 1b00 62a2 8011 525b 89f9  .i..!...b...R[..
 26         0x00e0:  b2d7 7bbf a5b6 fd87 36cd b15b 0ac1 acf5  ..{.....6..[....
 27         0x00f0:  dcff 9f5a a608 84f6 3f1a c779 2f03 8ace  ...Z....?..y/...
 28         0x0100:  aeb4 3421 1788 8dc3 0146 2a25 0aa2 edc0  ..4!.....F*%....
 29         0x0110:  89d7 9fb3 601a f85e 68c9 ce35 58b7 61e4  ....`..^h..5X.a.
 30         0x0120:  fca0 5046 7396 680f fe4d e1a1 5297 6a76  ..PFs.h..M..R.jv
 31         0x0130:  df27 bad9 77fb cfe3 e9ee 6bab 435d 0355  .'..w.....k.C].U
 32         0x0140:  7c72 2fc3 1371 4f5b f3a6 930c ec2f 28d9  |r/..qO[...../(.
 33         0x0150:  952c 8e66 08e1 fb38 99fd 0041 3078 3c19  .,.f...8...A0x<.
 34         0x0160:  377d 19eb 055c 493f 0e85 35a6 4e82 33e2  7}...\I?..5.N.3.
 35         0x0170:  36a2 bfee 016c 34ce 9aa1 791c 4139 6ebe  6....l4...y.A9n.
 36         0x0180:  bf94 d84b 3bb8 d36d 8fbc 36d0 bf57 9f7d  ...K;..m..6..W.}
 37         0x0190:  1a2e 243c cf7a 76e6 ca45 2c95 35c5 23d8  ..$<.zv..E,.5.#.
 38         0x01a0:  5fb1 267d c7ce 5238 4c7f b28c 3dbf d51c  _.&}..R8L...=...
 39         0x01b0:  070a 5ff4 eac4 5cc3 9fdb b629 bdcb 44b2  .._...\....)..D.
 40         0x01c0:  489e 6290 14fe 0ee9 fd92 3e4c 35a5 04c7  H.b.......>L5...
 41         0x01d0:  534b 9213 b360 07b0 7020 e007 a9c9 242f  SK...`..p.....$/
 42         0x01e0:  f2bc a779 6174 6c1a 70d5 761b ad55 5e33  ...yatl.p.v..U^3
 43         0x01f0:  da3b 3609 e4b9 212b ce0d adf7 c5ed a77a  .;6...!+.......z
 44         0x0200:  c53f 3e45 a75b 2368 b75f f6cf b746 bdff  .?>E.[#h._...F..
 45         0x0210:  f7ea c1be 830f 966f 3a60 c3e3 943c 0228  .......o:`...<.(
 46         0x0220:  3a48 e580 0a28 a812 9db1 a13a e4a3 8513  :H...(.....:....
 47         0x0230:  9147 67fe d970 daea 6e6b 8d87 ceea 455f  .Gg..p..nk....E_
 48         0x0240:  80d4 933a 0f10 15fc 417f 3ec3 e677 c884  ...:....A.>..w..
 49         0x0250:  ca0d 4775 917a 314a 8f0d 580d eab9 9add  ..Gu.z1J..X.....
 50         0x0260:  aa30 1ac8 f099 8ac1 8309 d508 dfe0 f214  .0..............
 51         0x0270:  00f0 8d1a f612 11ac ab69 8e90 473f eeaf  .........i..G?..
 52         0x0280:  3f6d 8db4 b036 060a af43 650a 309d 8741  ?m...6...Ce.0..A
 53         0x0290:  4d00 6eca 73b2 73e6 c573 9fdf 1295 4750  M.n.s.s..s....GP
 54         0x02a0:  2042 50f7 9e0f 2f88 5fd9 4789 9707 6084  .BP.../._.G...`.
 55         0x02b0:  5981 9fc3 d4d4 6e63 5ada 1ca4 5783 ffe6  Y.....ncZ...W...
 56         0x02c0:  bc62 3986 66ac c514 acf1 a953 5ebe a054  .b9.f......S^..T
 57         0x02d0:  1fa0 6b5b a19b 5aec 5bea 63a1 2533 923a  ..k[..Z.[.c.%3.:
 58         0x02e0:  cf07 0562 e038 b118 fbc1 e22f b9c6 3a0b  ...b.8...../..:.
 59         0x02f0:  0f15 ba4c 9052 a1d5 0e35 0f67 bfc0 4e9c  ...L.R...5.g..N.
 60         0x0300:  89ef 9057 ac03 563e bfd0 9656 48cd bc3e  ...W..V>...VH..>
 61         0x0310:  66d3 1cfd 77fb 5c9d 9287 581a 988a 53e6  f...w.\...X...S.
 62         0x0320:  76b1 ebd9 40c6 5741 c7fa 9dc0 94d5 adaa  v...@.WA........
 63         0x0330:  02eb 7956 6477 99e6 52eb 827b 4bb0 fd62  ..yVdw..R..{K..b
 64         0x0340:  a740 6746 d53f                           .@gF.?
```

### 4. Identification and Authentication Failures

Program did not enforce good password hygine when creating a new user.

Fix: Check for common password ([10k-most-common.txt](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt)) and require length and complexity (numbers and letters)
