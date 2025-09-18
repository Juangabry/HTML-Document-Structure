import reflex as rx
from typing import TypedDict, Optional
import random
from collections import Counter


class SurveyResponse(TypedDict):
    id: int
    age: int
    gender: str
    marital_status: str
    position: str
    seniority: int
    has_consumed: bool
    substances: list[str]
    age_of_first_use: Optional[int]
    frequency: Optional[str]
    consumed_at_work: Optional[bool]
    absenteeism: Optional[bool]
    conflicts: Optional[bool]
    affects_performance: Optional[bool]
    willing_to_participate: Optional[bool]


class AnalysisState(rx.State):
    survey_data: list[SurveyResponse] = []
    chart_type: str = "bar"

    def _generate_mock_data(self):
        if self.survey_data:
            return
        positions = ["Engineer", "Designer", "Manager", "Analyst", "HR"]
        genders = ["Male", "Female"]
        marital_statuses = ["Single", "Married", "Divorced"]
        substances_list = ["alcohol", "tobacco", "cannabis", "cocaine", "amphetamines"]
        frequencies = ["monthly", "weekly", "daily"]
        data = []
        for i in range(1, 51):
            has_consumed = random.choice([True, False])
            age_of_first_use = random.randint(15, 25) if has_consumed else None
            entry = {
                "id": i,
                "age": random.randint(20, 60),
                "gender": random.choice(genders),
                "marital_status": random.choice(marital_statuses),
                "position": random.choice(positions),
                "seniority": random.randint(1, 20),
                "has_consumed": has_consumed,
                "substances": random.sample(substances_list, k=random.randint(0, 3))
                if has_consumed
                else [],
                "age_of_first_use": age_of_first_use,
                "frequency": random.choice(frequencies) if has_consumed else None,
                "consumed_at_work": random.choice([True, False])
                if has_consumed
                else None,
                "absenteeism": random.choice([True, False]) if has_consumed else None,
                "conflicts": random.choice([True, False]) if has_consumed else None,
                "affects_performance": random.choice([True, False])
                if has_consumed
                else None,
                "willing_to_participate": random.choice([True, False])
                if has_consumed
                else None,
            }
            data.append(entry)
        self.survey_data = data

    @rx.event
    def on_load(self):
        self._generate_mock_data()

    @rx.event
    def set_chart_type(self, chart_type: str):
        self.chart_type = chart_type

    @rx.var
    def consumers_vs_non_consumers(self) -> list[dict[str, int | str]]:
        if not self.survey_data:
            return []
        consumers = sum((1 for d in self.survey_data if d["has_consumed"]))
        non_consumers = len(self.survey_data) - consumers
        return [
            {"name": "Consumers", "value": consumers},
            {"name": "Non-consumers", "value": non_consumers},
        ]

    @rx.var
    def consumption_by_substance(self) -> list[dict[str, int | str]]:
        if not self.survey_data:
            return []
        substance_counts = Counter()
        for d in self.survey_data:
            if d["has_consumed"]:
                substance_counts.update(d["substances"])
        return [
            {"name": substance.capitalize(), "count": count}
            for substance, count in substance_counts.items()
        ]

    @rx.var
    def age_of_first_use_distribution(self) -> list[dict[str, int]]:
        if not self.survey_data:
            return []
        ages = [
            d["age_of_first_use"]
            for d in self.survey_data
            if d["age_of_first_use"] is not None
        ]
        age_counts = Counter(ages)
        return [
            {"age": age, "count": count} for age, count in sorted(age_counts.items())
        ]

    @rx.var
    def risk_indicators(self) -> dict[str, str]:
        if not self.survey_data:
            return {"absenteeism": "0.0%", "conflicts": "0.0%", "risk_level": "Low"}
        consumers = [d for d in self.survey_data if d["has_consumed"]]
        if not consumers:
            return {"absenteeism": "0.0%", "conflicts": "0.0%", "risk_level": "Low"}
        absenteeism_count = sum((1 for d in consumers if d["absenteeism"]))
        conflicts_count = sum((1 for d in consumers if d["conflicts"]))
        total_consumers = len(consumers)
        absenteeism_rate = absenteeism_count / total_consumers * 100
        conflicts_rate = conflicts_count / total_consumers * 100
        risk_score = (absenteeism_rate + conflicts_rate) / 2
        if risk_score > 66:
            risk_level = "High"
        elif risk_score > 33:
            risk_level = "Medium"
        else:
            risk_level = "Low"
        return {
            "absenteeism": f"{absenteeism_rate:.1f}%",
            "conflicts": f"{conflicts_rate:.1f}%",
            "risk_level": risk_level,
        }