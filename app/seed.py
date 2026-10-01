"""
Seed script to populate SQLite with Chapter 1 questions and answers
from documents/questionarios and documents/respostas.
"""

from app.database import init_db, save_chapter, save_question

CHAPTER_TITLES = [
    (1, "A Igreja Evangélica Assembleia de Deus e sua Missão", True),
    (2, "Teologia", True),
    (3, "Homilética", False),
    (4, "Hermenêutica", False),
    (5, "Pastoral & Clínica Pastoral", False),
    (6, "Vida Conjugal do Ministro", False),
    (7, "Ética Ministerial", False),
    (8, "Adoração e Liturgia", False),
    (9, "Cerimônias e Celebrações", False),
    (10, "A Igreja como Instituição de Ensino", False),
    (11, "Planejamento Estratégico e Recursos Humanos", False),
    (12, "Finanças na Igreja", False),
    (13, "Liderança Eficaz", False),
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

    # --- CHAPTER 1 QUESTIONS ---

    # Questão 1 (Múltipla Escolha)
    q1_prompt = "Os pentecostais foram caracterizados por cinco valores implícitos:"
    q1_options = [
        {
            "key": "a",
            "text": "Jesus Salva, Cura, Batiza com Espírito Santo e Breve Voltará.",
        },
        {
            "key": "b",
            "text": "A experiência pessoal, A comunicação oral, A espontaneidade, O repúdio ao mundanismo, A autoridade das Escrituras Sagradas.",
        },
        {
            "key": "c",
            "text": "O amor ao próximo, A autoridade das Escrituras Sagradas, A popularidade, O batismo no Espírito Santo, O avivamento.",
        },
    ]
    q1_correct = "b"
    q1_explanation = (
        'O capítulo 1 reproduz, na seção "Desenvolvimento da Teologia Pentecostal", a lista exata dos '
        'cinco valores implícitos: 1. A experiência pessoal; 2. A comunicação oral; 3. A espontaneidade; '
        '4. O repúdio ao mundanismo; 5. A autoridade das Escrituras Sagradas.\n\n'
        'A alternativa (a) está incorreta porque "Jesus Salva, Cura, Batiza com Espírito Santo e Breve Voltará" '
        'são os 4 alicerces bíblicos do evangelho sobre os quais a Igreja nasceu (quatro, e não cinco). '
        'A alternativa (c) também está incorreta, pois itens como "popularidade" e "avivamento" não compõem a lista original.'
    )

    save_question(
        chapter_number=1,
        question_number=1,
        question_type="multiple_choice",
        prompt=q1_prompt,
        options=q1_options,
        correct_answer=q1_correct,
        explanation=q1_explanation,
    )

    # Questão 2 (Verdadeiro ou Falso)
    q2_prompt = (
        "Em relação à Igreja Evangélica Assembleia de Deus, avalie cada afirmação como "
        "Verdadeira (V) ou Falsa (F):"
    )
    q2_options = [
        {
            "key": "a",
            "statement": "Igreja Evangélica Assembleia de Deus, nasceu em 1911, na data de 18 de junho, (com o nome de \"Missão de Fé Apostólica\").",
        },
        {
            "key": "b",
            "statement": "No Estado do Paraná, está presente desde 1920, e conta hoje com mais de 150 campos eclesiásticos.",
        },
        {
            "key": "c",
            "statement": "Gunnar de Vingren não era um pastor de formação teológica.",
        },
        {
            "key": "d",
            "statement": (
                "A igreja Missão de Fé Apostólica, passou a se chamar Assembleia de Deus em 11 de janeiro de 1918, "
                "quando Gunnar Vingren registrou o estatuto da igreja no cartório de Registro de Títulos e Documentos "
                "do 1 oficio, em Belém."
            ),
        },
    ]
    q2_correct = {
        "a": "V",
        "b": "F",
        "c": "F",
        "d": "V",
    }
    q2_sub_explanations = {
        "a": (
            'VERDADEIRO: O capítulo confirma: "A Igreja Evangélica Assembleia de Deus, nasceu em 1911, '
            'na data de 18 de junho [...] Foram 18 pessoas ao todo, que reunidos iniciaram a igreja \'Missão de Fé Apostólica\'".'
        ),
        "b": (
            'FALSO: O texto do capítulo informa que no Estado do Paraná a igreja "conta hoje com mais de 144 campos eclesiásticos", '
            'e não 150.'
        ),
        "c": (
            'FALSO: O texto diz expressamente o contrário: "Gunnar Vingren era um pastor de formação teológica, '
            'e muito se preocupou em instruir os primeiros crentes, com ênfase para a doutrina pentecostal".'
        ),
        "d": (
            'VERDADEIRO: O capítulo confirma na íntegra: "A igreja Missão de Fé Apostólica, passou a se chamar Assembleia de Deus '
            'em 11 de janeiro de 1918, quando Gunnar Vingren registrou o estatuto da igreja no cartório de Registro de Títulos e Documentos do 1 ofício, em Belém".'
        ),
    }
    q2_explanation = "Avaliação das afirmativas sobre a história, fundação e registro da Assembleia de Deus."

    save_question(
        chapter_number=1,
        question_number=2,
        question_type="true_false",
        prompt=q2_prompt,
        options=q2_options,
        correct_answer=q2_correct,
        explanation=q2_explanation,
        sub_explanations=q2_sub_explanations,
    )

    # --- CHAPTER 2 QUESTIONS ---

    # Questão 1 (Múltipla Escolha)
    c2_q1_prompt = "A Teologia se classifica de 4 maneiras, a saber:"
    c2_q1_options = [
        {
            "key": "a",
            "text": "Teologia Filosófica, Teologia Elementar, Teologia Bíblica e Teologia Pentecostal.",
        },
        {
            "key": "b",
            "text": "Teologia Exegética, Teologia Bíblica, Teologia Histórica e Teologia Dogmática.",
        },
        {
            "key": "c",
            "text": "Teologia Exegética, Teologia Hermenêutica, Teologia Escatológica, Teologia Histórica.",
        },
    ]
    c2_q1_correct = "b"
    c2_q1_explanation = (
        'Na seção "Classificação da Teologia", o capítulo 2 enumera exatamente quatro categorias: '
        '1. Teologia Exegética: exegese vem do grego, e significa "Sacar, extrair a verdade". '
        '2. Teologia Bíblica: destaca o progresso da verdade através dos diversos livros bíblicos. '
        '3. Teologia Histórica: traça a história do desenvolvimento da interpretação doutrinária. '
        '4. Teologia Dogmática: também chamada de Teologia Prática, estuda as verdades fundamentais da fé.\n\n'
        'A alternativa (a) está incorreta porque não há menção a "Teologia Filosófica" ou "Elementar". '
        'A alternativa (c) também está incorreta, pois "Hermenêutica" é tratada no capítulo 4 e Escatologia é parte da Teologia Própria.'
    )

    save_question(
        chapter_number=2,
        question_number=1,
        question_type="multiple_choice",
        prompt=c2_q1_prompt,
        options=c2_q1_options,
        correct_answer=c2_q1_correct,
        explanation=c2_q1_explanation,
    )

    # Questão 2 (Verdadeiro ou Falso)
    c2_q2_prompt = "Em relação às doutrinas e estrutura bíblica abordadas no Capítulo 2, avalie cada afirmação como Verdadeira (V) ou Falsa (F):"
    c2_q2_options = [
        {
            "key": "a",
            "statement": "Em Gênesis 1.1 encontramos 7 doutrinas relacionadas com a pessoa de Deus, a saber: A Existência de Deus, A Eternidade de Deus, O Poder de Deus, A Soberania de Deus, A Vontade de Deus, A Sabedoria de Deus, A Providência de Deus.",
        },
        {
            "key": "b",
            "statement": "A Bíblia é dividida em duas partes: Antigo e Novo Testamento. Possui: 65 livros, sendo 38 no Antigo Testamento, e 27 no Novo Testamento.",
        },
        {
            "key": "c",
            "statement": "Hamartiologia é a Doutrina da Salvação.",
        },
        {
            "key": "d",
            "statement": "No Estudo do Espírito Santo há a Paracletologia: o termo Paracletologia vem do grego Paracleto (Advogado, Consolador, Ajudador).",
        },
    ]
    c2_q2_correct = {
        "a": "V",
        "b": "F",
        "c": "F",
        "d": "V",
    }
    c2_q2_sub_explanations = {
        "a": (
            'VERDADEIRO: O capítulo 2 reproduz exatamente essas 7 doutrinas em Gênesis 1.1: '
            'Existência, Eternidade, Poder, Soberania, Vontade, Sabedoria e Providência de Deus.'
        ),
        "b": (
            'FALSO: O texto do livro ensina que a Bíblia possui 66 livros (sendo 39 no Antigo Testamento e 27 no Novo Testamento), '
            'e não 65/38.'
        ),
        "c": (
            'FALSO: Hamartiologia é a Doutrina do Pecado. A Doutrina da Salvação chama-se Soteriologia (do grego Soteria).'
        ),
        "d": (
            'VERDADEIRO: Na Pneumatologia, Paracletologia vem do grego Paracleto (Advogado, Consolador, Ajudador).'
        ),
    }
    c2_q2_explanation = "Avaliação doutrinária sobre Gênesis 1.1, divisão bíblica e termos teológicos fundamentais."

    save_question(
        chapter_number=2,
        question_number=2,
        question_type="true_false",
        prompt=c2_q2_prompt,
        options=c2_q2_options,
        correct_answer=c2_q2_correct,
        explanation=c2_q2_explanation,
        sub_explanations=c2_q2_sub_explanations,
    )

    print("Database initialized and Chapters 1 & 2 seeded successfully!")


if __name__ == "__main__":
    seed()
