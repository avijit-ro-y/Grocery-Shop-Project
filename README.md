# 🛒 Grocery Shop Backend API

A complete **Grocery Shop Backend REST API** built using **Django** and **Django Rest Framework (DRF)**.  
This project supports **users, sellers, admins, products, carts, orders, deposits, reviews, ratings, and dashboards**, following real-world backend architecture and academic evaluation requirements.

---

## 🚀 Tech Stack

- Python 3.13
- Django 5.x
- Django Rest Framework
- JWT Authentication (SimpleJWT)
- Postman / ModHeader for API Testing

---
## API Endpoints
Authentication
/api/users/register/
/api/users/login/
/api/users/logout/
/api/users/token/refresh/
Products
/api/products/
/api/products/
/api/products/{id}/
/api/products/{id}/
Reviews
/api/reviews/
/api/reviews/{id}/
/api/reviews/{id}/
/api/products/{id}/reviews/
Cart
/api/cart/
/api/cart/
/api/cart/{id}/

Deposit
/api/deposit/
---

## 📦 Project Apps

| App Name | Description |
|--------|-------------|
| users | Authentication, JWT, user profile |
| product | Products, categories, reviews, ratings |
| cart | Shopping cart and shopping list |
| order | Orders and order items |
| review | Product reviews and ratings |
| dashboard | Seller and admin dashboards |

---

## 🔐 Authentication & Security

- JWT-based authentication
- Secure login and logout
- Token refresh support
- Role-based access control:
  - Admin
  - Seller
  - Customer

---

## 👤 User Features

### Registration & Login
- User registration via API
- JWT login and logout
- Password change functionality

### Customer Profile
- View profile details
- Purchase history
- Wishlist management
- Deposit balance tracking

---

## 🛍️ Product Management

### Admin Capabilities
- Add, edit, and delete any product
- Manage product availability
- Remove inappropriate listings

### Seller Capabilities
- Add and manage own products
- View inventory
- Track sales history
- View orders placed for their products

---

## 🔍 Product Filters

- Filter products by category
- Display only available products
- View ratings and reviews on product listing

---

## ⭐ Reviews & Ratings

- Customers can review products they have purchased
- Rating system (1–5 stars)
- Edit or delete own reviews
- One review per user per product
- Average rating displayed on product page

---

## 🛒 Shopping Cart & Shopping List

### Shopping Cart
- Add products to cart
- View cart items
- Update quantity
- Remove items

### Shopping List
- Personal shopping list per user
- Add, update, and remove items

---

## 💰 Deposit System

- Customers can deposit money into their account
- Deposit balance stored securely
- Balance used for future purchases
- Deposit history maintained

---

## 📦 Orders & Purchase System

- Orders created from cart items
- Orders contain multiple order items
- Orders linked to customers and sellers
- Purchase history stored
- Sellers can view orders related to their products

---

## 📊 Seller & Admin Dashboard

### Admin Dashboard
- Manage all users
- Manage all products
- Monitor platform activity

### Seller Dashboard
- View own products
- View orders placed for seller’s products
- Manage inventory
- Track sales history

---

## 🔗 Sample API Endpoints

### Authentication
