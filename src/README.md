# 🏥 Assistente Clínico CAPS — Co-piloto para Projetos Terapêuticos Singulares (PTS)

O **Assistente Clínico CAPS** é um protótipo de agente de Inteligência Artificial conversacional desenvolvido para apoiar equipes multiprofissionais (médicos, psicólogos, assistentes sociais e enfermeiros) em Centros de Atenção Psicossocial (Caps). 

O objetivo principal do agente é automatizar a leitura de relatórios fragmentados e históricos de consultas para **gerar minutas estruturadas de Projetos Terapêuticos Singulares (PTS)**, além de responder de forma rápida a dúvidas pontuais sobre o histórico do paciente.

---

## 🔒 Privacidade e Segurança Absoluta (LGPD)

Por lidar com dados altamente sensíveis de saúde mental, este projeto foi desenhado sob uma **arquitetura 100% local**:
* Utiliza o **Ollama** para rodar modelos de linguagem diretamente na máquina do usuário.
* **Nenhum dado do paciente é enviado para APIs externas** ou servidores de terceiros.
* Total conformidade com as regras de sigilo do prontuário médico e com a Lei Geral de Proteção de Dados (LGPD).

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Interface do Usuário:** Streamlit
* **Processamento de Dados:** Pandas & PyPDF
* **Orquestração e IA:** Ollama (rodando localmente modelos como `Llama3`, `Mistral` ou `Gemma2`)

---

## 📂 Estrutura de Pastas do Projeto

Para que o agente funcione corretamente, garanta que a estrutura do seu diretório esteja organizada da seguinte forma:

```text
meu-projeto/
├── data/
│   ├── diretrizes_caps_pts.json     # Catálogo de oficinas e regras do SUS
│   ├── historico_consultas.csv      # Tabela de evolução histórica (simulada)
│   └── documento_paciente_exemplo.txt # Exemplo de relatório clínico
├── app.py                           # Código-fonte principal da aplicação Streamlit
├── requirements.txt                 # Dependências do projeto
└── README.md                        # Documentação do projeto
```

---

## 🚀 Passo a Passo para Configuração e Execução

Siga as etapas abaixo para colocar o projeto para rodar em seu computador local:

### 1. Instalar e Configurar o Ollama
1. Acesse o site oficial do [Ollama](https://ollama.com) e faça o download para o seu sistema operacional.
2. Abra o terminal do seu computador e baixe o modelo de sua preferência (o código utiliza por padrão o `llama3`). Execute o comando:
   ```bash
   ollama run llama3
   ```
3. Mantenha o terminal aberto ou certifique-se de que o serviço do Ollama esteja rodando em segundo plano.

### 2. Clonar o Repositório e Configurar o Ambiente Python
1. No seu terminal, navegue até a pasta do projeto:
   ```bash
   cd caminho/para/o/seu-projeto
   ```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   # No Mac/Linux:
   source venv/bin/activate
   ```

### 3. Instalar as Dependências
Instale todos os pacotes necessários listados no arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```
*(Caso não tenha criado o arquivo, os pacotes principais são: `pip install streamlit pandas requests pypdf`)*

### 4. Executar a Aplicação
Com o Ollama ativo e as bibliotecas instaladas, inicie o painel do Streamlit com o comando:
```bash
streamlit run app.py
```

Uma aba será aberta automaticamente no seu navegador de internet padrão (geralmente no endereço `http://localhost:8501`).

---

## 💡 Como Usar a Aplicação

1. **Anexe o arquivo do paciente:** Na barra lateral esquerda (*Sidebar*), clique em carregar arquivo e envie um relatório clínico do paciente no formato **.txt** ou **.pdf**.
2. **Faça uma solicitação completa (PTS):** Na caixa de chat inferior, envie um comando amplo como: *"Gere a minuta do PTS com base no arquivo fornecido"*. O agente lerá o arquivo, cruzará com as diretrizes do Caps e devolverá o plano completo estruturado em **5 etapas obrigatórias** (Aviso de segurança, Síntese do caso, Regime recomendado, Oficinas indicadas, Medicação centralizada e Lacunas identificadas).
3. **Faça perguntas pontuais:** Caso queira apenas uma busca rápida, pergunte algo direto como: *"Quantas faltas este paciente teve no histórico?"*. O agente identificará sua intenção e responderá em poucos parágrafos sem a rigidez da estrutura de 5 etapas.
