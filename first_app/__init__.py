from flask import Flask

app = Flask(__name__) 
# flask 객체 생성

# route 데코레이터 사용, 뷰 함수 등록 -> 반드시 return 사용
@app.route("/")
def helloworld():
    return "Hello world"
