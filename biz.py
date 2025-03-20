import json
import os.path


class Biz:
    def get_table_list(self) -> list[str]:
        return []

    def get_ext_prompt(self) -> str:
        return ""


class PhysicalInstant(Biz):
    def __init__(self):
        pass

    def get_table_list(self) -> list[str]:
        ret = [

        ]
        return ret

    def get_ext_prompt(self) -> str:
        s = '''
        '''
        return s


class DigitalInstant(Biz):
    def get_table_list(self) -> list[str]:
        ret = [

        ]
        return ret

    def get_ext_prompt(self) -> str:
        s = '''
        '''
        return s


customBiz = {
    "physical_instant": PhysicalInstant(),
    "digital_instant": DigitalInstant()
}


def load_session():
    if os.path.exists("sessionExtinfo.json"):
        f = open("sessionExtinfo.json", "r")
        js = json.load(f)
        f.close()
        return js
    else:
        return {}


def storage_session(js):
    f = open("sessionExtinfo.json", "w")
    f.write(json.dumps(js))
    f.close()


def save_session(session_id, ext_info):
    s = load_session()
    s[session_id] = ext_info
    storage_session(s)


def get_session_extinfo(session_id):
    s = load_session()
    if session_id in s:
        return s[session_id]
    else:
        return {}


if __name__ == "__main__":
    print(get_session_extinfo("123"))
    save_session("123", {"app_name": "456"})
    print(get_session_extinfo("123"))

