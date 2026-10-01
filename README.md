# Simulado - Introdução ao Santo Ministério

Aplicativo interativo de simulado e autoavaliação teológica com validação imediata, pontuação, gabarito fundamentado e histórico de tentativas.

## Stack do Projeto
- **Gerenciador de Dependências**: [`uv`](https://docs.astral.sh/uv/)
- **Backend**: FastAPI + Python 3.11+
- **Banco de Dados Local**: SQLite (`data/simulado.db`)
- **Frontend / UX**: HTMX + Jinja2 + Tailwind CSS (zero build overhead, reativo e responsivo)

---

## Como Executar o Simulado

```bash
# Iniciar a aplicação web
uv run main.py

# Ou diretamente via uvicorn com reload automático:
uv run uvicorn app.main:app --reload --port 8000
```

Acesse no navegador: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## Funcionalidades Atuais (Passo a Passo)

1. **Dashboard de Capítulos**:
   - Visualização dos 13 capítulos do livro com status de disponibilidade.
   - **Capítulo 1 Ativo**: com questões de múltipla escolha e verdadeiro/falso extraídas de `documents/questionarios` e `documents/respostas`.
   - Estatísticas gerais (número de tentativas, média de acertos, melhor nota).

2. **Questionário Interativo (HTMX)**:
   - Questões de múltipla escolha com opções personalizadas.
   - Questões de Verdadeiro (V) ou Falso (F) por afirmação individual.
   - Confirmação antes do envio e validação sem recarregar a página (`hx-post`).

3. **Validação & Gabarito Comentado**:
   - Cálculo automático da nota percentual (0 a 100%).
   - Indicação visual verde/vermelho para cada questão e afirmativa.
   - Justificativa teológica e histórica detalhada para cada item extraída do material de estudo.

4. **Histórico Local em SQLite**:
   - Registro permanente de todas as tentativas do usuário com timestamp, acertos, percentual e detalhes das respostas.
   - Acesso em `/historico`.

---

# PDF to DOCX Converter

A fast, high-fidelity PDF to Microsoft Word (`.docx`) conversion tool built with `pdf2docx` and `PyMuPDF`. It accurately reconstructs document layout, fonts, headings, tables, and images.

---

## Quick Start

You can convert any PDF directly using the wrapper script `./convert.sh`:

```bash
# Convert entire PDF (defaults to same name with .docx extension)
./convert.sh "documents/Introdução ao Santos Ministério.pdf"

# Specify a custom output file
./convert.sh "documents/Introdução ao Santos Ministério.pdf" "output.docx"

# Convert specific pages (e.g. pages 1 to 10)
./convert.sh -p "1-10" "documents/Introdução ao Santos Ministério.pdf"

# Convert discontinuous pages (e.g. pages 1, 3, 5-8)
./convert.sh -p "1,3,5-8" "documents/Introdução ao Santos Ministério.pdf"

# Convert by start and end page
./convert.sh -s 11 -e 30 "documents/Introdução ao Santos Ministério.pdf"

# Inspect PDF structure and metadata without converting
./convert.sh -i "documents/Introdução ao Santos Ministério.pdf"
```

---

## Python API Usage

You can also import and use the converter directly in your Python code:

```python
from pdf_to_docx import convert_pdf_to_docx

# Convert entire file with multi-core parallel processing
convert_pdf_to_docx(
    pdf_path="documents/Introdução ao Santos Ministério.pdf",
    docx_path="output.docx",
    multi_processing=True
)

# Convert specific page range
convert_pdf_to_docx(
    pdf_path="documents/Introdução ao Santos Ministério.pdf",
    docx_path="capitulo_1.docx",
    start_page=11,
    end_page=30
)
```

---

## Command Line Options

| Option | Description | Example |
|---|---|---|
| `input` | Path to the PDF file (positional or default) | `documents/book.pdf` |
| `output` | Destination `.docx` path (optional) | `documents/book.docx` |
| `-i`, `--info` | Show PDF metadata, page count & TOC | `./convert.sh -i file.pdf` |
| `-p`, `--pages` | 1-indexed page selection | `-p 1-10` or `-p 1,3,5-9` |
| `-s`, `--start` | 1-indexed starting page | `-s 10` |
| `-e`, `--end` | 1-indexed ending page (inclusive) | `-e 50` |
| `-c`, `--cpu-count` | Number of CPU cores for parallel conversion | `-c 4` |
| `--no-parallel` | Disable multi-core processing | `--no-parallel` |
