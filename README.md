# 🐍 Guia Completo: Desenvolvendo Agentes com (py)AutoGen

Este guia é uma base de conhecimento completa para iniciar o desenvolvimento de agentes de IA usando o framework `pyautogen`. O objetivo é configurar um repositório Python robusto, com ambiente virtual, linting, formatação e um exemplo prático de "agente-ferramenta".

## 📖 Índice

1. [Introdução: O que é (py)AutoGen?](https://www.google.com/search?q=%23introdu%C3%A7%C3%A3o-o-que-%C3%A9-pyautogen)
2. [🎯 Pré-requisitos](https://www.google.com/search?q=%23-pr%C3%A9-requisitos)
3. [Parte 1: Configuração do Repositório e Ambiente](https://www.google.com/search?q=%23parte-1-configura%C3%A7%C3%A3o-do-reposit%C3%B3rio-e-ambiente)
4. [Parte 2: Instalação do AutoGen e Chaves de API](https://www.google.com/search?q=%23parte-2-instala%C3%A7%C3%A3o-do-autogen-e-chaves-de-api)
5. [Parte 3: Configuração do VSCode](https://www.google.com/search?q=%23parte-3-configura%C3%A7%C3%A3o-do-vscode)
6. [Parte 4: Exemplo (Agente de Linting de Markdown)](https://www.google.com/search?q=%23parte-4-exemplo-de-implementa%C3%A7%C3%A3o-agente-de-linting-de-markdown)
7. [Parte 5: Repositórios de Exemplo Oficiais](https://www.google.com/search?q=%23parte-5-reposit%C3%B3rios-de-exemplo-oficiais)
8. [Parte 6: Documentação Essencial do Repositório](https://www.google.com/search?q=%23parte-6-documenta%C3%A7%C3%A3o-essencial-do-reposit%C3%B3rio)

-----

## Introdução: O que é (py)AutoGen?

(py)AutoGen é o framework original e principal da Microsoft para o desenvolvimento de agentes. Ele é projetado para simplificar a criação, orquestração e automação de fluxos de trabalho complexos usando múltiplos agentes de IA que conversam entre si (e com humanos e ferramentas) para resolver tarefas.

Sua principal força está em como os agentes podem usar ferramentas, executar código Python e interagir de forma fluida para alcançar objetivos complexos.

## 🎯 Pré-requisitos

Antes de começarmos, garanta que você tenha o seguinte software instalado:

  * **Python:** Versão 3.10 ou superior.
  * **VSCode:** Nosso editor de código principal.
  * **Chave de API LLM:** Uma chave de API da OpenAI (GPT-4, etc.) ou do Google AI Studio (Gemini).

-----

## Parte 1: Configuração do Repositório e Ambiente

Vamos criar um novo projeto Python robusto usando um ambiente virtual (`venv`).

### 1. Criação do Projeto

Abra seu terminal e execute os seguintes comandos:

```bash
# Cria o diretório e entra nele
mkdir autogen-py-projeto
cd autogen-py-projeto

# Inicia o controle de versão
git init

# Cria um ambiente virtual (venv)
python -m venv venv
```

### 2. Ativação do Ambiente Virtual

Você **deve** ativar o `venv` para isolar suas dependências.

  * **No Windows (PowerShell):**
    ```powershell
    .\venv\Scripts\Activate
    ```
  * **No macOS / Linux (bash/zsh):**
    ```bash
    source venv/bin/activate
    ```

(Seu terminal deve agora mostrar `(venv)` no início da linha de comando.)

### 3. Atualização do Pip

É uma boa prática garantir que o pip esteja atualizado dentro do venv:

```bash
python -m pip install --upgrade pip
```

-----

## Parte 2: Instalação do AutoGen e Chaves de API

### 1. Instalação das Dependências Principais

Com seu `venv` ativo, instale os pacotes principais do AutoGen e `python-dotenv` para gerenciar nossas chaves de API:

```bash
pip install pyautogen python-dotenv
```

### 2. Configuração da Chave de API (OAI_CONFIG_LIST)

O AutoGen usa a variável de ambiente `OAI_CONFIG_LIST` para configurar seus LLMs. Crie um arquivo chamado `.env` na **raiz do seu projeto**.

**Adicione `.env` ao seu arquivo `.gitignore` para nunca vazar suas chaves!**

Escolha **uma** das opções abaixo e cole o conteúdo no seu arquivo `.env`.

-----

#### Opção A: Configurando a API da OpenAI (Recomendado para "Function Calling")

1.  Obtenha sua chave de API em: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2.  Cole o seguinte no seu arquivo `.env`:

```ini
# .env (Exemplo OpenAI)
OAI_CONFIG_LIST='[
  {
    "model": "gpt-4-turbo",
    "api_key": "sk-SUA_CHAVE_API_DA_OPENAI_AQUI"
  }
]'
```

-----

#### Opção B: Configurando a API do Gemini (Google AI Studio)

1.  Obtenha sua chave de API em: [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2.  Cole o seguinte no seu arquivo `.env`:

```ini
# .env (Exemplo Gemini)
OAI_CONFIG_LIST='[
  {
    "model": "gemini-1.5-flash-latest",
    "api_key": "SUA_CHAVE_API_DO_GOOGLE_AI_STUDIO_AQUI",
    "api_type": "google"
  }
]'
```

  * **`"api_type": "google"`**: Isso é crucial. Informa ao AutoGen para usar o cliente da API do Google.

**Nota Importante:** O script da Parte 4 (`src/main.py`) usará automaticamente qualquer configuração que você colocar no arquivo `.env`, graças à função `autogen.config_list_from_env()`.

-----

## Parte 3: Configuração do VSCode

Um ambiente Python consistente é fundamental.

### 1. Extensões Recomendadas

Pressione `Ctrl+Shift+X` no VSCode e instale estas extensões:

  * `ms-python.python`: O pacote principal de suporte ao Python.
  * `ms-python.pylance`: O servidor de linguagem (intellisense, tipos).
  * `ms-python.black-formatter`: O formatador de código padrão.
  * `charliermarsh.ruff`: Ferramenta de linting e formatação ultra-rápida.

### 2. Arquivo de Configurações (`.vscode/settings.json`)

Crie a pasta `.vscode` e, dentro dela, o arquivo `settings.json` para garantir que todos os desenvolvedores usem a mesma formatação e linting.

```json
// .vscode/settings.json
{
  // --- Configurações Gerais ---
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": "explicit",
    "source.organizeImports": "explicit"
  },

  // --- Configurações do Python ---
  "python.analysis.autoImportCompletions": true,
  "python.analysis.typeCheckingMode": "basic",

  // --- Formatação (Black) ---
  "editor.defaultFormatter": "ms-python.black-formatter",
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  },

  // --- Linting (Ruff) ---
  "ruff.lint.onSave": true,
  "ruff.fixAll": true,
  "ruff.organizeImports": true
}
```

-----

## Parte 4: Exemplo de Implementação (Agente de Linting de Markdown)

Vamos criar um sistema de dois agentes onde um agente de IA (`LinterAgent`) usa uma ferramenta Python (`lint_and_fix_markdown`) executada por outro agente (`Executor`).

### 1. Dependências Adicionais

Precisamos de uma biblioteca Python para fazer o linting de Markdown.

```bash
pip install "pymarkdown-linter[all]"
```

### 2. Arquivo de Exemplo (`input.md`)

Crie um arquivo na raiz do projeto chamado `input.md` com alguns erros:

```markdown
# titulo com erro

Esta   linha tem  espaços   extras.

E esta tem *enfase incorreta*.

###   Subtitulo com espaços
```

### 3. O Código (`src/main.py`)

Crie a pasta `src` e dentro dela o arquivo `main.py`.

```bash
mkdir src
```

Cole o seguinte código em `src/main.py`:

```python
# src/main.py
import logging
import os
import autogen
from pathlib import Path
from pymarkdown.api import fix_markdown_file
from dotenv import load_dotenv

# 1. Configuração Inicial
# Carrega as variáveis do arquivo .env (OAI_CONFIG_LIST)
load_dotenv()

# Configura o logging para vermos o que está acontecendo
logging.basicConfig(level=logging.INFO)

# 2. Definição da Ferramenta (Tool)
# Esta é a função Python que os agentes poderão executar.
def lint_and_fix_markdown(file_path: str) -> str:
    """
    Executa o lint e corrige automaticamente um arquivo markdown específico.
    Retorna uma string indicando sucesso ou falha.
    """
    logging.info(f"[Tool] Iniciando lint e correção para: {file_path}")
    
    full_path = Path(file_path).resolve()
    
    if not full_path.exists():
        logging.error(f"[Tool] Erro: Arquivo não encontrado em {full_path}")
        return f"Erro: Arquivo não encontrado em {file_path}"
    
    try:
        # A função fix_markdown_file do pymarkdown corrige o arquivo "in-place"
        fix_markdown_file(str(full_path))
        
        logging.info(f"[Tool] Arquivo corrigido e salvo em: {full_path}")
        return f"Sucesso: O arquivo '{file_path}' foi corrigido e salvo."
        
    except Exception as e:
        logging.error(f"[Tool] Erro ao corrigir o arquivo: {e}")
        return f"Erro: Não foi possível corrigir o arquivo {file_path}. Detalhe: {e}"

# 3. Função Principal (Main)
def main():
    print("Iniciando o sistema de agentes...")

    # 4. Configuração do LLM
    # Carrega a configuração do .env (OAI_CONFIG_LIST)
    config_list = autogen.config_list_from_env()
    
    llm_config = {
        "config_list": config_list,
        "temperature": 0.1,
    }

    # 5. Instanciando os Agentes

    # O AssistantAgent (LinterAgent)
    # Este é o agente de IA que entende o objetivo e decide usar ferramentas.
    linter_agent = autogen.AssistantAgent(
        name="LinterAgent",
        system_message="""Você é um assistente especialista em formatação de Markdown.
        Seu objetivo é corrigir arquivos .md usando a ferramenta 'lint_and_fix_markdown'.
        Não escreva o código da correção você mesmo. Apenas peça para a ferramenta ser executada no arquivo solicitado.
        Responda 'TERMINATE' quando a tarefa estiver concluída com sucesso.
        """,
        llm_config=llm_config,
    )

    # O UserProxyAgent (Executor)
    # Este agente atua como um proxy do usuário e executa o código/ferramentas.
    executor = autogen.UserProxyAgent(
        name="Executor",
        human_input_mode="NEVER",
        code_execution_config={
            # Importante: "use_docker": False significa que o código (a chamada da função)
            # será executado no ambiente local (onde o script está rodando).
            "use_docker": False,
        },
    )

    # 6. CRUCIAL: Registro da Ferramenta
    
    # 6a. Definição do Schema da Ferramenta (para o LLM entender)
    tool_schema = {
        "type": "function",
        "function": {
            "name": "lint_and_fix_markdown",
            "description": "Executa o lint e corrige automaticamente um arquivo markdown específico.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "O caminho do arquivo .md a ser corrigido (ex: ./input.md)",
                    }
                },
                "required": ["file_path"],
            },
        },
    }
    
    # 6b. "Ensinando" os agentes sobre a ferramenta
    
    # Damos ao LinterAgent (LLM) o schema da ferramenta
    linter_agent.llm_config["tools"] = [tool_schema]
    
    # Damos ao Executor (Código) a função Python real
    executor.register_function(
        function_map={
            "lint_and_fix_markdown": lint_and_fix_markdown
        }
    )

    # 7. Iniciando a Conversa
    print("Iniciando a conversa...")
    executor.initiate_chat(
        linter_agent,
        message="Por favor, corrija o lint do arquivo './input.md'.",
    )

# Executa a função principal
if __name__ == "__main__":
    main()
```

### 4. Execução

Abra seu terminal (com o `venv` ativo) e execute o script:

```bash
python src/main.py
```

**O que Acontece:**

1.  O `Executor` envia a mensagem inicial.
2.  O `LinterAgent` (LLM) recebe a mensagem, consulta suas `tools`, e responde que usará `lint_and_fix_markdown(file_path='./input.md')`.
3.  O `Executor` recebe essa instrução, vê que tem a função `lint_and_fix_markdown` em seu `function_map`, e a executa.
4.  O `Executor` envia o resultado da função (ex: "Sucesso...") de volta para o LinterAgent.
5.  O `LinterAgent` vê que a tarefa foi bem-sucedida e responde `TERMINATE`.

**Resultado:** Verifique seu arquivo `input.md`. Ele estará perfeitamente formatado.

-----

## Parte 5: Repositórios de Exemplo Oficiais

Para explorar conceitos mais avançados (GroupChat, agentes que escrevem e executam código, etc.), o repositório oficial do `pyautogen` é o melhor lugar.

  * **Repositório Principal (Python):** [https://github.com/microsoft/autogen](https://github.com/microsoft/autogen)
  * **Link Direto para Exemplos (Samples):** [https://github.com/microsoft/autogen/tree/main/samples](https://github.com/microsoft/autogen/tree/main/samples)

-----

## Parte 6: Documentação Essencial do Repositório

Para uma boa base de conhecimento (para humanos e LLMs), crie os seguintes arquivos na raiz do seu repositório.

### 1. `AGENTS.MD`

*Conteúdo para o arquivo `AGENTS.MD`*:

```markdown
# 🤖 Registro de Agentes do Projeto

Este documento descreve os agentes customizados e suas responsabilidades neste repositório.

## Agentes de Propósito Geral

### 1. `LinterAgent` (autogen.AssistantAgent)

* **System Message:** "Você é um assistente especialista em formatação de Markdown. Seu objetivo é corrigir arquivos .md usando a ferramenta 'lint_and_fix_markdown'..."
* **Funções/Ferramentas (Schema):**
    * `lint_and_fix_markdown(file_path: string)`: O schema da ferramenta é fornecido ao LLM para que ele saiba como usá-la.
* **Propósito:** Orquestrar tarefas de linting de documentação.

### 2. `Executor` (autogen.UserProxyAgent)

* **Configuração:** `human_input_Mode: 'NEVER'`, `code_execution_config: {'use_docker': False}`
* **Funções/Ferramentas Registradas (function_map):**
    * `lint_and_fix_markdown`: Mapeado para a função Python real em `src/main.py`.
* **Propósito:** Atuar como o "executor" de ferramentas do lado do código Python.

---

*(Adicione novos agentes aqui conforme o projeto cresce)*
```

-----

### 2. `GEMINI.MD`

*Conteúdo para o arquivo `GEMINI.MD`*:

```markdown
# 🚀 Usando Modelos Gemini com (py)AutoGen

O (py)AutoGen suporta nativamente a API do Google Gemini através da configuração `OAI_CONFIG_LIST`.

## Configuração (via `.env`)

1. **Obtenha sua Chave de API:** Acesse o [Google AI Studio](https://aistudio.google.com/app/apikey) e gere uma chave de API.

2. **Atualize seu `.env`:**

   Este é o formato exato que o `pyautogen` espera. Use o modelo `flash` para testes e baixo custo.

   ```ini
   # .env
   OAI_CONFIG_LIST='[
     {
       "model": "gemini-1.5-flash-latest",
       "api_key": "SUA_CHAVE_API_DO_GOOGLE_AI_STUDIO_AQUI",
       "api_type": "google"
     }
   ]'
   ```
   
   * **`model`**: O nome do modelo.
   * **`api_key`**: Sua chave do AI Studio.
   * **`api_type`: "google"**: Essencial. Isso instrui o `pyautogen` a usar o cliente Python `google-generativeai` por baixo dos panos.

## Uso no Código

O seu script `src/main.py` já está pronto para isso. A linha:

```python
config_list = autogen.config_list_from_env()
```

Irá carregar automaticamente essa configuração do Gemini, e o `AssistantAgent` a utilizará sem qualquer alteração adicional no código.
```

---

### 3. `OPENAI.MD`

*Conteúdo para o arquivo `OPENAI.MD`*:

```markdown
# 🔑 Usando Modelos OpenAI com (py)AutoGen

O (py)AutoGen usa a API da OpenAI como padrão. A configuração é simples e direta.

## Configuração (via `.env`)

1. **Obtenha sua Chave de API:** Acesse [OpenAI Platform](https://platform.openai.com/api-keys) e gere uma nova chave secreta.

2. **Atualize seu `.env`:**

   Este é o formato padrão.

   ```ini
   # .env
   OAI_CONFIG_LIST='[
     {
       "model": "gpt-4-turbo",
       "api_key": "sk-SUA_CHAVE_API_DA_OPENAI_AQUI"
     }
   ]'
   ```
   
   * **`model`**: O nome do modelo (ex: `gpt-4-turbo`, `gpt-3.5-turbo`).
   * **`api_key`**: Sua chave secreta `sk-...`.
   * Não é necessário `api_type` quando se usa a API oficial da OpenAI.

## Uso no Código

O seu script `src/main.py` já está pronto para isso. A linha:

```python
config_list = autogen.config_list_from_env()
```

Irá carregar automaticamente essa configuração da OpenAI.
```

---

### 4. `COPILOT-INSTRUCTIONS.MD`

*Conteúdo para o arquivo `COPILOT-INSTRUCTIONS.MD`*:

```markdown
# 🔧 Configurando o GitHub Copilot/IntelliCode

Para obter o máximo do GitHub Copilot e do IntelliCode neste repositório Python, siga estas etapas.

## 1. Instale as Extensões (Se ainda não o fez)

* `github.copilot` (Inclui Copilot Chat)
* `ms-python.python` (Necessário para o Copilot entender o contexto Python)
* `ms-python.pylance` (Melhora as sugestões baseadas em tipos)

## 2. "Treine" o Copilot sobre o Repositório

O Copilot fica mais inteligente quando entende o contexto do seu projeto. Este `README.md` e os outros arquivos `.MD` são feitos para isso.

### Use o `@workspace` no Copilot Chat

Abra o Chat do Copilot (`Ctrl+Shift+I`) e use o agente `@workspace` para fazer perguntas sobre todo o seu código:

* `@workspace como a função lint_and_fix_markdown está implementada?`
* `@workspace quais agentes estão definidos em AGENTS.MD?`
* `@workspace como eu configuro a API do Gemini?`

### Adicione Contexto ao Chat

Você pode "alimentar" o Copilot com arquivos específicos para ajudá-lo a gerar código melhor:

1. Abra `src/main.py`.
2. Abra `AGENTS.MD`.
3. No chat do Copilot, digite `/include src/main.py` e `/include AGENTS.MD`.
4. Faça sua pergunta: `com base nesses arquivos, sugira um novo agente que possa ler arquivos de texto.`

## 3. Configurações do VSCode

O arquivo `.vscode/settings.json` já incluído neste repositório ajuda o Copilot:

* **Formatação ao Salvar (Black):** Garante que o código gerado pelo Copilot seja formatado imediatamente.
* **Linting (Ruff):** O `settings.json` ativa o Ruff, que ajuda o Copilot a aprender com os erros e a sugerir código que siga suas regras de linting.
```
