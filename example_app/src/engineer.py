"""Represent the Engineer class to test with"""
from typing import List
from dataclasses import dataclass
from src.project import Project


@dataclass
class Engineer:

    name: str
    projects: List[Project]
    income: int = 0

    def calc_income(self) -> int:
        income = 0
        if self.projects:
            for p in self.projects:
                income += p.calculate_project_income()
        return income
