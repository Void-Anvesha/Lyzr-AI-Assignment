# Automated GitHub Pull Request Review Agent

An intelligent, multi-agent system that automatically analyzes GitHub Pull Requests and provides comprehensive code reviews with actionable feedback. Built using the Lyzr AI framework to demonstrate enterprise-grade GenAI application development.

## 📋 Problem Statement

This project addresses the challenge of automated code review by building a PR Review Agent that:

- Reads and parses GitHub PR diffs (via GitHub API or manual input)
- Understands code changes at the line level
- Employs multi-agent reasoning for comprehensive analysis
- Identifies issues across multiple dimensions: logic, readability, performance, and security
- Generates structured, actionable review comments similar to human reviewers

## 🎯 Project Overview

The Automated PR Review Agent leverages Lyzr's multi-agent orchestration capabilities to simulate a team of specialized code reviewers. Each agent focuses on specific aspects of code quality, working together to provide comprehensive feedback that helps developers improve their code before merging.

## ✨ Key Features

### Multi-Agent Architecture
- **Logic Analyzer Agent**: Reviews code logic, flow, and correctness
- **Readability Agent**: Evaluates code clarity, naming conventions, and documentation
- **Performance Agent**: Identifies potential performance bottlenecks and optimization opportunities
- **Security Agent**: Scans for security vulnerabilities and best practice violations

### Core Capabilities
- **GitHub Integration**: Fetches PR diffs directly via GitHub API
- **Intelligent Parsing**: Understands code context and change implications
- **Structured Output**: Generates organized review comments with severity levels
- **Actionable Feedback**: Provides specific suggestions for improvement
- **Multi-Language Support**: Analyzes various programming languages

## 🏗️ System Architecture

```
┌─────────────────┐
│   GitHub API    │
│   PR Fetcher    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Diff Parser &  │
│  Code Analyzer  │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│     Multi-Agent Review Pipeline     │
│                                     │
│  ┌─────────┐  ┌──────────────┐    │
│  │  Logic  │  │ Readability  │    │
│  │ Analyst │  │    Agent     │    │
│  └─────────┘  └──────────────┘    │
│                                     │
│  ┌─────────┐  ┌──────────────┐    │
│  │Security │  │ Performance  │    │
│  │  Agent  │  │    Agent     │    │
│  └─────────┘  └──────────────┘    │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────┐
│ Review Comment  │
│   Generator     │
└─────────────────┘
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- GitHub Personal Access Token (for API access)
- OpenAI API key or other LLM provider credentials
- Git installed on your system

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Void-Anvesha/Lyzr-AI-Assignment.git
cd Lyzr-AI-Assignment
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

Required packages include:
- `lyzr-automata` or `lyzr` (for agent framework)
- `PyGithub` or `requests` (for GitHub API)
- `openai` (for LLM integration)
- `python-dotenv` (for environment management)
- `streamlit` (if using web interface)

4. **Configure environment variables**
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
```env
GITHUB_TOKEN=your_github_personal_access_token
OPENAI_API_KEY=your_openai_api_key
# Optional: Configure specific model
OPENAI_MODEL=gpt-4
```

## 💻 Usage

### Method 1: Analyze PR via GitHub URL

```bash
python app.py --pr-url https://github.com/owner/repo/pull/123
```

### Method 2: Manual Diff Input

```bash
python app.py --diff-file path/to/diff.patch
```

### Method 3: Interactive Mode (Streamlit)

```bash
streamlit run app.py
```

Then enter your PR URL or paste the diff content in the web interface.

### Example Output

```
🔍 PR Review Summary
Repository: owner/repo
PR #123: Feature/add-user-authentication

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 LOGIC REVIEW
──────────────
File: src/auth/login.py
Line 45: Critical
Issue: Missing null check before user.email access
Suggestion: Add validation: if user is None: return error

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📖 READABILITY REVIEW
─────────────────────
File: src/auth/login.py
Line 23: Minor
Issue: Variable name 'x' is not descriptive
Suggestion: Rename to 'authentication_token' for clarity

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ PERFORMANCE REVIEW
────────────────────
File: src/database/queries.py
Line 67: Major
Issue: N+1 query detected in loop
Suggestion: Use bulk query or join to reduce database calls

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔒 SECURITY REVIEW
──────────────────
File: src/api/endpoints.py
Line 102: Critical
Issue: SQL injection vulnerability - unsanitized user input
Suggestion: Use parameterized queries or ORM methods

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Overall Assessment: 3 Critical, 1 Major, 1 Minor issues found
Recommendation: Address critical issues before merging
```

## 📁 Project Structure

```
Lyzr-AI-Assignment/
├── app.py                      # Main application entry point
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
│
├── agents/
│   ├── __init__.py
│   ├── logic_agent.py         # Logic analysis agent
│   ├── readability_agent.py   # Code readability agent
│   ├── performance_agent.py   # Performance optimization agent
│   └── security_agent.py      # Security vulnerability agent
│
├── tasks/
│   ├── __init__.py
│   ├── diff_parser.py         # Parse GitHub diffs
│   ├── code_analyzer.py       # Analyze code changes
│   └── review_generator.py    # Generate review comments
│
├── utils/
│   ├── __init__.py
│   ├── github_client.py       # GitHub API integration
│   ├── prompt_templates.py    # Agent prompt templates
│   └── formatters.py          # Output formatting utilities
│
├── tests/
│   ├── test_agents.py
│   ├── test_parser.py
│   └── sample_diffs/
│
└── README.md
```

## 🔧 Configuration

### Customizing Review Criteria

Edit `agents/` files to adjust review focus:

```python
# agents/security_agent.py
SECURITY_CHECKS = [
    "SQL Injection",
    "XSS Vulnerabilities",
    "Authentication Issues",
    "Sensitive Data Exposure",
    "CSRF Protection"
]
```

### Adjusting Severity Levels

Configure in `utils/formatters.py`:
- **Critical**: Security vulnerabilities, logic errors causing failures
- **Major**: Performance issues, significant readability problems
- **Minor**: Style inconsistencies, minor optimizations

## 🎯 How It Works

### 1. PR Data Acquisition
- Fetches PR information using GitHub API
- Retrieves diff content showing added/removed/modified lines
- Extracts file paths, line numbers, and change context

### 2. Diff Parsing & Analysis
- Parses unified diff format
- Identifies code blocks and change regions
- Maintains context of surrounding code for better understanding

### 3. Multi-Agent Review Pipeline
Each specialized agent independently analyzes the changes:

**Logic Agent**:
- Validates control flow and conditional logic
- Checks for potential null pointer exceptions
- Identifies unreachable code or logic errors

**Readability Agent**:
- Evaluates variable and function naming
- Checks code structure and organization
- Reviews comments and documentation quality

**Performance Agent**:
- Identifies inefficient algorithms
- Detects potential memory leaks
- Flags unnecessary computations or loops

**Security Agent**:
- Scans for common vulnerabilities (OWASP Top 10)
- Checks input validation and sanitization
- Reviews authentication and authorization logic

### 4. Comment Generation
- Aggregates findings from all agents
- Prioritizes issues by severity
- Formats output as structured review comments
- Provides line-specific feedback with suggestions

## 🛠️ Technologies Used

- **Lyzr AI Framework**: Multi-agent orchestration and task management
- **Python 3.8+**: Core programming language
- **GitHub API**: PR data fetching and integration
- **OpenAI GPT-4**: Large Language Model for intelligent analysis
- **PyGithub/requests**: GitHub API interaction
- **Streamlit**: Optional web interface
- **python-dotenv**: Environment configuration

## 📊 Supported Languages

The agent currently supports comprehensive review for:
- Python
- JavaScript/TypeScript
- Java
- C/C++
- Go
- Rust
- Ruby
- PHP

Additional languages can be configured by extending the agent prompts.

## 🔐 Security & Privacy

- GitHub tokens are stored securely in environment variables
- No code is stored permanently; analysis happens in memory
- Supports private repositories with proper authentication
- API keys are never logged or exposed

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m pytest tests/

# Test specific agent
python -m pytest tests/test_agents.py -k security

# Test with sample diffs
python app.py --diff-file tests/sample_diffs/test_pr.patch
```

