# Deeper — Roteiro de apresentação para a FSB Holding

**Contexto:** apresentação de entrega do MVP · público: FSB Holding (cliente) · duração sugerida 45–60 min + Q&A
**Como usar este documento:** cada bloco tem (a) o objetivo, (b) o que falar, (c) frases-chave que valem ser ditas literalmente, (d) números conferidos. Não decore — internalize a lógica de cada bloco.

**Regra de ouro da apresentação:** a palavra **MVP** aparece nos primeiros 60 segundos. Tudo que vem depois é lido como "protótipo funcional que superou o esperado" em vez de "produto com buracos". Enquadramento errado transforma qualidade em decepção.

---

## BLOCO 0 — Abertura (2 min)

**Objetivo:** dizer em 30 segundos o que é, e comprar o direito de falar por mais 45 minutos.

Fale:
- Quem é você: aluno de Comunicação da FGV ECMI, interesse em dados, plataformas digitais e IA aplicada.
- O que você traz: um MVP funcional — não um conceito, não um slide — de uma ferramenta de inteligência sobre executivos, construída do zero para a FSB.
- O contrato da conversa: "vou mostrar funcionando, explicar como funciona por dentro, ser transparente sobre o que ele **não** faz, falar de custo e de legalidade, e terminar com o que eu proponho como próximo passo."

**Frase-chave de abertura:**
> "O que vou apresentar é um MVP — um protótipo funcional. Ele roda, coleta dados reais e produz dossiês reais; ainda não é um sistema instalado e disponível para a equipe. A diferença entre esses dois estágios é exatamente o que vou detalhar no final."

---

## BLOCO 1 — O problema (4 min)

**Objetivo:** fazer a plateia reconhecer a dor antes de ver a solução. Se eles concordarem com o problema, o produto se vende sozinho.

Fale:
- A rotina real: um analista precisa preparar aproximação com um executivo — para um pitch, um media training, um mapeamento de stakeholders, uma crise. O que ele faz hoje? Google, LinkedIn aberto em outra aba, três reportagens, um documento no Word. Entre 1 e 2 horas de trabalho, e o resultado depende de quem pesquisou.
- Os três defeitos desse processo:
  1. **Não é reproduzível** — dois analistas produzem dossiês diferentes da mesma pessoa.
  2. **Envelhece mal** — a informação fica num documento que ninguém atualiza.
  3. **Perde a rede** — a parte mais valiosa (com quem essa pessoa se relaciona) é a que mais dá trabalho de levantar, então quase nunca é feita.
- A pergunta que o analista precisa responder, e que virou a espinha do produto:

**Frase-chave (repita ao longo da apresentação — é o slogan do produto):**
> "Quem é, o que pensa, como a mídia o trata, e quem ele conhece."

- O pedido original da FSB: uma ferramenta para pesquisar figuras C-level e encontrar informações de negócio de acesso público através das redes — em especial o LinkedIn: cargos, trajetória, participação em eventos, valores, conexões — com a possibilidade de montar um grafo de conexões que facilite o contato.

---

## BLOCO 2 — Demonstração ao vivo (10–12 min)

**Objetivo:** provar que funciona antes de explicar como funciona. Explicação depois da prova convence; antes, soa como promessa.

> ⚠️ **Preparação obrigatória (faça 30 min antes):** subir a API (`uvicorn app.main:app --reload`), subir o worker (`python scripts\rodar_worker.py`), abrir o `index_v2.html`, conferir a aba **Status** (tudo verde) e deixar **pelo menos dois dossiês já no acervo** (ex.: Eduardo Bartolomeo e mais um executivo relevante para a FSB — de preferência alguém ligado a um cliente da casa). Tenha **prints de um dossiê completo** como plano B caso a internet caia.

Roteiro da demo, na ordem:

