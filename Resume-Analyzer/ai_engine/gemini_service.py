import google.generativeai as genai
import os
import json
import logging

class GeminiService:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("Gemini API key is required.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def get_resume_feedback(self, resume_text):
        """Generates detailed feedback and suggestions for the resume."""
        prompt = f"""
        Analyze the following resume text and provide feedback in JSON format.
        The JSON should have three keys: 
        1. 'suggestions': A list of actionable points to improve the resume.
        2. 'suitability': A short paragraph about the overall profile quality.
        3. 'quantification_tips': Specific advice on how to add numbers/results to their experience.

        Resume Text:
        {resume_text}
        
        Strictly return ONLY JSON.
        """
        try:
            response = self.model.generate_content(prompt)
            # Find and extract JSON from response (sometimes Gemini adds markdown backticks)
            text = response.text
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            elif "```" in text:
                text = text.split("```")[1].split("```")[0].strip()
            
            return json.loads(text)
        except Exception as e:
            logging.error(f"Gemini API error (Feedback): {e}")
            return {
                "suggestions": ["Could not generate AI suggestions at this time."],
                "suitability": "AI analysis unavailable.",
                "quantification_tips": "N/A"
            }

    def get_semantic_match(self, resume_text, job_desc):
        """Calculates a semantic match score between resume and job description."""
        if not job_desc or len(job_desc.strip()) < 10:
            return 0.0
            
        prompt = f"""
        Compare the following Resume and Job Description.
        Provide a match score between 0 and 100 based on how well the candidate fits the role.
        
        Return ONLY a number as your response.
        
        Resume:
        {resume_text}
        
        Job Description:
        {job_desc}
        """
        try:
            response = self.model.generate_content(prompt)
            score_text = response.text.strip()
            # Extract digits only in case of verbose output
            import re
            match = re.search(r'\d+', score_text)
            if match:
                return float(match.group())
            return 0.0
        except Exception as e:
            logging.error(f"Gemini API error (Match): {e}")
            return 0.0
