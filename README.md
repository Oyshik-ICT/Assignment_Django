# DataShift Project

DataShift is a Django-based web application that manages hotel property data. It includes functionality to migrate data from a Scrapy database to a Django database, handle various property attributes, and display the information in the Django admin interface.

## 🚨 Important Update 🚨

```diff
+ I apologize for the inconvenience, but there has been an important change to the Scrapy project.
+ Please use the new Scrapy project from the following repository:
+
+ [https://github.com/Oyshik-ICT/Assignment_Scrapy_Modified](https://github.com/Oyshik-ICT/Assignment_Scrapy_Modified)
+
+ This new version includes necessary modifications for compatibility with the Django project.
```

## Setup Instructions

````diff
+ 1. Clone the updated Scrapy project:
+    ```
+    git clone https://github.com/Oyshik-ICT/Assignment_Scrapy_Modified.git
+    cd Assignment_Scrapy_Modified
+    ```
+
+ 2. Set up and run the Scrapy project according to its README instructions.
+
+ 3. Once the Scrapy project has successfully run and populated its database, proceed with the Django project setup:
````

```
git clone https://github.com/Oyshik-ICT/Assignment_Django.git
cd Assignment_Django
```

4. Create a virtual environment and activate it:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

5. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

6. Set up PostgreSQL databases:

   - Create two databases: one for Django and one for Scrapy
   - Create a PostgreSQL service file (`~/.pg_service.conf`) with the following content:

     ```
     [my_service]
     host=localhost
     user=your_username
     dbname=your_django_db_name
     port=5432

     [my_scrapy_service]
     host=localhost
     user=your_username
     dbname=your_scrapy_db_name
     port=5432
     ```

7. Apply migrations:

   ```
   python manage.py migrate
   ```

8. Create a superuser for the Django admin:

   ```
   python manage.py createsuperuser
   ```

9. Configure VS Code settings (Optional but recommended):

   If you're using VS Code as your editor, you can use the following `settings.json` file configuration to ensure code quality and formatting consistency:

   ```json
   {
     "python.linting.enabled": true,
     "python.linting.flake8Enabled": true,
     "python.formatting.provider": "autopep8",
     "python.formatting.autopep8Args": ["--max-line-length=79"],
     "editor.formatOnSave": true,
     "python.linting.flake8Args": ["--max-line-length=79"]
   }
   ```

## Running the Project

1. Start the Django development server:

   ```
   python manage.py runserver
   ```

2. Access the Django admin interface at `http://127.0.0.1:8000/admin/`

## Data Migration

To migrate data from the Scrapy database to the Django database:

1. Ensure your Scrapy database is populated with hotel data
2. Run the custom management command:
   ```
   python manage.py migrate_scrapy_data
   ```

This command will transfer hotel data from the Scrapy database to the Django database and migrate images to the Django media directory.

```diff
+ Thank you for your understanding regarding these changes. If you encounter any issues, please don't hesitate to reach out.
```
