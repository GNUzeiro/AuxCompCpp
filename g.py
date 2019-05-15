#!/usr/bin/python
import sys
import os

def main():
    source_dir = '~/scripts/cpp/sources/'
    executable_dir = '~/scripts/cpp/executaveis/'
    arq = sys.argv[1] #pega o argumento com o nome do .cpp/.cc
    nome = arq.split('.') #separa o nome da extensão
    cod = nome[0] #nome pronto para compilação
    if nome[1] == "cc":
        stx = 'g++ ponto -o exec' #sintaxe da compilação
        stx = stx.replace('ponto', '%s' %arq)
        stx = stx.replace('exec', '%s' %cod)
        os.system("%s" %stx) #dá o comando de compilação
    else:
        stx = 'gcc ponto -o exec'
        stx = stx.replace('ponto', '%s' %arq)
        stx = stx.replace('exec', '%s' %cod)
        os.system("%s" %stx)        
    mov = 'mv arq dir'
    mov = mov.replace('arq', '%s' %cod)
    mov = mov.replace('dir', '%s' %executable_dir)
    os.system("%s" %mov)
    cd = 'cd dir && ./run'
    cd = cd.replace('dir','%s' %executable_dir)
    cd = cd.replace('run','%s' %cod)
    os.system("%s" %cd)   
    
if __name__ == '__main__':
    main()
