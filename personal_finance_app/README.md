# Personal Finance App

A comprehensive personal finance management application built with FastAPI and modern JavaScript.

## Features

- 💰 **Wallet Management** - Multiple wallets with different types (cash, bank, credit card, investment)
- 📊 **Transaction Tracking** - Income, expenses, and transfers with automatic balance updates
- 🏷️ **Category System** - Hierarchical categorization with parent-child relationships
- 📈 **Dashboard Analytics** - Visual charts and financial summaries
- 🔒 **Secure Authentication** - JWT-based user authentication
- 📱 **Responsive Design** - Works on desktop and mobile devices

## Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database
- **Pydantic** - Data validation using Python type hints
- **JWT** - JSON Web Tokens for authentication

### Frontend
- **Vanilla JavaScript** - Modern ES6+ features
- **Chart.js** - Interactive charts and graphs
- **CSS3** - Modern styling with animations
- **Responsive Design** - Mobile-first approach

## Quick Start

### Backend Setup

1. Create virtual environment:
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

3. Create environment file:
```powershell
Copy-Item .env.example .env
# Edit .env with your settings
```

4. Run the server:
```powershell
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`
API documentation at `http://localhost:8000/docs`

### Frontend Setup

1. Navigate to frontend directory:
```powershell
cd frontend
```

2. Install dependencies:
```powershell
npm install
```

3. Start development server:
```powershell
npm start
```

The app will be available at `http://localhost:3000`

### Using Docker

Run the entire application with Docker Compose:

```powershell
docker-compose up --build
```

## Project Structure

```
personal_finance_app/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API routes
│   │   ├── crud/           # Database operations
│   │   ├── models/         # SQLAlchemy models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── services/       # Business logic
│   │   └── utils/          # Utility functions
│   ├── tests/              # Test files
│   └── requirements.txt    # Python dependencies
├── frontend/               # Frontend application
│   ├── src/
│   │   ├── components/     # Reusable components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API services
│   │   └── utils/          # Utility functions
│   └── package.json        # Node.js dependencies
└── docker-compose.yml      # Docker configuration
```

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - User login
- `GET /api/v1/auth/me` - Get current user

### Wallets
- `GET /api/v1/wallets` - Get all wallets
- `POST /api/v1/wallets` - Create wallet
- `GET /api/v1/wallets/{id}` - Get wallet by ID
- `PUT /api/v1/wallets/{id}` - Update wallet
- `DELETE /api/v1/wallets/{id}` - Delete wallet

### Transactions
- `GET /api/v1/transactions` - Get all transactions
- `POST /api/v1/transactions` - Create transaction
- `GET /api/v1/transactions/{id}` - Get transaction by ID
- `PUT /api/v1/transactions/{id}` - Update transaction
- `DELETE /api/v1/transactions/{id}` - Delete transaction

### Categories
- `GET /api/v1/categories` - Get all categories
- `POST /api/v1/categories` - Create category
- `GET /api/v1/categories/tree` - Get category tree
- `PUT /api/v1/categories/{id}` - Update category
- `DELETE /api/v1/categories/{id}` - Delete category

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is licensed under the MIT License.
