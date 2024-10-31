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
        element = soup.select("div.content-description")
        for e in element:
            text += e.text
    except Exception as _:
        text = ''

    text = ''.join(e if e.isalnum() or e.isspace() else ' ' for e in text)

    return text


def getProblems():
    problems = [["Name", "URL", "Text"],]

    soup = webPage("https://dmoj.ca/problems/")

    no_of_pages = int(soup.select("ul.pagination > li")[-2].text)

    problemList = []

    for i in range(1, no_of_pages + 1):
        soup = webPage(f"https://dmoj.ca/problems/?page={i}")

        for j in soup.select("table#problem-table > tbody > tr"):
            url = j.select("td")[0].select("a")[0].get("href")
            name = j.select("td")[0].text
            category = j.select("td")[1].text

            problemList.append(
                {"name": name, "url": url, "category": category})

    for problemInfo in problemList:
        url = f"https://dmoj.ca/{problemInfo['url']}"
        name = problemInfo['name'].strip().replace("\n", "")
        text = fetchText(url)
        text += problemInfo['category'] + " " + problemInfo['category']
        problems.append([name, url, text])

    saveCsv(problems)
    return


if __name__ == "__main__":
    getProblems()
