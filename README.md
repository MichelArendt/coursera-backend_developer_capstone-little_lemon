
This project is a simple back-end implementation for the Little Lemon restaurant, developed as part of the Back-End Developer Capstone course from Meta on Coursera. It utilizes Django, Django Rest Framework, and Djoser to:

-   **Connect to MySQL:** Integrate the Little Lemon back-end with a MySQL database.
-   **Restaurant Booking API:** Set up a comprehensive API for managing restaurant bookings.
-   **Data Management:** Insert and manage booking data in the database via the API.

**Note:** Before testing the project, don't forget to configure and populate the MySQL database with the necessary data.

# Website Links
  - http://localhost:8000/: home page
  - http://localhost:8000/menu: retrieves all menu items currently in the database (only staff can create menu items through API calls)
  - http://localhost:8000/booking: allows users to reserve tables (only staff can view booked times through API calls)

# API Endpoints
You can view available API endpoints at API Root View on the following link:
- http://127.0.0.1:8000/api/

## Menu and Booking

### Menu: "http://127.0.0.1:8000/api/menu"
- **GET (all users):** retrieve all menu items
- **POST (staff only):** add new items to the menu

### Menu - View specific item (by ID): "http://127.0.0.1:8000/api/menu/1/"
- **GET (all users):** retrieve a specific menu item
- **PUT, PATCH, DELETE (staff only):** modify or delete item

### Bookings: "http://127.0.0.1:8000/api/booking",
- **GET (staff only):** retrieve all bookings
- **POST (all users):** add a new booking

### Bookings - View specific booking (by ID): "http://127.0.0.1:8000/api/booking/1/"
- **GET (staff only):** retrieve a specific booking
- **POST (staff only):** modify or delete booking

## Authorization Endpoints from Djoser
- users (POST: staff only): "http://127.0.0.1:8000/api/auth/users/",
- user-activation: "http://127.0.0.1:8000/api/auth/users/activation/",
- user-me: "http://127.0.0.1:8000/api/auth/users/me/",
- user-resend-activation: "http://127.0.0.1:8000/api/auth/users/resend_activation/",
- user-reset-password: "http://127.0.0.1:8000/api/auth/users/reset_password/",
- user-reset-password-confirm: "http://127.0.0.1:8000/api/auth/users/reset_password_confirm/",
- user-reset-username: "http://127.0.0.1:8000/api/auth/users/reset_username/",
- user-reset-username-confirm: "http://127.0.0.1:8000/api/auth/users/reset_username_confirm/",
- user-set-password: "http://127.0.0.1:8000/api/auth/users/set_password/",
- user-set-username: "http://127.0.0.1:8000/api/auth/users/set_username/",
- api-root: "http://127.0.0.1:8000/api/auth/",
- login: "http://127.0.0.1:8000/api/auth/token/login",
- logout: "http://127.0.0.1:8000/api/auth/token/logout"

# Tests
To run some basic tests go to '**src**' folder and run the following command:
- **python .\manage.py test tests/**