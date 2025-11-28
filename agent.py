from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from prompts import PR_REVIEW_SYSTEM_PROMPT, PR_REVIEW_USER_PROMPT_TEMPLATE
import os

def analyze_pr(diff_data, gemini_api_key=None):
    """
    Analyzes the PR diff using LangChain and Gemini.
    """
    if not gemini_api_key:
        gemini_api_key = os.getenv("GEMINI_API_KEY")
    
    if not gemini_api_key:
        return "Error: Gemini API Key is missing. Please provide it in the sidebar or environment variables."

    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.2,
            google_api_key=gemini_api_key
        )
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", PR_REVIEW_SYSTEM_PROMPT),
            ("user", PR_REVIEW_USER_PROMPT_TEMPLATE)
        ])
        
        chain = prompt | llm | StrOutputParser()
        
        # Format the diff data for the prompt
        formatted_diff = ""
        for file in diff_data:
            formatted_diff += f"File: {file['filename']}\n"
            formatted_diff += f"Changes:\n{file['patch']}\n\n"
            
        response = chain.invoke({"diff_data": formatted_diff})
        return response
        
    except Exception as e:
        return f"Error during analysis: {str(e)}"
