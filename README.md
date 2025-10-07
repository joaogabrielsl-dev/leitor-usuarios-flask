# Leitor de Usuários com Flask e Azure

Aplicação web simples desenvolvida com Python e Flask que lê uma lista de usuários de um arquivo `usuarios.json` e exibe seus nomes em uma página web.

Este projeto foi criado como parte de uma avaliação técnica, demonstrando o ciclo completo de desenvolvimento: codificação, versionamento com Git, publicação na nuvem (Azure) e automação de deploy com CI/CD.

---

### **Acesse a Aplicação ao Vivo**

A aplicação está publicada no Azure App Service e pode ser acessada através do link abaixo:

**[https://leitor-usuarios-flask-joaogabriellima.azurewebsites.net/](https://leitor-usuarios-flask-joaogabriellima.azurewebsites.net/)**

---

### Principais Funcionalidades

-   Leitura de dados de um arquivo `usuarios.json` local.
-   Exibição dinâmica dos dados em um template HTML.
-   Tratamento de erros para casos onde o arquivo não existe ou está mal formatado.
-   Publicação contínua configurada com GitHub Actions.

### Tecnologias Utilizadas

-   **Backend:** Python 3.13 com Flask
-   **Hospedagem:** Azure App Service
-   **Automação (CI/CD):** GitHub Actions

---

### 🔧 Como Executar Localmente

Para rodar este projeto na sua máquina local, siga os passos abaixo.

**Pré-requisitos:**
* Git
* Python 3.13

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/joaogabrielsl-dev/leitor-usuarios-flask.git
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd leitor-usuarios-flask
    ```

3.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute a aplicação:**
    ```bash
    flask run
    ```
    A aplicação estará disponível em `http://127.0.0.1:5000`.

### ⚙️ Automação (CI/CD)

Este repositório possui uma esteira de CI/CD configurada com GitHub Actions. Qualquer `push` para a branch `main` irá automaticamente disparar um workflow que publica a versão mais recente da aplicação no Azure App Service.
