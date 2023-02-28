"""Represent the Project class to test with"""
from enum import Enum
from dataclasses import dataclass


class ProjectTypes(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    BIG = "big"


@dataclass
class Project:

    name: str
    contract_price: int
    size_of_project: ProjectTypes

    def calc_project_length(self) -> int:
        """
        Calculate the project length based on project size.
        """
        length = None
        if self.size_of_project.value == "small":
            length = 1
        elif self.size_of_project.value == "medium":
            length = 3
        elif self.size_of_project.value == "big":
            length = 6
        return length

    def calculate_project_income(self) -> int:
        """
        Calculate the project income based on project length.
        :return:
        """
        return self.contract_price * self.calc_project_length()
