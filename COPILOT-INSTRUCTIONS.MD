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
