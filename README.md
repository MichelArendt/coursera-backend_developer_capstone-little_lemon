# coursera-backend_developer_capstone-little_lemon

# API Endpoints
## Menu and Booking
### Menu: "http://127.0.0.1:8000/api/menu"
- GET (all users): retrieve all menu items
- POST (staff only): add new items to the menu
### Menu - View specific item (by ID): "http://127.0.0.1:8000/api/menu/1/"
- GET (all users): retrieve a specific menu item
- PUT, PATCH, DELETE (staff only): modify or delete item
### Bookings: "http://127.0.0.1:8000/api/booking",
- GET (staff only): retrieve all bookings
- POST (all users): add a new booking
### Bookings - View specific booking (by ID): "http://127.0.0.1:8000/api/booking/1/"
- GET (staff only): retrieve a specific booking
- POST (staff only): modify or delete booking

## Authorization Endpoints from Djoser
users (POST: staff only): "http://127.0.0.1:8000/api/auth/users/",
user-activation: "http://127.0.0.1:8000/api/auth/users/activation/",
user-me: "http://127.0.0.1:8000/api/auth/users/me/",
user-resend-activation: "http://127.0.0.1:8000/api/auth/users/resend_activation/",
user-reset-password: "http://127.0.0.1:8000/api/auth/users/reset_password/",
user-reset-password-confirm: "http://127.0.0.1:8000/api/auth/users/reset_password_confirm/",
user-reset-username: "http://127.0.0.1:8000/api/auth/users/reset_username/",
user-reset-username-confirm: "http://127.0.0.1:8000/api/auth/users/reset_username_confirm/",
user-set-password: "http://127.0.0.1:8000/api/auth/users/set_password/",
user-set-username: "http://127.0.0.1:8000/api/auth/users/set_username/",
api-root: "http://127.0.0.1:8000/api/auth/",
login: "http://127.0.0.1:8000/api/auth/token/login",
logout: "http://127.0.0.1:8000/api/auth/token/logout"


# Users

Password for all: pass@123

admin (Token d50f3aa7c4582e33ac07ddb103d4b6f639a56206)
JohnDoe (Token 2be3f6008ea7bf4f7f926518d22e342a484aabca)

# Tests
Go to 'src' folder and run the following command:

python .\manage.py test tests/