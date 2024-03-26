from flask import jsonify
from flask_smorest import Blueprint
from flask.views import MethodView


blp = Blueprint("Chapter Quiz", __name__, "For Geting ChapterQuiz")

JSONQUIZ  = [
    {
        "question" : "Your dog bites your neighbor and they need medical attention.Which of the following is covered by your property insurance?",
        "correct_answer" : "The cost of your neighbor's medical bills",
        "incorrect_answer1" : "The cost of a new fence to keep your dog in your yard",
        "incorrect_answer2" : "The cost of obedience training for your dog"
    },
    {
        "question" : "Protecting your personal identifiable information (PII) is important for preventing identity theft. There are many ways you can protect your PII, but it's important to know what steps you should take.",
        "correct_answer" : "write down all your passwords on a piece of paper and always carry it with you",
        "incorrect_answer1" : "Create strong, distinct passwords for each account",
        "incorrect_answer2" : "Use one password for all your online accounts"
    },
    {
        "question" : "Information on a W-2 can be grouped into two groups: sections (labeled a-f) and boxes",
        "correct_answer" : "The history of your previous jobs for the last 5 years",
        "incorrect_answer1" : "Your job title and job description",
        "incorrect_answer2" : "Your personal information and your employer's information"
    },
    {
        "question" : "Your dog bites your neighbor and they need medical attention.Which of the following is covered by your property insurance?",
        "correct_answer" : "the cost of your neighbor's medical bills",
        "incorrect_answer1" : "the cost of a new fence to keep your dog in your yard",
        "incorrect_answer2" : "the cost of obedience training for your dog"
    },
    {
        "question" : "Which of the following is an example of bad debt?",
        "correct_answer" : "Using a loan to buy a faster gaming laptop",
        "incorrect_answer1" : "Borrowing money to start your own business",
        "incorrect_answer2" : "Taking out a loan to pay for home improvements"
    },
    {
        "question" : "You are buying a house. The company lending you money wants to know if you want to buy insurance. If you die, this insurance will pay off your house for you. \n What is this type of insurance called?",
        "correct_answer" : "An extended warranty",
        "incorrect_answer1" : "debt cancellation coverage",
        "incorrect_answer2" : "A mortgage protection"
    },
    {
        "question" : "Short, medium, and long term goals are different types of financial goals that you set for yourself based on how much time, money, and risk you need to achieve them. \n What is an example of a short term goal?",
        "correct_answer" : "Paying off a car loan",
        "incorrect_answer1" : "Retiring",
        "incorrect_answer2" : "Saving for an emergency fund"
    },
]

@blp.route("/api/v1/finance/get_quiz_questions")
class ChapterQuiz(MethodView):
    def get(self):
        return jsonify({
            "data" : JSONQUIZ
        }), 200