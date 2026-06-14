# JARVIS Acadêmico — Assistente de Estudos Autônomo

O JARVIS Acadêmico é um agente inteligente desenvolvido para atuar como um organizador pessoal e tutor de conteúdo para estudantes. Ele integra um pipeline de recuperação de informações (RAG) com automações de agenda atráves do Google Calendar API e Google Tasks API.

---

## Modelos de Inteligência Artificial Utilizados

Os modelos utilizados para a implementação ágil do trabalho foram:
* **GPT** (OpenAI)
* **Claude** (Anthropic)
* **Gemini** (Google)

---

## Configuração do Ambiente (`.env`)
Para o correto funcionamento do sistema, é obrigatório criar um arquivo chamado `.env` na mesma pasta onde residem os códigos principais do agente. Este arquivo armazena caminhos locais e chaves privadas de forma segura.
O formato estruturado do arquivo deve ser o seguinte:

- LIA_API_KEY=api_key
- PASTA_MD='caminho para pasta com os markdowns'
- PASTA_EMBEDDINGS="caminho para pasta com os embeddings"
- CREDENTIALS_JSON='credenciais do google cloud para acesso às apis'
- PASTA_PDF='caminho para a pasta com os pdfs'
- PASTA_CHUNKS='caminho para pasta com os chunks'

## Ferramentas Implementadas (Tool Calling)

O JARVIS utiliza o mecanismo de Tool Calling para interagir com o sistema operacional local e APIs de nuvem. Quando o agente decide executar uma ação, ele suspende a conversação e emite exclusivamente uma estrutura JSON estruturada para o motor em Python.

Abaixo estão listadas as 9 ferramentas mapeadas em seu barramento de execução:
1. consultar_agenda

    Uso: Acionada quando o usuário pergunta sobre eventos, aulas, compromissos ou provas de um dia específico ou de um mês inteiro.

    Formato do JSON:

        Busca diária: {"tool": "consultar_agenda", "args": {"data": "YYYY-MM-DD"}}

        Busca mensal: {"tool": "consultar_agenda", "args": {"data": "YYYY-MM"}}

2. listar_tarefas

    Uso: Ativada quando o usuário manifesta o desejo de visualizar suas tarefas pendentes ou concluídas.

    Formato do JSON: {"tool": "listar_tarefas", "args": {"status": "pendente"}}

    Nota: O argumento status aceita estritamente os valores "pendente" ou "concluida".

3. adicionar_tarefa

    Uso: Utilizada para criar uma nova tarefa acadêmica no gerenciador de atividades.

    Formato do JSON: {"tool": "adicionar_tarefa", "args": {"titulo": "Estudar IA", "prazo": "YYYY-MM-DD", "prioridade": "alta"}}

    Nota: O argumento prioridade aceita estritamente os valores "alta", "media" ou "baixa".

4. concluir_tarefa

    Uso: Chamada imediatamente após o usuário informar que finalizou uma atividade local ou do ecossistema.

    Formato do JSON: {"tool": "concluir_tarefa", "args": {"id_tarefa": 1}}

5. buscar_material_rag

    Uso: Disparada obrigatoriamente sempre que o usuário faz perguntas sobre o conteúdo acadêmico teórico, conceitos científicos, definições ou fórmulas.

    Formato do JSON: {"tool": "buscar_material_rag", "args": {"query": "termo ou pergunta de busca"}}

6. adicionar_evento_agenda

    Uso: Destinada à inserção de eventos gerais, feriados ou lembretes pessoais (como aniversários) diretamente na Agenda do Google, contanto que não representem tarefas acadêmicas com prazos avaliativos.

    Formato do JSON: {"tool": "adicionar_evento_agenda", "args": {"titulo": "Aniversário da Roseli", "data": "YYYY-MM-DD"}}

7. remover_evento_agenda

    Uso: Executada quando o usuário solicita explicitamente o cancelamento ou a remoção definitiva de um compromisso ou lembrete do calendário em nuvem.

    Formato do JSON: {"tool": "remover_evento_agenda", "args": {"titulo": "Nome do Evento"}}

8. deletar_tarefa

    Uso: Responsável por remover e expurgar permanentemente do banco de dados uma tarefa do sistema através do seu indexador numérico.

    Formato do JSON: {"tool": "deletar_tarefa", "args": {"id_tarefa": 1}}

9. buscar_evento_por_titulo

    Uso: Ferramenta auxiliar de segurança. É executada antes de qualquer processo de exclusão de calendário para rastrear e verificar os metadados exatos (data e hora) de um evento a partir de uma busca textual por título.

    Formato do JSON: {"tool": "buscar_evento_por_titulo", "args": {"titulo": "Nome do Evento"}}