1. **Tela inicial.** "A ferramenta chama Deeper. Uma barra de busca — é tudo que o analista precisa saber para usar."
2. **Busca por cargo, não por nome.** Digite algo como *"CEO do Nubank"*. Mostre o painel de sugestões: acervo + candidatos do LinkedIn com o headline de cada um.
   > **Frase-chave:** "Repare que ela não pesquisa direto. Ela pergunta 'quem exatamente você quer dizer?'. Isso não é um detalhe de usabilidade — é a diferença entre um dossiê certo e um dossiê de um homônimo. Volto nesse ponto."
3. **Escolha um candidato** e deixe a coleta rodar. Enquanto roda (20–60s), narre as etapas na tela: imprensa → LinkedIn → análise com IA → grafo. Aproveite para dizer que dá para cancelar e que a coleta continua no servidor.
4. **O dossiê.** Percorra na ordem: briefing executivo (leia dois períodos em voz alta — é o produto), trajetória, menções com sentimento, eventos.
   > **Frase-chave:** "Cada afirmação aqui tem fonte clicável. Nada é 'a IA disse'."
5. **O grafo — o clímax.** Abra em tela cheia. Mostre: nó raiz, tipos de laço (formal x imprensa), clique numa aresta para exibir as evidências, mostre uma conexão marcada como **lista/ranking** e ligue o filtro para escondê-la.
   > **Frase-chave:** "Este é o diferencial que eu mais gosto: a ferramenta sabe distinguir 'essas duas pessoas se relacionam' de 'essas duas pessoas apareceram no mesmo ranking dos 50 mais ricos'. A segunda não é uma relação — e o mercado costuma tratar como se fosse."
6. **Navegação em rede.** Clique num nó secundário e use o botão **Pesquisar** para saltar para outra pessoa. "É assim que um mapeamento de stakeholders vira uma sessão de 15 minutos."
7. **Acervo e cache.** Abra a aba Acervo: "o que a equipe pesquisa fica disponível para todo mundo, por 7 dias, sem custo de nova coleta."

---

## BLOCO 3 — Como funciona por dentro (10 min)

**Objetivo:** mostrar que existe engenharia real por baixo, em linguagem de comunicação — sem jargão gratuito, mas sem infantilizar.

### 3.1 O caminho de uma busca (desenhe isso num slide)

```
Você escolhe a pessoa (identidade confirmada)
        ↓
[1] IMPRENSA — busca no Google restrita a 10 portais brasileiros
        ↓        (Valor, Estadão, Folha, O Globo, Exame, InfoMoney, NeoFeed, Veja, IstoÉ Dinheiro, Brazilian Report)
[2] LEITURA — baixa o corpo das matérias, não só a manchete
        ↓
[3] LINKEDIN — perfil público: trajetória, formação, bio, foto
        ↓
[4] IA (extração) — lê cada matéria e devolve dados estruturados
        ↓        (pessoas citadas, empresas, eventos, valores, temas, sentimento)
[5] GRAFO — cruza tudo e monta a rede de conexões
        ↓
[6] IA (síntese) — escreve o briefing de 3 parágrafos a partir do conjunto
        ↓
     DOSSIÊ
```

Tempo total: **20 a 60 segundos**. Tudo roda em segundo plano — a interface não trava.

### 3.2 Dois usos diferentes de IA (este ponto impressiona quem entende)

Fale que o LLM (Claude Sonnet, da Anthropic) é usado de **duas formas distintas**:

- **Extração estruturada:** para cada matéria, o modelo é obrigado a preencher um formulário fixo (quem foi citado, que empresas, que valores, que temas, que sentimento de −1 a +1). Ele não escreve texto livre — preenche campos. Isso reduz drasticamente o espaço para invenção.
- **Síntese:** só no final, com todos os dados já estruturados e verificados na mão, o modelo escreve o briefing.

> **Frase-chave:** "A IA não 'pesquisa' o executivo. Ela lê o que nós coletamos de fontes que nós escolhemos, e organiza. A diferença entre isso e perguntar para o ChatGPT é a diferença entre um analista com as fontes na mesa e um analista de memória."

### 3.3 O grafo: dois tipos de conexão

