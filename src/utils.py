import os
import inspect as ins


def log(cat: str, msg: str, loc: str):
    print(cat.upper() + ":", msg, "|", loc)


def logc(msg: str):
    log("critical", msg, os.path.basename(ins.stack()[1].filename))


def logw(msg: str):
    log("warning", msg, os.path.basename(ins.stack()[1].filename))


def logi(msg: str):
    log("info", msg, os.path.basename(ins.stack()[1].filename))
