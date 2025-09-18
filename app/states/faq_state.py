import reflex as rx
from typing import Optional


class FaqState(rx.State):
    faqs: list[dict[str, str]] = [
        {
            "question": "What is Bateria Psico?",
            "answer": "Bateria Psico is a comprehensive suite of psychological assessment and analysis tools designed for professionals. It helps in evaluating cognitive functions, personality traits, and more.",
        },
        {
            "question": "Who can use this platform?",
            "answer": "Our platform is designed for psychologists, therapists, researchers, and HR professionals who require reliable tools for assessment and data analysis.",
        },
        {
            "question": "Is my data secure?",
            "answer": "Yes, data security is our top priority. We use end-to-end encryption and comply with all relevant data protection regulations to ensure your and your clients' information is safe.",
        },
        {
            "question": "What subscription plans are available?",
            "answer": "We offer multiple subscription tiers, including Basic, Medium, and Complete plans, to cater to different needs and budgets. You can find more details on our pricing page.",
        },
        {
            "question": "Can I integrate this with other software?",
            "answer": "We are constantly working on expanding our integration capabilities. Please contact our support team to discuss your specific integration needs.",
        },
    ]
    open_question_index: Optional[int] = None

    @rx.event
    def toggle_question(self, index: int):
        if self.open_question_index == index:
            self.open_question_index = None
        else:
            self.open_question_index = index