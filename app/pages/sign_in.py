import reflex as rx
from app.components.sign_in_card import sign_in_card
from app.components.virtual_assistant import virtual_assistant
from reflex_google_auth import google_oauth_provider


def sign_in():
    return google_oauth_provider(
        rx.el.div(
            sign_in_card(),
            virtual_assistant(),
            class_name="flex flex-col items-center justify-center h-screen bg-gray-100",
        )
    )