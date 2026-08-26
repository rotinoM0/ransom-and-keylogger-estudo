# Projeto de Estudo: Simulacao de Malware em Python

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-green.svg)](https://ubuntu.com/)
[![Status](https://img.shields.io/badge/Status-Educacional-orange.svg)](https://dio.me/)

---

## Visao Geral

Projeto de estudo para a plataforma **[dio.me](https://dio.me/)** que simula o comportamento de malwares em ambiente seguro e controlado. O objetivo e demonstrar como ransomware e keylogger funcionam, incentivando a reflexao sobre defesa e seguranca da informacao.

> **AVISO IMPORTANTE**: Este projeto e para fins **EDUCACIONAIS** apenas. Os scripts aqui contidos nao devem ser usados para fins maliciosos. Use sempre em ambiente de laboratorio controlado.

---

## Objetivos de Aprendizado

1. Entender como ransomware funciona (criptografia de arquivos)
2. Compreender como keylogger captura dados (captura de teclas)
3. Aprender tecnicas de ofuscacao usadas por malware
4. Refletir sobre medidas de defesa e prevencao
5. Desenvolver consciencia sobre seguranca da informacao

---

## Estrutura do Projeto

```
malwares/
├── README.md                           # Este arquivo
├── requirements.txt                    # Dependencias Python
├── ransomware/
│   ├── __init__.py
│   ├── encrypt.py                      # Criptografa arquivos de teste
│   ├── decrypt.py                      # Descriptografa arquivos
│   ├── ransom_message.py               # Mensagem de resgate
│   └── test_files/                     # Arquivos para criptografar
│       ├── documento1.txt
│       ├── documento2.txt
│       └── notas.txt
├── keylogger/
│   ├── __init__.py
│   ├── keylogger_basic.py              # Keylogger simples
│   ├── keylogger_stealth.py            # Keylogger com ofuscacao
│   ├── email_sender.py                 # Envio de logs por email
│   └── logs/                           # Diretorio de logs
│       └── .gitkeep
└── defesa/
    ├── README.md                       # Visao geral das defesas
    ├── medidas_prevencao.md            # Antivirus, firewall, sandboxing
    └── conscientizacao_usuario.md      # Boas praticas e conscientizacao
```

---

## Requisitos

- **Python**: 3.8 ou superior
- **Sistema Operacional**: Linux (recomendado) ou Windows
- **Dependencias**: ver `requirements.txt`

---

## Instalacao

### 1. Clone o repositorio

```bash
git clone https://github.com/seu-usuario/malwares-estudo.git
cd malwares-estudo
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Instale as dependencias

```bash
pip install -r requirements.txt
```

---

## Como Usar

### 1. Ransomware Simulado

#### Criptografar arquivos

```bash
cd ransomware
python encrypt.py
```

**Saidas:**
- Arquivos `.enc` criptografados em `test_files/`
- Chave de criptografia salva em `secret.key`
- Mensagem de resgate exibida no terminal

#### Descriptografar arquivos

```bash
python decrypt.py
```

**Saidas:**
- Arquivos `.txt` restaurados em `test_files/`
- Arquivos `.enc` removidos

#### Ver mensagem de resgate

```bash
python ransom_message.py
```

---

### 2. Keylogger Simulado

#### Keylogger Basico

```bash
cd keylogger
python keylogger_basic.py
```

**Saidas:**
- Captura de teclas em tempo real
- Log salvo em `logs/log_YYYY-MM-DD.txt`
- Parada com `Ctrl+C`

#### Keylogger com Ofuscacao

```bash
python keylogger_stealth.py
```

**Saidas:**
- Mesma funcionalidade do basico
- Nome de arquivo ofuscado
- Formato de log minimalista

#### Enviar logs por email

```bash
# Configura variaveis de ambiente primeiro
export SMTP_SERVER="smtp.gmail.com"
export SMTP_PORT="587"
export EMAIL_USER="seu-email@gmail.com"
export EMAIL_PASS="sua-senha-app"
export EMAIL_DEST="destinatario@exemplo.com"

# Execute o envio
python email_sender.py
```

**Nota:** Para Gmail, use senhas de app: https://myaccount.google.com/apppasswords

---

### 3. Documentacao de Defesa

Leia a documentacao de defesa para entender como se proteger:

```bash
cd defesa
# Leia os arquivos .md com seu editor favorito
```

**Documentacao disponivel:**
- `README.md` - Visao geral das defesas
- `medidas_prevencao.md` - Antivirus, firewall, sandboxing
- `conscientizacao_usuario.md` - Boas praticas

---

## Conceitos Demonstrados

### Ransomware

| Conceito | Descricao |
|----------|-----------|
| **Criptografia Simetrica** | Uso de Fernet (AES-128-CBC) |
| **Exfiltracao de Chaves** | Chave salva em arquivo |
| **Mensagem de Resgate** | Comunicacao com vitima |
| **Persistencia** | Arquivos criptografados permanecem |

### Keylogger

| Conceito | Descricao |
|----------|-----------|
| **Captura de Teclas** | Monitoramento de entrada |
| **Armazenamento** | Logs com timestamps |
| **Ofuscacao** | Nomes falsos, formato minimalista |
| **Exfiltracao** | Envio por email (SMTP) |
| **Evaisao** | Thread daemon, limpeza de evidencias |

---

## Defesa e Prevencao

### Contra Ransomware

1. **Backups regulares**: Regra 3-2-1
2. **Atualizacoes**: Manter sistema e software atualizados
3. **Antivirus**: Solucao atualizada e ativa
4. **Treinamento**: Conscientizacao sobre phishing
5. **Segmentacao de rede**: Limitar propagacao

### Contra Keylogger

1. **Antivirus**: Deteccao de software malicioso
2. **Gerenciador de senhas**: Evitar digitar senhas
3. **Autenticacao 2FA**: Mesmo com senha comprometida
4. **Teclado virtual**: Para senhas criticas
5. **Monitoramento**: Verificar processos ativos

### Geral

1. **Defesa em profundidade**: Multiplas camadas
2. **Menor privilegio**: Apenas o necessario
3. **Monitoramento**: Logs e alertas
4. **Resposta a incidentes**: Plano de acao
5. **Conscientizacao**: Usuarios treinados

---

## Aprendizados e Reflexoes

### O que aprendi com este projeto

1. **Ransomware**: Entendi como a criptografia e usada para extorsao
2. **Keylogger**: Compreendi como dados sao capturados e exfiltrados
3. **Ofuscacao**: Aprendi tecnicas para dificultar deteccao
4. **Defesa**: Entendi a importancia de multiplas camadas
5. **Conscientizacao**: Usuarios sao o elo mais fraco

### Reflexoes sobre Seguranca

- Tecnologia sozinha nao basta
- Usuarios bem treinados sao a melhor defesa
- Backups regulares salvam vidas (de dados)
- Seguranca e um processo continuo
- Aprendizado e a melhor defesa

---

## Tecnologias Utilizadas

| Tecnologia | Uso no Projeto |
|------------|----------------|
| Python 3.8+ | Linguagem principal |
| cryptography | Criptografia Fernet |
| pynput | Captura de teclas |
| smtplib | Envio de email |
| pathlib | Manipulacao de arquivos |
| datetime | Timestamps |

---

## Contribuindo

Este e um projeto de estudo. Se quiser contribuir:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudancas (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

---

## Licenca

Este projeto esta sob a licenca MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## Contato

- **Plataforma**: [dio.me](https://dio.me/)
- **Autor**: Seu nome
- **Email**: seu-email@exemplo.com

---

## Avisos Legais

> **ATENCAO**: Este projeto e estritamente para fins **EDUCACIONAIS** e de **ESTUDO** em seguranca da informacao.
>
> - Nao use este codigo para fins maliciosos
> - Nao tente infectar sistemas reais
> - Use apenas em ambiente de laboratorio controlado
> - Respeite as leis e regulamentacoes de seu pais
>
> O autor nao se responsabiliza pelo uso indevido deste codigo.

---

## Referencias

- [OWASP](https://owasp.org/) - Open Web Application Security Project
- [MITRE ATT&CK](https://attack.mitre.org/) - Base de conhecimento de ameacas
- [NIST](https://www.nist.gov/) - National Institute of Standards and Technology
- [SANS](https://www.sans.org/) - SysAdmin, Audit, Network, Security

---

Feito com dedicacao para aprendizado de seguranca da informacao.
