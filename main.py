from codeforce import codeforce
from leetcode import leetcode
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root(q: str = "", n: int = -1):
    if (q == ""):
        return {"message": "Please provide a query."}

    cf_questions = codeforce.query(q)
    lc_questions = leetcode.query(q)

    total_questions = cf_questions + lc_questions
    total_questions.sort(key=lambda x: x["score"], reverse=True)
    if (n > 0 and n < len(total_questions)):
        total_questions = total_questions[:n]

    return total_questions


@app.get("/codeforce/")
def codeforce_query(q: str = "", n: int = -1):
    if q == "":
        return {"message": "Please provide a query."}
    query = codeforce.query(q)
    if (n > 0 and n < len(query)):
        query = query[:n]
    return query


@app.get("/leetcode/")
def leetcode_query(q: str = "", n: int = -1):
    if q == "":
        return {"message": "Please provide a query."}
    query = leetcode.query(q)
    if (n > 0 and n < len(query)):
        query = query[:n]
    return query
