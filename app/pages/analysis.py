import reflex as rx
from app.components.analysis_dashboard import analysis_dashboard
from app.states.auth_state import AuthState


def analysis() -> rx.Component:
    return rx.el.div(analysis_dashboard(), class_name="font-['Inter']")