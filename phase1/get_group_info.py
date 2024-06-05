#!/usr/bin/env python
import pandas as pd

# Data preparation
data = {
    "Participants": [
        "Babic, Cabaua",
        "Fabian Henning, Sontheimer",
        "Jessica Sattler, Oppermann",
        "Schaschinek, Wedler",
        "Dinh, Oheim",
        "Abele, Bernauer",
        "Rehwald, Zentarra",
        "Wüst, Reimund",
        "Stirn, Schmid",
        "Richter, Julia Henning",
        "Steimer, Önkal",
        "Grabisch, Schöck",
        "Alina Sattler, Seitz",
        "Mignoli, Lepiorz",
        "Schneider, Sittler",
        "Cichy, Hirsch",
        "Gasparro, Emrulai",
        "Karagol, Kittich",
        "Löhn, Reick",
        "Rittberger, Throm",
        "Madeo, Fetai",
        "Albrecht, Schober",
        "Frei, Weber",
        "Meßmer, Meister",
        "Walter, Seng",
        "Schwegler, Wagner",
        "Watzal, Friedl",
        "Ernst",
        "Müller",
    ],
    "Project": [
        "Kurveninterpolation",
        "Schlangenwürfel",
        "Kurveninterpolation",
        "Schlangenwürfel",
        "Partikelsimulation",
        "Magnetfeld",
        "Magnetfeld",
        "Viergewinnt",
        "Schlangenwürfel",
        "Newton-Fraktale",
        "Kurveninterpolation",
        "Newton-Fraktale",
        "Newton-Fraktale",
        "Schlangenwürfel",
        "Magnetfeld",
        "Viergewinnt",
        "Magnetfeld",
        "Viergewinnt",
        "Viergewinnt",
        "Partikelsimulation",
        "Partikelsimulation",
        "Newton-Fraktale",
        "Magnetfeld",
        "Viergewinnt",
        "Schlangenwürfel",
        "Newton-Fraktale",
        "Kurveninterpolation",
        "Kurveninterpolation",
        "Partikelsimulation",
    ],
}

supervisors = {
    "Kurveninterpolation": "Haasdonk",
    "Magnetfeld": "Cheng",
    "Newton-Fraktale": "Cheng",
    "Partikelsimulation": "Nottoli",
    "Schlangenwürfel": "Nottoli",
    "Viergewinnt": "Cheng",
}

name = "Cheng"

# Create DataFrame
df = pd.DataFrame(data)
df["Supervisor"] = df["Project"].map(supervisors)
my_group = df[df["Supervisor"] == name].copy()
my_group.sort_values(by=["Project", "Participants"], inplace=True)
my_group["Group"] = range(1, len(my_group) + 1)
my_group = my_group[["Group", "Participants", "Project", "Supervisor"]]
my_group.to_csv(f"groups_{name.lower()}.csv", index=False)
