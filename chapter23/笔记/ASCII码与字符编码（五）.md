## 一、什么是ASCII码

- 计算机存储的就是bit

如何将文本进行存储？

文本--》数字形式

编码系统：将每一个字母赋予一个编码（数字）

构成这些编码需要多少个bit?

大写字母（26）+小写字母（26）+数字（0-9）= 62 个 （2**5=32 ）

其它的标点符号 > 64 = 2\*\*6

2\*\*7 = 128    

编码系统用7位bit

```python
二进制码    字符
0000 0011   A    48
0000 1001   2    90
```

编码系统设计好了，别人也设计了一套（A -129）

为了解决这种混乱的局面，标准化就显得意义非凡了。

幸运的是，这种标准化已经存在并且广泛使用了，我们已经有了这样一个标准，即美国信息交换标准代码（American Standard Code for Information Interchange），简写为 ASCII码。它1967年正式公布，此后一直是计算机工业界最为重要的标准。

ASCII码是7位编码，它的二进制取值范围为0000000-1111111，对应于十六进制就是00h-7Fh，如下所示：

| DEC  | OCT  | HEX  | BIN      | 缩写/符号 | 描述                                |
| ---- | ---- | ---- | -------- | --------- | ----------------------------------- |
| 0    | 000  | 00   | 00000000 | NUL       | Null char (空字符)                  |
| 1    | 001  | 01   | 00000001 | SOH       | Start of Heading (标题开始)         |
| 2    | 002  | 02   | 00000010 | STX       | Start of Text (正文开始)            |
| 3    | 003  | 03   | 00000011 | ETX       | End of Text (正文结束)              |
| 4    | 004  | 04   | 00000100 | EOT       | End of Transmission (传输结束)      |
| 5    | 005  | 05   | 00000101 | ENQ       | Enquiry (请求)                      |
| 6    | 006  | 06   | 00000110 | ACK       | Acknowledgment (收到通知)           |
| 7    | 007  | 07   | 00000111 | BEL       | Bell (响铃)                         |
| 8    | 010  | 08   | 00001000 | BS        | Back Space (退格)                   |
| 9    | 011  | 09   | 00001001 | HT        | Horizontal Tab (水平制表符)         |
| 10   | 012  | 0A   | 00001010 | LF        | Line Feed (换行键)                  |
| 11   | 013  | 0B   | 00001011 | VT        | Vertical Tab (垂直制表符)           |
| 12   | 014  | 0C   | 00001100 | FF        | Form Feed (换页键)                  |
| 13   | 015  | 0D   | 00001101 | CR        | Carriage Return (回车键)            |
| 14   | 016  | 0E   | 00001110 | SO        | Shift Out / X-On (不用切换)         |
| 15   | 017  | 0F   | 00001111 | SI        | Shift In / X-Off (启用切换)         |
| 16   | 020  | 10   | 00010000 | DLE       | Data Line Escape (数据链路转义)     |
| 17   | 021  | 11   | 00010001 | DC1       | Device Control 1 (设备控制1)        |
| 18   | 022  | 12   | 00010010 | DC2       | Device Control 2 (设备控制2)        |
| 19   | 023  | 13   | 00010011 | DC3       | Device Control 3 (设备控制3)        |
| 20   | 024  | 14   | 00010100 | DC4       | Device Control 4 (设备控制4)        |
| 21   | 025  | 15   | 00010101 | NAK       | Negative Acknowledgement (拒绝接收) |
| 22   | 026  | 16   | 00010110 | SYN       | Synchronous Idle (同步空闲)         |
| 23   | 027  | 17   | 00010111 | ETB       | End of Transmit Block (传输块结束)  |
| 24   | 030  | 18   | 00011000 | CAN       | Cancel (取消)                       |
| 25   | 031  | 19   | 00011001 | EM        | End of Medium (介质中断)            |
| 26   | 032  | 1A   | 00011010 | SUB       | Substitute (替补)                   |
| 27   | 033  | 1B   | 00011011 | ESC       | Escape (溢出)                       |
| 28   | 034  | 1C   | 00011100 | FS        | File Separator (文件分割符)         |
| 29   | 035  | 1D   | 00011101 | GS        | Group Separator (分组符)            |
| 30   | 036  | 1E   | 00011110 | RS        | Record Separator (记录分离符)       |
| 31   | 037  | 1F   | 00011111 | US        | Unit Separator (单元分隔符)         |
| 32   | 040  | 20   | 00100000 |           | Space (空格)                        |
| 33   | 041  | 21   | 00100001 | !         | Exclamation mark                    |
| 34   | 042  | 22   | 00100010 | "         | Double quotes                       |
| 35   | 043  | 23   | 00100011 | #         | Number                              |
| 36   | 044  | 24   | 00100100 | $         | Dollar                              |
| 37   | 045  | 25   | 00100101 | %         | Procenttecken                       |
| 38   | 046  | 26   | 00100110 | &         | Ampersand                           |
| 39   | 047  | 27   | 00100111 | '         | Single quote                        |
| 40   | 050  | 28   | 00101000 | (         | Open parenthesis                    |
| 41   | 051  | 29   | 00101001 | )         | Close parenthesis                   |
| 42   | 052  | 2A   | 00101010 | *         | Asterisk                            |
| 43   | 053  | 2B   | 00101011 | +         | Plus                                |
| 44   | 054  | 2C   | 00101100 | ,         | Comma                               |
| 45   | 055  | 2D   | 00101101 | -         | Hyphen                              |
| 46   | 056  | 2E   | 00101110 | .         | Period, dot or full stop            |
| 47   | 057  | 2F   | 00101111 | /         | Slash or divide                     |
| 48   | 060  | 30   | 00110000 | 0         | Zero                                |
| 49   | 061  | 31   | 00110001 | 1         | One                                 |
| 50   | 062  | 32   | 00110010 | 2         | Two                                 |
| 51   | 063  | 33   | 00110011 | 3         | Three                               |
| 52   | 064  | 34   | 00110100 | 4         | Four                                |
| 53   | 065  | 35   | 00110101 | 5         | Five                                |
| 54   | 066  | 36   | 00110110 | 6         | Six                                 |
| 55   | 067  | 37   | 00110111 | 7         | Seven                               |
| 56   | 070  | 38   | 00111000 | 8         | Eight                               |
| 57   | 071  | 39   | 00111001 | 9         | Nine                                |
| 58   | 072  | 3A   | 00111010 | :         | Colon                               |
| 59   | 073  | 3B   | 00111011 | ;         | Semicolon                           |
| 60   | 074  | 3C   | 00111100 | <         | Less than                           |
| 61   | 075  | 3D   | 00111101 | =         | Equals                              |
| 62   | 076  | 3E   | 00111110 | >         | Greater than                        |
| 63   | 077  | 3F   | 00111111 | ?         | Question mark                       |
| 64   | 100  | 40   | 01000000 | @         | At symbol                           |
| 65   | 101  | 41   | 01000001 | A         | Uppercase A                         |
| 66   | 102  | 42   | 01000010 | B         | Uppercase B                         |
| 67   | 103  | 43   | 01000011 | C         | Uppercase C                         |
| 68   | 104  | 44   | 01000100 | D         | Uppercase D                         |
| 69   | 105  | 45   | 01000101 | E         | Uppercase E                         |
| 70   | 106  | 46   | 01000110 | F         | Uppercase F                         |
| 71   | 107  | 47   | 01000111 | G         | Uppercase G                         |
| 72   | 110  | 48   | 01001000 | H         | Uppercase H                         |
| 73   | 111  | 49   | 01001001 | I         | Uppercase I                         |
| 74   | 112  | 4A   | 01001010 | J         | Uppercase J                         |
| 75   | 113  | 4B   | 01001011 | K         | Uppercase K                         |
| 76   | 114  | 4C   | 01001100 | L         | Uppercase L                         |
| 77   | 115  | 4D   | 01001101 | M         | Uppercase M                         |
| 78   | 116  | 4E   | 01001110 | N         | Uppercase N                         |
| 79   | 117  | 4F   | 01001111 | O         | Uppercase O                         |
| 80   | 120  | 50   | 01010000 | P         | Uppercase P                         |
| 81   | 121  | 51   | 01010001 | Q         | Uppercase Q                         |
| 82   | 122  | 52   | 01010010 | R         | Uppercase R                         |
| 83   | 123  | 53   | 01010011 | S         | Uppercase S                         |
| 84   | 124  | 54   | 01010100 | T         | Uppercase T                         |
| 85   | 125  | 55   | 01010101 | U         | Uppercase U                         |
| 86   | 126  | 56   | 01010110 | V         | Uppercase V                         |
| 87   | 127  | 57   | 01010111 | W         | Uppercase W                         |
| 88   | 130  | 58   | 01011000 | X         | Uppercase X                         |
| 89   | 131  | 59   | 01011001 | Y         | Uppercase Y                         |
| 90   | 132  | 5A   | 01011010 | Z         | Uppercase Z                         |
| 91   | 133  | 5B   | 01011011 | [         | Opening bracket                     |
| 92   | 134  | 5C   | 01011100 | \         | Backslash                           |
| 93   | 135  | 5D   | 01011101 | ]         | Closing bracket                     |
| 94   | 136  | 5E   | 01011110 | ^         | Caret - circumflex                  |
| 95   | 137  | 5F   | 01011111 | _         | Underscore                          |
| 96   | 140  | 60   | 01100000 | `         | Grave accent                        |
| 97   | 141  | 61   | 01100001 | a         | Lowercase a                         |
| 98   | 142  | 62   | 01100010 | b         | Lowercase b                         |
| 99   | 143  | 63   | 01100011 | c         | Lowercase c                         |
| 100  | 144  | 64   | 01100100 | d         | Lowercase d                         |
| 101  | 145  | 65   | 01100101 | e         | Lowercase e                         |
| 102  | 146  | 66   | 01100110 | f         | Lowercase f                         |
| 103  | 147  | 67   | 01100111 | g         | Lowercase g                         |
| 104  | 150  | 68   | 01101000 | h         | Lowercase h                         |
| 105  | 151  | 69   | 01101001 | i         | Lowercase i                         |
| 106  | 152  | 6A   | 01101010 | j         | Lowercase j                         |
| 107  | 153  | 6B   | 01101011 | k         | Lowercase k                         |
| 108  | 154  | 6C   | 01101100 | l         | Lowercase l                         |
| 109  | 155  | 6D   | 01101101 | m         | Lowercase m                         |
| 110  | 156  | 6E   | 01101110 | n         | Lowercase n                         |
| 111  | 157  | 6F   | 01101111 | o         | Lowercase o                         |
| 112  | 160  | 70   | 01110000 | p         | Lowercase p                         |
| 113  | 161  | 71   | 01110001 | q         | Lowercase q                         |
| 114  | 162  | 72   | 01110010 | r         | Lowercase r                         |
| 115  | 163  | 73   | 01110011 | s         | Lowercase s                         |
| 116  | 164  | 74   | 01110100 | t         | Lowercase t                         |
| 117  | 165  | 75   | 01110101 | u         | Lowercase u                         |
| 118  | 166  | 76   | 01110110 | v         | Lowercase v                         |
| 119  | 167  | 77   | 01110111 | w         | Lowercase w                         |
| 120  | 170  | 78   | 01111000 | x         | Lowercase x                         |
| 121  | 171  | 79   | 01111001 | y         | Lowercase y                         |
| 122  | 172  | 7A   | 01111010 | z         | Lowercase z                         |
| 123  | 173  | 7B   | 01111011 | {         | Opening brace                       |
| 124  | 174  | 7C   | 01111100 | \|        | Vertical bar                        |
| 125  | 175  | 7D   | 01111101 | }         | Closing brace                       |
| 126  | 176  | 7E   | 01111110 | ~         | Equivalency sign (tilde)            |
| 127  | 177  | 7F   | 01111111 |           | Delete                              |

像这样的一段字符串：

> Hi，Boy！

转换成ASCII码，用十六进制数表示为：

```python
48 69 2C 42 6F 79 21
```

其中逗号的编码为 2C，感叹号的编码为 21。

在ASCII码中大写字母和小写字母相差20h，给编程在某种程度上带来方便。

## 二、ASCII码的扩展

扩展一倍，引入8个bit 2\*\*8 = 256

>非拉丁字母的希腊文（Greek）、阿拉伯文（Arabic）、希伯来文（Hebrew）

在这种字符集中，00h-7Fh与之前的ASCII保持一致，80h-FFh可以用来引入其它的字符，如下所示：

| DEC  | OCT  | HEX  | BIN      | 缩写/符号 | 描述                                       |
| ---- | ---- | ---- | -------- | --------- | ------------------------------------------ |
| 128  | 200  | 80   | 10000000 | €         | Euro sign                                  |
| 129  | 201  | 81   | 10000001 |           |                                            |
| 130  | 202  | 82   | 10000010 | ‚         | Single low-9 quotation mark                |
| 131  | 203  | 83   | 10000011 | ƒ         | Latin small letter f with hook             |
| 132  | 204  | 84   | 10000100 | „         | Double low-9 quotation mark                |
| 133  | 205  | 85   | 10000101 | …         | Horizontal ellipsis                        |
| 134  | 206  | 86   | 10000110 | †         | Dagger                                     |
| 135  | 207  | 87   | 10000111 | ‡         | Double dagger                              |
| 136  | 210  | 88   | 10001000 | ˆ         | Modifier letter circumflex accent          |
| 137  | 211  | 89   | 10001001 | ‰         | Per mille sign                             |
| 138  | 212  | 8A   | 10001010 | Š         | Latin capital letter S with caron          |
| 139  | 213  | 8B   | 10001011 | ‹         | Single left-pointing angle quotation       |
| 140  | 214  | 8C   | 10001100 | Œ         | Latin capital ligature OE                  |
| 141  | 215  | 8D   | 10001101 |           |                                            |
| 142  | 216  | 8E   | 10001110 | Ž         | Latin capital letter Z with caron          |
| 143  | 217  | 8F   | 10001111 |           |                                            |
| 144  | 220  | 90   | 10010000 |           |                                            |
| 145  | 221  | 91   | 10010001 | ‘         | Left single quotation mark                 |
| 146  | 222  | 92   | 10010010 | ’         | Right single quotation mark                |
| 147  | 223  | 93   | 10010011 | “         | Left double quotation mark                 |
| 148  | 224  | 94   | 10010100 | ”         | Right double quotation mark                |
| 149  | 225  | 95   | 10010101 | •         | Bullet                                     |
| 150  | 226  | 96   | 10010110 | –         | En dash                                    |
| 151  | 227  | 97   | 10010111 | —         | Em dash                                    |
| 152  | 230  | 98   | 10011000 | ˜         | Small tilde                                |
| 153  | 231  | 99   | 10011001 | ™         | Trade mark sign                            |
| 154  | 232  | 9A   | 10011010 | š         | Latin small letter S with caron            |
| 155  | 233  | 9B   | 10011011 | ›         | Single right-pointing angle quotation mark |
| 156  | 234  | 9C   | 10011100 | œ         | Latin small ligature oe                    |
| 157  | 235  | 9D   | 10011101 |           |                                            |
| 158  | 236  | 9E   | 10011110 | ž         | Latin small letter z with caron            |
| 159  | 237  | 9F   | 10011111 | Ÿ         | Latin capital letter Y with diaeresis      |
| 160  | 240  | A0   | 10100000 |           | Non-breaking space                         |
| 161  | 241  | A1   | 10100001 | ¡         | Inverted exclamation mark                  |
| 162  | 242  | A2   | 10100010 | ¢         | Cent sign                                  |
| 163  | 243  | A3   | 10100011 | £         | Pound sign                                 |
| 164  | 244  | A4   | 10100100 | ¤         | Currency sign                              |
| 165  | 245  | A5   | 10100101 | ¥         | Yen sign                                   |
| 166  | 246  | A6   | 10100110 | ¦         | Pipe, Broken vertical bar                  |
| 167  | 247  | A7   | 10100111 | §         | Section sign                               |
| 168  | 250  | A8   | 10101000 | ¨         | Spacing diaeresis - umlaut                 |
| 169  | 251  | A9   | 10101001 | ©         | Copyright sign                             |
| 170  | 252  | AA   | 10101010 | ª         | Feminine ordinal indicator                 |
| 171  | 253  | AB   | 10101011 | «         | Left double angle quotes                   |
| 172  | 254  | AC   | 10101100 | ¬         | Not sign                                   |
| 173  | 255  | AD   | 10101101 | ­         | Soft hyphen                                |
| 174  | 256  | AE   | 10101110 | ®         | Registered trade mark sign                 |
| 175  | 257  | AF   | 10101111 | ¯         | Spacing macron - overline                  |
| 176  | 260  | B0   | 10110000 | °         | Degree sign                                |
| 177  | 261  | B1   | 10110001 | ±         | Plus-or-minus sign                         |
| 178  | 262  | B2   | 10110010 | ²         | Superscript two - squared                  |
| 179  | 263  | B3   | 10110011 | ³         | Superscript three - cubed                  |
| 180  | 264  | B4   | 10110100 | ´         | Acute accent - spacing acute               |
| 181  | 265  | B5   | 10110101 | µ         | Micro sign                                 |
| 182  | 266  | B6   | 10110110 | ¶         | Pilcrow sign - paragraph sign              |
| 183  | 267  | B7   | 10110111 | ·         | Middle dot - Georgian comma                |
| 184  | 270  | B8   | 10111000 | ¸         | Spacing cedilla                            |
| 185  | 271  | B9   | 10111001 | ¹         | Superscript one                            |
| 186  | 272  | BA   | 10111010 | º         | Masculine ordinal indicator                |
| 187  | 273  | BB   | 10111011 | »         | Right double angle quotes                  |
| 188  | 274  | BC   | 10111100 | ¼         | Fraction one quarter                       |
| 189  | 275  | BD   | 10111101 | ½         | Fraction one half                          |
| 190  | 276  | BE   | 10111110 | ¾         | Fraction three quarters                    |
| 191  | 277  | BF   | 10111111 | ¿         | Inverted question mark                     |
| 192  | 300  | C0   | 11000000 | À         | Latin capital letter A with grave          |
| 193  | 301  | C1   | 11000001 | Á         | Latin capital letter A with acute          |
| 194  | 302  | C2   | 11000010 | Â         | Latin capital letter A with circumflex     |
| 195  | 303  | C3   | 11000011 | Ã         | Latin capital letter A with tilde          |
| 196  | 304  | C4   | 11000100 | Ä         | Latin capital letter A with diaeresis      |
| 197  | 305  | C5   | 11000101 | Å         | Latin capital letter A with ring above     |
| 198  | 306  | C6   | 11000110 | Æ         | Latin capital letter AE                    |
| 199  | 307  | C7   | 11000111 | Ç         | Latin capital letter C with cedilla        |
| 200  | 310  | C8   | 11001000 | È         | Latin capital letter E with grave          |
| 201  | 311  | C9   | 11001001 | É         | Latin capital letter E with acute          |
| 202  | 312  | CA   | 11001010 | Ê         | Latin capital letter E with circumflex     |
| 203  | 313  | CB   | 11001011 | Ë         | Latin capital letter E with diaeresis      |
| 204  | 314  | CC   | 11001100 | Ì         | Latin capital letter I with grave          |
| 205  | 315  | CD   | 11001101 | Í         | Latin capital letter I with acute          |
| 206  | 316  | CE   | 11001110 | Î         | Latin capital letter I with circumflex     |
| 207  | 317  | CF   | 11001111 | Ï         | Latin capital letter I with diaeresis      |
| 208  | 320  | D0   | 11010000 | Ð         | Latin capital letter ETH                   |
| 209  | 321  | D1   | 11010001 | Ñ         | Latin capital letter N with tilde          |
| 210  | 322  | D2   | 11010010 | Ò         | Latin capital letter O with grave          |
| 211  | 323  | D3   | 11010011 | Ó         | Latin capital letter O with acute          |
| 212  | 324  | D4   | 11010100 | Ô         | Latin capital letter O with circumflex     |
| 213  | 325  | D5   | 11010101 | Õ         | Latin capital letter O with tilde          |
| 214  | 326  | D6   | 11010110 | Ö         | Latin capital letter O with diaeresis      |
| 215  | 327  | D7   | 11010111 | ×         | Multiplication sign                        |
| 216  | 330  | D8   | 11011000 | Ø         | Latin capital letter O with slash          |
| 217  | 331  | D9   | 11011001 | Ù         | Latin capital letter U with grave          |
| 218  | 332  | DA   | 11011010 | Ú         | Latin capital letter U with acute          |
| 219  | 333  | DB   | 11011011 | Û         | Latin capital letter U with circumflex     |
| 220  | 334  | DC   | 11011100 | Ü         | Latin capital letter U with diaeresis      |
| 221  | 335  | DD   | 11011101 | Ý         | Latin capital letter Y with acute          |
| 222  | 336  | DE   | 11011110 | Þ         | Latin capital letter THORN                 |
| 223  | 337  | DF   | 11011111 | ß         | Latin small letter sharp s - ess-zed       |
| 224  | 340  | E0   | 11100000 | à         | Latin small letter a with grave            |
| 225  | 341  | E1   | 11100001 | á         | Latin small letter a with acute            |
| 226  | 342  | E2   | 11100010 | â         | Latin small letter a with circumflex       |
| 227  | 343  | E3   | 11100011 | ã         | Latin small letter a with tilde            |
| 228  | 344  | E4   | 11100100 | ä         | Latin small letter a with diaeresis        |
| 229  | 345  | E5   | 11100101 | å         | Latin small letter a with ring above       |
| 230  | 346  | E6   | 11100110 | æ         | Latin small letter ae                      |
| 231  | 347  | E7   | 11100111 | ç         | Latin small letter c with cedilla          |
| 232  | 350  | E8   | 11101000 | è         | Latin small letter e with grave            |
| 233  | 351  | E9   | 11101001 | é         | Latin small letter e with acute            |
| 234  | 352  | EA   | 11101010 | ê         | Latin small letter e with circumflex       |
| 235  | 353  | EB   | 11101011 | ë         | Latin small letter e with diaeresis        |
| 236  | 354  | EC   | 11101100 | ì         | Latin small letter i with grave            |
| 237  | 355  | ED   | 11101101 | í         | Latin small letter i with acute            |
| 238  | 356  | EE   | 11101110 | î         | Latin small letter i with circumflex       |
| 239  | 357  | EF   | 11101111 | ï         | Latin small letter i with diaeresis        |
| 240  | 360  | F0   | 11110000 | ð         | Latin small letter eth                     |
| 241  | 361  | F1   | 11110001 | ñ         | Latin small letter n with tilde            |
| 242  | 362  | F2   | 11110010 | ò         | Latin small letter o with grave            |
| 243  | 363  | F3   | 11110011 | ó         | Latin small letter o with acute            |
| 244  | 364  | F4   | 11110100 | ô         | Latin small letter o with circumflex       |
| 245  | 365  | F5   | 11110101 | õ         | Latin small letter o with tilde            |
| 246  | 366  | F6   | 11110110 | ö         | Latin small letter o with diaeresis        |
| 247  | 367  | F7   | 11110111 | ÷         | Division sign                              |
| 248  | 370  | F8   | 11111000 | ø         | Latin small letter o with slash            |
| 249  | 371  | F9   | 11111001 | ù         | Latin small letter u with grave            |
| 250  | 372  | FA   | 11111010 | ú         | Latin small letter u with acute            |
| 251  | 373  | FB   | 11111011 | û         | Latin small letter u with circumflex       |
| 252  | 374  | FC   | 11111100 | ü         | Latin small letter u with diaeresis        |
| 253  | 375  | FD   | 11111101 | ý         | Latin small letter y with acute            |
| 254  | 376  | FE   | 11111110 | þ         | Latin small letter thorn                   |
| 255  | 377  | FF   | 11111111 | ÿ         | Latin small letter y with diaeresis        |

遗憾的是随着不断的发展，ASCII码扩展表出现很多不同的版本，严重影响了编码的一致性。

从1988年开始，几大著名计算机公司合作研究出一种用来替代ASCII码的编码系统，取名位Unicode（统一化字符编码标准），这是一套独一无二的编码系统，可用于世界上所有的语言文字。

相较于ASCII编码系统，Unicode采用了16位编码，每一个字符需要2个字节。也就是Unicode的字符编码范围为0000h-FFFFh，总共可以表示65536个不同的字符。不过这是最初的体系，这样要表示各种语言中所有的字符是远远不够的，定义了一组附加字符编码，附加字符编码采用2个16位来表示，这样最多可以定义1048576个附加字符，也就是说Unicode最多可以表示4个字节。

Unicode并不是从零开始设计的，它在ASCII的基础上进行设计，所以前128个字符，0000h-007Fh对应于ASCII码字符，但是Unicode这样做意味着之前的ASCII码需要一个字节存储的字符，对应于Unicode需要两个字节存储，这样就付出了存储空间的代价。

## 三、Unicode与UTF8

Unicode实际就是一个字符集，就是一个字符对应一个码点（十六进制数）：

|      | 00   | 01   | 02   | 03   | 04   | 05   | 06   | 07   | 08   | 09   | 0A   | 0B   | 0C   | 0D   | 0E   | 0F   | 10   | 11   | 12   | 13   | 14   | 15   | 16   | 17   | 18   | 19   | 1A   | 1B   | 1C   | 1D   | 1E   | 1F   |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 2C00 | Ⰰ    | Ⰱ    | Ⰲ    | Ⰳ    | Ⰴ    | Ⰵ    | Ⰶ    | Ⰷ    | Ⰸ    | Ⰹ    | Ⰺ    | Ⰻ    | Ⰼ    | Ⰽ    | Ⰾ    | Ⰿ    | Ⱀ    | Ⱁ    | Ⱂ    | Ⱃ    | Ⱄ    | Ⱅ    | Ⱆ    | Ⱇ    | Ⱈ    | Ⱉ    | Ⱊ    | Ⱋ    | Ⱌ    | Ⱍ    | Ⱎ    | Ⱏ    |
| 2C20 | Ⱐ    | Ⱑ    | Ⱒ    | Ⱓ    | Ⱔ    | Ⱕ    | Ⱖ    | Ⱗ    | Ⱘ    | Ⱙ    | Ⱚ    | Ⱛ    | Ⱜ    | Ⱝ    | Ⱞ    | Ⱟ    | ⰰ    | ⰱ    | ⰲ    | ⰳ    | ⰴ    | ⰵ    | ⰶ    | ⰷ    | ⰸ    | ⰹ    | ⰺ    | ⰻ    | ⰼ    | ⰽ    | ⰾ    | ⰿ    |
| 2C40 | ⱀ    | ⱁ    | ⱂ    | ⱃ    | ⱄ    | ⱅ    | ⱆ    | ⱇ    | ⱈ    | ⱉ    | ⱊ    | ⱋ    | ⱌ    | ⱍ    | ⱎ    | ⱏ    | ⱐ    | ⱑ    | ⱒ    | ⱓ    | ⱔ    | ⱕ    | ⱖ    | ⱗ    | ⱘ    | ⱙ    | ⱚ    | ⱛ    | ⱜ    | ⱝ    | ⱞ    | ⱟ    |
| 2C60 | Ⱡ    | ⱡ    | Ɫ    | Ᵽ    | Ɽ    | ⱥ    | ⱦ    | Ⱨ    | ⱨ    | Ⱪ    | ⱪ    | Ⱬ    | ⱬ    | Ɑ    | Ɱ    | Ɐ    | Ɒ    | ⱱ    | Ⱳ    | ⱳ    | ⱴ    | Ⱶ    | ⱶ    | ⱷ    | ⱸ    | ⱹ    | ⱺ    | ⱻ    | ⱼ    | ⱽ    | Ȿ    | Ɀ    |
| 2C80 | Ⲁ    | ⲁ    | Ⲃ    | ⲃ    | Ⲅ    | ⲅ    | Ⲇ    | ⲇ    | Ⲉ    | ⲉ    | Ⲋ    | ⲋ    | Ⲍ    | ⲍ    | Ⲏ    | ⲏ    | Ⲑ    | ⲑ    | Ⲓ    | ⲓ    | Ⲕ    | ⲕ    | Ⲗ    | ⲗ    | Ⲙ    | ⲙ    | Ⲛ    | ⲛ    | Ⲝ    | ⲝ    | Ⲟ    | ⲟ    |
| 2CA0 | Ⲡ    | ⲡ    | Ⲣ    | ⲣ    | Ⲥ    | ⲥ    | Ⲧ    | ⲧ    | Ⲩ    | ⲩ    | Ⲫ    | ⲫ    | Ⲭ    | ⲭ    | Ⲯ    | ⲯ    | Ⲱ    | ⲱ    | Ⲳ    | ⲳ    | Ⲵ    | ⲵ    | Ⲷ    | ⲷ    | Ⲹ    | ⲹ    | Ⲻ    | ⲻ    | Ⲽ    | ⲽ    | Ⲿ    | ⲿ    |
| 2CC0 | Ⳁ    | ⳁ    | Ⳃ    | ⳃ    | Ⳅ    | ⳅ    | Ⳇ    | ⳇ    | Ⳉ    | ⳉ    | Ⳋ    | ⳋ    | Ⳍ    | ⳍ    | Ⳏ    | ⳏ    | Ⳑ    | ⳑ    | Ⳓ    | ⳓ    | Ⳕ    | ⳕ    | Ⳗ    | ⳗ    | Ⳙ    | ⳙ    | Ⳛ    | ⳛ    | Ⳝ    | ⳝ    | Ⳟ    | ⳟ    |
| 2CE0 | Ⳡ    | ⳡ    | Ⳣ    | ⳣ    | ⳤ    | ⳥    | ⳦    | ⳧    | ⳨    | ⳩    | ⳪    | Ⳬ    | ⳬ    | Ⳮ    | ⳮ    | ⳯    | ⳰    | ⳱    | Ⳳ    | ⳳ    | ⳴    | ⳵    | ⳶    | ⳷    | ⳸    | ⳹    | ⳺    | ⳻    | ⳼    | ⳽    | ⳾    | ⳿    |
| 2D00 | ⴀ    | ⴁ    | ⴂ    | ⴃ    | ⴄ    | ⴅ    | ⴆ    | ⴇ    | ⴈ    | ⴉ    | ⴊ    | ⴋ    | ⴌ    | ⴍ    | ⴎ    | ⴏ    | ⴐ    | ⴑ    | ⴒ    | ⴓ    | ⴔ    | ⴕ    | ⴖ    | ⴗ    | ⴘ    | ⴙ    | ⴚ    | ⴛ    | ⴜ    | ⴝ    | ⴞ    | ⴟ    |
| 2D20 | ⴠ    | ⴡ    | ⴢ    | ⴣ    | ⴤ    | ⴥ    | ⴦    | ⴧ    | ⴨    | ⴩    | ⴪    | ⴫    | ⴬    | ⴭ    | ⴮    | ⴯    | ⴰ    | ⴱ    | ⴲ    | ⴳ    | ⴴ    | ⴵ    | ⴶ    | ⴷ    | ⴸ    | ⴹ    | ⴺ    | ⴻ    | ⴼ    | ⴽ    | ⴾ    | ⴿ    |
| 2D40 | ⵀ    | ⵁ    | ⵂ    | ⵃ    | ⵄ    | ⵅ    | ⵆ    | ⵇ    | ⵈ    | ⵉ    | ⵊ    | ⵋ    | ⵌ    | ⵍ    | ⵎ    | ⵏ    | ⵐ    | ⵑ    | ⵒ    | ⵓ    | ⵔ    | ⵕ    | ⵖ    | ⵗ    | ⵘ    | ⵙ    | ⵚ    | ⵛ    | ⵜ    | ⵝ    | ⵞ    | ⵟ    |
| 2D60 | ⵠ    | ⵡ    | ⵢ    | ⵣ    | ⵤ    | ⵥ    | ⵦ    | ⵧ    | ⵨    | ⵩    | ⵪    | ⵫    | ⵬    | ⵭    | ⵮    | ⵯ    | ⵰    | ⵱    | ⵲    | ⵳    | ⵴    | ⵵    | ⵶    | ⵷    | ⵸    | ⵹    | ⵺    | ⵻    | ⵼    | ⵽    | ⵾    | ⵿    |
| 2D80 | ⶀ    | ⶁ    | ⶂ    | ⶃ    | ⶄ    | ⶅ    | ⶆ    | ⶇ    | ⶈ    | ⶉ    | ⶊ    | ⶋ    | ⶌ    | ⶍ    | ⶎ    | ⶏ    | ⶐ    | ⶑ    | ⶒ    | ⶓ    | ⶔ    | ⶕ    | ⶖ    | ⶗    | ⶘    | ⶙    | ⶚    | ⶛    | ⶜    | ⶝    | ⶞    | ⶟    |
| 2DA0 | ⶠ    | ⶡ    | ⶢ    | ⶣ    | ⶤ    | ⶥ    | ⶦ    | ⶧    | ⶨ    | ⶩ    | ⶪ    | ⶫ    | ⶬ    | ⶭ    | ⶮ    | ⶯    | ⶰ    | ⶱ    | ⶲ    | ⶳ    | ⶴ    | ⶵ    | ⶶ    | ⶷    | ⶸ    | ⶹ    | ⶺ    | ⶻ    | ⶼ    | ⶽ    | ⶾ    | ⶿    |
| 2DC0 | ⷀ    | ⷁ    | ⷂ    | ⷃ    | ⷄ    | ⷅ    | ⷆ    | ⷇    | ⷈ    | ⷉ    | ⷊ    | ⷋ    | ⷌ    | ⷍ    | ⷎ    | ⷏    | ⷐ    | ⷑ    | ⷒ    | ⷓ    | ⷔ    | ⷕ    | ⷖ    | ⷗    | ⷘ    | ⷙ    | ⷚ    | ⷛ    | ⷜ    | ⷝ    | ⷞ    | ⷟    |
| 2DE0 | ⷠ    | ⷡ    | ⷢ    | ⷣ    | ⷤ    | ⷥ    | ⷦ    | ⷧ    | ⷨ    | ⷩ    | ⷪ    | ⷫ    | ⷬ    | ⷭ    | ⷮ    | ⷯ    | ⷰ    | ⷱ    | ⷲ    | ⷳ    | ⷴ    | ⷵ    | ⷶ    | ⷷ    | ⷸ    | ⷹ    | ⷺ    | ⷻ    | ⷼ    | ⷽ    | ⷾ    | ⷿ    |
| 2E00 | ⸀    | ⸁    | ⸂    | ⸃    | ⸄    | ⸅    | ⸆    | ⸇    | ⸈    | ⸉    | ⸊    | ⸋    | ⸌    | ⸍    | ⸎    | ⸏    | ⸐    | ⸑    | ⸒    | ⸓    | ⸔    | ⸕    | ⸖    | ⸗    | ⸘    | ⸙    | ⸚    | ⸛    | ⸜    | ⸝    | ⸞    | ⸟    |
| 2E20 | ⸠    | ⸡    | ⸢    | ⸣    | ⸤    | ⸥    | ⸦    | ⸧    | ⸨    | ⸩    | ⸪    | ⸫    | ⸬    | ⸭    | ⸮    | ⸯ    | ⸰    | ⸱    | ⸲    | ⸳    | ⸴    | ⸵    | ⸶    | ⸷    | ⸸    | ⸹    | ⸺    | ⸻    | ⸼    | ⸽    | ⸾    | ⸿    |
| 2E40 | ⹀    | ⹁    | ⹂    | ⹃    | ⹄    | ⹅    | ⹆    | ⹇    | ⹈    | ⹉    | ⹊    | ⹋    | ⹌    | ⹍    | ⹎    | ⹏    | ⹐    | ⹑    | ⹒    | ⹓    | ⹔    | ⹕    | ⹖    | ⹗    | ⹘    | ⹙    | ⹚    | ⹛    | ⹜    | ⹝    | ⹞    | ⹟    |
| 2E60 | ⹠    | ⹡    | ⹢    | ⹣    | ⹤    | ⹥    | ⹦    | ⹧    | ⹨    | ⹩    | ⹪    | ⹫    | ⹬    | ⹭    | ⹮    | ⹯    | ⹰    | ⹱    | ⹲    | ⹳    | ⹴    | ⹵    | ⹶    | ⹷    | ⹸    | ⹹    | ⹺    | ⹻    | ⹼    | ⹽    | ⹾    | ⹿    |
| 2E80 | ⺀   | ⺁   | ⺂   | ⺃   | ⺄   | ⺅   | ⺆   | ⺇   | ⺈   | ⺉   | ⺊   | ⺋   | ⺌   | ⺍   | ⺎   | ⺏   | ⺐   | ⺑   | ⺒   | ⺓   | ⺔   | ⺕   | ⺖   | ⺗   | ⺘   | ⺙   | ⺚   | ⺛   | ⺜   | ⺝   | ⺞   | ⺟   |
| 2EA0 | ⺠   | ⺡   | ⺢   | ⺣   | ⺤   | ⺥   | ⺦   | ⺧   | ⺨   | ⺩   | ⺪   | ⺫   | ⺬   | ⺭   | ⺮   | ⺯   | ⺰   | ⺱   | ⺲   | ⺳   | ⺴   | ⺵   | ⺶   | ⺷   | ⺸   | ⺹   | ⺺   | ⺻   | ⺼   | ⺽   | ⺾   | ⺿   |
| 2EC0 | ⻀   | ⻁   | ⻂   | ⻃   | ⻄   | ⻅   | ⻆   | ⻇   | ⻈   | ⻉   | ⻊   | ⻋   | ⻌   | ⻍   | ⻎   | ⻏   | ⻐   | ⻑   | ⻒   | ⻓   | ⻔   | ⻕   | ⻖   | ⻗   | ⻘   | ⻙   | ⻚   | ⻛   | ⻜   | ⻝   | ⻞   | ⻟   |
| 2EE0 | ⻠   | ⻡   | ⻢   | ⻣   | ⻤   | ⻥   | ⻦   | ⻧   | ⻨   | ⻩   | ⻪   | ⻫   | ⻬   | ⻭   | ⻮   | ⻯   | ⻰   | ⻱   | ⻲   | ⻳   | ⻴   | ⻵   | ⻶   | ⻷   | ⻸   | ⻹   | ⻺   | ⻻   | ⻼   | ⻽   | ⻾   | ⻿   |
| 2F00 | ⼀   | ⼁   | ⼂   | ⼃   | ⼄   | ⼅   | ⼆   | ⼇   | ⼈   | ⼉   | ⼊   | ⼋   | ⼌   | ⼍   | ⼎   | ⼏   | ⼐   | ⼑   | ⼒   | ⼓   | ⼔   | ⼕   | ⼖   | ⼗   | ⼘   | ⼙   | ⼚   | ⼛   | ⼜   | ⼝   | ⼞   | ⼟   |
| 2F20 | ⼠   | ⼡   | ⼢   | ⼣   | ⼤   | ⼥   | ⼦   | ⼧   | ⼨   | ⼩   | ⼪   | ⼫   | ⼬   | ⼭   | ⼮   | ⼯   | ⼰   | ⼱   | ⼲   | ⼳   | ⼴   | ⼵   | ⼶   | ⼷   | ⼸   | ⼹   | ⼺   | ⼻   | ⼼   | ⼽   | ⼾   | ⼿   |
| 2F40 | ⽀   | ⽁   | ⽂   | ⽃   | ⽄   | ⽅   | ⽆   | ⽇   | ⽈   | ⽉   | ⽊   | ⽋   | ⽌   | ⽍   | ⽎   | ⽏   | ⽐   | ⽑   | ⽒   | ⽓   | ⽔   | ⽕   | ⽖   | ⽗   | ⽘   | ⽙   | ⽚   | ⽛   | ⽜   | ⽝   | ⽞   | ⽟   |
| 2F60 | ⽠   | ⽡   | ⽢   | ⽣   | ⽤   | ⽥   | ⽦   | ⽧   | ⽨   | ⽩   | ⽪   | ⽫   | ⽬   | ⽭   | ⽮   | ⽯   | ⽰   | ⽱   | ⽲   | ⽳   | ⽴   | ⽵   | ⽶   | ⽷   | ⽸   | ⽹   | ⽺   | ⽻   | ⽼   | ⽽   | ⽾   | ⽿   |
| 2F80 | ⾀   | ⾁   | ⾂   | ⾃   | ⾄   | ⾅   | ⾆   | ⾇   | ⾈   | ⾉   | ⾊   | ⾋   | ⾌   | ⾍   | ⾎   | ⾏   | ⾐   | ⾑   | ⾒   | ⾓   | ⾔   | ⾕   | ⾖   | ⾗   | ⾘   | ⾙   | ⾚   | ⾛   | ⾜   | ⾝   | ⾞   | ⾟   |
| 2FA0 | ⾠   | ⾡   | ⾢   | ⾣   | ⾤   | ⾥   | ⾦   | ⾧   | ⾨   | ⾩   | ⾪   | ⾫   | ⾬   | ⾭   | ⾮   | ⾯   | ⾰   | ⾱   | ⾲   | ⾳   | ⾴   | ⾵   | ⾶   | ⾷   | ⾸   | ⾹   | ⾺   | ⾻   | ⾼   | ⾽   | ⾾   | ⾿   |
| 2FC0 | ⿀   | ⿁   | ⿂   | ⿃   | ⿄   | ⿅   | ⿆   | ⿇   | ⿈   | ⿉   | ⿊   | ⿋   | ⿌   | ⿍   | ⿎   | ⿏   | ⿐   | ⿑   | ⿒   | ⿓   | ⿔   | ⿕   | ⿖   | ⿗   | ⿘   | ⿙   | ⿚   | ⿛   | ⿜   | ⿝   | ⿞   | ⿟   |
| 2FE0 | ⿠   | ⿡   | ⿢   | ⿣   | ⿤   | ⿥   | ⿦   | ⿧   | ⿨   | ⿩   | ⿪   | ⿫   | ⿬   | ⿭   | ⿮   | ⿯   | ⿰   | ⿱   | ⿲   | ⿳   | ⿴   | ⿵   | ⿶   | ⿷   | ⿸   | ⿹   | ⿺   | ⿻   | ⿼   | ⿽   | ⿾   | ⿿   |

如上是一部分的Unicode字符集，完整版可参考：[Unicode字符集](http://www.tamasoft.co.jp/en/general-info/unicode.html)

比如：上面的`车`字，在Unicode的字符集中对应的码点是`2ECB`，接着就是将其转成二进制，存储在计算机中，这个步骤叫编码，按照一般的习惯就是直接将十六进制转成二进制即可，但是我们刚刚明明说了根据不同的情况存入，也就是能省则省的原则，因此，引出不同的编码规则，比如UTF8。

UTF-8的特点是对不同范围的字符使用不同长度的编码。对于0x00-0x7F之间的字符，UTF-8编码与ASCII编码完全相同。UTF-8编码的最大长度是4个字节。

| UCS-4（UNICODE）编码    | UTF-8字节流                                           |
| ----------------------- | ----------------------------------------------------- |
| U-00000000 – U-0000007F | 0xxxxxxx                                              |
| U-00000080 – U-000007FF | 110xxxxx 10xxxxxx                                     |
| U-00000800 – U-0000FFFF | 1110xxxx 10xxxxxx 10xxxxxx                            |
| U-00010000 – U-001FFFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx                   |
| U-00200000 – U-03FFFFFF | 111110xx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx          |
| U-04000000 – U-7FFFFFFF | 1111110x 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx |

对于`2ECB`这个码点在上面表格中的那个范围呢？

```python
# 转成十进制比较
2ECB = 2 * 16^3 + 14 * 16^2 + 12 * 16^1 + 11*16^0 = 11979
# 第三行
0000FFFF = 65535
# 第二行
000007FF = 2047
```

显然这个码点在第三行的范围：	

```python
 2    E    C    B
0010 1110 1100 1011   二进制的 2ECB
    0010   111011   001011    二进制的 2ECB
1110XXXX 10XXXXXX 10XXXXXX 模版（上表第三行）
11100010 10111011 10001011 代入模版
   E   2    B   B    8   B 
```

这就是将 U+2ECB 按照 UTF-8 编码为字节序列` E2BB8B` 的过程，也就是一个汉字占用3个字节。这就是UTF-8以 8 位为一个编码单位的可变长编码。会将一个码位编码为 1 到 4 个字节。

所以从上面我们可以看出：Unicode是一套字符集，字符与唯一码点的对应关系；而UTF8是编码规则，将具体的字符以何种方式进行存储。当然除了UTF8还有UTF-16、UTF-32等编码规则

















































