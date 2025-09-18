import reflex as rx
from app.components.header import header
from app.components.footer import footer


def tutorial_content_card(
    title: str, video_url: str, description: list[str]
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.iframe(
                src=video_url,
                class_name="absolute top-0 left-0 w-full h-full",
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture",
                allowFullScreen=True,
            ),
            class_name="relative w-full overflow-hidden pt-[56.25%] rounded-xl",
        ),
        rx.el.div(
            rx.el.h3(title, class_name="text-2xl font-bold text-gray-900"),
            rx.el.div(
                *[rx.el.p(d, class_name="text-gray-700") for d in description],
                class_name="mt-4 space-y-2 text-base",
            ),
            class_name="mt-6",
        ),
        class_name="w-full max-w-4xl",
    )


def main_tutorial() -> rx.Component:
    return rx.el.div(
        header(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "Platform Tutorial",
                    class_name="text-4xl font-extrabold tracking-tight lg:text-5xl text-blue-900",
                ),
                rx.el.p(
                    "Welcome! This guide will walk you through the key features of our platform.",
                    class_name="mt-4 text-lg text-gray-600",
                ),
                class_name="text-center mb-16",
            ),
            rx.el.div(
                tutorial_content_card(
                    "1. Navigating the Dashboard",
                    "https://www.youtube.com/embed/dQw4w9WgXcQ",
                    [
                        "The main dashboard gives you an overview of all your projects and their current status.",
                        "Use the sidebar to navigate between different sections like Analysis, User Form, and other tutorials.",
                    ],
                ),
                tutorial_content_card(
                    "2. Using the Analysis Tools",
                    "https://www.youtube.com/embed/dQw4w9WgXcQ",
                    [
                        "In the Analysis section, you can select projects to view detailed task breakdowns and progress metrics.",
                        "Switch between Bar, Line, and Area charts to visualize data in different ways.",
                    ],
                ),
                tutorial_content_card(
                    "3. Submitting Information",
                    "https://www.youtube.com/embed/dQw4w9WgXcQ",
                    [
                        "The User Form section allows you to input and submit relevant information securely.",
                        "Ensure you accept the terms and conditions before submitting the form.",
                    ],
                ),
                class_name="flex flex-col items-center gap-16",
            ),
            class_name="container mx-auto max-w-7xl px-4 py-12 md:py-24",
        ),
        footer(),
        class_name="bg-gray-50 text-gray-900 font-['Inter']",
    )