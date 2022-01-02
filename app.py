from flask import Flask, render_template, request
from data import salary_list

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    # 返回网页文件
    return render_template('index.html')


@app.route('/login',methods=["POST"])
def hello_login():
    # 登录到服务器 获取用户名或密码，进行校验记录信息，在返回后台页面
    # print(request.form)
    username = request.form.get('username')
    password = request.form.get('password')
    print(username,password)
    # 获取用户名或密码，进行校验记录信息
    # for sal in salary_list:
    #    if sal['name'] == username:

    # 登陆成功后返回后台页面
    return render_template('admin.html',
                           salary_list=salary_list)

@app.route('/delete/<name>')
def hello_delete(name):  # put application's code here
    # 删除逻辑 先找到学员信息再删除
    for salary in salary_list:
        if salary['name'] == name:

            salary_list.remove(salary)
    return render_template('admin.html',
                           salary_list=salary_list)



@app.route('/change/<name>')
def hello_change(name):  # put application's code here
    # 删除逻辑 先找到学员信息再删除
    for salary in salary_list:
        if salary['name'] == name:
            # 在前端修改
            return render_template('change.html',
                           user=salary)

    return render_template('admin.html',
                           salary_list=salary_list)


@app.route('/changed/<name>',methods=['POST'])
def hello_changed(name):
    """"修改 拿到提交的信息"""
    # 删除逻辑 先找到学员信息再删除
    for salary in salary_list:
        if  salary['name'] == name:
            salary['id'] = request.form.get('id')
            salary['name'] = request.form.get('name')
            salary['sex'] = request.form.get('sex')
            salary['department'] = request.form.get('department')
            salary['position'] = request.form.get('position')
            salary['salary'] = request.form.get('salary')
            salary['tel'] = request.form.get('tel')


    return render_template('admin.html',
                           salary_list=salary_list)


@app.route('/add')
def hello_add():
    return render_template('add.html')


@app.route('/add2',methods=['POST'])
def hello_add2():
    salary = {}
    # 获取浏览器发送过来的数据
    salary['id'] = request.form.get('id')
    salary['name'] = request.form.get('name')
    salary['sex'] = request.form.get('sex')
    salary['department'] = request.form.get('department')
    salary['position'] = request.form.get('position')
    salary['salary'] = request.form.get('salary')
    salary['tel'] = request.form.get('tel')
    # 将数据保存
    salary_list.insert(0,salary)
    # 返回保存之后的页面
    return render_template('admin.html',
                           salary_list=salary_list)


if __name__ == '__main__':
    app.run()

