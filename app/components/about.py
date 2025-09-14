import reflex as rx


def about() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Know us",
                    class_name="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl text-blue-900",
                ),
                rx.el.p(
                    "We are a company dedicated to providing the best solutions for our clients. Our team is composed of experts in various fields, ready to tackle any challenge.",
                    class_name="mx-auto max-w-[700px] text-gray-700 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed",
                ),
                class_name="text-center space-y-4",
            ),
            class_name="container mx-auto px-4 md:px-6",
        ),
        id="about",
        class_name="w-full py-12 md:py-24 lg:py-32 bg-blue-50",
    )