import reflex as rx
from reflex_google_auth import GoogleAuthState


class AuthState(GoogleAuthState):
    users: dict[str, dict[str, str | bool]] = {
        "admin@reflex.com": {"password": "password123", "subscribed": False}
    }
    in_session: bool = False
    current_user_email: str = ""

    @rx.event
    def sign_up(self, form_data: dict):
        if form_data["email"] in self.users:
            yield rx.toast.error("Email already in use")
        else:
            self.users[form_data["email"]] = {
                "password": form_data["password"],
                "subscribed": False,
            }
            self.in_session = True
            self.current_user_email = form_data["email"]
            return rx.redirect("/")

    @rx.event
    def sign_in(self, form_data: dict):
        user_data = self.users.get(form_data["email"])
        if user_data and user_data["password"] == form_data["password"]:
            self.in_session = True
            self.current_user_email = form_data["email"]
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

    @rx.var
    def is_subscribed(self) -> bool:
        if self.in_session and self.current_user_email:
            user = self.users.get(self.current_user_email)
            if user:
                return user.get("subscribed", False)
        return False

    @rx.event
    def subscribe(self):
        if self.in_session and self.current_user_email:
            self.users[self.current_user_email]["subscribed"] = True
            return rx.redirect("/member-space")
        else:
            return rx.redirect("/sign-in")

    @rx.event
    def check_subscription(self):
        if not self.in_session:
            return rx.redirect("/sign-in")
        if not self.is_subscribed:
            yield rx.toast.error("You need a subscription to access this page.")
            return rx.redirect("/payment")