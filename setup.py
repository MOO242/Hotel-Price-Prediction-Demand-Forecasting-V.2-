from setuptools import setup, find_packages


def get_requirements(file_path: str) -> list[str]:
    """This function will return the list of requirements"""

    requirements = []
    with open(file_path, "r") as file:
        requirements = file.readlines()
        requirements = [
            req.replace("\n", "") for req in requirements if not req.startswith("-e")
        ]

    print(requirements)
    return requirements


setup(
    name="Hotel-Price-Prediction-Demand-Forecasting-V.2",
    version="0.1.0",
    author="Mohamed Al Razek",
    author_email="Mohamedalboshey89@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
print("Setup completed successfully.")
