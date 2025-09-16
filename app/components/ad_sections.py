import reflex as rx


def ad_section(
    title: str, text: str, image_src: str, reverse: bool = False
) -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.img(
                    src=image_src,
                    alt=title,
                    class_name="mx-auto aspect-video overflow-hidden rounded-xl object-cover object-center sm:w-full",
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.h2(
                    title,
                    class_name="text-3xl font-bold tracking-tighter sm:text-5xl text-blue-900",
                ),
                rx.el.p(
                    text,
                    class_name="max-w-[600px] text-gray-700 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed",
                ),
                class_name="flex flex-1 flex-col justify-center space-y-4",
            ),
            class_name=f"mx-auto grid max-w-7xl items-center gap-6 px-4 py-12 md:grid-cols-2 md:gap-12 md:px-6 lg:py-16 {('md:grid-flow-col-dense' if reverse else '')}",
        ),
        class_name="w-full",
    )


def ad_sections() -> rx.Component:
    return rx.el.div(
        ad_section(
            title="Unlock Your Potential with Our Advanced Tools",
            text="Our platform provides state-of-the-art tools designed to boost your productivity and streamline your workflow. Experience efficiency like never before.",
            image_src="/placeholder.svg",
            reverse=False,
        ),
        ad_section(
            title="Data-Driven Insights for Smarter Decisions",
            text="Leverage the power of data with our comprehensive analytics. Gain valuable insights to make informed decisions and drive your business forward.",
            image_src="/placeholder.svg",
            reverse=True,
        ),
        class_name="bg-white",
    )