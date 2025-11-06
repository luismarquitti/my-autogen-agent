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
