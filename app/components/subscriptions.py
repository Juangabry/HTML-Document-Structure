import reflex as rx


def subscription_card(tier: str, price: str, features: list[str]) -> rx.Component:
    return rx.el.div(
        rx.el.h3(tier, class_name="text-2xl font-bold text-center"),
        rx.el.p(
            rx.el.span(f"${price}", class_name="text-4xl font-bold"),
            rx.el.span("/month", class_name="text-gray-500"),
            class_name="mt-4 text-center text-gray-900",
        ),
        rx.el.ul(
            *[
                rx.el.li(
                    rx.icon("check", class_name="text-green-500 mr-2"),
                    feature,
                    class_name="flex items-center",
                )
                for feature in features
            ],
            class_name="mt-8 space-y-4",
        ),
        rx.el.a(
            "Get Started",
            href="/payment",
            class_name="mt-8 block w-full text-center bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600",
        ),
        class_name="w-full max-w-sm p-8 bg-white rounded-lg shadow-md border border-gray-200",
    )


def subscriptions() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Pricing Plans",
                class_name="text-3xl font-bold tracking-tighter sm:text-5xl text-blue-900 text-center",
            ),
            rx.el.p(
                "Choose the plan that's right for you.",
                class_name="max-w-[900px] text-gray-700 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed text-center mx-auto",
            ),
            rx.el.div(
                subscription_card(
                    "Basic", "$10", ["Feature 1", "Feature 2", "Feature 3"]
                ),
                subscription_card(
                    "Medium",
                    "$20",
                    ["Feature 1", "Feature 2", "Feature 3", "Feature 4"],
                ),
                subscription_card(
                    "Complete",
                    "$30",
                    ["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5"],
                ),
                class_name="mt-12 grid gap-8 md:grid-cols-2 lg:grid-cols-3",
            ),
            class_name="container mx-auto px-4 md:px-6",
        ),
        id="subscriptions",
        class_name="w-full py-12 md:py-24 lg:py-32 bg-blue-50",
    )