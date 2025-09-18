import reflex as rx
from app.states.faq_state import FaqState


def faq_item(item: dict, index: int) -> rx.Component:
    is_open = FaqState.open_question_index == index
    return rx.el.div(
        rx.el.dt(
            rx.el.button(
                rx.el.span(item["question"], class_name="text-left font-medium"),
                rx.icon(
                    tag="chevron-down",
                    class_name=rx.cond(
                        is_open,
                        "w-5 h-5 transform rotate-180 transition-transform",
                        "w-5 h-5 transition-transform",
                    ),
                ),
                on_click=lambda: FaqState.toggle_question(index),
                class_name="flex w-full items-start justify-between text-left text-gray-900",
            )
        ),
        rx.cond(
            is_open,
            rx.el.dd(
                rx.el.p(item["answer"], class_name="text-base leading-7 text-gray-600"),
                class_name="mt-2 pr-12",
            ),
            rx.fragment(),
        ),
        class_name="border-b border-gray-200 py-6",
    )


def faq() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Frequently Asked Questions",
                class_name="text-3xl font-bold tracking-tighter sm:text-5xl text-blue-900 text-center",
            ),
            rx.el.p(
                "Find answers to common questions about our platform and services.",
                class_name="max-w-[900px] text-gray-700 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed text-center mx-auto mt-4",
            ),
            rx.el.div(
                rx.el.dl(
                    rx.foreach(FaqState.faqs, faq_item),
                    class_name="space-y-6 divide-y divide-gray-900/10",
                ),
                class_name="mt-12 max-w-4xl mx-auto",
            ),
            class_name="container mx-auto px-4 md:px-6",
        ),
        class_name="w-full py-12 md:py-24 lg:py-32 bg-blue-50",
    )