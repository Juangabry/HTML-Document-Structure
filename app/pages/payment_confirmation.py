import reflex as rx
from app.states.auth_state import AuthState


def payment_confirmation() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("check_check", class_name="h-16 w-16 text-green-500 mx-auto"),
            rx.el.h1(
                "Payment Successful!",
                class_name="text-3xl font-bold text-center mt-4 text-gray-800",
            ),
            rx.el.p(
                "Thank you for your subscription. You now have access to the members area.",
                class_name="text-center mt-2 text-gray-600",
            ),
            rx.el.button(
                "Go to Members Area",
                on_click=AuthState.go_to_member_space,
                class_name="mt-8 w-full bg-blue-500 text-white py-3 rounded-lg hover:bg-blue-600 transition-all duration-300 transform hover:scale-105 shadow-lg",
            ),
            class_name="max-w-md mx-auto bg-white p-8 rounded-xl shadow-2xl border border-gray-100",
        ),
        class_name="min-h-screen bg-gray-50 flex items-center justify-center font-['Inter']",
    )