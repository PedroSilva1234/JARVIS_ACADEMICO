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

## Regras de Comportamento e Protocolos de Execução

As seguintes regras foram aplicadas ao Jarvis para eliminar possíveis alucinações e fazer com que ele correspondesse ao que se espera de um 
tutor acadêmico:

- Use buscar_material_rag ANTES de responder sobre conteúdo.
- Quando acionar uma ferramenta, responda APENAS com o JSON no formato especificado.
- Se o usuário pedir duas ou mais coisas, você PODE e DEVE gerar os múltiplos JSONs na mesma resposta, um em cada linha.
- REGRA DE CONFIRMAÇÃO (APENAS PARA EXCLUIR EVENTOS DA AGENDA): Se o usuário pedir para deletar ou remover um evento do calendário, NUNCA chame 'remover_evento_agenda' de imediato. Você DEVE usar 'buscar_evento_por_titulo' primeiro, apresentar a data ao usuário e perguntar "Tem certeza que deseja remover?". Aguarde o "sim" para prosseguir.
- REGRA DE TAREFAS (SEM CONFIRMAÇÃO, AÇÃO IMEDIATA): NUNCA adivinhe o ID de uma tarefa. Se o usuário pedir para concluir ou deletar uma tarefa, use 'listar_tarefas' primeiro para descobrir o ID. ASSIM QUE O PYTHON DEVOLVER O ID, VOCÊ DEVE EMITIR O JSON DE 'concluir_tarefa' OU 'deletar_tarefa' IMEDIATAMENTE NA PRÓXIMA RODADA. NÃO peça confirmação e NÃO faça perguntas ao usuário sobre tarefas. Apenas execute.
- NUNCA afirme textualmente que uma tarefa ou evento foi criado, concluído ou deletado a menos que você tenha visto o resultado de sucesso da ferramenta correspondente nos logs do sistema.
- Nunca invente dados. Se não tiver certeza, diga que não encontrou a informação.
