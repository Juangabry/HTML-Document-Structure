import reflex as rx
from app.states.auth_state import AuthState


def payment_form() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Payment Details", class_name="text-2xl font-bold mb-6 text-center"),
        rx.el.form(
            rx.el.div(
                rx.el.label(
                    "Card Number", class_name="block text-sm font-medium text-gray-700"
                ),
                rx.el.input(
                    placeholder="0000 0000 0000 0000",
                    class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Expiry Date",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        placeholder="MM/YY",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="w-1/2 pr-2",
                ),
                rx.el.div(
                    rx.el.label(
                        "CVC", class_name="block text-sm font-medium text-gray-700"
                    ),
                    rx.el.input(
                        placeholder="123",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="w-1/2 pl-2",
                ),
                class_name="flex mb-6",
            ),
            rx.el.button(
                "Pay Now",
                class_name="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 transition-colors",
                on_click=AuthState.subscribe,
            ),
        ),
        class_name="max-w-md mx-auto bg-white p-8 rounded-lg shadow-md border border-gray-200",
    )


def payment() -> rx.Component:
    return rx.el.div(
        payment_form(),
        class_name="min-h-screen bg-gray-100 flex items-center justify-center",
    )