- **Laço formal** (laranja, sólido): as duas pessoas trabalharam na mesma empresa em períodos que se sobrepõem, ou dividem um conselho — inferido das trajetórias do LinkedIn. É verificável.
- **Co-menção na imprensa** (cinza): apareceram juntas em matérias. Mais fraco, mas revelador.
- **Rótulo de contexto:** cada evidência é classificada como *direta* ou *lista/ranking*. Conexões que só existem porque as duas pessoas apareceram na mesma listagem nascem esmaecidas e podem ser filtradas.

> **Frase-chave:** "O grafo cresce com o uso. Cada executivo novo que a equipe pesquisa enriquece a rede dos que já estão lá."

### 3.4 O que o sistema faz sozinho (mencione rápido — mostra maturidade)

- **Cache de 7 dias** por pessoa: pesquisa repetida abre na hora, sem custo.
- **Cache do LinkedIn de 30 dias:** mesmo forçando recoleta, não se paga o perfil de novo.
- **Auto-recuperação:** se uma etapa falhou (API instável), a próxima busca reprocessa o que ficou pendente.
- **Higienização:** remove páginas de índice ("Tudo sobre Fulano"), funde matérias duplicadas com URLs de rastreamento diferentes, preenche datas faltantes lendo a URL da matéria.
- **Tolerância a falha:** cada fonte pode cair sem derrubar a coleta — o dossiê fica mais pobre, não quebra.

---

## BLOCO 4 — As decisões difíceis (8 min) ⭐

**Objetivo:** este é o bloco que separa "um aluno fez um app" de "alguém pensou sobre o problema". Cada item é um caso real que aconteceu no desenvolvimento e mudou o produto. Conte como história.

### Caso 1 — O homônimo (o mais importante)
Pesquisei "Renato Costa" querendo o CEO da Friboi. O sistema achou um Renato Costa que é CIO da Odontoprev. Pior: quando corrigi, o dossiê continuou misturado, porque o sistema tratava "quem tem o mesmo nome" como "a mesma pessoa".
**O que mudou:** identidade passou a ser confirmada por perfil do LinkedIn, não por nome; trocar de perfil apaga o dossiê antigo por inteiro; e a IA passou a receber o cargo junto do nome para descartar matérias sobre homônimos.
> "A ferramenta hoje se recusa a pesquisar alguém novo sem que você aponte quem é. Foi uma decisão de produto contraintuitiva — adicionar um clique — tomada porque um dossiê errado é pior que dossiê nenhum."

### Caso 2 — A lista dos 50 mais ricos
O grafo mostrava um executivo "conectado" a meia dúzia de bilionários. A origem era uma matéria de ranking.
**O que mudou:** classificação de contexto em cada evidência e filtro na interface.
> "Um mapa de relacionamento que trata coincidência como relação é pior que não ter mapa: ele produz confiança injustificada."

### Caso 3 — A imprensa desatualizada
O dossiê do Eduardo Bartolomeo dizia "CEO da Vale", porque é isso que as matérias de 2024 dizem. O LinkedIn dele mostra o cargo atual: conselheiro na Boston Metal.
> "Notícia envelhece; o LinkedIn é o registro vivo. Cruzar as duas fontes não é redundância — é o que permite acertar o presente."

### Caso 4 — A data errada
Numa versão inicial, a IA lia "assumiu o cargo em março de 2019" e registrava isso como data da matéria — gerando erro factual no briefing.
**O que mudou:** datas só vêm da URL/metadados da matéria, nunca do texto interpretado.
> "Num produto de reputação, um erro factual custa mais do que uma informação faltando."

### Caso 5 — A manchete não nomeia ninguém
O grafo de CEOs de grandes empresas vinha quase vazio, enquanto o de figuras políticas vinha cheio. A razão: o sistema lia só título e resumo, e manchete de economia não cita nomes ("Itaú lucra R$ X bi"), enquanto manchete de política cita.
**O que mudou:** passamos a baixar e ler o corpo das matérias — de ~200 para até 4.000 caracteres por matéria.

---

## BLOCO 5 — Legalidade e ética (8 min) ⭐⭐

