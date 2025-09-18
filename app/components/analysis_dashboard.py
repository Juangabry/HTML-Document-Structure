import reflex as rx
from app.states.analysis_state import AnalysisState, Project, Task


def summary_card(title: str, value: rx.Var, icon: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name=f"h-6 w-6 {color}"),
            class_name="p-3 bg-gray-100 rounded-lg",
        ),
        rx.el.div(
            rx.el.p(title, class_name="text-sm font-medium text-gray-500"),
            rx.el.p(f"{value.to_string()}%", class_name="text-2xl font-bold"),
            class_name="flex flex-col",
        ),
        class_name="flex items-center gap-4 p-4 bg-white rounded-lg shadow-sm border border-gray-200",
    )


def project_table() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Projects", class_name="text-2xl font-semibold text-gray-800 mb-4"),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "ID",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Name",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Description",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        class_name="bg-gray-50",
                    )
                ),
                rx.el.tbody(
                    rx.foreach(AnalysisState.projects, render_project_row),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200 shadow border-b border-gray-200 sm:rounded-lg",
            ),
            class_name="overflow-x-auto",
        ),
        class_name="w-full p-6 bg-white rounded-lg shadow-md",
    )


def render_project_row(project: Project) -> rx.Component:
    project_id = project["id"]
    is_selected = AnalysisState.selected_project_id == project_id
    return rx.el.tr(
        rx.el.td(
            project_id,
            class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900",
        ),
        rx.el.td(
            project["name"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-700",
        ),
        rx.el.td(
            project["description"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        on_click=lambda: AnalysisState.select_project(project_id),
        class_name=rx.cond(
            is_selected,
            "bg-blue-100 hover:bg-blue-200 cursor-pointer transition-colors duration-150",
            "hover:bg-gray-100 cursor-pointer transition-colors duration-150",
        ),
    )


def chart_selection() -> rx.Component:
    return rx.el.div(
        rx.el.label("Chart Type", class_name="text-sm font-medium text-gray-700 mr-2"),
        rx.el.select(
            rx.el.option("Bar Chart", value="bar"),
            rx.el.option("Line Chart", value="line"),
            rx.el.option("Area Chart", value="area"),
            value=AnalysisState.chart_type,
            on_change=AnalysisState.set_chart_type,
            class_name="block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm rounded-md shadow-sm",
        ),
        class_name="flex items-center mb-4",
    )


def bar_chart_component() -> rx.Component:
    return rx.recharts.bar_chart(
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
        rx.recharts.graphing_tooltip(),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.legend(),
        rx.recharts.bar(data_key="tasks", fill="#8884d8"),
        data=AnalysisState.project_task_counts,
        height=300,
        class_name="w-full",
    )


def line_chart_component() -> rx.Component:
    return rx.recharts.line_chart(
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
        rx.recharts.graphing_tooltip(),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.legend(),
        rx.recharts.line(data_key="tasks", stroke="#8884d8", type_="monotone"),
        data=AnalysisState.project_task_counts,
        height=300,
        class_name="w-full",
    )


def area_chart_component() -> rx.Component:
    return rx.recharts.area_chart(
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
        rx.recharts.graphing_tooltip(),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.legend(),
        rx.recharts.area(
            data_key="tasks", stroke="#8884d8", fill="#8884d8", type_="monotone"
        ),
        data=AnalysisState.project_task_counts,
        height=300,
        class_name="w-full",
    )


def task_table() -> rx.Component:
    return rx.cond(
        AnalysisState.selected_project_id != None,
        rx.el.div(
            rx.el.h2(
                "Tasks for: ",
                rx.el.span(
                    AnalysisState.selected_project["name"],
                    class_name="font-bold text-blue-600",
                ),
                class_name="text-2xl font-semibold text-gray-800 mb-4",
            ),
            rx.el.div(
                summary_card(
                    "Completed",
                    AnalysisState.completed_tasks_percentage,
                    "check_check",
                    "text-green-500",
                ),
                summary_card(
                    "In Progress",
                    AnalysisState.in_progress_tasks_percentage,
                    "loader",
                    "text-yellow-500",
                ),
                summary_card(
                    "Pending",
                    AnalysisState.pending_tasks_percentage,
                    "badge_alert",
                    "text-red-500",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4",
            ),
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Task ID",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Task Name",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Status",
                                class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                            ),
                            class_name="bg-gray-50",
                        )
                    ),
                    rx.el.tbody(
                        rx.foreach(
                            AnalysisState.selected_project_tasks, render_task_row
                        ),
                        class_name="bg-white divide-y divide-gray-200",
                    ),
                    rx.cond(
                        AnalysisState.selected_project_tasks.length() == 0,
                        rx.el.caption(
                            rx.el.div(
                                "No tasks found for this project.",
                                class_name="text-center text-gray-500 py-4 italic",
                            )
                        ),
                    ),
                    class_name="min-w-full divide-y divide-gray-200 shadow border-b border-gray-200 sm:rounded-lg",
                ),
                class_name="overflow-x-auto",
            ),
            rx.el.div(
                chart_selection(),
                rx.match(
                    AnalysisState.chart_type,
                    ("bar", bar_chart_component()),
                    ("line", line_chart_component()),
                    ("area", area_chart_component()),
                    bar_chart_component(),
                ),
                class_name="w-full p-6 bg-white rounded-lg shadow-md mt-8",
            ),
            class_name="w-full p-6 bg-white rounded-lg shadow-md mt-8",
        ),
    )


def render_task_row(task: Task) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            task["id"],
            class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900",
        ),
        rx.el.td(
            task["name"], class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-700"
        ),
        rx.el.td(
            rx.el.span(
                task["status"],
                class_name=rx.match(
                    task["status"],
                    (
                        "Completed",
                        "px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800",
                    ),
                    (
                        "In Progress",
                        "px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800",
                    ),
                    (
                        "Pending",
                        "px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800",
                    ),
                    "px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-100 text-gray-800",
                ),
            ),
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
        ),
        class_name="hover:bg-gray-50 transition-colors duration-150",
    )


def analysis_dashboard() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Project Analysis Dashboard",
                class_name="text-4xl font-bold text-center text-gray-900 mb-10",
            ),
            project_table(),
            task_table(),
            class_name="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
        ),
        class_name="min-h-screen bg-gray-50",
    )