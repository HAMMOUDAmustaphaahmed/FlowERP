-- Users table
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(64) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    first_name VARCHAR(64),
    last_name VARCHAR(64),
    password_hash VARCHAR(128) NOT NULL,
    role ENUM('admin', 'manager', 'employee', 'user') DEFAULT 'user',
    is_active BOOLEAN DEFAULT TRUE,
    company_id INT,
    department_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES company(id),
    FOREIGN KEY (department_id) REFERENCES department(id)
);

-- Company table
CREATE TABLE company (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    address VARCHAR(255),
    email VARCHAR(120),
    phone VARCHAR(32),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Department table
CREATE TABLE department (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    description TEXT,
    company_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES company(id)
);

-- Inventory table
CREATE TABLE inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    description TEXT,
    department_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES department(id)
);

-- Product table
CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    description TEXT,
    sku VARCHAR(32) NOT NULL UNIQUE,
    quantity INT DEFAULT 0,
    min_stock_alert INT DEFAULT 0,
    unit_price DECIMAL(12,2) DEFAULT 0.00,
    location VARCHAR(64),
    inventory_id INT,
    image_path VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (inventory_id) REFERENCES inventory(id)
);

-- Purchase Request table
CREATE TABLE purchase_request (
    id INT AUTO_INCREMENT PRIMARY KEY,
    number VARCHAR(32) NOT NULL UNIQUE,
    status ENUM('draft','pending','approved','rejected','ordered','received') DEFAULT 'draft',
    department_id INT,
    user_id INT,
    date_requested DATE,
    date_required DATE,
    priority ENUM('low','medium','high') DEFAULT 'medium',
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES department(id),
    FOREIGN KEY (user_id) REFERENCES user(id)
);

-- Purchase Request Item table
CREATE TABLE purchase_request_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    purchase_request_id INT,
    product_id INT,
    name VARCHAR(128),
    quantity INT,
    unit_price DECIMAL(12,2),
    FOREIGN KEY (purchase_request_id) REFERENCES purchase_request(id),
    FOREIGN KEY (product_id) REFERENCES product(id)
);

-- Quotation table
CREATE TABLE quotation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    number VARCHAR(32) NOT NULL UNIQUE,
    purchase_request_id INT,
    supplier_name VARCHAR(128),
    supplier_email VARCHAR(120),
    supplier_phone VARCHAR(32),
    status ENUM('draft','sent','accepted','rejected') DEFAULT 'draft',
    total_amount DECIMAL(12,2),
    payment_terms VARCHAR(128),
    delivery_time VARCHAR(128),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (purchase_request_id) REFERENCES purchase_request(id)
);

-- Quotation Item table
CREATE TABLE quotation_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quotation_id INT,
    product_id INT,
    name VARCHAR(128),
    quantity INT,
    unit_price DECIMAL(12,2),
    FOREIGN KEY (quotation_id) REFERENCES quotation(id),
    FOREIGN KEY (product_id) REFERENCES product(id)
);

-- Invoice table
CREATE TABLE invoice (
    id INT AUTO_INCREMENT PRIMARY KEY,
    number VARCHAR(32) NOT NULL UNIQUE,
    quotation_id INT,
    status ENUM('unpaid','paid','overdue') DEFAULT 'unpaid',
    due_date DATE,
    paid BOOLEAN DEFAULT FALSE,
    total_amount DECIMAL(12,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (quotation_id) REFERENCES quotation(id)
);

-- Delivery Note table
CREATE TABLE delivery_note (
    id INT AUTO_INCREMENT PRIMARY KEY,
    number VARCHAR(32) NOT NULL UNIQUE,
    purchase_request_id INT,
    received BOOLEAN DEFAULT FALSE,
    date_received DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (purchase_request_id) REFERENCES purchase_request(id)
);