import reflex as rx
from reflex_google_auth import GoogleAuthState


class AuthState(GoogleAuthState):
    users: dict = {"admin@reflex.com": "password123"}
    in_session: bool = False

    @rx.event
    def sign_up(self, form_data: dict):
        if form_data["email"] in self.users:
            yield rx.toast.error("Email already in use")
        else:
            self.users[form_data["email"]] = form_data["password"]
            self.in_session = True
            return rx.redirect("/")

    @rx.event
    def sign_in(self, form_data: dict):
        if (
            form_data["email"] in self.users
            and self.users[form_data["email"]] == form_data["password"]
        ):
            self.in_session = True
            return rx.redirect("/")
        else:
            self.in_session = False
            yield rx.toast.error("Invalid email or password")

    @rx.event
    def sign_out(self):
        self.in_session = False
        return rx.redirect("/sign-in")

    @rx.event
    def check_session(self):
        if self.in_session:
            return
        else:
            return rx.redirect("/sign-in")