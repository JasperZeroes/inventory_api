# Online Store Inventory and Supplier Management API

## Overview

This Django project provides an API for managing inventory items and suppliers for an online store. It allows users to add, view, update, and remove items from the inventory, as well as manage suppliers.

## Requirements

- Python 3.x
- Django 3.x
- Django REST Framework 3.x

## Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/JasperZeroes/inventory_api.git
    cd inventory_api
    ```

2. **Create a Virtual Environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/macOS
    # Or
    venv\Scripts\activate      # For Windows
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser (Optional):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Start the Development Server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the API:**

    Open a web browser and go to `http://127.0.0.1:8000/api/` to access the API endpoints.

8. **Access Admin Panel (Optional):**

    You can access the Django admin panel by going to `http://127.0.0.1:8000/admin/` and logging in with the superuser credentials.

## API Endpoints

- **Items:**
  - `GET /api/items/`: List all items or create a new item.
  - `GET /api/items/<id>/`: Retrieve, update, or delete a specific item.

- **Suppliers:**
  - `GET /api/suppliers/`: List all suppliers or create a new supplier.
  - `GET /api/suppliers/<id>/`: Retrieve, update, or delete a specific supplier.

## Testing

To run the automated tests, execute the following command:

```bash
python manage.py test


### Link to Loom Video
https://www.loom.com/share/fdc9edc163b749ce9db48db75b2d1bc9
