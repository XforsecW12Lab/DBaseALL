import base36, base58, base62, base64, base91
import py3base92 as base92
# color
from termcolor import colored
# argv
import sys

class baseAll:
    def __init__(self):
        self.baseAbDict = [
            r"!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_abcdefghijklmnopqrstuvwxyz{|}", # base92_ab
            ''.join(base91.base91_alphabet),                                                                # base91_ab
            base64._b85alphabet,                                                                            # base85_ab
            r"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",                            # base64_ab
            base62.CHARSET_DEFAULT,                                                                         # base62_ab
            base58.BITCOIN_ALPHABET,                                                                         # base58_ab
            base36.alphabet,                                                                                # base36_ab
            base64._b32alphabet,                                                                            # base32_ab
            r"0123456789abcdef"                                                                             # base16_ab
        ]
        '''
        self.bRes = [
            # b16_res,
            # b32_res,
            # b36_res,
            # b58_res,
            # b62_res,
            # b64_res,
            # b85_res,
            # b91_res,
            # b92_res
        ]
        '''
        self.baseDecodeFunc = [
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
        self.infoList = [
            'Base'+colored('92','red',attrs=['bold']),
            'Base'+colored('91','red',attrs=['bold']),
            'Base'+colored('85','red',attrs=['bold']),
            'Base'+colored('64','red',attrs=['bold']),
            'Base'+colored('62','red',attrs=['bold']),
            'Base'+colored('58','red',attrs=['bold']),
            'Base'+colored('36','red',attrs=['bold']),
            'Base'+colored('32','red',attrs=['bold']),
            'Base'+colored('16','red',attrs=['bold']),
        ]

    def baseDecodeAll(self,decodeStr:str,alphabet:str=None):
        # 统一设置
        lineLength = 64
        lineColor = 'blue'
        findFlagList = []
        flagList = []
        isprintTableList = []

        if alphabet is None or alphabet=='':
            print(colored('+' + '=' * lineLength + '+\n' , 'blue'))
            for index,oneFunc in enumerate(self.baseDecodeFunc):
                try:
                    # 友好打印
                    print(self.infoList[index])
                    # 尝试base计算
                    res = oneFunc(decodeStr)
                    print('Res: ' + colored(res,'yellow',attrs=['bold']))

                    # flag确认
                    if str(res).find('flag')!=-1:
                        print(colored(' '*12+'!!!Find Flag!!!'+' '*12,'red','on_white',attrs=['bold','underline']))
                        findFlagList.append(index)
                        flagList.append(res)
                    # checkPrintTable
                    if str(res).isprintable():
                        isprintTableList.append(index)
                    print(colored('\n+' + '=' * lineLength + '+\n',lineColor))

                except Exception as ex:
                    # 失败友好打印
                    print(colored('Can Not Decode On This Base! Error:',lineColor))
                    print(colored(ex.args[0],'blue'))
                    print(colored('\n+' + '=' * lineLength + '+\n', lineColor))
        else:
            newAlphabetLen = len(alphabet)
            # 根据长度判断alphabet
            for index,oneAb in enumerate(self.baseAbDict):
                if newAlphabetLen == len(oneAb):
                    # 尝试转换后进行decode
                    print('May '+self.infoList[index]+' alphabet. Try to Translate And Decode:')
                    if type(oneAb) == bytes :
                        oneAb = bytes.decode(oneAb)
                    trans = str.maketrans(alphabet,oneAb)
                    # 尝试对应解码
                    res = self.baseDecodeFunc[index](decodeStr.translate(trans))
                    # 友好打印
                    print('Res: ' + colored(res,'yellow',attrs=['bold']))
        # 均为可打印字符提示
        if len(isprintTableList) != 0:
            print(colored('*' * 64, 'blue', attrs=['bold']))
            print(colored('May True Res In: ', 'blue', attrs=['bold']), end='')
            for oneIndex in findFlagList:
                print(self.infoList[oneIndex], end=' ')
            print(colored('\n' + '*' * 64, 'blue', attrs=['bold']))
        # 找到flag提示
        if len(findFlagList) != 0:
            print(colored('*' * 64, 'red', attrs=['bold']))
            print(colored('Find flag in: ', 'red', attrs=['bold']))
            for index,oneIndex in enumerate(findFlagList):
                print(self.infoList[oneIndex] + ' : ' + colored(flagList[index],'yellow',attrs=['bold']))
            print(colored('*' * 64, 'red', attrs=['bold']))

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
