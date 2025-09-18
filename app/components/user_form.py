import reflex as rx
from app.states.member_dashboard_state import MemberDashboardState


def form_section(title: str, *children) -> rx.Component:
    return rx.el.fieldset(
        rx.el.legend(
            title,
            class_name="text-xl font-semibold text-gray-800 mb-4 border-b pb-2 w-full",
        ),
        rx.el.div(*children, class_name="grid grid-cols-1 md:grid-cols-2 gap-6"),
        class_name="space-y-6",
    )


def form_input(
    name: str, label: str, placeholder: str, type: str = "text", required: bool = True
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="text-base font-medium leading-none"),
        rx.el.input(
            type=type,
            name=name,
            placeholder=placeholder,
            required=required,
            class_name="flex h-11 w-full rounded-md border bg-transparent px-3 py-2 text-base shadow-sm transition-colors focus-visible:outline-none focus-visible:ring-1 md:text-sm font-medium",
        ),
        class_name="space-y-2",
    )


def form_select(name: str, label: str, options: list[str]) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="text-base font-medium leading-none"),
        rx.el.select(
            rx.foreach(
                options, lambda option: rx.el.option(option, value=option.lower())
            ),
            name=name,
            class_name="flex h-11 w-full rounded-md border bg-transparent px-3 py-2 text-base shadow-sm transition-colors focus-visible:outline-none focus-visible:ring-1 md:text-sm font-medium",
        ),
        class_name="space-y-2",
    )


def form_radio_group(name: str, legend: str, options: list[str]) -> rx.Component:
    return rx.el.fieldset(
        rx.el.legend(legend, class_name="text-base font-medium leading-none mb-2"),
        rx.el.div(
            rx.foreach(
                options,
                lambda option: rx.el.label(
                    rx.el.input(
                        type="radio", name=name, value=option.lower(), class_name="mr-2"
                    ),
                    option,
                    class_name="flex items-center",
                ),
            ),
            class_name="flex gap-4",
        ),
    )


def form_checkbox_group(legend: str, options: list[str]) -> rx.Component:
    return rx.el.fieldset(
        rx.el.legend(legend, class_name="text-base font-medium leading-none mb-2"),
        rx.el.div(
            rx.foreach(
                options,
                lambda option: rx.el.label(
                    rx.el.input(
                        type="checkbox",
                        name=f"substance_{option.lower()}",
                        class_name="mr-2",
                    ),
                    option,
                    class_name="flex items-center",
                ),
            ),
            class_name="grid grid-cols-2 md:grid-cols-3 gap-2",
        ),
    )


def user_form() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Encuesta de Consumo de Sustancias",
            class_name="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl",
        ),
        rx.el.p(
            "Por favor, complete el siguiente formulario con información veraz.",
            class_name="mt-3 max-w-2xl text-lg text-gray-600",
        ),
        rx.el.form(
            form_section(
                "Sección A: Datos Sociodemográficos",
                form_input("age", "Edad", "e.g., 30", type="number"),
                form_select("gender", "Sexo", ["Masculino", "Femenino", "Otro"]),
                form_select(
                    "marital_status",
                    "Estado Civil",
                    ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"],
                ),
                form_input(
                    "position", "Cargo/Área de Trabajo", "e.g., Ingeniero de Software"
                ),
                form_input(
                    "seniority",
                    "Antigüedad en la empresa (años)",
                    "e.g., 5",
                    type="number",
                ),
            ),
            form_section(
                "Sección B: Consumo de Sustancias",
                form_radio_group(
                    "has_consumed",
                    "¿Ha consumido alguna sustancia psicoactiva en los últimos 12 meses?",
                    ["Sí", "No"],
                ),
                form_checkbox_group(
                    "Sustancia(s) consumida(s)",
                    [
                        "Alcohol",
                        "Tabaco",
                        "Cannabis",
                        "Cocaína",
                        "Anfetaminas",
                        "Medicamentos sin prescripción",
                        "Otras",
                    ],
                ),
                form_input(
                    "age_of_first_use",
                    "Edad de inicio de consumo",
                    "e.g., 18",
                    type="number",
                    required=False,
                ),
                form_select(
                    "frequency",
                    "Frecuencia de Consumo",
                    ["Nunca", "Mensual", "Semanal", "Diaria"],
                ),
                form_input(
                    "quantity",
                    "Cantidad aproximada por consumo",
                    "e.g., 2 cervezas",
                    required=False,
                ),
            ),
            form_section(
                "Sección C: Contexto Laboral",
                form_radio_group(
                    "consumed_at_work",
                    "¿Ha consumido en el lugar de trabajo?",
                    ["Sí", "No"],
                ),
                form_radio_group(
                    "absenteeism",
                    "¿Ha presentado ausencias o bajo rendimiento por consumo?",
                    ["Sí", "No"],
                ),
                form_radio_group(
                    "conflicts",
                    "¿Ha tenido conflictos con compañeros o superiores relacionados con el consumo?",
                    ["Sí", "No"],
                ),
            ),
            form_section(
                "Sección D: Percepción y Riesgo",
                form_radio_group(
                    "affects_performance",
                    "¿Cree que su consumo afecta su desempeño laboral?",
                    ["Sí", "No"],
                ),
                form_radio_group(
                    "willing_to_participate",
                    "¿Estaría dispuesto a participar en programas de apoyo o prevención?",
                    ["Sí", "No"],
                ),
            ),
            rx.el.button(
                "Enviar Encuesta",
                type="submit",
                class_name="inline-flex items-center justify-center whitespace-nowrap rounded-lg text-base font-semibold ring-offset-background transition-transform transform hover:scale-105 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-blue-600 text-white hover:bg-blue-700 h-12 px-8 py-3 w-full md:w-auto shadow-lg mt-8",
            ),
            class_name="space-y-12 mt-8",
            on_submit=MemberDashboardState.handle_survey_submit,
            reset_on_submit=True,
        ),
        class_name="w-full max-w-5xl mx-auto p-6 sm:p-8 md:p-10 bg-white rounded-xl shadow-lg border border-gray-200 mt-8",
    )