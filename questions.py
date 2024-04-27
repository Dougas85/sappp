
# questions.py

import random

QUESTIONS = [
    {
        "question": " Lista 01 - Item 01 - É realizado o acompanhamento constante de cada etapa do processo produtivo interno? Aspectos: Produtividade e Prioridade",
        "answer": "OBJETIVO DO ITEM: Asssegurar que as atividades ocorram sob o acompanhamento dos gestores. FORMA DE AVALIAR: Verificar se pelo menos um dos gestores acompanha a execução das etapas do processo produtivo interno, principalmente as atividades da Primeira Triagem dois distritos postais (CDD) e indução na área de tratamento de encomendas. PONTO DE VERIFICAÇÃO: Salão Operacional. PERÍODO: Nos dias da verificação. AMOSTRA: Momentos de triagem/indução. MARGEM DE TOLERÂNCIA: Não há. Peso do Item: 4"},
    {
        "question": "Lista 01 - Item 02 - Os equipamentos estão etiquetados/rotulados/identificados de acordo com o padrão estabelecido? Aspectos: informação e produtividade ",
        "answer": "OBJETIVO DO ITEM: Realizar gestão visual e gerar ganho no processo. FORMA DE AVALIAR: (Considerar unitizadores com carga de objetos de alternância, antecipada, etc.) 1. No CDD Verificar: a) No salão operacional, se as mesas para carteiro: I - têm as etiquetas de primeira e segunda triagens ou TD e SL, conforme o padrão estabelecido; II - nas etiquetas de SL/2ª triagens constam a marcação de priorização de DA e GU, quando houver. b) se as mesas para carteiro têm as etiquetas de acordo com a posição indicada pelo SRO. Considerar Conforme em unidades cujos distritos tenham excesso de quebra da faixa de CEP, mas a unidade disponibilize na parte interna do escaninho2. No CEE Verificar se as direções das estações de pré-triagem, triagem e expedição estão identificadas em todos os equipamentos utilizados. PONTO DE VERIFICAÇÃO: Salão OperacionalPERÍODO: Nos dias da verificação.AMOSTRA: Todos os equipamentos. MARGEM DE TOLERÂNCIA: Não há. Peso do Item - 02 - Referência: MANPOC 15/1 anexo3 MANDIS 2/1 anexo 2 "},
    {
        "question": "Lista 01 - Item 03 - Os objetos são manuseados/tratados de forma a preservar sua integridade ao longo de todo o processo? Aspectos: Produtividade, Segurança e Ergonomia ",
        "answer": "OBJETIVO DO ITEM: Garantir a integridade da carga e a produtividade do processo. FORMA DE AVALIAR: 1. Verificar se: a) os objetos são colocados (e não jogados) dentro/sobre os equipamentos (unitizadores, carrinhos, MMU etc.); a) os objetos não são dobrados formando vincos; b) os pacotes e malotes são faceados, e os envelopes são encabeçados e faceados; c) a carga de envelopes/pequenos pacotes está organizada nas caixetas. 2. Não considerar objetos fora do padrão que impossibilitem o faceamento (cilindros, esferas, grandes formatos, dentre outros).PONTO DE VERIFICAÇÃO: Toda a unidade. PERÍODO: Nos dias da verificação AMOSTRA: Todos os objetos. TOLERÂNCIA: Não há. Peso do Item 03 - Referência: MANDIS 2/2 MANDIS 2/1 Anexo 2  "},
    {
        "question": "Lista 01 - Item 04 - O tratamento e a organização dos unitizadores esvaziados é feito conforme o previsto? Aspectos: Segurança e Informação ",
        "answer": "OBJETIVO DO ITEM: Evitar resíduo de objetos nos unitizadores. FORMA DE AVALIAR: 1. Observar durante o processo de abertura, e imediatamente após serem esvaziados, se: a) as malas e os sambags são avessados, as caixetas emborcadas; b) não há quaisquer resíduos nos CDL/CAF; c) bases, tampas e mangas dos CDLs, após serem esvaziados, são disponibilizados no local previsto, logo após o término das atividades na célula. 2. Verificar se foram retirados os rótulos de todos os unitizadores imediatamente após esvaziar o unitizador. 3. Considerar Não Conforme se for encontrado objeto e/ou rótulo nos unitizadores disponibilizados na área de unitizadores vazios. PONTO DE VERIFICAÇÃO: Área Operacional, e Área de Unitizadores Vazios. PERÍODO: Nos dias da verificação. AMOSTRA: Todos os unitizadores. MARGEM DETOLERÂNCIA: Não há. Peso do Item 02 - Referência: MANDIS 2/1 Anexo 2"},
    {
        "question": "Lista 01 - Item 05 - O desabastecimento é realizado conforme o previsto? Aspectos: Produtividade e Prioridade ",
        "answer": "OBJETIVO DO ITEM: Manter a organização do processo. FORMA DE AVALIAR: 1. Verificar se o desabastecimento ocorre: a) nas unidade sem AIS: ao final da primeira triagem ou da TD; b) nas unidade com AIS: de forma contínua, pela parte traseira da mesa. 2. Considerar NA para as verificações em CEE. PONTO DE VERIFICAÇÃO: Salão Operacional. PERÍODO: Nos dias da verificação MARGEM DE TOLERÂNCIA: Não há. Peso do Item 04 - Referência: MANORG 11/6 e 7 MANDIS 2/2"},
    {
        "question": "Lista 01 - Item 06 - A segunda triagem/SL é realizada conforme o previsto e os GUs e DAs são priorizados no ordenamento? Aspectos: Informação e Produtividade ",
        "answer": "OBJETIVO DO ITEM: Garantir que as direções de segunda triagem/SL sejam respeitadas e que haja priorização de DA e GU. FORMA DE AVALIAR: 1. Verificar se: a) não há triagem de forma improvisada sobre a bancada, sobre o armário, em caixetas ou em escaninhos sem identificação; b) há priorização no tratamento dos objetos de GU e/ou DA e se são disponibilizados respeitando o horário estabelecido para a saída da linha. 2. Considerar NA para as verificações em CEE. PONTO DE VERIFICAÇÃO: Salão Operacional. PERÍODO: Nos dias da verificação. AMOSTRA: Todos os distritos. MARGEM DE TOLERÂNCIA: Não há. Peso do Item: 02 - Referência: MANDIS 2/2 "},
    {
        "question": "Lista 01 - Item 07 - O tratamento dos objetos qualificados/encomendas é realizado conforme o previsto? Aspectos: Informação, Produtividade e Prioridade ",
        "answer": "OBJETIVO DO ITEM: Garantir a entrega no prazo. 1. Verificar se: a) a LOEC Automática é utilizada em 100% dos distritos; b) é realizada a triagem de acordo com o distrito indicado no sistema, simultaneamente à leitura. 2. É permitida a realização da pré- triagem: a) antes da leitura, caso a localidade não seja codificada por logradouro; b) antes ou após a leitura da carga quando o centro de tratamento enviá-la em bruto ou em menor quantidade de estações de LOEC previstas (entende-se por estação de LOEC cada célula composta de 3 a 5 distritos). 1. No CDD para os distritos postais é permitida a realização da pré-triagem quando a quantidade de objetos nos GUs da unidade representar mais que 25% da carga qualificada da unidade dimensionada em SD; PONTO DE VERIFICAÇÃO: Toda a unidade. PERÍODO: Nos dias da verificação. AMOSTRA: Observar o processo no mínimo 10 minutos. MARGEM DE TOLERÂNCIA: Não há. Peso do Item 05 - Referência: MANDIS 2/2"},
    {
        "question": "Lista 01 - Item 08 - Todos os objetos com prazo de entrega previsto para o dia saem para a distribuição? Aspectos: Informação e Prioridade ",
        "answer": "OBJETIVO DO ITEM: Garantir o cumprimento do prazo acordado com o cliente. FORMA DE AVALIAR: 1. Selecionar objetos e verificar se o período entre a data da postagem e a data da saida para a distribuição está no prazo previsto. 2. Considerar Conforme: a) os objetos anotados previamente com os motivos endereço insuficiente e/ou não existe o número indicado; b) a carga enviada antecipadamente pelo centro de tratamento ou a carga com prazo de entrega programado; c) objetos com entrega alternada. PONTO DE VERIFICAÇÃO: Salão Operacional. PERÍODO: Nos dias da verificação. AMOSTRA: 10 objetos aleatórios em 30% dos distritos. MARGEM DE TOLERÂNCIA: Não há. Peso do Item 04 - Referência: MANDIS 2/1 anexo 2 e 3"},
    {
        "question": "Lista 01 - Item 09 - Todos os Malotes a serem entregues pela unidade são tratados conforme o previsto? Aspectos: Informação e Segurança  ?",
        "answer": "OBJETIVO DO ITEM: Evitar evasão de receita. FORMA DE AVALIAR: 1. Verificar se o tratamento dos malotes ocorre conforme o previsto.https://sapppmobile.correios.com.br/app/listas/index.php 2. Realizar a leitura do malote no SIGMA. 2. Caso haja malotes identificados na funcionalidade de ¿Importação¿ sem o evento de postagem na origem, verificar se esses foram pesados e as informações lançadas no SIGMA. 2. Considerar Não Conforme se houver lançamento manual de malotes na LEM. 3. Considerar NA se a unidade não entregar malote. PONTO DE VERIFICAÇÃO: Toda a unidade e veículos e arquivo de LEMs. PERÍODO: Um dos dias da verificação e mais 5 dias entre os 30 dias anteriores. AMOSTRA: Todos os malotes e LEMs do período. MARGEM DE TOLERÂNCIA: Sistema inoperante, desde que comprovado com o envio de e-mail ao Gestor Regional do SIGMA. Peso do Item 02 - Referência:  "},
    {
        "question": "Lista 01 - Item 10 - Os objetos sujeitos a recondicionamento recebem o tratamento conforme previsto? Aspecto: Segurança ",
        "answer": "OBJETIVO DO ITEM: Garantir a Segurança Postal. FORMA DE AVALIAR: 1. Observar se o estado físico dos objetos/malotes é verificado e, em caso de irregularidades, se são disponibilizados de imediato para a área de recondicionamento. 2. Entende-se por área de recondicionamento o local definido dentro da unidade passível de supervisão onde estejam disponíveis os materiais/equipamentos necessários para a realização da atividade (fita, plástico, formulário, etc.). Se a unidade não tiver uma balança nesse local, pode ser feito o compartilhamento com outra balança. 3. Considerar NA se não houver necessidade de recondicionamento no período avaliado. PONTO DE VERIFICAÇÃO: Toda a unidade e formulário. PERÍODO: Nos dias da verificação. AMOSTRA: Todos os objetos/malotes que apresentem invólucros avariados. MARGEM DE TOLERÂNCIA: Não há. Peso do Item 01 - Referência: MANDIS 2/2 MANENC 2/12 MANENC 6/7"},
    {
        "question": "Lista 01 - Item 11 - Há conferência da quantidade de objetos qualificados e de serviços adicionais sob responsabilidade do carteiro? Aspectos: Segurança e Prioridade ",
        "answer": "OBJETIVO DO ITEM: Garantir a segurança dos objetos qualificados recebidos pelos carteiros. FORMA DE AVALIAR: 1. Observar se, antes da saída dos carteiros, os objetos são conferidos por empregados designados para esta atividade (a conferência da quantidade não pode ser executada por terceirizado nem pela mesma pessoa que fez o ordenamento). 2. Considerar Conforme caso seja realizada a conferência exaustiva nos distritos, utilizando a função E do SRO na presença do carteiro. PONTO DE VERIFICAÇÃO: Salão operacional. OBSERVAÇÃO: Para os distritos postais a verificação deve ser feita no momento do recebimento dos objetos Para os distritos especiais: Na saída do Salão Operacional. PERÍODO: Nos dias da verificação. AMOSTRA: Todos os distritos. MARGEM DE TOLERÂNCIA: Não há. Peso do Item 04 - Referência: MANDIS 2/2 MANDIS 3/1 "},
    {
        "question": "Lista 01 - Item 12 - A conferência exaustiva dos objetos é realizada conforme o previsto? Aspectos: Segurança e Prioridade PONTO DE VERIFICAÇÃO: Salão Operacional, SRO e Relatório de Conferência da Função E.PERÍODO: Os dias da verificação e mais 3 dias entre os últimos 30. AMOSTRA: 01 Relatório por dia. MARGEM DE TOLERÂNCIA: Distritos da plataformização. ",
        "answer": "OBJETIVO: Garantir a segurança da carga. FORMA DE AVALIAR: 1. Observar se o supervisor ou outra pessoa designada realiza a conferência exaustiva dos distritos especiais, na quantidade e frequência prevista e na presença do carteiro, no momento da saída para distribuição ou na estação da LOEC automática. 2. Verificar se o relatório emitido pelo SRO na função (E) está arquivado eletronicamente na unidade. 3. Verificar no arquivo se há registro da conferência para todos os dias em que houver operação do período em análise. 4. Caso se identifique na amostra divergência durante a conferência, comparar com o rastreamento e verificar se: a) a baixa do objeto foi feita no mesmo dia; b) em caso de extravio, se há documentação formal de apuração por meio de processo SEI. 5. Para unidades que utilizam a plataformização, verificar apenas os distritos que utilizam o APP Operacional. Peso do Item 04 - Referência: MANDIS 2/2 MANDIS 3/1 anexo 2"},
    {
        "question": "Lista 01 - Item 13 - Os objetos ME e MD recebem o tratamento conforme previsto? Aspectos: Informação e Produtividade ",
        "answer": "OBJETIVO DO ITEM: Garantir o correto tratamento e o fluxo dos objetos FORMA DE AVALIAR: 1. Selecionar objetos ME e MD e verificar se receberam o tratamento previsto. PONTO DE VERIFICAÇÃO: Salão Operacional. PERÍODO: Nos dias de verificação. AMOSTRA: Todos os objetos. TOLERÂNCIA: Não há. Peso do Item 02 - Referência: MANDIS 2/3"},
    {
        "question": "Lista 01 - Item 14 - A entrega interna de objetos é realizada conforme previsto? Aspectos: Informação e Segurança PERÍODO: Nos últimos 30 dias (incluir os dias da verificação). AMOSTRA: 10 listas (LDI + LEM) ou todas as listas se a quantidade total for menor que 10. MARGEM DE TOLERÂNCIA: Não há. ",
        "answer": "OBJETIVO DO ITEM: Garantir que o objeto seja entregue ao destinatário correto e com os procedimentos previstos. FORMA DE AVALIAR: 1. Para unidades que realizam a entrega interna por meio do SRO Móvel rastrear os objetos e observar se: a) a qualidade das imagens permite identificação dos dados conforme o previsto; b) há assinatura legível do recebedor e confere como o nome do destinatário/remetente, e se há autorização; c) há o número do documento do recebedor; d) caso não haja a foto do objeto no SRO, verificar se a unidade gerou a LDI impressa e se os procedimentos previstos foram realizados. 3. Verificar nas LEMs internas se: a) todos os campos necessários estão preenchidos; b) a assinatura é da pessoa autorizada a receber o malote. 4. Considerar NA se a unidade não realizar nenhuma entrega interna no período avaliado ou se a unidade não faz entrega interna. PONTO DE VERIFICAÇÃO: Arquivos de LDIs, LEM do distrito de entrega interna e (balcão de atendimento). Peso do Item 02 - Referência: MANDIS 3/1 anexo 2 MANATE 4/1 Anexo 2 "},
    {
        "question": "Lista 01 - Item 15 - Os procedimentos dos objetos destinados ao LOCKER estão sendo realizados conforme o previsto? Aspecto: Informação ",
        "answer": "OBJETIVO DO ITEM: Garantir a informação correta para o cliente. FORMA DE AVALIAR: 1. Identificar os distritos que possuem vinculação com o LOCKER. 2. Pesquisar os objetos lançados para o LOCKER. 3. Verificar se foram realizados corretamente os procedimentos de indução e disponibilização do objeto. 4. Em caso de inoperância do LOCKER, verificar se a baixa ocorre conforme o previsto. 5. Considerar o item Conforme caso tenham sido realizadas correções de eventos no mesmo dia. 6. Considerar NA para as unidades que não possuem LOCKER vinculado ou se não houve objeto destinado ao LOCKER no período. PONTO DE VERIFICAÇÃO: SRO. PERÍODO: Últimos 10 dias anteriores à verificação e o primeiro dia da verificação. AMOSTRA: 100% dos objetos do período. MARGEM DE TOLERÂNCIA: Não há. Peso do Item 01 - Referência: MANDIS 3/1 Anexo 4 Caderno Operacional do LOCKER "},
    {
        "question": "Lista 01 - Item 16 - Os procedimentos dos objetos destinados a CCI estão sendo realizados conforme o previsto? Aspecto: Informação. ",
        "answer": "OBJETIVO DO ITEM: Garantir a informação correta para o cliente. FORMA DE AVALIAR: 1. Identificar os distritos que possuem vinculação com CCI. 2. Pesquisar os objetos lançados para o CCI. 3. Verificar se foram realizados corretamente os procedimentos de indução e disponibilização do objeto. 4. Em caso de inoperância da CCI, verificar se a baixa ocorre conforme o previsto. 5. Considerar o item Conforme caso tenham sido realizadas correções de eventos no mesmo dia. 6. Considerar NA para as unidades que não possuem CCI vinculada ou se não houve objeto destinado ao CCI no período avaliado. PONTO DE VERIFICAÇÃO: SRO. PERÍODO: Últimos 10 dias anteriores à verificação e o primeiro dia da verificação. AMOSTRA: 100% dos objetos do período. MARGEM DE TOLERÂNCIA: Não há. Peso do Item 01 - Referência: MANDIS 3/1 Anexo 4 Cartilha 5Ps "},
    """"{"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "Quem pintou a Mona Lisa?", "answer": "Leonardo da Vinci"},"""

    # Adicione mais perguntas conforme necessário
]


def get_random_question():
    return random.choice(QUESTIONS)