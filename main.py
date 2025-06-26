from fastapi import FastAPI
import psutil

password = "<password>"

app = FastAPI()

@app.get("/whoami")
async def whoami():
    return {"software": "SystemRecoursesAPI", "version": "0.1"}

@app.get("/cpu/{request}/{password_auth}")
async def cpu(request: str, password_auth: str):
    if password_auth == password:
        if request == "threads":
            threads = str(psutil.cpu_count(logical=True))
            return {"response": threads}
        elif request == "cores":
            cores = str(psutil.cpu_count(logical=False))
            return {"response": cores}
        elif request == "percent":
            percent = str(psutil.cpu_percent(1))
            percent = percent + "%"
            return {"response": percent}
        else:
            return {"error": "doesn't exist"}
    else:
        return {"error": "wrong password"}

@app.get("/memory/{request}/{password_auth}")
async def memory(request: str, password_auth: str):
    if password_auth == password:
        if request == "used":
            used = str(psutil.virtual_memory()[3])
            return {"response": used}
        elif request == "total":
            total = str(psutil.virtual_memory()[0])
            return {"response": total}
        else:
            return {"error": "doesn't exist"}
    else:
        return {"error": "wrong password"}
