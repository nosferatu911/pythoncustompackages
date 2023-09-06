from setuptools import setup, find_packages

setup(
    name="nosferatu911",
    version="0.0.4",
    author="Dmytro Olkhovskyi",
    author_email="ab190987ods@gmail.com",
    url="https://www.youtube.com/",
    description="An application that informs you of the time in different locations and timezones",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["nosferatu911 = src.main:main"]},
)
