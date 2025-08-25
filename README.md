# CV Analyser with RAG 📄🤖

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

## 🎯 Overview

**CV Analyser with RAG** is an intelligent resume optimization tool that uses **Retrieval Augmented Generation (RAG)** to help job seekers tailor their CVs for specific job postings. The system analyzes job descriptions and automatically adapts resume content to maximize compatibility with **Applicant Tracking Systems (ATS)** while maintaining authenticity and personal branding.

### 🔍 The Problem We Solve

In today's competitive job market:
- **95% of Fortune 500 companies** use ATS to filter resumes before human review
- Many qualified candidates are rejected due to **keyword mismatches** between their CV and job descriptions
- Manual resume tailoring is **time-consuming and error-prone**
- Job seekers struggle to **optimize for ATS without losing their authentic voice**

### 💡 Our Solution

This project combines **AI-powered analysis** with **semantic search** to:

1. **📄 Extract & Structure**: Convert PDF resumes into structured JSON format using [JSON Resume Schema](https://jsonresume.org/schema)
2. **🧠 Understand Context**: Use Google Gemini AI to analyze job descriptions and identify key requirements
3. **🔍 Semantic Matching**: Leverage ChromaDB vector database to find relevant experiences from your CV
4. **✨ Intelligent Optimization**: Generate ATS-friendly content that maintains your personal brand and uses active voice
5. **🎯 Maximize Compatibility**: Ensure 100% ATS compatibility while keeping content concise and compelling

### 🏗️ Why Kedro?

We chose **Kedro** as our pipeline framework because:
- **Reproducible Pipelines**: Ensures consistent CV processing across different job applications
- **Data Lineage**: Track how your original CV transforms into optimized versions
- **Modular Architecture**: Easy to add new analysis steps or AI models
- **Configuration Management**: Securely handle API credentials and processing parameters
- **Experiment Tracking**: Compare different optimization strategies and their effectiveness

## 🚀 Core Features

### 📊 Intelligent CV Analysis
- **PDF to JSON Conversion**: Automatically extract structured data from PDF resumes
- **Schema Validation**: Ensure data compatibility with JSON Resume standard
- **Content Categorization**: Organize experiences, skills, education, and achievements

### 🎯 Job Description Matching
- **Keyword Extraction**: Identify critical terms and requirements from job postings
- **Semantic Understanding**: Go beyond simple keyword matching using AI embeddings
- **Context Awareness**: Understand industry-specific terminology and requirements

### 🔍 RAG-Powered Optimization
- **Vector Search**: Use ChromaDB to find relevant experiences from your CV history
- **Contextual Retrieval**: Retrieve the most relevant past experiences for each job
- **Smart Adaptation**: Intelligently modify descriptions while preserving accuracy

### ✨ ATS Optimization
- **Keyword Integration**: Naturally incorporate job-specific keywords
- **Active Voice Conversion**: Transform descriptions to use compelling active voice
- **Concise Formatting**: Optimize length and structure for ATS parsing
- **Brand Consistency**: Maintain your personal voice and professional brand

## 🏛️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   PDF Resume    │───▶│  Kedro Pipeline  │───▶│ Optimized CV    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                               │
                               ▼
       ┌─────────────────────────────────────────────────────┐
       │                 Core Components                     │
       ├─────────────────┬─────────────────┬─────────────────┤
       │   Google Gemini │   ChromaDB      │ JSON Resume     │
       │   (AI Analysis) │ (Vector Store)  │   (Schema)      │
       └─────────────────┴─────────────────┴─────────────────┘
```

**Tech Stack:**
- 🧠 **Google Gemini API**: Advanced language understanding and generation
- 🗄️ **ChromaDB**: Vector database for semantic search and embeddings
- ⚙️ **Kedro**: Pipeline orchestration and data management
- 📋 **JSON Resume Schema**: Standardized CV data structure
- 🐍 **Python**: Core development language with rich AI/ML ecosystem

## How to install dependencies

The dependencies are handled through the `pyproject.toml` file using [`uv`](https://astral.sh/blog/uv). To install `uv`, you can consult the [`uv` documentation](https://docs.astral.sh/uv/getting-started/installation/). To install the dependencies, run the following command:

```bash
uv venv
source .venv/bin/activate  # on Windows use > . .venv\Scripts\Activate.ps1
uv sync
```

The first and second lines will create and activate a virtual environment and the third will install all the necessary dependencies for the project.

If you are a developer, you can run the following command to install the optional dependencies and install the pre-commit hooks:

```bash
uv sync --all-extras
pre-commit install
```

### 🪟 Windows-specific requirements (C++ compiler)

Some dependencies in this project (e.g., `chroma-hnswlib`, required by `chromadb`) need to be compiled from source, which requires a C++ compiler on Windows.

If you're on Windows, please make sure you install the Microsoft C++ Build Tools before running `uv sync`:

- Download from: [https://visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

- During installation, make sure to check:
    - ✅ C++ build tools
    - ✅ Windows 10 SDK
    - ✅ MSVC v14.x

Once installed, restart your terminal and re-run:

```bash
uv sync
```

If you skip this step, you may get errors like:

```
error: Microsoft Visual C++ 14.0 or greater is required
```

## How to Add Gemini API Credentials

To use the Gemini API in this project, you need to provide your API credentials. Follow these steps to securely add and access your credentials:

### 1. Locate the `credentials.yml` File
The credentials for your project are stored in a YAML file located in the `conf/local/` directory. This file is ignored by version control to keep your sensitive information secure.

If the file does not exist, create it at the following path:
```
conf/local/credentials.yml
```

### 2. Add Your Gemini API Credentials
Open the `credentials.yml` file and add your Gemini API credentials in the following format:
```yaml
google_api_credentials:
  key: "your_gemini_api_key"
```
By following these steps, you can securely configure and use the Gemini API in your Kedro project.

## How to run your Kedro pipeline

You can run your Kedro project with:

```bash
kedro run
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```bash
pytest
```

You can configure the coverage threshold in your project's `pyproject.toml` file under the `[tool.coverage.report]` section.


## Project dependencies

To see and update the dependency requirements for your project use `requirements.txt`. You can install the project requirements with `pip install -r requirements.txt`.

[Further information about project dependencies](https://docs.kedro.org/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `context`, 'session', `catalog`, and `pipelines`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r requirements.txt` (or `uv sync`) you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```bash
pip install jupyter
uv pip install jupyter  # if you are using uv
```

After installing Jupyter, you can start a local notebook server:

```bash
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```bash
pip install jupyterlab
uv pip install jupyterlab  # if you are using uv
```

You can also start JupyterLab:

```bash
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```bash
kedro ipython
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can use tools like [`nbstripout`](https://github.com/kynan/nbstripout). For example, you can add a hook in `.git/config` with `nbstripout --install`. This will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://docs.kedro.org/en/stable/tutorial/package_a_project.html)

## 🎯 Project Objectives

### Short-term Goals
- ✅ **Core Pipeline**: Implement end-to-end CV processing pipeline
- ✅ **RAG Integration**: Enable semantic search and content retrieval
- ✅ **ATS Optimization**: Generate ATS-compatible resume variations
- 🔄 **Multi-language Support**: Support for Spanish and English optimization
- 🔄 **Batch Processing**: Handle multiple job descriptions efficiently

### Long-term Vision
- 🚀 **Real-time API**: Web service for instant CV optimization
- 📊 **Success Analytics**: Track application success rates and optimize accordingly
- 🎨 **Template Generation**: Generate formatted resumes in multiple styles
- 🤖 **Interview Prep**: Extend to interview question preparation based on job analysis
- 🌐 **Platform Integration**: Direct integration with job boards and application systems

## 🤝 How to Contribute

We welcome contributions! Here are ways to get involved:

### 🐛 Found a Bug?
1. Check existing [issues](https://github.com/framunoz/cv-analyser-with-rag/issues)
2. Create a detailed bug report with reproduction steps
3. Include sample data (anonymized) if relevant

### 💡 Have an Idea?
1. Open a feature request issue
2. Describe the use case and expected behavior
3. Discuss implementation approaches

### 🔧 Want to Code?
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Follow the existing code style and add tests
4. Submit a pull request with clear description

### 📚 Improve Documentation?
- Fix typos or unclear explanations
- Add examples and use cases
- Translate content to other languages
- Improve code comments and docstrings

## 📋 Next Steps

Ready to optimize your CV? Here's what to do:

1. **📥 Setup**: Follow the installation instructions above
2. **🔑 Configure**: Add your Gemini API credentials
3. **📄 Prepare**: Place your PDF resume in the `data/01_raw/` folder
4. **🏃‍♂️ Run**: Execute `kedro run` to process your CV
5. **🎯 Optimize**: Use the notebooks to analyze specific job descriptions
6. **📊 Review**: Check the generated optimized content in `data/08_reporting/`

### 📖 Learning Resources
- [Kedro Documentation](https://docs.kedro.org) - Learn about the pipeline framework
- [JSON Resume Schema](https://jsonresume.org/schema) - Understand the CV data structure
- [Google Gemini API](https://ai.google.dev/) - Explore AI capabilities
- [ChromaDB Documentation](https://docs.trychroma.com/) - Vector database operations

### 🎓 Advanced Usage
Check out our notebooks for advanced features:
- `00-pdf-to-json.ipynb`: Convert and validate PDF resumes
- `01-fmg-rag.ipynb`: Interactive RAG analysis
- `02-fmg-refactor.ipynb`: Batch processing and optimization
- `colab-rag.ipynb`: Google Colab compatible version

---

**⚠️ Important**: Always review AI-generated content before using it in real applications. This tool assists with optimization but human judgment is essential for final decisions.

**🔒 Privacy**: Your CV data is processed locally. API calls to Google Gemini only send anonymized text snippets for analysis.
