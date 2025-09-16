import reflex as rx


def service_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, class_name="h-8 w-8 text-blue-700"),
        rx.el.h3(title, class_name="text-xl font-bold"),
        rx.el.p(description, class_name="text-gray-500"),
        class_name="flex flex-col items-center justify-center space-y-4 rounded-lg bg-white p-6 text-center border border-gray-200 shadow-sm",
    )


def services() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Our services",
                    class_name="text-3xl font-bold tracking-tighter sm:text-5xl text-blue-900",
                ),
                rx.el.p(
                    "We offer a wide range of services to meet your needs.",
                    class_name="max-w-[900px] text-gray-700 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed",
                ),
                class_name="space-y-4 px-4 md:px-6",
            ),
            rx.el.div(
                service_card(
                    "code",
                    "Web Development",
                    "We build modern and responsive websites.",
                ),
                service_card(
                    "pen-tool",
                    "Graphic design",
                    "We create attractive and functional designs.",
                ),
                service_card(
                    "bar-chart", "Digital Marketing", "We help you reach your audience."
                ),
                class_name="mx-auto grid max-w-5xl items-center gap-6 py-12 lg:grid-cols-3 lg:gap-12",
            ),
            class_name="container mx-auto text-center",
        ),
        id="services",
        class_name="w-full py-12 md:py-24 lg:py-32 bg-blue-50",
    )