**Objetivo:** este bloco é obrigatório e você deve levantá-lo você mesmo, antes que perguntem. Uma empresa cuja mercadoria é reputação precisa ver que o autor pensou nisso. Levantar o tema é sinal de maturidade; ser pego sem resposta é o oposto.

**Abra assim:**
> "Antes de falar de custo, preciso falar de uma coisa que ninguém aqui perguntou ainda mas que toda empresa de comunicação deveria perguntar: isso é legal? A resposta honesta é 'sim, com condições' — e eu quero detalhar as condições."

### 5.1 O que a ferramenta coleta — e o que ela não coleta

| Coleta | Não coleta |
|---|---|
| Perfil **público** do LinkedIn (o que qualquer pessoa vê sem login) | Nada atrás de login ou de conexão aceita |
| Matérias de imprensa publicadas | Mensagens, e-mails, telefone, dados de contato |
| Dados **profissionais** de figuras públicas em capacidade profissional | Dados sensíveis (saúde, religião, opinião política, biometria) |
| | Lista de conexões do LinkedIn — **não é pública e não é acessada** |

> **Frase-chave:** "A rede de conexões que vocês viram no grafo **não** é a lista de contatos do LinkedIn — essa não é pública e nós não acessamos. Nossa rede é inferida de fatos públicos: trajetórias que se sobrepõem e matérias que citam as duas pessoas. É por isso que cada aresta vem com as evidências anexadas."

### 5.2 O cenário jurídico do scraping (seja preciso aqui)

**Nos EUA — o caso hiQ Labs vs. LinkedIn**, a referência mundial do tema:
- A Corte de Apelações do 9º Circuito decidiu que **raspar dados públicos não viola o CFAA** (a lei criminal de acesso não autorizado), porque não há "acesso sem autorização" a páginas abertas ao público.
- **Mas** o caso terminou em dezembro de 2022 com acordo desfavorável à hiQ: US$ 500 mil e proibição permanente de raspar o LinkedIn — com base em **quebra de contrato** (os Termos de Uso), e em condutas específicas dela, como criar contas falsas para acessar páginas protegidas por senha.
- **A lição prática, que é exatamente a nossa fronteira:** dado público não é crime de acesso; mas violar termos de uso gera responsabilidade contratual, e usar login falso muda o jogo por completo.
- **Onde estamos:** não usamos login, não criamos contas, não acessamos página protegida. Usamos um serviço terceirizado (Apify) sobre páginas públicas. Isso reduz o risco a uma zona cinzenta de termos de uso do LinkedIn — a mesma zona em que opera boa parte do mercado de inteligência de dados. **Não vou dizer que é risco zero, porque não é.**

**No Brasil — LGPD:**
- Dado pessoal tornado **manifestamente público pelo titular** dispensa consentimento (art. 7º, §4º) — um CEO que publica o próprio cargo no LinkedIn se enquadra aqui.
- **Mas a dispensa não é passe livre:** a própria lei ressalva "os direitos do titular e os princípios previstos nesta Lei". Continuam valendo finalidade legítima, adequação, necessidade, transparência e o direito do titular de pedir informação e exclusão.
- A base legal adequada para o nosso uso é o **legítimo interesse** (art. 7º, IX): inteligência de comunicação corporativa sobre executivos em capacidade profissional é finalidade legítima e proporcional.
- Não tratamos dados sensíveis (art. 11), o que evita a exigência mais rígida da lei.

### 5.3 As recomendações que eu levo junto com a ferramenta (diga que são suas)

1. **Política de retenção** — dossiês têm validade; definir por quanto tempo ficam armazenados.
2. **Canal de exclusão** — se um executivo pedir remoção, a FSB precisa ter processo para atender.
3. **Uso interno e profissional** — a ferramenta apoia relacionamento institucional; não deve alimentar decisão automatizada sobre a pessoa nem ser revendida como base de dados.
4. **Rastreabilidade** — já está no produto: toda afirmação do grafo tem fonte. Isso não é só usabilidade, é defesa.
5. **Antes de virar produção, passar pelo jurídico da casa** — inclusive para decidir se a FSB prefere trocar o scraping por uma fonte licenciada, o que é uma opção real e que eu recomendo avaliar.

