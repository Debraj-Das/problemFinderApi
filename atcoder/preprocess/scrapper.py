from bs4 import BeautifulSoup
import requests
import pandas as pd


def saveCsv(problems):
    df = pd.DataFrame(problems[1:], columns=problems[0])
    df.to_csv('problem.csv', index=False)


def webPage(url):
    re = requests.get(url)
    soup = BeautifulSoup(re.content, 'lxml')
    return soup


def fetchText(url):
    soup = webPage(url)

    text = ''
    try:
        element = soup.select("div.part > section")
        for i in element:
            text += i.text
    except Exception as _:
        text = ''

    text = ''.join(e if e.isalnum() or e.isspace() else ' ' for e in text)

    return text


def getProblems(problemUrl):
    problems = [["Name", "URL", "Text"],]
    problemlist = requests.get(
        "https://kenkoooo.com/atcoder/resources/problems.json").json()

    for problemInfo in problemlist:
        url = f"https://atcoder.jp/contests/{problemInfo['contest_id']}/tasks/{problemInfo['id']}"
        name = problemInfo['name']
        text = fetchText(url)
        problems.append([name, url, text])

    saveCsv(problems)
    return


if __name__ == "__main__":
    problemUrl = "https://atcoder.jp/contests"
    getProblems(problemUrl)
