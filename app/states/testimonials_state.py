import reflex as rx
from typing import TypedDict


class Testimonial(TypedDict):
    quote: str
    author: str
    role: str
    avatar: str


class TestimonialsState(rx.State):
    testimonials: list[Testimonial] = [
        {
            "quote": "This platform has revolutionized our workflow. The analysis tools are top-notch and incredibly intuitive.",
            "author": "Jane Doe",
            "role": "CEO, Tech Solutions Inc.",
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=JaneDoe",
        },
        {
            "quote": "An indispensable tool for any data-driven team. The insights we've gained are invaluable.",
            "author": "John Smith",
            "role": "Data Scientist, QuantumLeap Analytics",
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=JohnSmith",
        },
        {
            "quote": "The user interface is clean, responsive, and a joy to use. Highly recommended for project management.",
            "author": "Emily White",
            "role": "Project Manager, Innovate Corp.",
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=EmilyWhite",
        },
    ]
    current_index: int = 0

    @rx.event
    def next_testimonial(self):
        self.current_index = (self.current_index + 1) % len(self.testimonials)

    @rx.event
    def prev_testimonial(self):
        self.current_index = (self.current_index - 1 + len(self.testimonials)) % len(
            self.testimonials
        )

    @rx.var
    def current_testimonial(self) -> Testimonial:
        return self.testimonials[self.current_index]