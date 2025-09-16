import reflex as rx
from app.states.auth_state import AuthState


def member_space() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Welcome to the Members Area!",
                class_name="text-4xl font-bold text-blue-900",
            ),
            rx.el.p(
                "Thank you for subscribing. Here you will find exclusive content.",
                class_name="mt-4 text-lg text-gray-700",
            ),
            rx.el.div(
                rx.el.a(
                    "Go to Analysis",
                    href="/analysis",
                    class_name="mt-8 inline-block bg-green-500 text-white py-2 px-4 rounded-md hover:bg-green-600 transition-colors",
                ),
                rx.el.a(
                    "Go back to Home",
                    href="/",
                    class_name="mt-8 inline-block bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 transition-colors",
                ),
                class_name="flex gap-4",
            ),
            class_name="text-center bg-white p-12 rounded-lg shadow-md border border-gray-200",
        ),
        class_name="min-h-screen bg-gray-100 flex items-center justify-center font-['Inter']",
    )