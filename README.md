# Personal Finance Management App

A comprehensive personal finance management application built with FastAPI (backend) and modern JavaScript (frontend).

## 🌟 Features

### 💰 Wallet Management
- Create multiple wallets (Checking, Savings, Cash, Credit Card, Investment, Business)
- Set initial balances
- Real-time balance tracking
- Wallet-specific transaction history

### 💸 Income & Expense Tracking
- **Income Categories**: Salary, Freelance, Investment Returns, Business Income, Rental Income, Loan Received
- **Expense Categories**: Food & Dining, Transportation, Shopping, Entertainment, Bills & Utilities, Healthcare, Education, Travel, Housing, Insurance
- Add custom categories with icons and colors
- Automatic balance updates

### 🔄 Inter-Wallet Transfers
- Transfer money between any wallets
- Automatic balance adjustments
- Transfer history tracking
- Insufficient funds warnings

### 📊 Dashboard & Reports
- Total balance across all wallets
- Income vs expenses summary
- Recent transaction history
- Visual statistics

### 💾 Data Persistence
- Local storage for data persistence
- No data loss between sessions
- Import/export capabilities (coming soon)

## 🚀 Quick Start

### Backend Setup (FastAPI)

1. **Navigate to backend directory:**
   ```powershell
   cd backend
   ```

2. **Create virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Create environment file:**
   ```powershell
   Copy-Item .env.example .env
   ```

5. **Start the server:**
   ```powershell
   uvicorn app.main:app --reload
   ```

   The API will be available at: `http://127.0.0.1:8000`
   
   API Documentation: `http://127.0.0.1:8000/docs`

### Frontend Setup (Standalone HTML)

1. **Open the frontend:**
   ```
   Open `complete_finance_app.html` in your web browser
   ```

2. **Or serve with a local server:**
   ```powershell
   # Using Python
   python -m http.server 8080
   
   # Using Node.js (if you have it)
   npx serve .
   ```

## 📁 Project Structure

```
personal-finance-app/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API routes
│   │   ├── models/         # Database models
│   │   ├── schemas/        # Pydantic schemas
│   │   └── main.py         # FastAPI application
│   ├── requirements.txt    # Python dependencies
│   └── .env.example        # Environment variables template
├── complete_finance_app.html # Complete frontend application
├── README.md               # This file
└── .gitignore             # Git ignore rules
```

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

### Frontend
- **Vanilla JavaScript** - No frameworks, pure JS
- **Chart.js** - Interactive charts
- **Font Awesome** - Icons
- **CSS3** - Modern styling with animations
- **LocalStorage** - Client-side data persistence

## 🔧 Development

### Adding New Features

1. **Backend API Endpoints:**
   - Add routes in `backend/app/api/`
   - Define models in `backend/app/models/`
   - Create schemas in `backend/app/schemas/`

2. **Frontend Features:**
   - Add functions to `complete_finance_app.html`
   - Update UI components
   - Modify data handling logic

### Database Schema

The app uses the following main entities:
- **Users** - User authentication and profiles
- **Wallets** - Financial accounts/wallets
- **Categories** - Income and expense categories
- **Transactions** - All financial transactions
- **Transfers** - Inter-wallet transfers

## 📊 API Endpoints

### Authentication
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/register` - User registration
- `GET /api/v1/auth/me` - Current user info

### Wallets
- `GET /api/v1/wallets` - Get all wallets
- `POST /api/v1/wallets` - Create wallet
- `PUT /api/v1/wallets/{id}` - Update wallet
- `DELETE /api/v1/wallets/{id}` - Delete wallet

### Transactions
- `GET /api/v1/transactions` - Get all transactions
- `POST /api/v1/transactions` - Create transaction
- `GET /api/v1/transactions/summary/stats` - Financial summary

### Categories
- `GET /api/v1/categories` - Get all categories
- `POST /api/v1/categories` - Create category
- `GET /api/v1/categories/tree` - Get category hierarchy

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Commit your changes: `git commit -am 'Add feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- Chart.js for beautiful charts
- Font Awesome for icons
- All contributors and testers

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page
2. Create a new issue with detailed description
3. Include steps to reproduce the problem

## 🎯 Roadmap

### Upcoming Features
- [ ] Multi-user support with authentication
- [ ] Data import/export (CSV, Excel)
- [ ] Budget planning and tracking
- [ ] Bill reminders and recurring transactions
- [ ] Investment portfolio tracking
- [ ] Mobile app (React Native)
- [ ] Advanced reporting and analytics
- [ ] Multi-currency support
- [ ] Bank account integration
- [ ] Receipt scanning and OCR

### Version History
- **v1.0.0** - Initial release with core features
  - Wallet management
  - Income/expense tracking
  - Inter-wallet transfers
  - Category management
  - Dashboard and reporting

---

Made with ❤️ for better financial management
