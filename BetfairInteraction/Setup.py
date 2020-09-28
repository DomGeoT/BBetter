import betfairlightweight
import json


def setupLogin(loginDir: str):
    loginFile = loginDir + "loginDetails.json"
    with open(loginFile) as f:
        data = json.load(f)

    username = data["username"]
    password = data["password"]
    delayedAppKey = data["delayedAppKey"]
    liveAppKey = data["liveAppKey"]

    trading = betfairlightweight.APIClient(username, password, app_key=delayedAppKey)

    trading.login_interactive()

    return trading

