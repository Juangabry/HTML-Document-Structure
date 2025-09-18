import reflex as rx
from app.states.member_dashboard_state import MemberDashboardState
from app.states.auth_state import AuthState


def sidebar_link(text: str, icon_name: str, view: str) -> rx.Component:
    is_active = MemberDashboardState.active_view == view
    return rx.el.li(
        rx.el.a(
            rx.icon(icon_name, class_name="h-5 w-5"),
            rx.el.span(text, class_name="ml-3"),
            on_click=lambda: MemberDashboardState.set_active_view(view),
            class_name=rx.cond(
                is_active,
                "flex items-center p-2 text-gray-900 rounded-lg bg-blue-100 font-semibold",
                "flex items-center p-2 text-gray-900 rounded-lg hover:bg-gray-100",
            ),
            href="#",
        )
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.a(
                rx.icon("layout-dashboard", class_name="h-8 w-8 text-blue-900"),
                rx.el.span(
                    "Member Area",
                    class_name="ml-3 text-xl font-bold text-blue-900 tracking-wide",
                ),
                href="/",
                class_name="flex items-center mb-6 p-2",
            ),
            rx.el.ul(
                sidebar_link("Analysis", "bar-chart-2", "analysis"),
                sidebar_link("User Form", "file-text", "form"),
                sidebar_link("Tutorial", "book-open", "tutorial"),
                class_name="space-y-2 font-medium",
            ),
            class_name="flex-1",
        ),
        rx.el.div(
            rx.el.a(
                rx.icon("log-out", class_name="h-5 w-5"),
                rx.el.span("Sign Out", class_name="ml-3"),
                on_click=AuthState.sign_out,
                class_name="flex items-center p-2 text-gray-900 rounded-lg hover:bg-red-100 hover:text-red-700",
                href="#",
            )
        ),
        class_name=rx.cond(
            MemberDashboardState.show_sidebar,
            "fixed z-40 top-0 left-0 flex flex-col w-64 h-screen px-4 py-8 bg-white border-r border-gray-200 transition-transform duration-300 transform md:sticky md:translate-x-0",
            "fixed z-40 top-0 left-0 flex flex-col w-64 h-screen px-4 py-8 bg-white border-r border-gray-200 transition-transform duration-300 transform -translate-x-full md:sticky md:translate-x-0",
        ),
    )