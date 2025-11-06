# 🚀 Usando Modelos Gemini com (py)AutoGen

O (py)AutoGen suporta nativamente a API do Google Gemini através da configuração `OAI_CONFIG_LIST`.

## Visão Geral do Projeto

Este projeto demonstra como usar o `pyautogen` para criar um sistema de agentes de IA para realizar tarefas de linting de markdown. O sistema é composto por dois agentes:

*   **`LinterAgent`**: Um `AssistantAgent` que entende o objetivo de corrigir arquivos markdown e usa a ferramenta `lint_and_fix_markdown`.
*   **`Executor`**: Um `UserProxyAgent` que executa a ferramenta `lint_and_fix_markdown`.

O projeto é configurado para usar a API do Gemini para o `LinterAgent`, mas também pode ser configurado para usar a API da OpenAI.

## Construindo e Executando o Projeto

Para construir e executar o projeto, siga estas etapas:

1.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Configure sua chave de API:**

    *   Crie um arquivo `.env` na raiz do projeto.
    *   Adicione sua chave de API do Google AI Studio ao arquivo `.env`, como mostrado abaixo:

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

3.  **Execute o projeto:**

    ```bash
    python src/main.py
    ```

## Convenções de Desenvolvimento

*   **Linting:** O projeto usa o `ruff` para linting de Python e o `pymarkdown-linter` for markdown linting.
*   **Formatação:** O projeto usa o `black` para formatação de código Python.
*   **Ambiente Virtual:** O projeto usa um ambiente virtual (`venv`) para gerenciar as dependências.
*   **Testes:** Atualmente, não há testes automatizados no projeto.

## Testando a API do Gemini

Para testar se a API do Gemini está configurada corretamente, você pode adicionar o seguinte código ao final do arquivo `src/main.py`:

```python
if __name__ == "__main__":
    # ... (código existente)

    # Adicione este código para testar a API do Gemini
    try:
        response = linter_agent.generate_reply(messages=[{"role": "user", "content": "Olá!"}])
        print("Resposta da API do Gemini:", response)
    except Exception as e:
        print("Erro ao testar a API do Gemini:", e)
```

Este código enviará uma mensagem simples para o `LinterAgent` e imprimirá a resposta. Se a API do Gemini estiver configurada corretamente, você deverá ver uma resposta do modelo.