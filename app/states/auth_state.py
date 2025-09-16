import reflex as rx
from reflex_google_auth import GoogleAuthState


class AuthState(GoogleAuthState):
    users: dict[str, dict[str, str | bool]] = {
        "admin@reflex.com": {"password": "password123", "subscribed": False}
    }
    in_session: bool = False
    current_user_email: str = ""

    @rx.var
    def is_subscribed(self) -> bool:
        if not self.in_session or not self.current_user_email:
            return False
        return self.users.get(self.current_user_email, {}).get("subscribed", False)

    @rx.event
    def sign_up(self, form_data: dict):
        email = form_data["email"]
        if email in self.users:
            yield rx.toast.error("Email already in use")
        else:
            self.users[email] = {"password": form_data["password"], "subscribed": False}
            self.in_session = True
            self.current_user_email = email
            return rx.redirect("/")

    @rx.event
    def sign_in(self, form_data: dict):
        email = form_data["email"]
        if (
            email in self.users
            and self.users[email]["password"] == form_data["password"]
        ):
            self.in_session = True
            self.current_user_email = email
            return rx.redirect("/")
        else:
            self.in_session = False
            yield rx.toast.error("Invalid email or password")

    @rx.event
    def sign_out(self):
        self.in_session = False
        self.current_user_email = ""
        return rx.redirect("/sign-in")

    @rx.event
    def check_session(self):
        if not self.in_session:
            return rx.redirect("/sign-in")

    @rx.event
    def handle_payment(self):
        if self.in_session and self.current_user_email:
            self.users[self.current_user_email]["subscribed"] = True
            yield rx.toast.success("Subscription successful! Welcome to the club.")
            return rx.redirect("/member-space")
        else:
            yield rx.toast.error("You must be logged in to subscribe.")
            return rx.redirect("/sign-in")

    @rx.event
    def check_subscription(self):
        if not self.in_session:
            return rx.redirect("/sign-in")
        if not self.is_subscribed:
            return rx.redirect("/")