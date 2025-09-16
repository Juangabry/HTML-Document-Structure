import reflex as rx
from app.states.header_state import HeaderState
from app.states.auth_state import AuthState


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.icon("mountain", class_name="h-6 w-6 text-white"),
                rx.el.span("Your Company", class_name="sr-only"),
                href="#",
                class_name="flex items-center gap-2",
            ),
            rx.el.nav(
                rx.el.a(
                    "About",
                    href="#about",
                    class_name="text-sm font-medium text-white hover:underline underline-offset-4",
                ),
                rx.el.a(
                    "Services",
                    href="#services",
                    class_name="text-sm font-medium text-white hover:underline underline-offset-4",
                ),
                rx.cond(
                    AuthState.is_subscribed,
                    rx.el.a(
                        "Members Area",
                        href="/member-space",
                        class_name="text-sm font-medium text-white hover:underline underline-offset-4",
                    ),
                    rx.fragment(""),
                ),
                rx.el.a(
                    "Contact",
                    href="#contact",
                    class_name="text-sm font-medium text-white hover:underline underline-offset-4",
                ),
                class_name="hidden md:flex flex-1 justify-center items-center gap-6 text-lg font-medium",
            ),
            rx.el.div(
                rx.cond(
                    AuthState.in_session,
                    rx.el.button(
                        "Sign Out",
                        on_click=AuthState.sign_out,
                        class_name="text-sm font-medium text-white hover:underline underline-offset-4",
                    ),
                    rx.el.div(
                        rx.el.a(
                            "Sign In",
                            href="/sign-in",
                            class_name="text-sm font-medium text-white hover:underline underline-offset-4",
                        ),
                        rx.el.a(
                            "Sign Up",
                            href="/sign-up",
                            class_name="text-sm font-medium text-white bg-blue-500 hover:bg-blue-600 px-4 py-2 rounded-md",
                        ),
                        class_name="flex items-center gap-4",
                    ),
                ),
                rx.el.button(
                    rx.icon("menu", class_name="h-6 w-6 text-white"),
                    class_name="md:hidden",
                    on_click=HeaderState.toggle_menu,
                ),
                class_name="flex items-center gap-4",
            ),
            class_name="container mx-auto flex h-16 items-center justify-between px-4 md:px-6",
        ),
        rx.cond(
            HeaderState.show_menu,
            rx.el.div(
                rx.el.a(
                    "About",
                    href="#about",
                    class_name="block py-2 px-4 text-sm text-white hover:bg-blue-800",
                    on_click=HeaderState.toggle_menu,
                ),
                rx.el.a(
                    "Services",
                    href="#services",
                    class_name="block py-2 px-4 text-sm text-white hover:bg-blue-800",
                    on_click=HeaderState.toggle_menu,
                ),
                rx.cond(
                    AuthState.is_subscribed,
                    rx.el.a(
                        "Members Area",
                        href="/member-space",
                        class_name="block py-2 px-4 text-sm text-white hover:bg-blue-800",
                        on_click=HeaderState.toggle_menu,
                    ),
                    rx.fragment(""),
                ),
                rx.el.a(
                    "Contact",
                    href="#contact",
                    class_name="block py-2 px-4 text-sm text-white hover:bg-blue-800",
                    on_click=HeaderState.toggle_menu,
                ),
                rx.el.a(
                    "Sign In",
                    href="/sign-in",
                    class_name="block py-2 px-4 text-sm text-white hover:bg-blue-800",
                    on_click=HeaderState.toggle_menu,
                ),
                rx.el.a(
                    "Sign Up",
                    href="/sign-up",
                    class_name="block py-2 px-4 text-sm text-white hover:bg-blue-800",
                    on_click=HeaderState.toggle_menu,
                ),
                class_name="md:hidden bg-gray-900/90 border-t border-gray-800",
            ),
        ),
        class_name="fixed top-0 z-50 w-full bg-black/50 backdrop-blur-sm",
    )