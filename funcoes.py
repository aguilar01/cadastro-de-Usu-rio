# funcoes.py
import pandas as pd
import os

nome_arquivo_excel = "Dados2.xlsx"
dic = []
contador_id = 1

def verificar_arquivo():
    """Verifica se o arquivo Excel existe e o cria se não."""
    if not os.path.exists(nome_arquivo_excel):
        df = pd.DataFrame(columns=['ID', 'Usuário'])
        try:
            df.to_excel(nome_arquivo_excel, index=False)
            print(f'Arquivo "{nome_arquivo_excel}" criado com sucesso.')
        except Exception as e:
            print(f'Erro ao criar o arquivo "{nome_arquivo_excel}": {e}')

def inicializar_contador_id():
    """Carrega o último ID do arquivo Excel para continuar a sequência."""
    global contador_id
    try:
        df_existente = pd.read_excel(nome_arquivo_excel)
        if not df_existente.empty and 'ID' in df_existente.columns:
            if not df_existente['ID'].empty:
                contador_id = df_existente['ID'].max() + 1
            else:
                contador_id = 1
        else:
            contador_id = 1
    except FileNotFoundError:
        contador_id = 1
    except Exception as e:
        print(f'Erro ao ler o arquivo "{nome_arquivo_excel}" para inicializar ID: {e}')
        contador_id = 1

def salvar():
    """Salva a lista 'dic' em um arquivo Excel com uma coluna 'ID'."""
    global contador_id
    try:
        df_existente = pd.read_excel(nome_arquivo_excel)
    except FileNotFoundError:
        df_existente = pd.DataFrame(columns=['ID', 'Usuário'])
    except Exception as e:
        print(f'Erro ao ler o arquivo para salvar: {e}')
        return

    novos_usuarios = pd.DataFrame({'ID': range(contador_id, contador_id + len(dic)), 'Usuário': dic})

    if not df_existente.empty:
        df_final = pd.concat([df_existente, novos_usuarios], ignore_index=True)
    else:
        df_final = novos_usuarios

    try:
        df_final.to_excel(nome_arquivo_excel, index=False)
        contador_id += len(dic)
        dic.clear()
        print(f'Dados salvos com sucesso em "{nome_arquivo_excel}".')
    except Exception as e:
        print(f'Erro ao salvar o arquivo: {e}')

def mostrar():
    """Lê e exibe os dados do arquivo Excel."""
    try:
        df = pd.read_excel(nome_arquivo_excel)
        print(df)
        print('Carregado com sucesso')
    except FileNotFoundError:
        print(f'Arquivo "{nome_arquivo_excel}" não encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro ao ler o arquivo: {e}')

def buscar(id_para_buscar):
    """Busca um registro por ID e atualiza o nome do usuário diretamente no arquivo Excel."""
    try:
        df = pd.read_excel(nome_arquivo_excel)
        encontrou = False
        for index, row in df.iterrows():
            if row.get('ID') == id_para_buscar:
                encontrou = True
                novo = input("Digite um novo usuário: ")
                df.at[index,'Usuário'] = novo
                df.to_excel(nome_arquivo_excel, index=False)
                print('Atualizado!')
                break
        if not encontrou:
            print('ID Não encontrado')
    except FileNotFoundError:
        print(f'Arquivo "{nome_arquivo_excel}" não encontrado.')
    except KeyError:
        print("A coluna 'ID' não existe no arquivo.")
    except Exception as e:
        print(f'Ocorreu um erro ao ler/atualizar o arquivo: {e}')

def excluir(dele):
    """Exclui a linha do arquivo Excel onde a coluna 'ID' corresponde ao dele."""
    try:
        df = pd.read_excel(nome_arquivo_excel)
        df_sem_linha = df[df['ID'] != dele]
        df_sem_linha.to_excel(nome_arquivo_excel, index=False)
        print(f"Linha com ID '{dele}' excluída com sucesso.")
    except FileNotFoundError:
        print(f'Arquivo "{nome_arquivo_excel}" não encontrado.')
    except KeyError:
        print("A coluna 'ID' não existe no arquivo.")
    except Exception as e:
        print(f'Ocorreu um erro ao ler/excluir o arquivo: {e}')