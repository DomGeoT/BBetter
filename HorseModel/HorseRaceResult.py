from datetime import date, time


class HorseRaceResult:

    def __init__(self,
                 raceDate: date,
                 countryId: str,
                 track: str,
                 going: str,  # todo enum
                 raceType: str,  # todo enum
                 distanceId: str,
                 stall: int,
                 horseId: str,
                 age: int,
                 pace: int,
                 weight: str,
                 jockeyId: str,
                 trainerId: str,
                 place: int,
                 winningDistance: str,
                 runners: int):
        self._raceDate = raceDate,
        self._countryId = countryId,
        self._track = track,
        self._going = going,  # todo enum
        self._raceType = raceType,  # todo enum
        self._distanceId = distanceId,
        self._stall = stall,
        self._horseId = horseId,
        self._age = age,
        self._pace = pace,
        self._weight = weight,
        self._jockeyId = jockeyId,
        self._trainerId = trainerId,
        self._place = place,
        self._winningDistance = winningDistance,
        self._runners = runners

