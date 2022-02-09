from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fudging786hfg6hfg6h7f'


@app.route('/index')
@app.route('/')
def index():
    # Посадочная страничка приложения, на ней потом возможно сделать форму ввода и вывод результата или убрать если
    # не надо
    return render_template("index.html", title="Главная страница")


@app.route('/counts', methods=['POST'])
def counts():
    global urls_dict
    vh_dict = request.get_json(force=True, silent=True, cache=True)
    # Просмотр полученного словаря из JSONa
    # print(vh_dict)
    urls_list = []
    for req in (vh_dict.get('urls')):

        try:
            response = requests.get(req.get('url'), timeout=vh_dict.get('max_timeout'))
        except TimeoutError:
            print('TIMEOUT ERROR')


        if response.status_code != 200:
            res_status = 'error'
            # Если Timeout будет больше заданного вернётся код 408
            # 408 Request Timeout — время ожидания сервером передачи от клиента истекло
            # 408 это не 200, дополнительная проверка на Timeout не нужна
            append_dict = {'url': req.get('url'), 'status': res_status}
        else:
            res_status = 'ok'
            append_dict = {'url': req.get('url'), 'count': response.text.count(req.get('query')), 'status': res_status}
        urls_list.append(append_dict)
        urls_dict = {'urls': urls_list}
    # Просмотр словаря urls_dict
    # print(urls_dict)

    return urls_dict


if __name__ == '__main__':
    app.run(debug=True)
