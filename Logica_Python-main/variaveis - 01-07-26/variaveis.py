GLOBAL_VAR = 'valor global'

def exemplo_local():
    #Variavel local - so existe dentro desta função
    local_var = 'valor local'
    print('local_var:', local_var)
    # acessar variavel global para leitura funciona sem declarar 'global'
    print('GLOBAL_VAR:', GLOBAL_VAR)
    # usar um built-in (len)
    print('Built-in len(\'abc\'):',len('abc'))

def exemplo_modificada():
    # para modificar a variavel global dentro da função, declarar 'global'
    global GLOBAL_VAR
    GLOBAL_VAR = 'novo valor global'
    print("GLOBAL_VAR modificado para:", GLOBAL_VAR )

print('GLOBAL_VAR (ANTES):',GLOBAL_VAR)
exemplo_local()
exemplo_modificada()
print('GLOBAL_VAR (DEPOIS):',GLOBAL_VAR)