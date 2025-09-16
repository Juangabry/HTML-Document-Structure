import reflex as rx
from app.states.auth_state import AuthState


def member_space() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Welcome to the Member's Space!",
                class_name="text-4xl font-bold text-blue-900",
            ),
            rx.el.p(
                f"You are logged in as {AuthState.current_user_email}.",
                class_name="text-lg text-gray-700 mt-2",
            ),
            rx.el.p(
                "Here you can access exclusive content and features available only to our subscribed members.",
                class_name="mt-4 text-center max-w-2xl text-gray-600",
            ),
            rx.el.button(
                "Sign Out",
                on_click=AuthState.sign_out,
                class_name="mt-8 text-sm font-medium text-white bg-red-500 hover:bg-red-600 px-6 py-3 rounded-md transition-colors",
            ),
            class_name="text-center flex flex-col items-center justify-center p-8 bg-white rounded-lg shadow-md border border-gray-200",
        ),
        class_name="min-h-screen bg-gray-100 flex items-center justify-center font-['Inter']",
        on_mount=AuthState.check_subscription,
    )