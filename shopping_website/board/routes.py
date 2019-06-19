from flask_babel import gettext
from flask import Flask, render_template, url_for, flash, request, redirect, session, flash, send_from_directory, Blueprint
from shopping_website.main.routes import login_required
from shopping_website.forms import BoardForm, LocationForm, ProductForm, Submit_Form, Delete_Form
from shopping_website.db.db_fuctions import update_info, check_info, check_info2, insert_data, insert_data1, insert_data2, insert_data3, check_product, update_data, update_location, delete_data
#from flask_login import login_user, current_user, logout_user, login_required, LoginManager
import gc
from shopping_website.db.dbconnect import connection
from MySQLdb import escape_string as thwart
import hashlib

board = Blueprint('board', __name__)

@board.route('/board_write', methods=["GET", "POST"])
@login_required
def board_page():
    form = BoardForm(request.form)
    email = session['email']
    info_list = check_info("user_list", "email", email)
    username, password_db = info_list[0][1], info_list[0][2]
    print(username, password_db)
    if request.method == "POST" and form.validate():
        title, content, pass_data = form.title.data, form.content.data, form.password.data
        password_input = hashlib.sha256(pass_data.encode()).hexdigest()  # 입력된 비밀번호 암호화
        print(title, password_input)
        if password_db == password_input:
            (password_db, password_input)
            insert_data2("board", title, content, email)
            flash(username + "님 빠른 시일 내에 연락드리겠습니다.")
            gc.collect()
            return redirect(url_for('main.home'))
        else:
            flash('Wrong password')
            return render_template("board_write.html", form=form, title="board_write")
    else:
        return render_template("board_write.html", form=form, username=username, title="board_write")

@board.route('/board', methods=["GET","POST"])
def board_main():
    board_list = check_product("board")
    board_count_number = len(board_list)
    return render_template("board_main.html", board_list=board_list, board_count_n=board_count_number, title="board")


@board.route("/board_update/<int:board_num>", methods=["GET", "POST"])
def board_update(board_num):
    """
    board_num 에 일치하는 정보(board_num와 db상의 행번호가 다름) 가져온 후 해당 board의 작성자와 접속자가 같은지 판단(다를 시 권한 없음)

    """
    del_form = Delete_Form(request.form)
    update_form = BoardForm(request.form)
    board_list = check_product("board")
    board_count_number = len(board_list)
    board_num=board_num
    email = session['email']
    for i in range(len(board_list)):
        if board_list[i][0] == board_num:
            number_index = i                       # 리스트에는 비어있는 부분있어 인덱스 확인 필요
    if board_list[number_index][3] != email:       #로그인 이메일과 해당 게시판의 정보 불일치
        flash('권한 없음')
        return redirect(url_for('board.board_main'))
    if request.method == "GET":
        return render_template("board_update.html", board_list=board_list, board_count_n=board_count_number,i=number_index,title="board_update", update_form=update_form, del_form=del_form)
    else:
        if request.method == "POST":
            board_num = str(board_num)   # 테이블 입력시 int 안됌
            if update_form.validate():
                title, content, pass_data = update_form.title.data, update_form.content.data, update_form.password.data   # 사용자 - 보드 일치 확인 필요 (이메일로 들어가므로 불필요?)
                data = [title, content, board_num]
                c, conn = connection()
                c.execute("set names utf8")  # db에 한글 저장
                c.execute("UPDATE board SET title="+data[0]+", content="+data[1]+" WHERE board_n=%s", [thwart(data[2])])    # 하나라도 리스트로 해야함
                conn.commit()
                c.close()
                conn.close()
                flash("수정되었습니다.")
                return redirect(url_for('board.board_main'))
            if del_form.validate():
                delete_data("board", "board_n", board_num)
                flash(board_num + '번 글 삭제되었습니다.')
                return redirect(url_for('board.board_main'))
            else:
                return render_template("board_update.html", board_list=board_list, board_count_n=board_count_number, i=number_index, title="board_update", update_form=update_form, del_form=del_form)

