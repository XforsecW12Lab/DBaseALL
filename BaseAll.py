import base36, base58, base62, base64, base91
import py3base92 as base92
# color
from termcolor import colored
# argv
import sys

class baseAll:
    def __init__(self):
        # alphabet
        self.__baseAbDict = [
            r"!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_abcdefghijklmnopqrstuvwxyz{|}", # base92_ab
            ''.join(base91.base91_alphabet),                                                                # base91_ab
            base64._b85alphabet,                                                                            # base85_ab
            r"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",                            # base64_ab
            base62.CHARSET_DEFAULT,                                                                         # base62_ab
            base58.BITCOIN_ALPHABET,                                                                        # base58_ab
            base36.alphabet,                                                                                # base36_ab
            base64._b32alphabet,                                                                            # base32_ab
            r"0123456789abcdef"                                                                             # base16_ab
        ]

        # 解码函数
        self.__baseDecodeFunc = [
            base92.decode,
            base91.decode,
            base64.b85decode,
            base64.b64decode,
            base62.decodebytes,
            base58.b58decode,
            base36.loads,
            base64.b32decode,
            base64.b16decode,
        ]

        # 编码函数
        self.__encodeFunc = [
            base92.encode,
            base91.encode,
            base64.b85encode,
            base64.b64encode,
            base62.encodebytes,
            base58.b58encode,
            base36.dumps,
            base64.b32encode,
            base64.b16encode,
        ]

        # 信息标签
        self.__infoList = [
            'Base92',
            'Base91',
            'Base85',
            'Base64',
            'Base62',
            'Base58',
            'Base36',
            'Base32',
            'Base16',
        ]

    def encodeAll(self,encodeStr:str,alphabet:str=None) -> dict:
        # 统一设置
        lineLength = 64
        lineColor = 'green'
        # 返回值
        retDick = {}

        if alphabet is None or alphabet=='':
            print(colored('+' + '=' * lineLength + '+', lineColor))
            for index,oneFunc in enumerate(self.__encodeFunc):
                try:
                    # 编码类型
                    print(colored(self.__infoList[index], 'red', attrs=['bold']))
                    # 尝试编码
                    res  = oneFunc(encodeStr.encode())
                    retDick[self.__infoList[index]] = res
                    print(colored(res,'yellow',attrs=['bold']))
                except Exception as err:
                    print(colored('Can not encode on this Base! Error:','blue'))
                    print(colored(err,'blue'))
                # 底部横线
                print(colored('+' + '=' * lineLength + '+', lineColor))
        else:
            newAlphabetLen = len(alphabet)
            # 根据长度判断alphabet
            for index, oneAb in enumerate(self.__baseAbDict):
                if newAlphabetLen == len(oneAb):
                    # 尝试转换后进行decode
                    print('May ' + colored(self.__infoList[index], 'red',
                                           attrs=['bold']) + ' alphabet. Try to Translate And encode:')
                    if type(oneAb) == bytes:
                        oneAb = bytes.decode(oneAb)
                    trans = str.maketrans(alphabet, oneAb)
                    res = self.__encodeFunc[index](encodeStr.translate(trans).encode())
                    # 友好打印
                    print('Res: ' + colored(res, 'yellow', attrs=['bold']))
        return retDick



    def baseDecodeAll(self,decodeStr:str,alphabet:str=None) -> dict:
        # 统一设置
        lineLength = 64
        lineColor = 'blue'
        findFlagList = []
        flagList = []
        isprintTableList = []
        # 返回结果，用于模块间调用
        retDick = {}

        if alphabet is None or alphabet=='':
            print(colored('+' + '=' * lineLength + '+\n' , lineColor))
            for index,oneFunc in enumerate(self.__baseDecodeFunc):
                try:
                    # 友好打印
                    print(colored(self.__infoList[index], 'red', attrs=['bold']))
                    # 尝试base计算
                    res = oneFunc(decodeStr)
                    print('Res: ' + colored(res,'yellow',attrs=['bold']))
                    # 返回值
                    retDick[self.__infoList[index]] = res
                    # flag确认
                    if str(res).find('flag')!=-1:
                        print(colored(' '*12+'!!!Find Flag!!!'+' '*12,'red','on_white',attrs=['bold','underline']))
                        findFlagList.append(index)
                        flagList.append(res)
                    # checkPrintTable
                    if res.isascii():
                        isprintTableList.append(index)

                except Exception as ex:
                    # 失败友好打印
                    print(colored('Can Not Decode On This Base! Error:',lineColor))
                    print(colored(ex.args[0],'blue'))
                # 底部横线
                print(colored('\n+' + '=' * lineLength + '+\n', lineColor))
        else:
            newAlphabetLen = len(alphabet)
            # 根据长度判断alphabet
            for index,oneAb in enumerate(self.__baseAbDict):
                if newAlphabetLen == len(oneAb):
                    # 尝试转换后进行decode
                    print('May ' + colored(self.__infoList[index], 'red', attrs=['bold']) + ' alphabet. Try to Translate And Decode:')
                    if type(oneAb) == bytes :
                        oneAb = bytes.decode(oneAb)
                    trans = str.maketrans(alphabet,oneAb)
                    # 尝试对应解码
                    res = self.__baseDecodeFunc[index](decodeStr.translate(trans))
                    # 友好打印
                    print('Res: ' + colored(res,'yellow',attrs=['bold']))

        # 均为可打印字符提示
        if len(isprintTableList) != 0:
            print(colored('*' * 64, 'blue', attrs=['bold']))
            print(colored('May True Res In: ', 'blue', attrs=['bold']))
            for oneIndex in isprintTableList:
                print(colored(self.__infoList[oneIndex], 'red', attrs=['bold']) + ' : ' + str(retDick[self.__infoList[oneIndex]]))
            print(colored('*' * 64, 'blue', attrs=['bold']))

        # 找到flag提示
        if len(findFlagList) != 0:
            print(colored('*' * 64, 'red', attrs=['bold']))
            print(colored('Find flag in: ', 'red', attrs=['bold']))
            for index,oneIndex in enumerate(findFlagList):
                print(colored(self.__infoList[oneIndex], 'red', attrs=['bold']) + ' : ' + colored(flagList[index], 'yellow', attrs=['bold']))
            print(colored('*' * 64, 'red', attrs=['bold']))
        return retDick

def banner():
    print(colored(r'''

██████╗     ██████╗  █████╗ ███████╗███████╗ █████╗ ██╗     ██╗     
██╔══██╗    ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██║     ██║     
██║  ██║    ██████╔╝███████║███████╗█████╗  ███████║██║     ██║     
██║  ██║    ██╔══██╗██╔══██║╚════██║██╔══╝  ██╔══██║██║     ██║     
██████╔╝    ██████╔╝██║  ██║███████║███████╗██║  ██║███████╗███████╗
╚═════╝     ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝  w12
''','red',attrs=['bold']))
    print(colored('Can use args to do it. Like: BaseAll.py ZmxhZ2FzZGZhc2RmYXNkZg== {{alphabet}}','yellow',attrs=['bold']))

if __name__ == '__main__':
    banner()
    if len(sys.argv) > 2:
        baseAll().baseDecodeAll(sys.argv[1],sys.argv[2])
    elif len(sys.argv) == 1:
        decodeStr = input('Input need decode string >> ')
        alphabet = input('Input new Alphabet (Can don\'t input to use Default) >> ')
        baseAll().baseDecodeAll(decodeStr,alphabet)
    else :
        baseAll().baseDecodeAll(sys.argv[1])
