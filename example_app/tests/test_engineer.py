from src.engineer import Engineer
from src.project import Project, ProjectTypes


def test_engineer_construct():
    engineer_data = {
        "name": "Best engineer",
        "project": {"name": "Cool project",
                    "contract_price": 1250,
                    "size_of_project": ProjectTypes.MEDIUM}
    }

    engineer = Engineer(name=engineer_data.get("name"),
                        income=0,
                        projects=[
                            Project(
                                name=engineer_data.get("project").get("name"),
                                contract_price=engineer_data.get("project").get("contract_price"),
                                size_of_project=engineer_data.get("project").get("size_of_project"))
                        ])

    assert engineer.name == engineer_data.get("name")
    assert len(engineer.projects) == 1


def test_calc_income():
    engineer_data = {
        "name": "Best engineer",
        "project": {"name": "Cool project",
                    "contract_price": 1250,
                    "size_of_project": ProjectTypes.MEDIUM}
    }

    engineer = Engineer(name=engineer_data.get("name"),
                        income=0,
                        projects=[
                            Project(
                                name=engineer_data.get("project").get("name"),
                                contract_price=engineer_data.get("project").get("contract_price"),
                                size_of_project=engineer_data.get("project").get("size_of_project"))
                        ])

    # get Project income
    project = engineer.projects[0]
    project_income = project.calculate_project_income()

    assert engineer.calc_income() == project_income
