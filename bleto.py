import pyautogui as py
import time

time.sleep(5)

py.PAUSE = 4



import pandas as pd

tabela = pd.read_csv("cadastro1.csv")


for linha in tabela.index:


    py.click(x=221, y=217)
    py.click(x=250, y=453)

    py.scroll(-500)
    py.click(x=250, y=342)

    codigo = str(tabela.loc[linha, "nome"])    
    py.write(str(codigo))
    py.press('enter')

    py.click(x=397, y=527)

    py.PAUSE = 0.3
    
    py.press('down')
    py.press('down')
    py.press('down')
    py.press('down')
    py.press('down')
    py.press('down')
    py.press('down')
    py.press('down')

    py.PAUSE = 3

    py.click(x=520, y=531)
    py.write(str(tabela.loc[linha, "num_boleto"]))

    py.click(x=754, y=527)
    py.press('backspace')
    py.write(str(tabela.loc[linha, "valor"]))  

    py.click(x=560, y=609)
    py.press('backspace')
    py.write(str(tabela.loc[linha, "data"]))

    py.scroll(-800)
    py.click(x=439, y=423)
    py.click(x=326, y=514)
    py.click(x=534, y=517)
    py.press('backspace')
    py.write('20')
    py.click(x=240, y=617)
    py.press('backspace')
    py.write('2')

    py.scroll(-300)

    py.click(x=401, y=572)
    py.click(x=574, y=638)
    py.press('down')
    py.click(x=814, y=669)

    py.scroll(-300)

    py.click(x=490, y=584)
    py.click(x=493, y=646)
    py.press('down')
    py.click(x=813, y=678)

    py.scroll(-300)

    py.click(x=840, y=588)

    time.sleep(5)

    py.scroll(-5000)
    py.click(x=834, y=584)

    py.scroll(-5000)
    py.click(x=362, y=588)

    time.sleep(5)

    tabela_dois = pd.read_csv("cadastro2.csv")

    py.click(x=262, y=590)
    codigo = str(tabela_dois.loc[linha, "nome"])    
    py.write(str(codigo))
    py.press('enter')

    py.press('tab')
    py.write(str(tabela_dois.loc[linha, "cnpj"]))

    py.scroll(-5000)
    py.press('tab')
    py.press('tab')
    py.press('backspace')
    py.write(str(tabela_dois.loc[linha, "data"]))

    py.press('tab')
    py.write(str(tabela_dois.loc[linha, "data_venc"]))

    py.click(x=199, y=522)

    py.click(x=577, y=165)
    py.click(x=614, y=239)                                    
    py.press('down')
    py.press('enter')
    
    py.click(x=474, y=405)

    py.scroll(-5000)
    py.click(x=198, y=522)

    py.click(x=577, y=165)
    py.click(x=614, y=239)
    py.press('down')
    py.press('enter')

    py.click(x=844, y=405)

    time.sleep(10)

    py.click(x=1211, y=64)

    time.sleep(3)

    # py.click(x=948, y=606)    # abrir com adobe reader
    # time.sleep(10)
    # py.click(x=1331, y=23)


    py.click(x=1268, y=63)
    py.click(x=1075, y=173)
    py.click(x=1298, y=118)    # abrir com site
    py.click(x=1018, y=657)

    py.click(x=131, y=19)

    py.click(x=26, y=244)
    py.scroll(5000)

    py.click(x=130, y=126)