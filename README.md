# FlowERP 🚀

**A Complete Enterprise Resource Planning System**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)](https://mysql.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

FlowERP is a modern, secure, and scalable Enterprise Resource Planning system built with Flask. It provides comprehensive business management tools including inventory management, purchase workflows, department collaboration, and complete product lifecycle tracking.

## 🌟 Key Features

### 🏢 **Multi-Company Management**
- Complete company registration and profile management
- Isolated data for each company
- Customizable company settings and preferences

### 👥 **Advanced User Management**
- Secure authentication with session management
- Role-based access control (RBAC)
- Department-based permissions (read/write)
- Account lockout protection against brute force attacks

### 🏛️ **Department Organization**
- Flexible department structure
- Custom department creation
- User assignment with granular permissions
- Inter-department collaboration tools

### 📦 **Smart Inventory Management**
- Multiple inventories per department
- Customizable product columns
- Real-time stock tracking
- Low stock alerts and notifications
- Complete product lifecycle management

### 🛒 **Automated Purchase Workflow**
- Purchase request creation and approval
- Automatic routing to purchasing department
- Multi-supplier quotation management
- Invoice generation and tracking
- Delivery note verification
- Automatic stock updates

### 📊 **Complete Traceability**
- Full product history tracking
- Price change auditing
- Transfer and delivery logging
- User action audit trails
- Comprehensive reporting system

### 🔐 **Enterprise-Grade Security**
- Protection against SQL injection, XSS, and CSRF
- Secure password hashing
- Session management with timeouts
- Input validation and sanitization
- Security headers implementation

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- MySQL 8.0+
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flowERP.git
cd flowERP
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

```bash
# Create MySQL database
mysql -u root -p
CREATE DATABASE flowerp_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'flowerp_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON flowerp_db.* TO 'flowerp_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 5. Environment Configuration

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=mysql+pymysql://flowerp_user:your_password@localhost/flowerp_db
FLASK_ENV=development
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

### 6. Initialize Database

```bash
python scripts/init_db.py
```

### 7. Run the Application

```bash
python app.py
```

Visit `http://localhost:5000` to access FlowERP!

## 📁 Project Structure

```
FlowERP/
├── app/                    # Main application package
│   ├── models/            # Database models
│   ├── auth/              # Authentication blueprint
│   ├── admin/             # Admin management
│   ├── inventory/         # Inventory management
│   ├── purchase/          # Purchase workflow
│   ├── department/        # Department management
│   ├── api/               # REST API
│   ├── utils/             # Utility functions
│   ├── static/            # CSS, JS, images
│   └── templates/         # HTML templates
├── tests/                 # Test files
├── docs/                  # Documentation
├── scripts/               # Utility scripts
└── docker/                # Docker configuration
```

## 🎯 Core Modules

### Authentication & Security
- Secure login/logout system
- Password strength validation
- Session management
- Account lockout protection

### Inventory Management
- Create unlimited inventories per department
- Add custom columns for specific needs
- Track product quantities and locations
- Generate alerts for low stock

### Purchase Workflow
1. **Request Creation** - Departments create purchase requests
2. **Automatic Routing** - Requests sent to purchasing department
3. **Quotation Management** - Multiple supplier quotes
4. **Approval Process** - Review and approve quotations
5. **Invoice Generation** - Automatic invoice creation
6. **Delivery Tracking** - Delivery note verification
7. **Stock Update** - Automatic inventory updates

### Department Management
- Create custom departments
- Assign users with specific permissions
- Manage department-specific inventories
- Track inter-department transfers

## 🔧 Configuration

### Database Configuration

Edit `config.py` to configure database settings:

```python
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/flowerp_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Additional configuration...
```

### Security Settings

FlowERP includes comprehensive security features:

- **CSRF Protection**: Enabled by default
- **SQL Injection**: SQLAlchemy ORM protection
- **XSS Protection**: Input sanitization with bleach
- **Session Security**: Secure cookies and timeouts
- **Password Security**: Werkzeug hashing

### Email Configuration

Configure email settings in `.env`:

```env
MAIL_SERVER=your-smtp-server
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=your-email
MAIL_PASSWORD=your-password
```

## 📚 API Documentation

FlowERP provides a RESTful API for integration with external systems.

### Authentication

```bash
POST /api/auth/login
Content-Type: application/json

{
  "username": "your-username",
  "password": "your-password"
}
```

### Inventory Management

```bash
# Get all products
GET /api/inventory/products

# Create new product
POST /api/inventory/products
Content-Type: application/json

{
  "name": "Product Name",
  "sku": "SKU123",
  "quantity": 100,
  "price": 29.99
}
```

### Purchase Requests

```bash
# Create purchase request
POST /api/purchase/requests
Content-Type: application/json

{
  "department_id": 1,
  "priority": "high",
  "description": "Urgent supplies needed",
  "items": [
    {
      "product_name": "Office Supplies",
      "quantity": 50,
      "estimated_price": 15.00
    }
  ]
}
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_inventory.py

# Run with coverage
python -m pytest --cov=app tests/
```

## 🚀 Deployment

### Using Docker

```bash
# Build image
docker build -t flowERP .

# Run container
docker run -p 5000:5000 flowERP
```

### Using Docker Compose

```bash
docker-compose up -d
```

### Production Deployment

1. **Set environment variables**:
```bash
export FLASK_ENV=production
export DATABASE_URL=mysql+pymysql://user:password@host/db
```

2. **Use a production WSGI server**:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

3. **Configure reverse proxy** (Nginx recommended)

## 🔒 Security Best Practices

- **Keep dependencies updated**: Regularly update requirements
- **Use environment variables**: Never hardcode secrets
- **Enable HTTPS**: Use SSL certificates in production
- **Regular backups**: Implement database backup strategy
- **Monitor logs**: Set up log monitoring and alerts
- **Access control**: Implement proper user permissions

## 📊 Performance Optimization

- **Database indexing**: Optimize queries with proper indexes
- **Caching**: Implement Redis for session and data caching
- **Static files**: Use CDN for static assets
- **Connection pooling**: Configure database connection pooling
- **Monitoring**: Set up application performance monitoring

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 coding standards
- Write unit tests for new features
- Update documentation as needed
- Ensure security best practices

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: Check the `docs/` folder for detailed guides
- **Issues**: Report bugs on [GitHub Issues](https://github.com/yourusername/flowERP/issues)
- **Email**: support@flowERP.com
- **Community**: Join our [Discord](https://discord.gg/flowERP)

## 🗺️ Roadmap

### Version 2.0 (Planned)
- [ ] Advanced reporting and analytics
- [ ] Mobile application
- [ ] Integration with external accounting systems
- [ ] Advanced workflow automation
- [ ] AI-powered inventory predictions

### Version 1.5 (In Progress)
- [x] REST API implementation
- [ ] Enhanced user interface
- [ ] Advanced search and filtering
- [ ] Bulk operations support

## 🙏 Acknowledgments

- Flask community for the excellent framework
- SQLAlchemy for robust database ORM
- All contributors and testers
- Open source community

## 📈 Stats

- **Lines of Code**: ~15,000+
- **Test Coverage**: 90%+
- **Supported Languages**: English, French (more coming)
- **Database Support**: MySQL, PostgreSQL, SQLite

---

**Made with ❤️ for the business community**

*FlowERP - Streamline your business operations with confidence*