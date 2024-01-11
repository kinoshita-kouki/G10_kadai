from  flask import Flask, request, render_template
import random # ランダムデータ作成のためのライブラリ
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uranai/play', methods=["POST"])
def uranai_play():

    List = [5, 1, 3, 2, 4]

    name = request.form.get("name")
    name_num = len(name)

    now = datetime.date.today()
     # YYYYMMDD形式の整数に変換
    formatted_date = int(now.strftime('%Y%m%d'))

    birth_date_str = request.form.get('birthday')
    # 年、月、日が正しく入力されているか確認
    try:
        year, month, day = map(int, birth_date_str.split('-'))
        birth_num = year * 10000 + month * 100 + day
    except (ValueError, TypeError):
        result_message = "入力不備で占えませんでした"
        result_num = 1
        return render_template('uranai_play.html', result_message=result_message, result_num=result_num)

    # 名前が入力されているか確認
    if not name:
        result_message = "入力不備で占えませんでした"
        result_num = 1
        return render_template('uranai_play.html', result_message=result_message, result_num=result_num)

    # 占い結果処理
    if name_num == 0 or birth_num >= 100000000:
        result_message = "入力不備で占えませんでした"
        result_num = 1
        return render_template('uranai_play.html', result_message=result_message, result_num=result_num)
    else :
        index =  ((abs(formatted_date - birth_num)) * name_num) % 5
        print(index)
        result_num = int(List[index])
        if result_num == 5:
            result_message = "すごく良い！"
        if result_num == 4:
            result_message = "かなり良い！"
        if result_num == 3:
            result_message = "そこそこ良い"
        if result_num == 2:
            result_message = "ちょっと良くないかも…"
        if result_num == 1:
            result_message = "かなり良くない…"

    # 渡したいデータを先に定義しておいてもいいし、テンプレートを先に作っておいても良い
    return render_template('uranai_play.html',
                           result_message=result_message,
                           result_num = result_num)


if __name__ == '__main__':
    app.run()
    