from app import app
from flask import render_template, redirect, request, url_for, flash
from services.menuservice import *
from services.restaurantservice import get_restaurant


@app.route('/restaurant/<int:restaurant_id>/menu')
def restaurantMenu(restaurant_id):
    menu = get_restaurant_menu(restaurant_id)
    restaurant = get_restaurant(restaurant_id)
    return render_template('menu.html', menu=menu, restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/menuitem/new')
def newMenu(restaurant_id):
    restaurant = get_restaurant(restaurant_id)
    courses = get_all_courses()
    return render_template('newMenu.html', restaurant=restaurant, courses=courses)


@app.route('/restaurant/<int:restaurant_id>/menuitem/new', methods=['POST'])
def newMenuPOST(restaurant_id):
    save_menu_item(request, restaurant_id)
    flash('new menu item was added')
    return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))


@app.route('/restaurant/<int:restaurant_id>/menuitem/<int:item_id>/edit')
def editMenu(restaurant_id, item_id):
    courses = get_all_courses()
    restaurant = get_restaurant(restaurant_id)
    menuitem = get_menu_item(item_id)
    return render_template('editMenu.html', courses=courses, restaurant=restaurant, menuitem=menuitem)


@app.route('/restaurant/<int:restaurant_id>/menuitem/<int:item_id>/edit', methods=['POST'])
def editMenuPOST(restaurant_id, item_id):
    edit_menu_item(request, item_id)
    flash('menu item successfully edited')
    return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))


@app.route('/restaurant/<int:restaurant_id>/menuitem/<int:item_id>/delete')
def deleteMenu(restaurant_id, item_id):
    restaurant = get_restaurant(restaurant_id)
    menuitem = get_menu_item(item_id)
    return render_template('deleteMenu.html', restaurant=restaurant, menuitem=menuitem)


@app.route('/restaurant/<int:restaurant_id>/menuitem/<int:item_id>/delete', methods=['POST'])
def deleteMenuPOST(restaurant_id, item_id):
    delete_menu_item(item_id)
    flash('menu item successfully deleted')
    return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))