> **Frase-chave de fechamento do bloco:** "Minha recomendação é que a FSB trate isso como uma decisão de compliance consciente, e não como um detalhe técnico. A ferramenta foi construída para operar do lado defensável da linha, e para deixar rastro de tudo que faz."

### 5.4 Um ponto de privacidade que costuma passar batido

Os textos coletados são enviados para a API da Anthropic (EUA) para análise. São dados públicos, e a Anthropic não usa dados de API para treinar modelos por padrão — mas é um fluxo internacional de dados que o jurídico deve conhecer. Diga isso você mesmo.

---

## BLOCO 6 — Números: custo, tempo e escala (5 min)

**Objetivo:** transformar "que legal" em "quanto custa e o que economiza".

### Custo por dossiê novo

| Item | Custo aproximado |
|---|---|
| Coleta do perfil LinkedIn (Apify) | US$ 0,005 |
| Análise com IA (Claude Sonnet — ~20 extrações + 1 síntese) | ~US$ 0,17 |
| Buscas (SerpAPI — sugestões + imprensa) | ~US$ 0,03 |
| **Total por dossiê novo** | **≈ US$ 0,20 (cerca de R$ 1,00–1,20)** |
| Dossiê já no acervo (cache de 7 dias) | **R$ 0,00** |

> **Frase-chave:** "Um dossiê custa cerca de um real e leva um minuto. O mesmo trabalho feito à mão custa entre uma e duas horas de um analista. Não é uma economia marginal — é outra ordem de grandeza."

### Custo mensal em escala de equipe

| Item | Hoje (MVP) | Uso por equipe |
|---|---|---|
| SerpAPI | plano gratuito — 250 buscas/mês (~100 pesquisas novas) | ~US$ 75/mês (5.000 buscas) |
| Anthropic (IA) | pago por uso | ~US$ 20–60/mês dependendo do volume |
| Apify (LinkedIn) | crédito gratuito cobre o MVP | ~US$ 10–49/mês |
| Servidor (não existe hoje) | R$ 0 — roda na minha máquina | ~US$ 20–50/mês |
| **Total** | **praticamente zero** | **≈ US$ 125–235/mês** |

> **Frase-chave:** "O gargalo hoje não é dinheiro, é cota: o plano gratuito de busca banca cerca de 100 pesquisas novas por mês. Para uso de equipe, o custo total fica abaixo do valor de um dia de trabalho de um analista sênior."

### O que existe hoje, em números

- **69 testes automatizados** passando (cobrem o pipeline, os coletores, o grafo e a API)
- **~4.200 linhas** de Python (aplicação + testes) e **~1.200 linhas** de interface
- **7 tabelas** no banco · **6 endpoints** de API · **10 portais** de imprensa monitorados
- Dossiês reais já validados com executivos brasileiros de verdade

---

## BLOCO 7 — O que o app NÃO faz (4 min) ⭐

**Objetivo:** contra-intuitivo, mas este bloco **aumenta** a confiança. Quem lista as próprias limitações é lido como confiável no resto.

**Abra assim:**
> "Vou fazer agora a parte que normalmente não se faz numa apresentação: listar o que a ferramenta não faz. Prefiro que vocês ouçam de mim hoje do que descubram sozinhos na semana que vem."