## 🚧 Limitations & Future Enhancements

### Current Limitations
- Requires external LLM API (OpenAI, Anthropic, etc.)
- Review quality depends on LLM understanding
- May not catch all edge cases in complex codebases
- Limited context window for very large PRs

### Planned Enhancements
- [ ] Support for custom review rules and policies
- [ ] Integration with CI/CD pipelines
- [ ] Automated comment posting directly to GitHub PRs
- [ ] Historical analysis and improvement tracking
- [ ] Support for more programming languages
- [ ] Custom agent training on project-specific patterns
- [ ] Batch processing for multiple PRs
- [ ] Integration with issue trackers

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-enhancement
   ```
3. **Make your changes**
   - Add tests for new functionality
   - Update documentation as needed
4. **Commit your changes**
   ```bash
   git commit -m 'Add amazing enhancement'
   ```
5. **Push to your fork**
   ```bash
   git push origin feature/amazing-enhancement
   ```
6. **Open a Pull Request**

Please ensure your code follows the project's style guidelines and includes appropriate tests.

## 📄 License

This project is created as part of a Lyzr AI assignment and is available for educational purposes.

## 🙏 Acknowledgments

- **Lyzr AI** for the powerful agent orchestration framework
- **GitHub** for providing comprehensive API access
- **OpenAI** for GPT models enabling intelligent code analysis
- The open-source community for inspiration and best practices

## 📚 Resources & References

- [Lyzr Documentation](https://docs.lyzr.ai/)
- [Lyzr Agent Studio](https://agent.studio/)
- [GitHub REST API Documentation](https://docs.github.com/en/rest)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Code Review Best Practices](https://google.github.io/eng-practices/review/)

## 📧 Contact

**Repository**: [Lyzr-AI-Assignment](https://github.com/Void-Anvesha/Lyzr-AI-Assignment)

For questions, feedback, or collaboration:
- Open an [issue](https://github.com/Void-Anvesha/Lyzr-AI-Assignment/issues)
- Submit a [pull request](https://github.com/Void-Anvesha/Lyzr-AI-Assignment/pulls)

---

**Built with ❤️ using Lyzr AI Framework | Automated Code Review for Better Software Quality**
