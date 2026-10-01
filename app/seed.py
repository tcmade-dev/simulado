"""
Seed script to populate SQLite with questions and answers for all 13 chapters
from documents/questionarios and documents/respostas.
"""

from app.database import init_db, save_chapter, save_question

CHAPTER_TITLES = [
    (1, "A Igreja Evangélica Assembleia de Deus e sua Missão", True),
    (2, "Teologia", True),
    (3, "Homilética", True),
    (4, "Hermenêutica", True),
    (5, "Pastoral & Clínica Pastoral", True),
    (6, "Vida Conjugal do Ministro", True),
    (7, "Ética Ministerial", True),
    (8, "Adoração e Liturgia", True),
    (9, "Cerimônias e Celebrações", True),
    (10, "A Igreja como Instituição de Ensino", True),
    (11, "Planejamento Estratégico e Recursos Humanos", True),
    (12, "Finanças na Igreja", True),
    (13, "Liderança Eficaz", True),
]


def seed():
    init_db()

    # Seed chapters
    for number, title, active in CHAPTER_TITLES:
        save_chapter(
            number=number,
            title=title,
            description=f"Questionário do Capítulo {number}",
            is_active=active,
        )

    # ==========================================
    # CHAPTER 1
    # ==========================================
    save_question(
        chapter_number=1,
        question_number=1,
        question_type="multiple_choice",
        prompt="Os pentecostais foram caracterizados por cinco valores implícitos:",
        options=[
            {"key": "a", "text": "Jesus Salva, Cura, Batiza com Espírito Santo e Breve Voltará."},
            {"key": "b", "text": "A experiência pessoal, A comunicação oral, A espontaneidade, O repúdio ao mundanismo, A autoridade das Escrituras Sagradas."},
            {"key": "c", "text": "O amor ao próximo, A autoridade das Escrituras Sagradas, A popularidade, O batismo no Espírito Santo, O avivamento."},
        ],
        correct_answer="b",
        explanation='O capítulo 1 reproduz, na seção "Desenvolvimento da Teologia Pentecostal", a lista exata dos cinco valores implícitos: 1. A experiência pessoal; 2. A comunicação oral; 3. A espontaneidade; 4. O repúdio ao mundanismo; 5. A autoridade das Escrituras Sagradas.',
    )

    save_question(
        chapter_number=1,
        question_number=2,
        question_type="true_false",
        prompt="Em relação à Igreja Evangélica Assembleia de Deus, avalie cada afirmação como Verdadeira (V) ou Falsa (F):",
        options=[
            {"key": "a", "statement": 'Igreja Evangélica Assembleia de Deus, nasceu em 1911, na data de 18 de junho, (com o nome de "Missão de Fé Apostólica").'},
            {"key": "b", "statement": "No Estado do Paraná, está presente desde 1920, e conta hoje com mais de 150 campos eclesiásticos."},
            {"key": "c", "statement": "Gunnar Vingren não era um pastor de formação teológica."},
            {"key": "d", "statement": "A igreja Missão de Fé Apostólica, passou a se chamar Assembleia de Deus em 11 de janeiro de 1918, quando Gunnar Vingren registrou o estatuto da igreja no cartório de Registro de Títulos e Documentos do 1 oficio, em Belém."},
        ],
        correct_answer={"a": "V", "b": "F", "c": "F", "d": "V"},
        explanation="Avaliação das afirmativas sobre a história, fundação e registro da Assembleia de Deus.",
        sub_explanations={
            "a": 'VERDADEIRO: O capítulo confirma: "A Igreja Evangélica Assembleia de Deus, nasceu em 1911, na data de 18 de junho [...] Foram 18 pessoas ao todo, que reunidos iniciaram a igreja \'Missão de Fé Apostólica\'".',
            "b": 'FALSO: O texto do capítulo informa que no Estado do Paraná a igreja "conta hoje com mais de 144 campos eclesiásticos", e não 150.',
            "c": 'FALSO: O texto diz expressamente o contrário: "Gunnar Vingren era um pastor de formação teológica, e muito se preocupou em instruir os primeiros crentes, com ênfase para a doutrina pentecostal".',
            "d": 'VERDADEIRO: O capítulo confirma na íntegra: "A igreja Missão de Fé Apostólica, passou a se chamar Assembleia de Deus em 11 de janeiro de 1918, quando Gunnar Vingren registrou o estatuto da igreja no cartório de Registro de Títulos e Documentos do 1 ofício, em Belém".',
        },
    )

    # ==========================================
    # CHAPTER 2
    # ==========================================
    save_question(
        chapter_number=2,
        question_number=1,
        question_type="multiple_choice",
        prompt="A Teologia se classifica de 4 maneiras, a saber:",
        options=[
            {"key": "a", "text": "Teologia Filosófica, Teologia Elementar, Teologia Bíblica e Teologia Pentecostal."},
            {"key": "b", "text": "Teologia Exegética, Teologia Bíblica, Teologia Histórica e Teologia Dogmática."},
            {"key": "c", "text": "Teologia Exegética, Teologia Hermenêutica, Teologia Escatológica, Teologia Histórica."},
        ],
        correct_answer="b",
        explanation='Na seção "Classificação da Teologia", o capítulo 2 enumera exatamente quatro categorias: 1. Teologia Exegética; 2. Teologia Bíblica; 3. Teologia Histórica; 4. Teologia Dogmática (também chamada de Teologia Prática).',
    )

    save_question(
        chapter_number=2,
        question_number=2,
        question_type="true_false",
        prompt="Em relação às doutrinas e estrutura bíblica abordadas no Capítulo 2, avalie cada afirmação como Verdadeira (V) ou Falsa (F):",
        options=[
            {"key": "a", "statement": "Em Gênesis 1.1 encontramos 7 doutrinas relacionadas com a pessoa de Deus, a saber: A Existência de Deus, A Eternidade de Deus, O Poder de Deus, A Soberania de Deus, A Vontade de Deus, A Sabedoria de Deus, A Providência de Deus."},
            {"key": "b", "statement": "A Bíblia é dividida em duas partes: Antigo e Novo Testamento. Possui: 65 livros, sendo 38 no Antigo Testamento, e 27 no Novo Testamento."},
            {"key": "c", "statement": "Hamartiologia é a Doutrina da Salvação."},
            {"key": "d", "statement": "No Estudo do Espírito Santo há a Paracletologia: o termo Paracletologia vem do grego Paracleto (Advogado, Consolador, Ajudador)."},
        ],
        correct_answer={"a": "V", "b": "F", "c": "F", "d": "V"},
        explanation="Avaliação doutrinária sobre Gênesis 1.1, divisão bíblica e termos teológicos fundamentais.",
        sub_explanations={
            "a": "VERDADEIRO: O capítulo reproduz exatamente essas 7 doutrinas em Gênesis 1.1.",
            "b": "FALSO: A Bíblia possui 66 livros (sendo 39 no Antigo Testamento e 27 no Novo Testamento), e não 65/38.",
            "c": "FALSO: Hamartiologia é a Doutrina do Pecado. A Doutrina da Salvação é a Soteriologia.",
            "d": "VERDADEIRO: Na Pneumatologia, o termo Paracletologia vem do grego Paracleto (Advogado, Consolador, Ajudador).",
        },
    )

    # ==========================================
    # CHAPTER 3
    # ==========================================
    save_question(
        chapter_number=3,
        question_number=1,
        question_type="matching",
        prompt="Preencha a segunda coluna de acordo com a primeira:",
        options={
            "column_1": [
                {"key": "a", "text": "São Tipos de Sermão"},
                {"key": "b", "text": "São termos ligados à Homilética"},
                {"key": "c", "text": "Classificação dos Sermões quanto ao conteúdo"},
                {"key": "d", "text": "Um esboço precisa ter"},
            ],
            "column_2": [
                {"id": 1, "text": "Oratória, Eloquência, Retórica."},
                {"id": 2, "text": "Sermões Doutrinários, Sermões Morais, Sermões Históricos, Sermões da Experiência, Sermões Evangelísticos."},
                {"id": 3, "text": "Introdução, Desenvolvimento, Conclusão, Apelo."},
                {"id": 4, "text": "Sermão Temático, Sermão Textual, Sermão Expositivo."},
            ],
        },
        correct_answer={"1": "b", "2": "c", "3": "d", "4": "a"},
        explanation="Associação de conceitos fundamentais da Homilética.",
        sub_explanations={
            "1": "Termos ligados à Homilética: Oratória, Eloquência e Retórica.",
            "2": "Classificação dos Sermões quanto ao conteúdo: Doutrinários, Morais, Históricos, da Experiência e Evangelísticos.",
            "3": "Estrutura do esboço de sermão: Introdução, Desenvolvimento, Conclusão e Apelo.",
            "4": "Tipos de Sermão: Temático, Textual e Expositivo.",
        },
    )

    save_question(
        chapter_number=3,
        question_number=2,
        question_type="multiple_choice",
        prompt="Considerando o texto do Capítulo 3, assinale com 'X' a alternativa correta: São características de um pregador sob o ponto de vista técnico:",
        options=[
            {"key": "a", "text": "Autoridade/ousadia (Mc 1.21)"},
            {"key": "b", "text": "Chamado para obra (ordenança) (Mt 28.19)"},
            {"key": "c", "text": "Conhecimento da palavra (2 Tm 2.15)"},
        ],
        correct_answer="c",
        explanation='Na tabela comparativa do capítulo 3, "Conhecimento da palavra = 2 Tm 2.15" consta expressamente na coluna técnica. Autoridade/ousadia e Chamado para obra estão na coluna espiritual.',
    )

    # ==========================================
    # CHAPTER 4
    # ==========================================
    save_question(
        chapter_number=4,
        question_number=1,
        question_type="true_false",
        prompt="Em relação à Hermenêutica Bíblica, marque 'V' para as alternativas verdadeiras e 'F' para as falsas:",
        options=[
            {"key": "a", "statement": "A Hermenêutica Sagrada é a ciência de interpretar a Bíblia, e visa determinar o sentido exato que o autor bíblico tencionava transmitir aos leitores."},
            {"key": "b", "statement": "A palavra Hermenêutica vem do grego hermeneutike, e tem relação etimológica com o deus Hermes, mensageiro que interpretava a vontade dos deuses."},
            {"key": "c", "statement": "A Hermenêutica não possui regras para interpretar a Bíblia, cada leitor interpreta livremente conforme o seu sentimento pessoal."},
            {"key": "d", "statement": "Na Hermenêutica Bíblica, o texto bíblico possui vários sentidos e significados contraditórios simultâneos."},
        ],
        correct_answer={"a": "V", "b": "V", "c": "F", "d": "F"},
        explanation="Fundamentos e princípios básicos da ciência hermenêutica bíblica.",
        sub_explanations={
            "a": "VERDADEIRO: A hermenêutica busca extrair a intenção e sentido original do autor sagrado.",
            "b": "VERDADEIRO: O termo vem do grego e remonta historicamente ao papel de intérprete/mensageiro.",
            "c": "FALSO: A hermenêutica é uma ciência com regras gramaticais, históricas e teológicas bem definidas.",
            "d": "FALSO: Cada texto possui um sentido primordial original estabelecido pelo autor sob inspiração divina.",
        },
    )

    save_question(
        chapter_number=4,
        question_number=2,
        question_type="matching",
        prompt="Relacione a segunda coluna de acordo com a primeira (Contextos na Hermenêutica):",
        options={
            "column_1": [
                {"key": "a", "text": "Contexto Geral"},
                {"key": "b", "text": "Contexto Imediato"},
                {"key": "c", "text": "Contexto Referencial"},
                {"key": "d", "text": "Contexto Remoto"},
                {"key": "e", "text": "Contexto Histórico"},
            ],
            "column_2": [
                {"id": 1, "text": "É o que fica a longa distância do texto analisado, mas que tem com ele alguma ligação."},
                {"id": 2, "text": "É o texto que toda a Bíblia responde e auxilia as indagações feitas no texto que estamos estudando."},
                {"id": 3, "text": "Considera a Bíblia de modo geral, por completo, toda, avalia-se panoramicamente."},
                {"id": 4, "text": "É aquele que fica anterior ou posterior ao texto que se lê ou que se estuda."},
                {"id": 5, "text": "São passagens paralelas, correlatas, com o texto que se analisa."},
            ],
        },
        correct_answer={"1": "d", "2": "e", "3": "a", "4": "b", "5": "c"},
        explanation="Definições dos cinco tipos de contexto utilizados na análise hermenêutica.",
        sub_explanations={
            "1": "Contexto Remoto: Distante no texto analisado, mas com ligação temática.",
            "2": "Contexto Histórico: Informações históricas e teológicas do conjunto das Escrituras.",
            "3": "Contexto Geral: Visão panorâmica e completa da Bíblia.",
            "4": "Contexto Imediato: Versículos e parágrafos logo antes ou depois da passagem.",
            "5": "Contexto Referencial: Passagens bíblicas paralelas e correlatas.",
        },
    )

    # ==========================================
    # CHAPTER 5
    # ==========================================
    save_question(
        chapter_number=5,
        question_number=1,
        question_type="multiple_choice",
        prompt="Assinale com 'X' a alternativa correta. São Qualificações intelectuais do Pastor:",
        options=[
            {"key": "a", "text": "Uma Mente Aberta, Uma Mente Clara, Uma Mente Ativa, Uma Mente Educada."},
            {"key": "b", "text": "Conhecimento e sabedoria, Capacidade de Comunicação, Habilidade de Escuta, Inteligência emocional."},
            {"key": "c", "text": "Conhecimento Teológico, Autoridade e Domínio, Empatia, Sabedoria Financeira."},
        ],
        correct_answer="a",
        explanation='No capítulo 5, na seção "Qualificações Intelectuais", o autor lista expressamente: 1. Uma Mente Aberta; 2. Uma Mente Clara; 3. Uma Mente Ativa; 4. Uma Mente Educada.',
    )

    save_question(
        chapter_number=5,
        question_number=2,
        question_type="true_false",
        prompt="Em relação à Pastoral e Clínica Pastoral, avalie cada afirmação:",
        options=[
            {"key": "a", "statement": "O termo Pastor, aplicado ao obreiro tem sentido figurado."},
            {"key": "b", "statement": "O Pastor precisa ter maturidade espiritual, mas o mesmo não se aplica ao âmbito emocional e mental."},
            {"key": "c", "statement": "V. James Mannoia, apresenta em sua visão três modelos de Aconselhamento/Clinica Pastoral: Aconselhamento Diretivo, Aconselhamento não Diretivo, Aconselhamento Dimensional."},
            {"key": "d", "statement": "Histeria – É a mais simples e comum forma de neurose."},
        ],
        correct_answer={"a": "V", "b": "F", "c": "V", "d": "F"},
        explanation="Fundamentos do ministério pastoral e aspectos da clínica e aconselhamento.",
        sub_explanations={
            "a": "VERDADEIRO: O termo tem sentido figurado oriundo do cuidado com as ovelhas.",
            "b": "FALSO: A maturidade emocional e psicológica é indispensável para o ministério.",
            "c": "VERDADEIRO: O capítulo apresenta exatamente os três modelos de Mannoia.",
            "d": "FALSO: O texto classifica histeria como uma forma extrema de neurose, e não a mais simples/comum.",
        },
    )

    # ==========================================
    # CHAPTER 6
    # ==========================================
    save_question(
        chapter_number=6,
        question_number=1,
        question_type="multiple_choice",
        prompt="Assinale com 'X' a alternativa correta. Alguns passos que são imprescindíveis na vida do Ministro de Deus. Vejamos:",
        options=[
            {"key": "a", "text": "Experiência de Salvação, Novo Nascimento, Batismo em Águas, Batismo no Espírito Santo, Andar com Deus."},
            {"key": "b", "text": "Experiência com Evangelismo Pessoal, Experiência profissional, Andar com pessoas Influentes."},
            {"key": "c", "text": "Experiência com cultos Públicos, Experiência em lidar com Novos Convertidos."},
        ],
        correct_answer="a",
        explanation="O capítulo 6 enumera como passos indispensáveis: Salvação, Novo Nascimento, Batismo em Águas, Batismo no Espírito Santo e Andar com Deus em comunhão diária.",
    )

    save_question(
        chapter_number=6,
        question_number=2,
        question_type="true_false",
        prompt="Sobre a vida pessoal e conjugal do ministro de Deus, avalie:",
        options=[
            {"key": "a", "statement": "São qualidades espirituais esperadas do ministro: Amor, Fé, Santidade, Paciência, Perdão."},
            {"key": "b", "statement": "Vocação (chamada) é o único requisito para desenvolver o ministério."},
            {"key": "c", "statement": "A casa (lar/família) do ministro deve ser sua prioridade no ministério."},
            {"key": "d", "statement": "Faz parte das funções do Pastor (Obreiro) ter uma vida organizada de forma que seja modelo aos que o ouvem e o seguem."},
        ],
        correct_answer={"a": "V", "b": "F", "c": "V", "d": "V"},
        explanation="Qualidades espirituais, equilíbrio familiar e conduta pastoral.",
        sub_explanations={
            "a": "VERDADEIRO: Amor, fé, santidade, paciência e perdão são marcas espirituais exigidas.",
            "b": "FALSO: A chamada exige preparação, caráter, vida familiar equilibrada e qualificação contínua.",
            "c": "VERDADEIRO: O cuidado com a família antecede a liderança da igreja local (1 Tm 3.4-5).",
            "d": "VERDADEIRO: O ministro deve ser modelo de integridade e organização na vida diária.",
        },
    )

    # ==========================================
    # CHAPTER 7
    # ==========================================
    save_question(
        chapter_number=7,
        question_number=1,
        question_type="true_false",
        prompt="Em relação à Ética Ministerial, avalie cada assertiva:",
        options=[
            {"key": "a", "statement": "A função sacerdotal, na dispensação da graça, com relação à igreja, não existe como ministério."},
            {"key": "b", "statement": "Dogma: 'Parecer eclesiástico daquilo que a Bíblia deixa bem claro'."},
            {"key": "c", "statement": "A ética ministerial tem sido definida como 'ciência administrativa'."},
            {"key": "d", "statement": "É também de bom alvitre que o novo pastor não queira logo que assumir alterar os métodos de trabalho do seu antecessor."},
        ],
        correct_answer={"a": "V", "b": "F", "c": "F", "d": "V"},
        explanation="Conceitos fundamentais da ética ministerial e conduta pastoral.",
        sub_explanations={
            "a": "VERDADEIRO: Na dispensação da graça vigora o sacerdócio universal de todos os crentes.",
            "b": "FALSO: Dogma é parecer eclesiástico sobre aquilo que a Bíblia NÃO deixa expressamente claro.",
            "c": "FALSO: Ética ministerial é definida como 'ciência moral', e não meramente administrativa.",
            "d": "VERDADEIRO: Respeitar os processos do antecessor demonstra prudência e maturidade ética.",
        },
    )

    save_question(
        chapter_number=7,
        question_number=2,
        question_type="multiple_choice",
        prompt="Considerando os princípios éticos do ministério, assinale a alternativa correta:",
        options=[
            {"key": "a", "text": "Quando convidado a pregar em uma reunião de caráter interdenominacional, deve sempre que possível tirar vantagem denominacional da ocasião."},
            {"key": "b", "text": "Uma das táticas de Paulo era dirigir-se para áreas onde o evangelho ainda não havia sido pregado (Rm 15.20,23 e 2 Co 10.16)."},
            {"key": "c", "text": "Os escribas e fariseus se iraram contra Cristo em razão de sua franqueza e por isso Ele alterou os seus métodos."},
        ],
        correct_answer="b",
        explanation='O capítulo cita explicitamente o princípio paulino de pregar onde Cristo ainda não fora anunciado para não edificar sobre fundamento alheio.',
    )

    # ==========================================
    # CHAPTER 8
    # ==========================================
    save_question(
        chapter_number=8,
        question_number=1,
        question_type="true_false",
        prompt="Em relação à Adoração e Liturgia do culto cristão, avalie:",
        options=[
            {"key": "a", "statement": "Liturgia: A palavra liturgia vem do grego (λειτουργία,) significa 'serviço' ou 'trabalho público'."},
            {"key": "b", "statement": "Etimologicamente o significado da palavra culto é 'a forma mais básica de elogios direcionados a alguém'."},
            {"key": "c", "statement": "O tempo para uma palavra, deve ser entre cinco (5) e dez (10) minutos."},
            {"key": "d", "statement": "O ritualismo surge as vezes até em igrejas conhecidas pela informalidade e aversão ao ritualismo formal."},
        ],
        correct_answer={"a": "V", "b": "F", "c": "V", "d": "V"},
        explanation="Significados e aplicações da liturgia e ordem no culto cristão.",
        sub_explanations={
            "a": "VERDADEIRO: Liturgia tem origem grega significando serviço público a Deus e ao próximo.",
            "b": "FALSO: Culto procede do latim cultus, ligado a reverência, adoração e dedicação sagrada a Deus.",
            "c": "VERDADEIRO: Saudações e palavras breves de oportunidade devem ser concisas (5 a 10 min).",
            "d": "VERDADEIRO: Hábitos repetitivos criam formas litúrgicas mesmo em ambientes informais.",
        },
    )

    save_question(
        chapter_number=8,
        question_number=2,
        question_type="matching",
        prompt="Relacione a segunda coluna de acordo com a primeira (Liturgia e Prática do Culto):",
        options={
            "column_1": [
                {"key": "a", "text": "A Saudação"},
                {"key": "b", "text": "Liturgia"},
                {"key": "c", "text": "O estilo tradicional de culto"},
                {"key": "d", "text": "A pregação"},
            ],
            "column_2": [
                {"id": 1, "text": "É a prática do culto, ritual (Rm 6.13; 12.1); tem raízes absolutamente cristológicas."},
                {"id": 2, "text": "Surgiu logo após o fim da Idade Média."},
                {"id": 3, "text": "É apenas um cumprimento dirigido a igreja. Deve ser breve, não devendo passar de cinco (5) minutos."},
                {"id": 4, "text": "É o principal método pelo qual Deus torna a Sua voz conhecida."},
            ],
        },
        correct_answer={"1": "b", "2": "c", "3": "a", "4": "d"},
        explanation="Elementos constitutivos do culto cristão e sua fundamentação histórica.",
        sub_explanations={
            "1": "Liturgia: Prática do culto centrado em Cristo.",
            "2": "Estilo tradicional de culto: Consolidado após o término da Idade Média e Reforma.",
            "3": "Saudação: Cumprimento fraterno e breve.",
            "4": "Pregação: Proclamação da Palavra de Deus (1 Co 1.21).",
        },
    )

    # ==========================================
    # CHAPTER 9
    # ==========================================
    save_question(
        chapter_number=9,
        question_number=1,
        question_type="matching",
        prompt="Preencha a segunda coluna de acordo com a primeira (Cerimônias e Celebrações Eclesiásticas):",
        options={
            "column_1": [
                {"key": "a", "text": "Cerimônias"},
                {"key": "b", "text": "Culto de Ações de Graças"},
                {"key": "c", "text": "Cerimônia Fúnebre"},
                {"key": "d", "text": "Ceia do Senhor"},
            ],
            "column_2": [
                {"id": 1, "text": "É um culto especial, de agradecimento pelas bênçãos recebidas, e o ato de dividir esta alegria com os demais possui respaldo bíblico."},
                {"id": 2, "text": "Culto para o qual o obreiro deve se preparar emocionalmente."},
                {"id": 3, "text": "Faz parte do seu dever e ministério diário, e o ministro deveria familiarizar-se, aprendendo a oficiá-las com dignidade e correção."},
                {"id": 4, "text": "Não deve ser uma cerimônia realizada às pressas, pois é um ato solene, de caráter estritamente espiritual, dirigida exclusivamente aos crentes."},
            ],
        },
        correct_answer={"1": "b", "2": "c", "3": "a", "4": "d"},
        explanation="Princípios práticos na celebração das cerimônias cristãs.",
        sub_explanations={
            "1": "Culto de Ações de Graças: Gratidão pública pelas bênçãos recebidas.",
            "2": "Cerimônia Fúnebre: Momento de consolo que exige equilíbrio emocional e pastoral.",
            "3": "Cerimônias: Parte dos deveres litúrgicos e pastorais do ministro.",
            "4": "Ceia do Senhor: Celebração memorial solene do sacrifício de Cristo.",
        },
    )

    save_question(
        chapter_number=9,
        question_number=2,
        question_type="multiple_choice",
        prompt="Assinale com 'X' a alternativa correta em relação às ordenanças e cerimônias cristãs:",
        options=[
            {"key": "a", "text": "Apresentação de crianças: Não é bíblico, é apenas um costume das igrejas evangélicas."},
            {"key": "b", "text": "O Batismo em águas: É uma ordenança de Jesus e deve ser realizado por imersão em nome do Pai, do Filho e do Espírito Santo."},
            {"key": "c", "text": "Bodas de Casamento: Não é recomendável realizar cultos em celebrações matrimoniais."},
        ],
        correct_answer="b",
        explanation="O Batismo em águas é ordenança explícita de Jesus Cristo na Grande Comissão (Mt 28.19), ministrado por imersão aos convertidos.",
    )

    # ==========================================
    # CHAPTER 10
    # ==========================================
    save_question(
        chapter_number=10,
        question_number=1,
        question_type="multiple_choice",
        prompt="Assinale com 'X' a alternativa correta em relação à Igreja como Instituição de Ensino:",
        options=[
            {"key": "a", "text": "O jovem judeu não tinha liberdade de pensar por si mesmo, e de tornar-se perfeitamente familiarizado com as Escrituras."},
            {"key": "b", "text": "A EBD é o maior núcleo de ensino bíblico, do departamento de Educação Cristã das igrejas atualmente."},
            {"key": "c", "text": "A igreja é um templo de adoração, mas não deve ser um lugar onde são ensinadas as verdades divinas, como se fosse uma sala de aula."},
        ],
        correct_answer="b",
        explanation='O capítulo afirma que a Escola Bíblica Dominical (EBD) constitui o maior núcleo formador do departamento de educação cristã das igrejas.',
    )

    save_question(
        chapter_number=10,
        question_number=2,
        question_type="true_false",
        prompt="Em relação ao Ministério do Ensino e à Educação Cristã, avalie:",
        options=[
            {"key": "a", "statement": "Crianças judias, desde a tenra idade, frequentavam a escola na sinagoga."},
            {"key": "b", "statement": "O ministério do ensino não tem lugar na Grande Comissão."},
            {"key": "c", "statement": "O ministério de mestre está firmemente estabelecido e se reveste de capital importância."},
            {"key": "d", "statement": "Os diversos serviços da igreja local como a Escola Dominical, a Escola Bíblica de Obreiros e os cultos de ensino durante a semana não servem como setores de ensino."},
        ],
        correct_answer={"a": "V", "b": "F", "c": "V", "d": "F"},
        explanation="O papel do ensino bíblico na história judaico-cristã e na missão da igreja.",
        sub_explanations={
            "a": "VERDADEIRO: A educação religiosa desde a infância na sinagoga era pilar comunitário.",
            "b": "FALSO: Ensinar a guardar todas as coisas é mandamento central da Grande Comissão (Mt 28.20).",
            "c": "VERDADEIRO: O ministério de mestre/doutor é um dos dons ministeriais dados por Cristo (Ef 4.11).",
            "d": "FALSO: Todas essas instâncias são justamente os principais setores formativos de ensino da igreja.",
        },
    )

    # ==========================================
    # CHAPTER 11
    # ==========================================
    save_question(
        chapter_number=11,
        question_number=1,
        question_type="true_false",
        prompt="Em relação ao Planejamento Estratégico e Recursos Humanos na Igreja, avalie:",
        options=[
            {"key": "a", "statement": "São propósitos da organização eclesiástica: amoldar-se à natureza de Deus, prover o máximo de eficiência, assegurar a probidade administrativa."},
            {"key": "b", "statement": "A experiência do novo nascimento é imprescindível para que alguém se torne membro de uma igreja local."},
            {"key": "c", "statement": "Constitui-se função primordial do gestor elevar o espírito do trabalho voluntário conferindo a ele um significado profundo de amor a Deus."},
            {"key": "d", "statement": "O planejamento estratégico na igreja local desconsidera fatores como missão, visão e valores."},
        ],
        correct_answer={"a": "V", "b": "V", "c": "V", "d": "F"},
        explanation="Princípios de gestão e organização ministerial de pessoas na igreja.",
        sub_explanations={
            "a": "VERDADEIRO: Organização visa refletir a ordem divina e a probidade cristã.",
            "b": "VERDADEIRO: A regeneração é base espiritual para a comunhão eclesiástica.",
            "c": "VERDADEIRO: Motivar voluntários através do propósito eterno é dever da liderança.",
            "d": "FALSO: Missão, visão e valores são precisamente a fundação do planejamento estratégico.",
        },
    )

    save_question(
        chapter_number=11,
        question_number=2,
        question_type="matching",
        prompt="Relacione a segunda coluna de acordo com a primeira (Planejamento e Gestão de Pessoas):",
        options={
            "column_1": [
                {"key": "a", "text": "O recurso humano"},
                {"key": "b", "text": "O planejamento estratégico"},
                {"key": "c", "text": "Gestão de recursos humanos"},
                {"key": "d", "text": "As instituições religiosas"},
                {"key": "e", "text": "A propagação do Evangelho"},
            ],
            "column_2": [
                {"id": 1, "text": "Gestão de recursos humanos tem por finalidade selecionar, gerir e nortear os colaboradores na direção dos objetivos e metas de uma organização."},
                {"id": 2, "text": "O recurso humano é de fundamental importância para que nossas instituições possam cumprir a sua missão com excelência."},
                {"id": 3, "text": "A propagação do Evangelho se dá prioritariamente através dos relacionamentos."},
                {"id": 4, "text": "O planejamento estratégico define a natureza da igreja, sua missão, visão, valores e ações."},
                {"id": 5, "text": "As instituições religiosas devem se valer de pessoas que estejam dispostas e que tenham a motivação correta para desenvolver funções específicas no que tange a sua natureza e missão."},
            ],
        },
        correct_answer={"1": "c", "2": "e", "3": "a", "4": "b", "5": "d"},
        explanation="Papel das pessoas e do planejamento no cumprimento da missão eclesiástica.",
        sub_explanations={
            "1": "Gestão de Recursos Humanos: Selecionar e nortear pessoas para alcançar metas.",
            "2": "Importância dos Recursos Humanos para o cumprimento da missão.",
            "3": "Relações humanas: Canal prioritário para propagação do Evangelho.",
            "4": "Planejamento Estratégico: Missão, visão e valores orientadores.",
            "5": "Instituições Religiosas: Pessoas motivadas e vocacionadas pelo Espírito.",
        },
    )

    # ==========================================
    # CHAPTER 12
    # ==========================================
    save_question(
        chapter_number=12,
        question_number=1,
        question_type="true_false",
        prompt="Em relação às Finanças na Igreja, avalie cada assertiva:",
        options=[
            {"key": "a", "statement": "A igreja é uma comunidade de pessoas envolvidas em um sentimento religioso, de busca de satisfação da alma."},
            {"key": "b", "statement": "A igreja consegue prever com exatidão seus recursos porque depende da vontade das pessoas doarem estes recursos."},
            {"key": "c", "statement": "A Igreja de Cristo precisa de finanças, embora Deus seja o dono de tudo e além do mais, nos revestiu de poder, através do batismo com Espírito Santo, para que façamos como Jesus Cristo fez e muito mais."},
            {"key": "d", "statement": "A segunda multiplicação dos pães e peixes (Jo 6. 1-13), é um exemplo clássico de administração financeira eclesiástica."},
        ],
        correct_answer={"a": "V", "b": "F", "c": "V", "d": "V"},
        explanation="Particularidades e princípios bíblicos da gestão financeira na igreja.",
        sub_explanations={
            "a": "VERDADEIRO: A igreja é primordialmente comunidade de fé e comunhão espiritual.",
            "b": "FALSO: Como as doações são voluntárias, não há previsão com exatidão matemática irrestrita.",
            "c": "VERDADEIRO: Como entidade jurídica e atuante no mundo, necessita de recursos para sustentabilidade.",
            "d": "VERDADEIRO: O recolhimento das sobras (12 cestos) ilustra o princípio da economia e responsabilidade.",
        },
    )

    save_question(
        chapter_number=12,
        question_number=2,
        question_type="matching",
        prompt="Relacione a segunda coluna de acordo com a primeira (Administração Financeira Eclesiástica):",
        options={
            "column_1": [
                {"key": "a", "text": "O tesoureiro"},
                {"key": "b", "text": "Livro caixa ou relatório de registros financeiros"},
                {"key": "c", "text": "A igreja"},
                {"key": "d", "text": "Investimento"},
                {"key": "e", "text": "São parâmetros para considerar e analisar os riscos"},
            ],
            "column_2": [
                {"id": 1, "text": "A ele incumbe prestar contas dos valores sob sua guarda a quem de direito."},
                {"id": 2, "text": "Possui missão e objetivos totalmente avessos as organizações. (Consequentemente não pode ser administrada como um negócio)."},
                {"id": 3, "text": "É tudo aquilo que compramos ou contratamos no caso de serviços para melhorar o nosso projeto, para dar melhor estrutura a nossa instituição, equipamentos, utensílios, eventos e capacitação."},
                {"id": 4, "text": "Economia nacional, local, situação social, nível cultural e educacional, fatores como clima, região, culturas locais, hábitos locais, disposições econômicas."},
                {"id": 5, "text": "Trata-se do livro padrão utilizado por todas as igrejas."},
            ],
        },
        correct_answer={"1": "a", "2": "c", "3": "d", "4": "e", "5": "b"},
        explanation="Contabilidade, instrumentos de controle e zelo patrimonial na igreja.",
        sub_explanations={
            "1": "Tesoureiro: Responsável pela guarda e prestação de contas com transparência.",
            "2": "Natureza da Igreja: Organização sem fins lucrativos focada na salvação de vidas.",
            "3": "Investimento: Alocação de recursos para aprimorar a obra e infraestrutura.",
            "4": "Análise de Riscos: Variáveis socioeconômicas e locais a considerar.",
            "5": "Livro Caixa: Instrumento básico e universal de escrituração contábil.",
        },
    )

    # ==========================================
    # CHAPTER 13
    # ==========================================
    save_question(
        chapter_number=13,
        question_number=1,
        question_type="multiple_choice",
        prompt="Considerando os princípios de liderança e administração eclesiástica, assinale a alternativa correta:",
        options=[
            {"key": "a", "text": "“A Bíblia não contém princípios administrativos”."},
            {"key": "b", "text": "O termo administração vem do latim ad e minister, e significa literalmente “sustentar com as mãos”."},
            {"key": "c", "text": "Planejamento é a segunda grande função da administração eclesiástica, processo de gestão."},
        ],
        correct_answer="c",
        explanation='No capítulo 13, o Planejamento é caracterizado como função primordial no processo de gestão da igreja.',
    )

    save_question(
        chapter_number=13,
        question_number=2,
        question_type="matching",
        prompt="Relacione a segunda coluna de acordo com a primeira (Planejamento e Liderança Eclesiástica):",
        options={
            "column_1": [
                {"key": "a", "text": "O planejamento estratégico"},
                {"key": "b", "text": "O planejamento tático"},
                {"key": "c", "text": "O planejamento operacional"},
                {"key": "d", "text": "Fases do Planejamento na Igreja (e pessoal)"},
                {"key": "e", "text": "Rol de Membros"},
            ],
            "column_2": [
                {"id": 1, "text": "Compreende os recursos específicos. Seu desenvolvimento se dá pelos níveis organizacionais intermediários, tendo como objetivo a utilização eficiente dos recursos disponíveis com projeção em médio prazo."},
                {"id": 2, "text": "Correspondem a um conjunto de partes homogêneas do planejamento tático, ou seja, identifica os procedimentos e processos específicos requeridos nos níveis inferiores da organização, apresentando planos de ação ou planos operacionais."},
                {"id": 3, "text": "Relaciona-se com objetivos de longo prazo e com estratégias e ações para alcançá-los."},
                {"id": 4, "text": "Escolha de procedimentos, alocação de recursos financeiros, estabelecimento de controle."},
                {"id": 5, "text": "Pode ser um livro à parte ou ser uma seção do Livro da Secretaria."},
            ],
        },
        correct_answer={"1": "b", "2": "c", "3": "a", "4": "d", "5": "e"},
        explanation="Níveis do planejamento (estratégico, tático, operacional) e registros da igreja.",
        sub_explanations={
            "1": "Planejamento Tático: Nível intermediário com projeção em médio prazo.",
            "2": "Planejamento Operacional: Planos de ação específicos no nível operacional.",
            "3": "Planejamento Estratégico: Objetivos gerais de longo prazo.",
            "4": "Fases do Planejamento: Procedimentos, alocação de recursos e controle.",
            "5": "Rol de Membros: Registro formal dos membros sob a secretaria da igreja.",
        },
    )

    save_question(
        chapter_number=13,
        question_number=3,
        question_type="true_false",
        prompt="Em relação à liderança, ministérios e documentos eclesiásticos, avalie cada afirmação:",
        options=[
            {"key": "a", "statement": "A maneira como um pastor administra seus próprios bens não diz respeito ao seu ministério."},
            {"key": "b", "statement": "O encargo dos diáconos é uma invenção humana."},
            {"key": "c", "statement": "Os presbíteros ou anciãos podem servir em outras funções espirituais, até mesmo como responsáveis por congregações ou igrejas."},
            {"key": "d", "statement": "O Estatuto é um documento fundamental, escrito e registrado em cartório. É um conjunto de normas que estabelecem a estrutura e organização da instituição."},
            {"key": "e", "statement": "A ata é um documento auxiliar do Estatuto, nela estão contidas regras ou praxes secundarias e terciárias que a própria igreja estabelece para dar efeito ao Estatuto."},
        ],
        correct_answer={"a": "F", "b": "F", "c": "V", "d": "V", "e": "V"},
        explanation="Aspectos bíblicos e jurídicos da governança e liderança eclesiástica.",
        sub_explanations={
            "a": "FALSO: A administração dos próprios bens é crucial para a reputação e confiança no ministério.",
            "b": "FALSO: O diaconato tem instituição e fundamentação bíblica apostólica (Atos 6; 1 Tm 3).",
            "c": "VERDADEIRO: Presbíteros possuem respaldo bíblico para liderar e pastorear congregações.",
            "d": "VERDADEIRO: O Estatuto é o ato constitutivo que concede personalidade jurídica civil à igreja.",
            "e": "VERDADEIRO: Atas registram decisões complementares e assembleias em conformidade com o Estatuto.",
        },
    )

    print("All 13 chapters and 27 questions seeded successfully into SQLite!")


if __name__ == "__main__":
    seed()
