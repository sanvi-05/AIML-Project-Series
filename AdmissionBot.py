# -*- coding: utf-8 -*-
"""
Created on Thu May  2 19:01:44 2024

@author: Sanvi
"""

class AdmissionBot:
    def __init__(self):
        self.context = {}

    def handle_question(self, question):
        response = ""
        if "requirements" in question:
            response = "To apply, you'll need to submit your high school transcripts, standardized test scores, letters of recommendation, and a personal statement."
        elif "deadline" in question:
            response = "The application deadline for the upcoming semester is July 15th."
        elif "submit" in question or "application" in question:
            response = "You can submit your application online through our admissions portal on our website."
        elif "GPA" in question or "test score" in question:
            response = "While we don't have strict cutoffs, competitive applicants typically have a GPA above 3.0 and SAT/ACT scores above the national average."
        elif "scholarships" in question:
            response = "Yes, we offer merit-based scholarships for incoming students. You can find more information on our website or contact our financial aid office."
        elif "transfer student" in question:
            response = "Yes, we accept transfer students. You'll need to submit your college transcripts and follow our transfer admission process."
        else:
            response = "I'm sorry, I couldn't understand your question. Could you please rephrase or ask something else?"
        return response

    def chat(self):
        print("Welcome to the Admission Q&A Bot. How can I assist you today?")
        while True:
            user_input = input("> ").lower()
            if user_input == "exit":
                print("Thank you for using the Admission Q&A Bot. Goodbye!")
                break
            response = self.handle_question(user_input)
            print(response)


if __name__ == "__main__":
    bot = AdmissionBot()
    bot.chat()