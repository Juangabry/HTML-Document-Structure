import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.p(
                "© 2024 Your Company, Inc. All rights reserved.",
                class_name="text-xs text-gray-300",
            ),
            rx.el.nav(
                rx.el.a(
                    "Terms of Service",
                    href="#",
                    class_name="text-xs text-gray-300 hover:text-white hover:underline underline-offset-4",
                ),
                rx.el.a(
                    "Privacy",
                    href="#",
                    class_name="text-xs text-gray-300 hover:text-white hover:underline underline-offset-4",
                ),
                class_name="flex gap-4 sm:ml-auto",
            ),
            class_name="container mx-auto flex flex-col gap-2 sm:flex-row py-6 w-full shrink-0 items-center px-4 md:px-6",
        ),
        id="contact",
        class_name="bg-blue-900 text-white",
    )