10. montar_plano_estudos

    Uso: Responsável por consultar o google agenda do usuário para os próximo dias e identifica 

11. iniciar_active_recall
    -Uso: Usada quando o usuário pede para o Jarvis testá-lo sobre um conteúdo específico. O Jarvis analisa  o conteúdo específico de acordo com seu material e gera perguntas para o usuário. Ao responder o Jarvis analisa a resposta e corrige caso necessário, ditando Acertos, Lacunas, complemento da resposta e Avaliação. Então ao final ele diz o quanto o usuário acertou em sua avaliação, oferecendo tópicos a revisar.

    - JSON: {"tool": "iniciar_active_recall", "args": {"tema": "nome do tema"}}
    

12. gerar_exercícios
    Uso: Usada quando o usuário pede ao sistema para gerar exercícios sobre determinado conteúdo, o sistema gera no mínimo três perguntas sobre o tema. As perguntas podem ser questões de Verdadeiro/Falso, abertas ou de múltipla escolha. Ao final de cada pergunta o sistema demonstra o gabarito de cada pergunta
    - JSON: {"tool": "gerar_exercicios", "args": {"tema": "nome do tema", "tipo": "misto", "quantidade": 3}}
   - tipos de pergunta: "multipla_escolha", "verdadeiro_falso", "aberta", "misto"

## Regras de Comportamento e Protocolos de Execução

As seguintes regras foram aplicadas ao Jarvis para eliminar possíveis alucinações e fazer com que ele correspondesse ao que se espera de um 
tutor acadêmico:

REGRAS:
- Ao usar uma ferramenta, sua resposta deve conter EXCLUSIVAMENTE o(s) bloco(s) JSON válido(s), sem textos adicionais ou saudações. 
- Se o pedido do usuário exigir duas ou mais ações, você PODE e DEVE emitir todos os JSONs necessários na mesma resposta, um em cada linha.
- Converta qualquer data relativa ("hoje", "amanhã", "próxima segunda") para o formato YYYY-MM-DD antes de acionar as ferramentas. A data base é {hoje}. Nunca envie dias da semana em formato de texto para as APIs.
- Escreva qualquer equação, fração ou expressão matemática EXCLUSIVAMENTE em texto simples de teclado. É proibido o uso de formatação gráfica ou LaTeX (ex: escreva 'a^2 + b^2 = c^2' ou '1/2').
- Sempre que o assunto for acadêmico, conceitual ou explicativo, você DEVE usar 'buscar_material_rag' ANTES de responder. 
- Baseie sua resposta e eventuais "exemplos" EXCLUSIVAMENTE no material recuperado. Nunca invente dados. Se não tiver certeza ou a informação não constar nos materiais, diga claramente que não a encontrou.
- Ferramentas interativas ('iniciar_active_recall' e 'gerar_exercicios') NUNCA devem ser usadas por iniciativa própria ao explicar um conteúdo. Acione-as SOMENTE mediante comando explícito do usuário (ex: "exercício", "quiz", "me teste", "quero praticar").
- Ao final de uma explicação, você PODE oferecer a opção de praticar ("Quer fazer exercícios sobre este tema?"), mas NÃO acione a ferramenta até que o usuário confirme.
- Se o usuário pedir para ser testado mas NÃO especificar um tema, interrompa a ação. Liste os temas mais relevantes encontrados no RAG e exija que ele escolha um. APENAS DEPOIS da escolha, chame a ferramenta 'iniciar_active_recall' com o tema específico. 
- O conteúdo recuperado pelo 'buscar_material_rag' deve ser a base estrita para as perguntas geradas no active recall.
- Para deletar ou remover um evento do calendário, NUNCA chame 'remover_evento_agenda' diretamente.
- Você DEVE usar 'buscar_evento_por_titulo' primeiro. Em seguida, apresente a data/evento ao usuário e pergunte: "Tem certeza que deseja remover?". Aguarde o "sim" explícito para só então prosseguir com a exclusão.
- NUNCA adivinhe o ID de uma tarefa. Se o usuário pedir para concluir ou deletar uma tarefa, use 'listar_tarefas' primeiro.
- ASSIM QUE O SISTEMA DEVOLVER A LISTA COM O ID, você deve emitir o JSON de 'concluir_tarefa' ou 'deletar_tarefa' IMEDIATAMENTE na próxima rodada. NÃO peça confirmação e NÃO faça perguntas ao usuário. Apenas execute.
- Você é ESTRITAMENTE PROIBIDO de confirmar textualmente ao usuário que uma tarefa ou evento foi criado, concluído ou deletado sem antes ler o retorno real de sucesso fornecido pelos logs do sistema local. Nunca invente resultados.
"""
