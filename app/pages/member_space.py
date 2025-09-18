import reflex as rx
from app.states.auth_state import AuthState
from app.components.sidebar import sidebar
from app.components.analysis_dashboard import analysis_dashboard
from app.components.user_form import user_form
from app.states.member_dashboard_state import MemberDashboardState


def member_space() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.main(
            rx.match(
                MemberDashboardState.active_view,
                ("analysis", analysis_dashboard()),
                ("form", user_form()),
                analysis_dashboard(),
            ),
            class_name="flex-1 p-4 sm:p-6 lg:p-8 overflow-y-auto",
        ),
        class_name="flex min-h-screen bg-gray-50 font-['Inter']",
    )