1. **Não está instalada.** Roda na minha máquina, sem login, sem servidor. Hoje ela existe para demonstração — não para a equipe usar amanhã.
2. **Não monitora.** É uma fotografia sob demanda, não vigilância contínua. Não avisa quando um executivo aparece na imprensa. *(Este é, provavelmente, o pedido nº 1 que vocês farão — e está no roadmap.)*
3. **Não exporta.** O dossiê vive na tela. Dá para copiar o briefing; não dá para gerar um PDF para anexar num e-mail ao cliente.
4. **Cobertura nacional.** Dez portais brasileiros. Executivos internacionais saem pobres — o CEO da Nvidia rende pouco aqui.
5. **A rede começa rala.** O grafo engorda conforme a equipe pesquisa. Nos primeiros dias, redes pequenas.
6. **O briefing é gerado por IA.** É bom, tem fontes, e a arquitetura reduz muito o risco de invenção — mas não elimina. **Recomendo tratar o briefing como o rascunho de um analista júnior competente: sempre com revisão humana antes de ir para o cliente.**
7. **Sem autenticação.** Qualquer pessoa com acesso à rede acessaria. Resolvido na fase 2.

---

## BLOCO 8 — Roadmap: o que falta para virar produto (5 min)

**Objetivo:** aqui você deixa de apresentar o passado e passa a propor o futuro. É o bloco que transforma "obrigado pelo trabalho" em "vamos conversar".

**Fase 2 — colocar de pé (estimativa: 4–6 semanas)**
- Deploy em servidor + banco gerenciado (a equipe acessa por um link)
- Autenticação e perfis de usuário
- Exportação em PDF/DOCX do dossiê
- Log de uso e controle de cota

**Fase 3 — virar rotina (estimativa: 6–10 semanas)**
- **Monitoramento contínuo com alertas** (a pessoa entrou na imprensa hoje → aviso)
- Cobertura internacional (GDELT — base global e gratuita de notícias)
- Posts públicos do LinkedIn como sinal de relacionamento (quem a pessoa marca e comenta)
- Fontes formais brasileiras: quadros societários e conselhos de companhias abertas — enriquecem muito o grafo de laços formais
- Integração com as ferramentas que a FSB já usa

**Frase-chave:**
> "Existe um caminho claro entre o que vocês viram e uma ferramenta que a equipe usa toda semana. São dois a três meses de trabalho, não um recomeço."

---

## BLOCO 9 — Fechamento e proposta (3 min)

**Objetivo:** terminar com um pedido concreto. Apresentação sem pedido vira elogio e acaba ali.

Recapitule em três frases:
1. O MVP responde a pergunta que o analista precisa responder, em um minuto e por cerca de um real.
2. Ele foi construído com cuidado nas partes que importam para uma empresa de reputação: identidade correta, rastreabilidade de fonte, distinção entre conexão real e coincidência.
3. O que existe hoje é um protótipo funcional; o caminho até produção está mapeado.

**Escolha o seu pedido** (defina antes de entrar na sala — recomendo o primeiro):
- **A (recomendado):** "Gostaria de propor uma fase 2: colocar isso no ar para um grupo piloto da casa. Posso trazer um escopo fechado com prazo e custo."
- **B:** "Gostaria de discutir como isso poderia continuar dentro da FSB — como estágio, projeto ou parceria."
- **C:** "Gostaria do retorno de vocês sobre quais funcionalidades teriam mais valor no dia a dia, para priorizar o que construo em seguida."

**Última frase sugerida:**
> "Construí isso sozinho, em algumas semanas, como aluno de Comunicação — não de Engenharia. Se um MVP feito assim já produz o que vocês viram, imagino o que a FSB faria com essa capacidade instalada dentro de casa."

---

## ANEXO A — Perguntas difíceis e como responder

**"Isso não é ilegal? Não vamos ser processados?"**
> Dado público, sem login, sem conta falsa — a jurisprudência americana (hiQ vs. LinkedIn) diz que isso não é crime de acesso. O risco existente é contratual, de termos de uso do LinkedIn, e é a mesma zona em que opera boa parte do mercado. No Brasil, a LGPD permite tratar dado tornado público pelo titular com base em legítimo interesse, respeitados os princípios da lei. Minha recomendação é passar pelo jurídico antes de produção, e avaliar substituir o scraping por uma fonte licenciada.

**"E se a IA inventar alguma coisa sobre um executivo e isso vazar para o cliente?"**
> Risco real e por isso a arquitetura separa extração de síntese: o modelo preenche campos verificáveis antes de escrever qualquer texto, e cada afirmação tem fonte clicável. Ainda assim, recomendo formalmente revisão humana antes de qualquer uso externo. O briefing é rascunho de analista, não peça final.

