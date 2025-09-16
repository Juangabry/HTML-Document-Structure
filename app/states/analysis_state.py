import reflex as rx
from typing import TypedDict, Optional


class Task(TypedDict):
    id: int
    project_id: int
    name: str
    status: str


class Project(TypedDict):
    id: int
    name: str
    description: str


class AnalysisState(rx.State):
    projects: list[Project] = [
        {
            "id": 1,
            "name": "Quantum Leap Engine",
            "description": "Develop a faster-than-light propulsion system.",
        },
        {
            "id": 2,
            "name": "Project Chimera",
            "description": "Genetic modification for enhanced adaptability.",
        },
        {
            "id": 3,
            "name": "Aether Network",
            "description": "Establish a global psychic communication network.",
        },
        {
            "id": 4,
            "name": "Chronos Initiative",
            "description": "Investigate temporal displacement phenomena.",
        },
    ]
    tasks: dict[int, list[Task]] = {
        1: [
            {
                "id": 101,
                "project_id": 1,
                "name": "Stabilize antimatter core",
                "status": "Completed",
            },
            {
                "id": 102,
                "project_id": 1,
                "name": "Calibrate warp field",
                "status": "In Progress",
            },
            {
                "id": 103,
                "project_id": 1,
                "name": "Design navigation AI",
                "status": "Pending",
            },
            {
                "id": 104,
                "project_id": 1,
                "name": "Test FTL jump sequence",
                "status": "Pending",
            },
        ],
        2: [
            {
                "id": 201,
                "project_id": 2,
                "name": "Sequence target genome",
                "status": "Completed",
            },
            {
                "id": 202,
                "project_id": 2,
                "name": "Develop retroviral vector",
                "status": "In Progress",
            },
            {
                "id": 203,
                "project_id": 2,
                "name": "Conduct simulation trials",
                "status": "In Progress",
            },
            {
                "id": 204,
                "project_id": 2,
                "name": "Initiate controlled mutation",
                "status": "Pending",
            },
        ],
        3: [
            {
                "id": 301,
                "project_id": 3,
                "name": "Map global ley lines",
                "status": "Completed",
            },
            {
                "id": 302,
                "project_id": 3,
                "name": "Construct psychic amplifiers",
                "status": "In Progress",
            },
            {
                "id": 303,
                "project_id": 3,
                "name": "Establish first node connection",
                "status": "Pending",
            },
        ],
        4: [],
    }
    selected_project_id: Optional[int] = None

    @rx.event
    def select_project(self, project_id: int):
        if self.selected_project_id == project_id:
            self.selected_project_id = None
        else:
            self.selected_project_id = project_id

    @rx.var
    def selected_project(self) -> Optional[Project]:
        if self.selected_project_id is None:
            return None
        for project in self.projects:
            if project["id"] == self.selected_project_id:
                return project
        return None

    @rx.var
    def selected_project_tasks(self) -> list[Task]:
        if self.selected_project_id is None:
            return []
        return self.tasks.get(self.selected_project_id, [])

    @rx.var
    def completed_tasks_percentage(self) -> float:
        if not self.selected_project_id:
            return 0.0
        tasks = self.selected_project_tasks
        if not tasks:
            return 0.0
        completed_tasks = [task for task in tasks if task["status"] == "Completed"]
        return len(completed_tasks) / len(tasks) * 100

    @rx.var
    def in_progress_tasks_percentage(self) -> float:
        if not self.selected_project_id:
            return 0.0
        tasks = self.selected_project_tasks
        if not tasks:
            return 0.0
        in_progress_tasks = [task for task in tasks if task["status"] == "In Progress"]
        return len(in_progress_tasks) / len(tasks) * 100

    @rx.var
    def pending_tasks_percentage(self) -> float:
        if not self.selected_project_id:
            return 0.0
        tasks = self.selected_project_tasks
        if not tasks:
            return 0.0
        pending_tasks = [task for task in tasks if task["status"] == "Pending"]
        return len(pending_tasks) / len(tasks) * 100