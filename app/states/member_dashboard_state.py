import reflex as rx
from typing import TypedDict, Optional


class MemberDashboardState(rx.State):
    active_view: str = "analysis"
    form_data: dict = {}
    accepted_terms: bool = False

    def set_active_view(self, view: str):
        self.active_view = view

    @rx.event
    def handle_form_submit(self, form_data: dict):
        self.accepted_terms = form_data.get("accepted_terms", False)
        if not self.accepted_terms:
            return rx.toast.error("You must accept the terms and privacy policy.")
        self.form_data = form_data
        return rx.toast.success("Form submitted successfully!")