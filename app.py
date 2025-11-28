import streamlit as st
import os
from github_client import parse_pr_url, get_pr_details, get_pr_diff
from diff_parser import parse_diff
from agent import analyze_pr
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(page_title="PR Review Agent", page_icon="🤖", layout="wide")

st.title("🤖 Automated Pull Request Review Agent")
st.markdown("Enter a GitHub Pull Request URL to get an AI-powered code review.")

# Sidebar for API Keys
with st.sidebar:
    st.header("Configuration")
    gemini_api_key = st.text_input("Gemini API Key", type="password", value=os.getenv("GEMINI_API_KEY", ""))
    github_token = st.text_input("GitHub Token (Optional)", type="password", help="Required for private repos or to avoid rate limits.")
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("This agent uses LangChain and Gemini to analyze code changes in a GitHub PR.")

# Main Input
pr_url = st.text_input("GitHub PR URL", placeholder="https://github.com/owner/strerepo/pull/123")

if st.button("Analyze PR", type="primary"):
    if not pr_url:
        st.warning("Please enter a PR URL.")
    elif not gemini_api_key:
        st.error("Please provide a Gemini API Key.")
    else:
        owner, repo, number = parse_pr_url(pr_url)
        
        if not owner or not repo or not number:
            st.error("Invalid GitHub PR URL. Please ensure it follows the format: https://github.com/owner/repo/pull/NUMBER")
        else:
            try:
                with st.spinner("Fetching PR details..."):
                    details = get_pr_details(owner, repo, number, github_token)
                    st.success(f"Loaded PR: {details['title']}")
                    
                    with st.expander("PR Description"):
                        st.markdown(details['body'] or "No description provided.")
                
                with st.spinner("Fetching and parsing diff..."):
                    diff_text = get_pr_diff(owner, repo, number, github_token)
                    diff_data = parse_diff(diff_text)
                    st.info(f"Found {len(diff_data)} changed files.")
                    
                with st.spinner("Analyzing code changes with AI..."):
                    review = analyze_pr(diff_data, gemini_api_key)
                
                st.markdown("## 📋 AI Review")
                st.markdown(review)
                
                st.markdown("---")
                st.markdown("### Changed Files")
                for file in diff_data:
                    with st.expander(f"📄 {file['filename']}"):
                        st.code(file['patch'], language='diff')
                        
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
