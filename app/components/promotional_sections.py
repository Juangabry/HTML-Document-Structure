import reflex as rx


def promotional_sections() -> rx.Component:
    return rx.el.div(
        rx.el.section(
            rx.el.div(
                rx.el.img(
                    src="/compelling_related_productivity.png",
                    class_name="mx-auto aspect-video overflow-hidden rounded-xl object-cover object-center sm:w-full lg:order-last",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Boost Your Productivity",
                        class_name="text-3xl font-bold tracking-tighter sm:text-5xl text-blue-900",
                    ),
                    rx.el.p(
                        "Our services are designed to help you and your team work more efficiently and achieve your goals faster.",
                        class_name="max-w-[600px] text-gray-700 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed",
                    ),
                    rx.el.a(
                        "Learn More",
                        href="#services",
                        class_name="inline-flex h-12 items-center justify-center rounded-lg bg-blue-500 px-8 text-base font-semibold text-white shadow-lg transition-all duration-300 hover:bg-blue-600 hover:scale-105 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-700 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
                    ),
                    class_name="flex flex-col justify-center space-y-4",
                ),
                class_name="mx-auto grid max-w-7xl gap-6 py-12 px-4 md:px-6 lg:grid-cols-2 lg:gap-12",
            )
        ),
        rx.el.section(
            rx.el.div(
                rx.el.img(
                    src="/dynamic_vibrant_representing.png",
                    class_name="mx-auto aspect-video overflow-hidden rounded-xl object-cover object-center sm:w-full",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Unlock Premium Features",
                        class_name="text-3xl font-bold tracking-tighter sm:text-5xl text-blue-900",
                    ),
                    rx.el.p(
                        "Subscribe to our premium plans to get access to exclusive features and dedicated support.",
                        class_name="max-w-[600px] text-gray-700 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed",
                    ),
                    rx.el.a(
                        "View Pricing",
                        href="#subscriptions",
                        class_name="inline-flex h-12 items-center justify-center rounded-lg bg-blue-500 px-8 text-base font-semibold text-white shadow-lg transition-all duration-300 hover:bg-blue-600 hover:scale-105 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-700 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
                    ),
                    class_name="flex flex-col justify-center space-y-4",
                ),
                class_name="mx-auto grid max-w-7xl gap-6 py-12 px-4 md:px-6 lg:grid-cols-2 lg:gap-12",
            )
        ),
        class_name="bg-white",
    )