import reflex as rx
from app.states.analysis_state import AnalysisState


def summary_card(title: str, value: rx.Var, icon: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-6 w-6 text-gray-500"),
            class_name="p-3 bg-gray-100 rounded-lg",
        ),
        rx.el.div(
            rx.el.p(title, class_name="text-sm font-medium text-gray-500"),
            rx.el.p(value, class_name="text-2xl font-bold"),
            class_name="flex flex-col",
        ),
        class_name="flex items-center gap-4 p-4 bg-white rounded-lg shadow-sm border border-gray-200",
    )


def risk_summary() -> rx.Component:
    risk_level = AnalysisState.risk_indicators["risk_level"]
    return rx.el.div(
        rx.el.h3(
            "Work Risk Analysis", class_name="text-xl font-semibold text-gray-800 mb-4"
        ),
        rx.el.div(
            summary_card(
                "Absenteeism Rate (Consumers)",
                AnalysisState.risk_indicators["absenteeism"],
                "calendar-off",
            ),
            summary_card(
                "Conflict Rate (Consumers)",
                AnalysisState.risk_indicators["conflicts"],
                "swords",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        rx.match(
                            risk_level,
                            ("Low", "shield-check"),
                            ("Medium", "shield-alert"),
                            ("High", "shield-x"),
                            "shield",
                        ),
                        class_name=rx.match(
                            risk_level,
                            ("Low", "h-8 w-8 text-green-500"),
                            ("Medium", "h-8 w-8 text-yellow-500"),
                            ("High", "h-8 w-8 text-red-500"),
                            "h-8 w-8 text-gray-500",
                        ),
                    ),
                    class_name="p-3 bg-gray-100 rounded-lg",
                ),
                rx.el.div(
                    rx.el.p(
                        "Overall Risk Level",
                        class_name="text-sm font-medium text-gray-500",
                    ),
                    rx.el.p(risk_level, class_name="text-2xl font-bold"),
                ),
                class_name="flex items-center gap-4 p-4 bg-white rounded-lg shadow-sm border border-gray-200",
            ),
            class_name="grid grid-cols-1 md:grid-cols-3 gap-6",
        ),
        class_name="w-full p-6 bg-white rounded-lg shadow-md",
    )


def consumers_pie_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Consumers vs. Non-consumers",
            class_name="text-xl font-semibold text-gray-800 mb-4",
        ),
        rx.recharts.pie_chart(
            rx.recharts.graphing_tooltip(),
            rx.recharts.pie(
                data=AnalysisState.consumers_vs_non_consumers,
                data_key="value",
                name_key="name",
                cx="50%",
                cy="50%",
                outer_radius=80,
                fill="#8884d8",
                label=True,
            ),
            rx.recharts.legend(),
            width=400,
            height=300,
        ),
        class_name="w-full p-6 bg-white rounded-lg shadow-md flex flex-col items-center",
    )


def substance_bar_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Consumption by Substance",
            class_name="text-xl font-semibold text-gray-800 mb-4",
        ),
        rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
            rx.recharts.graphing_tooltip(),
            rx.recharts.x_axis(data_key="name"),
            rx.recharts.y_axis(),
            rx.recharts.legend(),
            rx.recharts.bar(data_key="count", fill="#82ca9d"),
            data=AnalysisState.consumption_by_substance,
            height=300,
        ),
        class_name="w-full p-6 bg-white rounded-lg shadow-md",
    )


def age_histogram() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Age of First Use Distribution",
            class_name="text-xl font-semibold text-gray-800 mb-4",
        ),
        rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
            rx.recharts.graphing_tooltip(),
            rx.recharts.x_axis(data_key="age", name="Age"),
            rx.recharts.y_axis(),
            rx.recharts.bar(data_key="count", fill="#ffc658"),
            data=AnalysisState.age_of_first_use_distribution,
            height=300,
        ),
        class_name="w-full p-6 bg-white rounded-lg shadow-md",
    )


def analysis_dashboard() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Substance Consumption Analysis",
                class_name="text-4xl font-bold text-center text-gray-900 mb-10",
            ),
            risk_summary(),
            rx.el.div(
                consumers_pie_chart(),
                substance_bar_chart(),
                class_name="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-8",
            ),
            rx.el.div(age_histogram(), class_name="mt-8"),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
        ),
        class_name="min-h-screen bg-gray-50",
        on_mount=AnalysisState.on_load,
    )