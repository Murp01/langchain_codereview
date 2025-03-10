# LangChain Code Review Assistant - README

## 🚀 Project Overview
The **LangChain Code Review Assistant** is an AI-powered tool designed to assist with automated code reviews for **Python and C#** projects. Using **LangChain** and either **OpenAI (GPT-4)** or **Ollama (Llama3)**, it analyzes code for:

- **Syntax issues**
- **Code quality and best practices**
- **Performance optimizations**
- **Security vulnerabilities**
- **Maintainability improvements**

This tool allows teams to streamline code reviews, enforce standards, and improve overall code quality.

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/langchain_code_review.git
cd langchain_code_review
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
# Activate the environment (Windows)
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🔑 Setting Up Environment Variables

Create a `.env` file in the project root to configure API keys and model selection:

```
# OpenAI Configuration (Optional)
OPENAI_API_KEY="your_api_key_here"
MODEL_NAME="gpt-4"

# Ollama Configuration (Default)
OLLAMA_MODEL="llama3"
```

- **Use OpenAI:** Set `MODEL_NAME` to `gpt-4` and provide an OpenAI API key.
- **Use Ollama (local model):** Ensure Ollama is installed and set `OLLAMA_MODEL="llama3"`.

---

## 🎯 How to Use

### 1️⃣ Run Code Review on a Single File
```sh
python src/main.py code_samples/sample.py --language Python
```

```sh
python src/main.py code_samples/sample.cs --language C#
```

### 2️⃣ Run Code Review on an Entire Project
```sh
python src/main.py /path/to/your/project --language Python
```

### 3️⃣ View Results
Results are saved in the `reports/` folder as a text file with structured feedback.

---

## 🔗 Optional Integrations

### 🔍 Git Pre-Commit Hook
Automatically review code before commits:
1. Navigate to `.git/hooks/` in your repository:
   ```sh
   cd .git/hooks/
   ```
2. Create a `pre-commit` file:
   ```sh
   touch pre-commit
   chmod +x pre-commit
   ```
3. Add the following script:
   ```sh
   #!/bin/bash
   echo "🔍 Running AI-Powered Code Review before commit..."
   python /path_to_langchain_code_review/src/main.py . --language Python
   if [ $? -ne 0 ]; then
       echo "❌ Code review detected issues. Commit aborted."
       exit 1
   else
       echo "✅ Code review passed. Proceeding with commit."
   fi
   ```

### ⚙️ GitHub Actions for CI/CD
Automatically review pull requests and commits with GitHub Actions:
```yaml
name: AI Code Review
on: [push, pull_request]

jobs:
  code_review:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.9"
      - name: Install dependencies
        run: |
          python -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt
      - name: Run AI Code Review
        run: |
          python src/main.py . --language Python
```

---

## 🛠 Future Enhancements
- **Improve Report Formatting**: Add JSON or Markdown outputs.
- **VS Code Extension**: Create an integrated VS Code plugin.
- **More Languages**: Expand support beyond Python and C#.

---

## 📜 License
This project is open-source under the **MIT License**.

---

## 🤝 Contributing
Contributions are welcome! Feel free to submit pull requests or open issues.

---

## 📞 Contact
For questions, reach out via GitHub Issues or email at `your_email@example.com`.

---

