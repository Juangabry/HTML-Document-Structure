import reflex as rx


def footer_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name="text-sm text-gray-300 hover:text-white hover:underline underline-offset-4 transition-colors",
    )


def social_link(icon: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.icon(
            icon, class_name="h-6 w-6 text-gray-300 hover:text-white transition-colors"
        ),
        href=href,
        target="_blank",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        rx.icon("brain-circuit", class_name="h-8 w-8 text-white"),
                        rx.el.span(
                            "Bateria psico", class_name="ml-2 text-xl font-bold"
                        ),
                        href="#",
                        class_name="flex items-center gap-2 mb-4",
                    ),
                    rx.el.p(
                        "Your trusted partner in success.",
                        class_name="text-sm text-gray-400 max-w-xs",
                    ),
                ),
                rx.el.div(
                    rx.el.h3(
                        "Quick Links",
                        class_name="text-base font-semibold text-white mb-4",
                    ),
                    rx.el.nav(
                        footer_link("About", "#about"),
                        footer_link("Services", "#services"),
                        footer_link("Pricing", "#subscriptions"),
                        footer_link("Contact", "#contact"),
                        class_name="flex flex-col gap-2",
                    ),
                ),
                rx.el.div(
                    rx.el.h3(
                        "Contact Us",
                        class_name="text-base font-semibold text-white mb-4",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.icon("map-pin", class_name="h-4 w-4 mr-2 text-gray-400"),
                            rx.el.p(
                                "123 Main St, Anytown, USA",
                                class_name="text-sm text-gray-300",
                            ),
                            class_name="flex items-center",
                        ),
                        rx.el.div(
                            rx.icon("phone", class_name="h-4 w-4 mr-2 text-gray-400"),
                            rx.el.p(
                                "(123) 456-7890", class_name="text-sm text-gray-300"
                            ),
                            class_name="flex items-center",
                        ),
                        rx.el.div(
                            rx.icon("mail", class_name="h-4 w-4 mr-2 text-gray-400"),
                            rx.el.p(
                                "info@yourcompany.com",
                                class_name="text-sm text-gray-300",
                            ),
                            class_name="flex items-center",
                        ),
                        class_name="flex flex-col gap-2",
                    ),
                ),
                rx.el.div(
                    rx.el.h3(
                        "Opening Hours",
                        class_name="text-base font-semibold text-white mb-4",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Monday - Friday: 9am - 6pm",
                            class_name="text-sm text-gray-300",
                        ),
                        rx.el.p(
                            "Saturday: 10am - 4pm", class_name="text-sm text-gray-300"
                        ),
                        rx.el.p("Sunday: Closed", class_name="text-sm text-gray-300"),
                        class_name="flex flex-col gap-1",
                    ),
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8",
            ),
            rx.el.div(class_name="border-t border-gray-700 my-8"),
            rx.el.div(
                rx.el.p(
                    "© 2024 Bateria psico, Inc. All rights reserved.",
                    class_name="text-sm text-gray-400",
                ),
                rx.el.div(
                    social_link("twitter", "#"),
                    social_link("facebook", "#"),
                    social_link("instagram", "#"),
                    social_link("linkedin", "#"),
                    class_name="flex gap-4 items-center",
                ),
                class_name="flex flex-col sm:flex-row justify-between items-center gap-4",
            ),
            class_name="container mx-auto px-4 md:px-6 py-8 md:py-12",
        ),
        id="contact",
        class_name="bg-blue-900 text-white",
    )