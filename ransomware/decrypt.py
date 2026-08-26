#!/usr/bin/env python3
"""
Ransomware Simulado - Script de Descriptografia
================================================

Este script descriptografa os arquivos criptografados pelo script encrypt.py.
Utiliza a chave salva em secret.key para reverter a criptografia Fernet.

AVISO: Este script e para fins EDUCACIONAIS apenas.

Uso:
    python decrypt.py

Saidas:
    - Arquivos .txt restaurados em test_files/
    - Arquivos .enc removidos apos descriptografia
"""

import os
import sys
from pathlib import Path

try:
    from cryptography.fernet import Fernet
except ImportError:
    print("[ERRO] Biblioteca 'cryptography' nao encontrada.")
    print("Execute: pip install cryptography")
    sys.exit(1)


def carregar_chave():
    """Carrega a chave de criptografia do arquivo secret.key."""
    chave_path = Path(__file__).parent / "secret.key"

    if not chave_path.exists():
        print(f"[ERRO] Chave nao encontrada: {chave_path}")
        print("[DICA] Execute primeiro: python encrypt.py")
        sys.exit(1)

    chave = chave_path.read_bytes()
    print(f"[+] Chave carregada de: {chave_path}")
    return chave


def descriptografar_arquivo(caminho_enc, chave):
    """Descriptografa um arquivo .enc usando Fernet."""
    fernet = Fernet(chave)

    with open(caminho_enc, "rb") as f:
        dados_criptografados = f.read()

    try:
        dados_originais = fernet.decrypt(dados_criptografados)
    except Exception as e:
        print(f"[ERRO] Falha ao descriptografar {caminho_enc}: {e}")
        return None

    # Remove a extensao .enc e restaura o nome original
    caminho_original = str(caminho_enc).replace(".enc", "")

    with open(caminho_original, "wb") as f:
        f.write(dados_originais)

    # Remove o arquivo criptografado
    os.remove(caminho_enc)

    return caminho_original


def descriptografar_diretorio(diretorio, chave):
    """Descriptografa todos os arquivos .enc no diretorio especificado."""
    descriptografados = []

    for arquivo in Path(diretorio).glob("*.enc"):
        print(f"[*] Descriptografando: {arquivo.name}")
        resultado = descriptografar_arquivo(arquivo, chave)
        if resultado:
            descriptografados.append(resultado)
            print(f"    -> Restaurado: {Path(resultado).name}")

    return descriptografados


def main():
    """Funcao principal do script de descriptografia."""
    print("=" * 60)
    print("  RANSOMWARE SIMULADO - Script de Descriptografia")
    print("  [PROJETO DE ESTUDO - NAO USAR EM PRODUCAO]")
    print("=" * 60)
    print()

    # Define o diretorio de arquivos de teste
    diretorio_teste = Path(__file__).parent / "test_files"

    if not diretorio_teste.exists():
        print(f"[ERRO] Diretorio nao encontrado: {diretorio_teste}")
        sys.exit(1)

    # Verifica se ha arquivos criptografados
    arquivos_enc = list(diretorio_teste.glob("*.enc"))
    if not arquivos_enc:
        print("[ERRO] Nenhum arquivo .enc encontrado em test_files/")
        print("[DICA] Execute primeiro: python encrypt.py")
        sys.exit(1)

    print(f"[*] Encontrados {len(arquivos_enc)} arquivos criptografados:")
    for arq in arquivos_enc:
        print(f"    - {arq.name}")
    print()

    # Carrega a chave
    print("[*] Carregando chave de descriptografia...")
    chave = carregar_chave()
    print()

    # Descriptografa os arquivos
    print("[*] Iniciando descriptografia dos arquivos...")
    descriptografados = descriptografar_diretorio(diretorio_teste, chave)
    print()

    # Resumo
    print("=" * 60)
    print("[+] DESCRIPTOGRAFIA CONCLUIDA COM SUCESSO!")
    print(f"[+] {len(descriptografados)} arquivos restaurados")
    print("=" * 60)
    print()
    print("[INFO] Todos os seus arquivos foram restaurados.")
    print("[INFO] Em um ataque real, os arquivos seriam perdidos.")
    print("[INFO] Sempre mantenha backups regulares!")

    # Remove a chave por seguranca (opcional)
    # chave_path = Path(__file__).parent / "secret.key"
    # os.remove(chave_path)
    # print("[+] Chave de criptografia removida.")


if __name__ == "__main__":
    main()
