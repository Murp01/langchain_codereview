CODE_REVIEW_PROMPT = """You are a software engineer conducting a code review.
Analyze the following code for:
- Code readability and maintainability
- Performance improvements
- Security vulnerabilities
- Best practices in {language}

Provide suggestions in a structured format."""

def get_code_review_prompt(language):
    return CODE_REVIEW_PROMPT.format(language=language)