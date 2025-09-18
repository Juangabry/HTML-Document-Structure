import reflex as rx
from app.components.sign_up_card import sign_up_card
from app.components.virtual_assistant import virtual_assistant


def sign_up():
    return rx.el.div(
        sign_up_card(),
        virtual_assistant(),
        class_name="flex flex-col items-center justify-center h-screen bg-gray-100",
    )