import reflex as rx


def tutorial_card(title: str, description: str, video_src: str) -> rx.Component:
    return rx.el.div(
        rx.el.h3(title, class_name="text-2xl font-bold text-gray-800 mb-2"),
        rx.el.p(description, class_name="text-gray-600 mb-4"),
        rx.el.div(
            rx.el.iframe(
                src=video_src,
                frame_border="0",
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture",
                allow_full_screen=True,
                class_name="w-full h-full",
            ),
            class_name="aspect-video bg-gray-200 rounded-lg overflow-hidden",
        ),
        class_name="bg-white p-6 rounded-lg shadow-md border border-gray-200",
    )


def tutorial_section() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Tutorials", class_name="text-4xl font-bold text-center text-gray-900 mb-10"
        ),
        rx.el.div(
            tutorial_card(
                "Getting Started",
                "Learn the basics of our platform and how to get started.",
                "https://www.youtube.com/embed/dQw4w9WgXcQ",
            ),
            tutorial_card(
                "Advanced Features",
                "Discover the advanced features and unlock the full potential.",
                "https://www.youtube.com/embed/dQw4w9WgXcQ",
            ),
            tutorial_card(
                "Tips and Tricks",
                "Get the most out of our platform with these tips and tricks.",
                "https://www.youtube.com/embed/dQw4w9WgXcQ",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8",
        ),
        class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
    )