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