**"Por que não usar só o ChatGPT/Claude direto?"**
> Porque um chatbot responde de memória, com data de corte, sem fonte e sem consistência entre duas perguntas iguais. Aqui as fontes são escolhidas, a coleta é datada, o resultado é auditável e fica armazenado para a equipe inteira. E o grafo de relações simplesmente não existe num chat.

**"Quanto custaria para colocar de pé?"**
> Infraestrutura e APIs ficam na casa de US$ 125–235 por mês em uso de equipe. O trabalho de desenvolvimento da fase 2 é de 4 a 6 semanas. Posso trazer uma proposta fechada.

**"Isso funciona para pessoas que não são CEOs?"**
> Funciona para qualquer pessoa com presença pública — quanto menor a exposição na imprensa, mais o dossiê depende só do LinkedIn. Para figuras sem presença digital, a ferramenta entrega pouco, e ela diz isso na tela em vez de inventar.

**"Os dados ficam com você?"**
> Hoje ficam na minha máquina, porque é um MVP. Na fase 2, ficam em servidor da FSB, com acesso controlado. Essa é uma das razões pelas quais eu chamo o estágio atual de protótipo.

**"Quem mantém isso se você sair?"**
> Pergunta justa. O código está documentado, com 69 testes automatizados que descrevem o comportamento esperado — é o que permite outra pessoa mexer sem quebrar. Mas a resposta honesta é que um projeto assim precisa de dono definido, e isso faz parte da conversa da fase 2.

---

## ANEXO B — Checklist do dia

**Véspera**
- [ ] Testar o fluxo completo do começo ao fim, com internet da sala se possível
- [ ] Deixar 2–3 dossiês prontos no acervo (incluir alguém ligado a um cliente da FSB)
- [ ] Tirar prints: tela inicial, sugestões, dossiê completo, grafo em tela cheia, painel de evidências de uma aresta
- [ ] Conferir saldo/cota das APIs (SerpAPI é o que acaba primeiro)

**No dia**
- [ ] API rodando · worker rodando · aba Status toda verde
- [ ] Navegador com zoom ajustado para projetor (fonte legível do fundo da sala)
- [ ] Notificações do sistema desligadas
- [ ] Plano B aberto numa aba: prints + este roteiro

**Se a demo falhar ao vivo:** não tente consertar na hora. Diga a frase e siga pelos prints:
> "É um MVP rodando ao vivo com fontes externas — e é exatamente por isso que a fase 2 prevê infraestrutura dedicada. Vou mostrar pelos registros da última execução."

---

## ANEXO C — Fontes citadas neste roteiro

- Ninth Circuit e o desfecho do caso hiQ Labs vs. LinkedIn (dezembro de 2022): [Morgan Lewis](https://www.morganlewis.com/blogs/sourcingatmorganlewis/2022/12/linkedin-v-hiq-landmark-data-scraping-suit-provides-guidance-to-data-scrapers-and-web-operators) · [Privacy World](https://www.privacyworld.blog/2022/12/linkedins-data-scraping-battle-with-hiq-labs-ends-with-proposed-judgment/) · [Fenwick](https://www.fenwick.com/insights/publications/hiq-labs-scrapes-by-again-the-ninth-circuit-reaffirms-that-data-scraping-does-not-violate-the-cfaa-1)
- LGPD, art. 7º §4º e os limites do dado manifestamente público: [Migalhas](https://www.migalhas.com.br/depeso/293745/a-excecao-dos-dados-pessoais-tornados-manifestamente-publicos-pelo-titular-na-lgpd) · [Conjur](https://www.conjur.com.br/2021-mai-05/maciel-data-scraping-responsabilidade-controlador/) · [Migalhas — desafios jurídicos do web scraping](https://www.migalhas.com.br/coluna/dados-publicos/378258/os-desafios-juridicos-do-web-scraping)
