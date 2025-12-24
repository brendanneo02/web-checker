import time
import datetime as dt
from pathlib import Path
import requests

logFile = Path("logs/checker.log")

def checkUrl(url: str, timeout: float = 5.0) -> dict:
    start = time.perf_counter()
    try:
        response = requests.get(url, timeout=timeout)
        elaspedTime = (time.perf_counter() - start) * 1000

        ok = 200 <= response.status_code < 400
        return{
            "url": url,
            "ok": ok,
            "statusCode": response.status_code,
            "elaspedTime": round(elaspedTime, 2),
            "error":"",
        }
    except requests.exceptions.RequestException as e:
        duration = (time.perf_counter() - start) * 1000
        return{
            "url": url,
            "ok": False,
            "statusCode": None,
            "elaspedTime": round(elaspedTime, 2),
            "error": str(e),
        }    

def logResult(result: dict) -> None:
    logFile.parent .mkdir(parents=True, exist_ok=True)

    timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    statusText = "UP" if result["ok"] else "DOWN"

    line = (f"[{timestamp}] {statusText} | {result['url']} | "
            f"code={result['statusCode']} | {result['elaspedTime']}ms"
    )

    if result["error"]:
        line += f" | error={result['error']}"

    print(line)
    logFile.open("a", encoding="utf-8").write(line + "\n")

def run(urls: list[str], intervalSeconds: int = 60) -> None:
    while True:
        for url in urls:
            result = checkUrl(url)
            logResult(result)
        time.sleep(intervalSeconds)

if __name__ == "__main__":
    URLS = [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.youtube.com",
        "https://www.x.com",
    ]

    run(URLS, intervalSeconds=60)