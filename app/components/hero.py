import reflex as rx


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h1(
                "BATERIA PSICO",
                class_name="text-5xl md:text-7xl lg:text-8xl font-extrabold text-white tracking-tighter",
            ),
            class_name="container mx-auto px-4 md:px-6 flex items-center justify-center text-center",
        ),
        class_name="w-full h-screen bg-cover bg-center bg-no-repeat flex items-center",
        style={"background_image": "url(/y_una_imagen.png)"},
    )