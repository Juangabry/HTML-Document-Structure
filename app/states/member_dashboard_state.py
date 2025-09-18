import reflex as rx
from typing import TypedDict, Optional


class MemberDashboardState(rx.State):
    active_view: str = "analysis"
    show_sidebar: bool = False

    @rx.event
    def set_active_view(self, view: str):
        self.active_view = view
        self.show_sidebar = False

    @rx.event
    def toggle_sidebar(self):
        self.show_sidebar = not self.show_sidebar

    @rx.event
    async def handle_survey_submit(self, form_data: dict):
        from app.states.analysis_state import AnalysisState

        analysis_state = await self.get_state(AnalysisState)
        analysis_state.update_data_from_form(form_data)
        yield rx.toast.success(
            "Encuesta enviada con éxito! Los análisis han sido actualizados."
        )
        self.active_view = "analysis"