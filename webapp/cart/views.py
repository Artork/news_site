from flask import Blueprint, render_template, flash, redirect, url_for
from marketplace.user.forms import LoginForm, RegistrationForm
from marketplace.cart.models import Cart, CartItem
from marketplace import db


cart_blueprint = Blueprint('cart', __name__, url_prefix='/cart', template_folder='templates')



# создание заказа
@cart_blueprint.route('/cart', methods=['POST'])
def cart():
    form = CartItemForm()
    if form.validate_on_submit():
        new_order = 
    pass


@blueprint.route('/')
def admin_index():
    title = "Редактирование категорий"
    return render_template('admin/index.html', page_title= title)






#добавление строки
@cart_blueprint.route('/cart', methods=['GET'])
def create_item():


#изменение строки 
def update_item():
    


#удаление
def delete_itemstr():



#оформление заказа
@cart_blueprint.route('/order', methods=['POST'])
def order():


"""
@user_blueprint.route('/login')
def login():
    # Блок исключающий повторнную авторизацию для уже авторизированных пользователей
    if current_user.is_authenticated:
        return redirect(url_for('general.get_index'))

    title = "Авторизация"
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@user_blueprint.route('/login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли на сайт')
            return redirect(url_for('general.get_index'))

    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))   


@user_blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы вышли из сессии')
    return redirect(url_for('general.get_index'))


@user_blueprint.route('/register')
def register():
    # Блок исключающий повторнную авторизацию для уже авторизированных пользователей
    if current_user.is_authenticated:
        return redirect(url_for('general.get_index'))

    title = "Регистрация"
    form = RegistrationForm()
    return render_template('user/registration.html', page_title=title, form = form)


@user_blueprint.route('/register', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role=form.roles.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('user.register'))