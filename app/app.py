import reflex as rx
from app.components.header import header
from app.components.hero import hero
from app.components.about import about
from app.components.services import services
from app.components.promotional_sections import promotional_sections
from app.components.subscriptions import subscriptions
from app.components.footer import footer
from app.pages.sign_in import sign_in
from app.pages.sign_up import sign_up
from app.pages.payment import payment
from app.pages.member_space import member_space
from app.states.auth_state import AuthState


def index() -> rx.Component:
    """The main view of the app."""
    return rx.el.div(
        header(),
        hero(),
        about(),
        services(),
        promotional_sections(),
        subscriptions(),
        footer(),
        class_name="bg-gray-50 text-gray-900 font-['Inter']",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, title="Landing Page")
app.add_page(sign_in, route="/sign-in")
app.add_page(sign_up, route="/sign-up")
app.add_page(payment, route="/payment", on_load=AuthState.check_session)
app.add_page(
    member_space,
    route="/member-space",
    on_load=[AuthState.check_session, AuthState.check_subscription],
)