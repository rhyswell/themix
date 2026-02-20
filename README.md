
```markdown
# 🧠 Themic  
### AI-Powered Thematic Analysis Engine (Desktop Application)

Themic is a modular, research-grade thematic analysis engine built with Python and OpenAI’s API.

It performs **open coding**, constructs themes, refines them, critiques analytical quality, and generates a structured **Markdown research report** — all through a clean Tkinter desktop interface.

Designed for qualitative researchers, AI experimentation, and production-grade LLM system design.

---

## 🚀 Features

- 📂 Batch processing of 10–50 `.txt` transcripts
- ✂️ Token-aware chunking using `tiktoken`
- 🏷 Open coding (qualitative, inductive)
- 🧩 AI-driven theme construction
- 🧠 Multi-stage theme refinement & critique
- ✍️ Academic rewriting
- 📝 Automated Markdown research report generation
- 🖥 Desktop GUI (Tkinter)
- ⚙️ Fully modular AI role architecture
- 📦 Package-structured Python project

---

## 🏗 Architecture Overview

Themic is designed as a **multi-role LLM pipeline**:

```

TXT Files
↓
Code Finder (Open Coding)
↓
Theme Builder
↓
Theme Refiner
↓
Theme Critiquer
↓
Theme Rewriter
↓
Report Writer (Markdown Output)

```

Each stage:
- Receives structured JSON
- Produces structured JSON
- Is independently testable and swappable

This architecture mirrors real-world LLM system orchestration.

---

## 🧠 AI Roles

| Role | Purpose |
|------|----------|
| **Code Finder** | Performs inductive open coding |
| **Theme Builder** | Clusters codes into conceptual themes |
| **Theme Refiner** | Merges, splits, clarifies themes |
| **Theme Critiquer** | Evaluates analytical quality |
| **Theme Rewriter** | Improves academic clarity |
| **Report Writer** | Generates structured Markdown report |

This separation demonstrates production-style LLM design patterns.

```

## 📁 Project Structure

themic/
│
├── main.py
├── config.json
├── config_loader.py
│
├── core/
│   ├── openai_client.py
│   ├── chunker.py
│   ├── file_loader.py
│   └── json_utils.py
│
├── roles/
│   ├── base_role.py
│   ├── code_finder.py
│   ├── theme_builder.py
│   ├── theme_refiner.py
│   ├── theme_critiquer.py
│   ├── theme_rewriter.py
│   └── report_writer.py
│
├── pipeline/
│   └── thematic_pipeline.py
│
├── gui/
│   ├── app.py
│   └── components.py
│
└── txt_inputs/

````

The project is structured as a proper Python package and uses absolute imports.

---

## 🛠 Tech Stack

- Python 3.10+
- OpenAI Responses API
- Tkinter (desktop UI)
- tiktoken (token-aware chunking)
- Modular LLM pipeline design
- Structured JSON contracts

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/rhyswell/themic.git
cd themic
````

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add your OpenAI API key

Edit `themic/config.json`:

```json
{
  "api_key": "sk",
  ...
}
```

---

## ▶️ Running Themic

From the project root:

```bash
python -m themic.main
```

Do NOT run `python main.py`.

---

## 📊 Example Workflow

1. Place transcripts in `themic/txt_inputs/`
2. Launch the application
3. Click **Start Analysis**
4. View generated Markdown report
5. Saved automatically in `outputs/`

---

## 📈 Future Improvements

* Async parallel API calls
* Caching layer (SQLite/Redis)
* Embedding-based theme clustering
* Cost estimation mode
* Export to PDF
* Dark mode UI
* Packaging as installable desktop app

---

## 🎯 Use Cases

* Qualitative research automation
* Interview transcript analysis
* Academic research support
* LLM system design demonstration
* AI internship portfolio project
