import reflex as rx
from app.states.auth_state import AuthState
from app.components.sidebar import sidebar
from app.components.analysis_dashboard import analysis_dashboard
from app.components.user_form import user_form
from app.components.tutorial_section import tutorial_section
from app.components.virtual_assistant import virtual_assistant
from app.states.member_dashboard_state import MemberDashboardState


def member_header() -> rx.Component:
    return rx.el.header(
        rx.el.button(
            rx.icon("menu", class_name="h-6 w-6"),
            on_click=MemberDashboardState.toggle_sidebar,
            class_name="md:hidden p-2 rounded-md hover:bg-gray-200",
        ),
        rx.el.h1(
            MemberDashboardState.active_view.capitalize(),
            class_name="text-2xl font-bold text-gray-800",
        ),
        class_name="flex items-center gap-4 p-4 border-b bg-white sticky top-0 z-30",
    )


def member_space() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            member_header(),
            rx.el.main(
                rx.match(
                    MemberDashboardState.active_view,
                    ("analysis", analysis_dashboard()),
                    ("form", user_form()),
                    ("tutorial", tutorial_section()),
                    analysis_dashboard(),
                ),
                class_name="flex-1 p-4 sm:p-6 lg:p-8 overflow-y-auto",
            ),
            class_name="relative flex-1 flex flex-col",
        ),
        virtual_assistant(),
        class_name="flex min-h-screen bg-gray-50 font-['Inter']",
    )