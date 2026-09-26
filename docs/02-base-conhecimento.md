# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_consultas.csv` | CSV | Registro histórico de presenças, faltas, crises e evoluções anteriores do paciente no Caps para análise de adesão ao tratamento. |
| `diretrizes_caps_pts.json` | JSON | Base de conhecimento fixa contendo o catálogo de oficinas terapêuticas, critérios de frequência (intensivo, semi-intensivo, não-intensivo) e protocolos de acolhimento baseados no Ministério da Saúde. |
| `documento_paciente.[pdf/txt]` | PDF / TXT | Arquivo anexado dinamicamente pelo profissional (anamnese, laudo ou relatório de transferência) contendo a situação atual do paciente. |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados foram totalmente reestruturados para o contexto de Saúde Mental Pública (SUS). Em vez de produtos financeiros e investimentos, o dataset simula dados clínicos reais de um Caps. Todos os arquivos de dados dos pacientes foram criados utilizando técnicas de anonimização estrita (substituindo nomes reais por IDs, mascarando CPFs e alterando endereços por bairros genéricos) para garantir conformidade com a LGPD e o sigilo médico.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

# 1. Carrega as diretrizes institucionais do CAPS (Catálogo de oficinas e regras)
with open('./data/diretrizes_caps_pts.json', 'r', encoding='utf-8') as f:
    diretrizes_caps = json.load(f)

# 2. Carrega o documento atual anexado do paciente (Texto Puro)
with open('./data/documento_paciente_exemplo.txt', 'r', encoding='utf-8') as f:
    documento_paciente = f.read()

# 3. Carrega o histórico de evolução de consultas anteriores (Tabela)
historico = pd.read_csv('./data/historico_consultas.csv', encoding='utf-8')

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

As diretrizes institucionais do Caps vão estruturadas dentro do System Prompt para garantir que a IA nunca sugira tratamentos fora da realidade do SUS. Já os dados específicos do paciente (histórico + arquivo anexado) são injetados dinamicamente no Contexto da Mensagem (User Prompt). O prompt força a LLM a cruzar o relatório do arquivo com as regras do JSON para gerar a minuta final do PTS.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
[DIRETRIZES DA INSTITUIÇÃO (Origem: diretrizes_caps_pts.json)]
Oficinas Disponíveis: Arteterapia, Cineclube, Horta e Jardinagem, Geração de Renda.
Regimes de Caps: 
- Intensivo (atendimento diário)
- Semi-intensivo (até 12 dias no mês)
- Não-intensivo (atendimentos mensais/esporádicos)

[HISTÓRICO DO PACIENTE (Origem: historico_consultas.csv)]
- Paciente ID: #CAPS-9872
- Data de Admissão: 14/03/2025
- Frequência Recente: Faltou às duas últimas consultas com a psicologia. Relato de isolamento social.

[DADOS DO ARQUIVO ANEXADO (Origem: documento_paciente.pdf - Relatório Psiquiátrico de 24/09/2026)]
"Paciente apresenta quadro de depressão maior com sintomas ansiosos graves. Relata insônia terminal e anedonia. Conduta Médica: Ajuste de Sertralina para 100mg/dia. Encaminho para intensificação de cuidados e inclusão em atividades comunitárias/oficinas."

```
