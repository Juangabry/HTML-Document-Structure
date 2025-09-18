import reflex as rx
from app.states.testimonials_state import TestimonialsState


def testimonial_card() -> rx.Component:
    return rx.el.figure(
        rx.el.blockquote(
            rx.el.p(
                f'''"{TestimonialsState.current_testimonial['quote']}"''',
                class_name="text-2xl font-semibold italic text-gray-900",
            ),
            class_name="border-l-4 border-blue-500 pl-6",
        ),
        rx.el.figcaption(
            rx.el.div(
                rx.el.img(
                    src=TestimonialsState.current_testimonial["avatar"],
                    alt=TestimonialsState.current_testimonial["author"],
                    class_name="w-14 h-14 rounded-full",
                ),
                rx.el.div(
                    rx.el.div(
                        TestimonialsState.current_testimonial["author"],
                        class_name="font-bold text-gray-900",
                    ),
                    rx.el.div(
                        TestimonialsState.current_testimonial["role"],
                        class_name="text-gray-500",
                    ),
                ),
            ),
            class_name="mt-6 flex items-center gap-4",
        ),
        class_name="max-w-4xl mx-auto",
    )


def testimonials() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "What Our Clients Say",
                class_name="text-3xl font-bold tracking-tighter sm:text-5xl text-blue-900 text-center",
            ),
            rx.el.p(
                "Hear from professionals who have transformed their work with our platform.",
                class_name="max-w-[900px] text-gray-700 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed text-center mx-auto mt-4",
            ),
            rx.el.div(testimonial_card(), class_name="mt-12 relative"),
            rx.el.div(
                rx.el.button(
                    rx.icon("arrow-left", class_name="w-6 h-6"),
                    on_click=TestimonialsState.prev_testimonial,
                    class_name="p-3 rounded-full bg-white/80 hover:bg-white shadow-md border transition-colors",
                ),
                rx.el.button(
                    rx.icon("arrow-right", class_name="w-6 h-6"),
                    on_click=TestimonialsState.next_testimonial,
                    class_name="p-3 rounded-full bg-white/80 hover:bg-white shadow-md border transition-colors",
                ),
                class_name="flex justify-center gap-4 mt-8",
            ),
            class_name="container mx-auto px-4 md:px-6",
        ),
        class_name="w-full py-12 md:py-24 lg:py-32 bg-white",
    )