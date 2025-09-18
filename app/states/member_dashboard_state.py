import reflex as rx
from typing import TypedDict, Optional


class MemberDashboardState(rx.State):
    active_view: str = "analysis"
    survey_data: dict = {}
    show_sidebar: bool = False

    @rx.event
    def set_active_view(self, view: str):
        self.active_view = view
        self.show_sidebar = False

    @rx.event
    def toggle_sidebar(self):
        self.show_sidebar = not self.show_sidebar

    @rx.event
    def handle_survey_submit(self, form_data: dict):
        self.survey_data = form_data
        yield rx.toast.success("Encuesta enviada con éxito!")
        self.active_view = "analysis"