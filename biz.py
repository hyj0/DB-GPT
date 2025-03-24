import json
import os.path
import re

import jpype
from jpype import JClass

jpype.startJVM(classpath=["sql-parse.jar"])
# 加载 Java 类
MainClass = JClass("com.example.ob.sql.Main")
main_instance = MainClass()

class Biz:
    def get_table_list(self) -> list[str]:
        return []

    def get_ext_prompt(self) -> str:
        return ""

    def check_sql(self, sql) -> bool:
        # check sql join
        pass

    def get_sql_er(self, sql):
        if not bool(re.match(r'^\s*select', sql, re.IGNORECASE)):
            return {}
        global main_instance
        result = main_instance.parseSelectSql(sql)
        return json.loads(str(result))

class PhysicalInstant(Biz):
    def __init__(self):
        # join: table1.column1 = table2.column2
        self.er_str = '''
        '''
        pass


    def check_sql(self, sql) -> bool:
        er_ret = self.get_sql_er(sql)
        print(er_ret)
        er_map = er_ret["relationMap"]
        er_list = er_ret["relationList"]
        for t1,m1 in er_map.items():
            for c1, l2 in m1.items():
                for m2 in l2:
                    t2 = m2["left"]
                    c2 = m2["right"]
                    if t1 < t2:
                        er_str = f"{t1}.{c1} = {t2}.{c2}"
                    else:
                        er_str = f"{t2}.{c2} = {t1}.{c1}"
                    print(er_str)
                    if self.get_ext_prompt().find(er_str) < 0 and self.er_str.find(er_str) < 0:
                        raise Exception(f"error:{sql} has join:{er_str} no in prompt!")
        for er_str in er_list:
            if self.get_ext_prompt().find(er_str) < 0 and self.er_str.find(er_str) < 0:
                raise Exception(f"error:{sql} has join:{er_str} no in prompt!")
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

    pi = PhysicalInstant()

    sql = ("SELECT * FROM users u left join order_info oi on u.uid = oi.uid"
           " WHERE age > 20")
    pi.check_sql(sql)
