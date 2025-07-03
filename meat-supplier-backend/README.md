# Meat Supplier Backend

This project is a FastAPI application that provides a backend for displaying contact information of a list of meat suppliers. It includes endpoints to retrieve supplier details and manage supplier data.

## Project Structure

```
meat-supplier-backend
├── app
│   ├── main.py          # Entry point of the application
│   ├── models.py        # Data models for the meat suppliers
│   ├── routes.py        # Route definitions for the application
│   └── database.py      # Database connection and interactions
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── .env                  # Environment variables
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd meat-supplier-backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Configure your environment variables in the `.env` file.

## Usage

To run the application, execute the following command:
```
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to access the automatically generated API documentation and test the endpoints.

## Endpoints

- `GET /suppliers`: Retrieve a list of all meat suppliers.
- `GET /suppliers/{id}`: Retrieve details of a specific supplier by ID.

## License

This project is licensed under the MIT License.