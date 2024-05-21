

from flask import Flask
from flask_restful import Api, Resource


app =Flask(__name__)
api =Api()


class Main(Resource):
    def get(self):
        return {"info" : "hello wrodl1", "num": 566, "very" :"lery lery", "number2":77, "hero": "Deky"}

api.add_resource(Main, "/api/main")
api.init_app(app)



if __name__=="__main__":
    app.run(debug=True, host="localhost")















# print("hello")
# import os
# import sys


# p_path = os.path.dirname(sys.executable)

# p_version= sys.version

# print(f"PATH__++ {p_path}   VERS {p_version}")
# print("hello3242343")


# import keyword

# kw = keyword.kwlist

# print(kw)

# for i in kw:
#     print(i)