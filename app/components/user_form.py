import reflex as rx
from app.states.member_dashboard_state import MemberDashboardState


def user_form() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "User Information Form",
            class_name="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl md:text-5xl",
        ),
        rx.el.p(
            "Please fill out the form below.",
            class_name="mt-4 max-w-2xl text-lg text-gray-600",
        ),
        rx.el.form(
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "First Name", class_name="text-base font-medium leading-none"
                    ),
                    rx.el.input(
                        type="text",
                        name="first_name",
                        placeholder="John",
                        required=True,
                        class_name="flex h-12 w-full rounded-lg border border-input bg-background px-4 py-3 text-base ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50",
                    ),
                    class_name="space-y-2",
                ),
                rx.el.div(
                    rx.el.label(
                        "Last Name", class_name="text-base font-medium leading-none"
                    ),
                    rx.el.input(
                        type="text",
                        name="last_name",
                        placeholder="Doe",
                        required=True,
                        class_name="flex h-12 w-full rounded-lg border border-input bg-background px-4 py-3 text-base ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50",
                    ),
                    class_name="space-y-2",
                ),
                class_name="grid grid-cols-1 gap-6 md:grid-cols-2",
            ),
            rx.el.div(
                rx.el.label("Message", class_name="text-base font-medium leading-none"),
                rx.el.textarea(
                    name="message",
                    placeholder="Your message here...",
                    required=True,
                    rows=6,
                    class_name="flex min-h-[120px] w-full rounded-lg border border-input bg-background px-4 py-3 text-base ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50",
                ),
                class_name="space-y-2",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.input(
                        type="checkbox",
                        name="accepted_terms",
                        default_checked=MemberDashboardState.accepted_terms,
                        class_name="h-5 w-5 rounded border-gray-300 text-blue-600 focus:ring-blue-600",
                    ),
                    rx.el.label(
                        "I accept the ",
                        rx.el.a(
                            "Terms of Service",
                            href="#",
                            class_name="font-semibold text-blue-600 hover:underline",
                        ),
                        " and ",
                        rx.el.a(
                            "Privacy Policy",
                            href="#",
                            class_name="font-semibold text-blue-600 hover:underline",
                        ),
                        ".",
                        class_name="ml-3 block text-base text-gray-900",
                    ),
                    class_name="flex items-center",
                )
            ),
            rx.el.button(
                "Submit",
                type="submit",
                class_name="inline-flex items-center justify-center whitespace-nowrap rounded-lg text-base font-semibold ring-offset-background transition-transform transform hover:scale-105 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-blue-600 text-white hover:bg-blue-700 h-12 px-8 py-3 w-full md:w-auto shadow-lg",
            ),
            class_name="space-y-8",
            on_submit=MemberDashboardState.handle_form_submit,
            reset_on_submit=True,
        ),
        class_name="w-full max-w-5xl mx-auto p-6 sm:p-8 md:p-10 bg-white rounded-xl shadow-lg border border-gray-200 mt-8",
    )