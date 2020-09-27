from datetime import datetime

import requests
import pandas as pd

from HorseModel.HorseRaceResult import HorseRaceResult


def getTodaysRacers() -> list:
    url = 'https://www.racing-bet-data.com/exceldl/RBD-Daily-Sample.xlsx'
    r = requests.get(url, allow_redirects=True)

    open('RBD-Daily-Sample.xlsx', 'wb').write(r.content)
    res = pd.read_excel('RBD-Daily-Sample.xlsx')

    parsedHorses = list()

    count = 0

    for index, row in res.iterrows():
        try:

            raceDate = row["Date"].to_pydatetime().date()

            countryId = row["Country ID"]
            track = row["Track"]
            going = row["Going ID"]
            raceType = row["Type ID"]
            distanceId = row["Distance ID"]
            stall = row["Stall"]
            horseId = row["Horse ID"]
            age = int(row["Age"])
            pace = row["Pace"]
            weight = row["Weight ID"]
            jockeyId = row["Jockey ID"]
            trainerId = row["Trainer ID"]
            place = row["Place"]
            winningDistance = row["Winning Distance"]
            runners = int(row["Runners"])

            parsedResult = HorseRaceResult(raceDate=raceDate,
                                           countryId=countryId,
                                           track=track,
                                           going=going,
                                           raceType=raceType,
                                           distanceId=distanceId,
                                           stall=stall,
                                           horseId=horseId,
                                           age=age,
                                           pace=pace,
                                           weight=weight,
                                           jockeyId=jockeyId,
                                           trainerId=trainerId,
                                           place=place,
                                           winningDistance=winningDistance,
                                           runners=runners)

            parsedHorses.append(parsedResult)

            count += 1
        except Exception as e:
            print("Error parsing index", index, e)

    print("Parsed", count, "entries")

    return parsedHorses


print(getTodaysRacers())
