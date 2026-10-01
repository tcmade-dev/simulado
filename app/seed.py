"""
Seed script to populate SQLite with Chapter 1 questions and answers
from documents/questionarios and documents/respostas.
"""

from app.database import init_db, save_chapter, save_question

CHAPTER_TITLES = [
    (1, "A Igreja Evangélica Assembleia de Deus e sua Missão", True),
    (2, "Teologia", False),
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

    print("Database initialized and Chapter 1 questions seeded successfully!")


if __name__ == "__main__":
    seed()
