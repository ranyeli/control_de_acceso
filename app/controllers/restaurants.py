from app import app
from flask import render_template, redirect, url_for, request, flash
from datetime import datetime
from services.restaurantservice import *


@app.route('/')
@app.route('/restaurants')
def restaurantHome():
    restaurants = get_all_restaurants()
    return render_template('restaurants.html', date=datetime.now().year, restaurants=restaurants)


@app.route('/restaurants/new')
def newRestaurant():
    return render_template('newRestaurant.html')


@app.route('/restaurants/new', methods=['POST'])
def newRestaurantPOST():
    save_restaurant(request)
    flash('new restaurant was created')
    return redirect(url_for('restaurantHome'))


@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    restaurant = get_restaurant(restaurant_id)
    return render_template('editRestaurant.html', restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/edit', methods=['POST'])
def editRestaurantPOST(restaurant_id):
    edit_restaurant(request, restaurant_id)
    flash('restaurant successfully edited')
    return redirect(url_for('restaurantHome'))


@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    restaurant = get_restaurant(restaurant_id)
    return render_template('deleteRestaurant.html', restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/delete', methods=['POST'])
def deleteRestaurantPOST(restaurant_id):
    delete_restaurant(restaurant_id)
    flash('restaurant successfully deleted')
    return redirect(url_for('restaurantHome'))
