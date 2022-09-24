import pyautogui, time, os

def open_program(principal_png, ok_png):
    t = 0
    # Abre o programa EFD ICMS IPI.
    pyautogui.press('winleft')
    pyautogui.write('EFD ICMS IPI')
    time.sleep(1)
    pyautogui.press('enter')
    # Espera o programa abrir.
    while (t == 0):
        time.sleep(1)
        teste = pyautogui.locateOnScreen(ok_png)
        if teste != None:            
            print("update")
            pyautogui.press('enter')            
            t = 1
        else:
            teste2 = pyautogui.locateOnScreen(principal_png)
            if teste2 != None:
                t = 1
    pyautogui.press('enter')

def move_arquivo(path, dest):
    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = f"{path}\\{file}"
            dest_path = f"{dest}\\{file}"
            os.rename(file_path, dest_path)
            return

def move_arquivo_erro(path, dest_error):
    for file in os.listdir():
        if file.endswith(".txt"):
            file_path_error = f"{path}\\{file}"
            dest_path_error = f"{dest_error}\\{file}"
            os.rename(file_path_error, dest_path_error)
            return

# Extrai o caminho do arquivo da variavel path.               
def extractPath(innie):
    iggy = str(innie)
    getridofme ="<_io.TextIOWrapper name='"
    getridofmetoo ="' mode='r' encoding='UTF-8'>"
    iggy = iggy.replace(getridofme, "")
    iggy = iggy.replace(getridofmetoo, "")
    # Retorna o path.
    return iggy

# Cria as pastas dos arquivos de saída.
def cria_pastas():
    cwd = os.getcwd()
    path = cwd + "/" + 'corretos'
    if os.path.isdir(path):
        path = cwd + "/" + 'erros'
        if os.path.isdir(path):
            return
        else:
            pasta = os.path.join(cwd + "/", 'erros')
            os.mkdir(pasta)            
    else:
        pasta = os.path.join(cwd + "/", 'corretos')
        os.mkdir(pasta)     
        path = cwd + "/" + 'erros'
        if os.path.isdir(path):
            return
        else:
            pasta = os.path.join(cwd + "/", 'erros')
            os.mkdir(pasta)    

def new_error(str1, dest_error):  
    pyautogui.moveTo(769, 287)
    pyautogui.click(button = 'left')
    move_arquivo_erro(str1, dest_error)

def new_adv(str1, dest):
    pyautogui.moveTo(769, 287)
    pyautogui.click(button = 'left')
    move_arquivo(str1, dest)

def main(path):
    path = extractPath(path)
    path = path.split("'")
    # Transforma a lista para string.
    str1 = ''.join(path[0])   
   
    dest = str1 + '\corretos' 
    dest_error = str1 + '\erros'

    error_png = 'D:\\applegal\\valida_sped\\imagens\\lookLikeThis.png'
    ok_png = 'D:\\applegal\\valida_sped\\imagens\\ok.png'
    done_png = 'D:\\applegal\\valida_sped\\imagens\\done.png'
    principal_png = 'D:\\applegal\\valida_sped\\imagens\\principal.png'
    qntd_arquivos = 0
    t = 0
    error = 0
    dont_move = 0

    # Checa primeiramente, quantos arquivos sped tem na pasta.
    os.chdir(str1)
    # Percorre todos os arquivos terminados em .txt neste diretório.
    for file in os.listdir():
        if file.endswith(".txt"):
            qntd_arquivos+=1

    # Pequeno alerta informando o inicio do programa.
    pyautogui.alert("Começando a automatização.")
    # Pausa entre os comandos do pyautogui.
    pyautogui.PAUSE = 0.5

    # Mouse location.
    test = pyautogui.position()
    print(test)

    cria_pastas()
    # Abre o programa.
    open_program(principal_png, ok_png)
    # Possível loop.
    for i in range(0, qntd_arquivos):
        # Importa escrituração.
        pyautogui.moveTo(332, 131)
        pyautogui.click(button = 'left')
        pyautogui.write(str1)
        pyautogui.press('enter')
        # Seleciona o arquivo sped.
        pyautogui.moveTo(489, 257)
        pyautogui.click(button = 'left')
        pyautogui.press('enter')
        # Screenshot que contém o icone de erro.
        teste = pyautogui.locateOnScreen(error_png)
        # Caso ache um arquivo com erro logo no inicio.
        if (teste != None):       
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(1)
            # Fecha o programa para conseguir mover o arquivo para outro diretório.
            pyautogui.moveTo(464, 135)
            pyautogui.click(button = 'left')
            time.sleep(1)        
            move_arquivo_erro(str1, dest_error)
            open_program(principal_png, ok_png)
        # Caso não tenha erro no inicio do sped.
        else:
            teste = None
            # Espera a primeira mensagem do programa.
            while (t == 0):
                time.sleep(1)
                teste = pyautogui.locateOnScreen(ok_png)
                teste1 = pyautogui.locateOnScreen(error_png)
                # Caso a mensagem seja um ok.
                if teste != None:
                    pyautogui.press('enter')
                    t = 1  
                # Caso seja um erro.
                if teste1 != None:
                    pyautogui.press('enter')
                    # Erro recebe 1.
                    error = 1
                    t = 1
            # Reseta as variáveis para o próximo loop do for.
            t = 0
            teste = None
            teste1 = None
            teste2 = None
            teste3 = None
            teste4 = None
            # Caso não tenha achado algum erro na leitura do arquivo.
            if (error == 0):
                while (t == 0):
                    time.sleep(1)
                    teste = pyautogui.locateOnScreen(ok_png)
                    teste1 = pyautogui.locateOnScreen(done_png)
                    # Caso encontre uma mensagem de ok.
                    if teste != None:
                        pyautogui.press('enter')
                        j = 0
                        while (j == 0):
                            time.sleep(1)
                            # Procura uma mensagem dizendo que o programa foi lido com sucesso.
                            teste2 = pyautogui.locateOnScreen(done_png)
                            teste3 = pyautogui.locateOnScreen(error_png)
                            teste4 = pyautogui.locateOnScreen(ok_png)
                            if teste2 != None:                                
                                pyautogui.press('enter')
                                j = 1
                            if teste3 != None:                        
                                pyautogui.press('enter')
                                new_error(str1, dest_error)                                                               
                                j = 1
                                dont_move = 1
                            if teste4 != None:                                
                                pyautogui.press('enter') 
                                new_adv(str1, dest)
                                j = 1
                                dont_move = 1
                        t = 1
                    # Procura uma mensagem dizendo que o programa foi lido com sucesso.   
                    if teste1 != None:                        
                        pyautogui.press('enter')
                        t = 1  
                t = 0
                j = 0
                if (dont_move != 1):                    
                    pyautogui.moveTo(482, 132)
                    pyautogui.click(button = 'left')
                    time.sleep(3)
                    move_arquivo(str1, dest)
                dont_move = 0
            else:
                pyautogui.moveTo(1340, 11)
                pyautogui.click(button = 'left')
                error = 0
                move_arquivo_erro(str1, dest_error)
    pyautogui.alert("Fim da automatização.")
