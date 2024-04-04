class User: 

    """A user account for the airline website.""" 

    def __init__(self, name, email, password): 
        """Initialize the user account with name, email, and password.""" 
        self.name = name 
        self.email = email 
        self.set_password(password) 

    def set_password(self, password): 
        """Set the user's password securely.""" 
        # In a real-world application, you would want to use a secure password hashing library 
        # to store a hashed version of the password instead of the plaintext password. 
        self._password = password 

    def change_password(self, new_password): 
        """Change the user's password.""" 
        self.set_password(new_password) 

    def login(self, email, password):
        """Login method to authenticate users."""
        if self.email == email and self._password == password:
            print("Login successful.")
            return True
        else:
            print("Invalid email or password.")
            return False

class Employee(User): 

    """An employee account for the airline website.""" 

    def __init__(self, name, email, password, employee_id): 
        """Initialize the employee account with name, email, password, and employee ID.""" 
        super().__init__(name, email, password) 
        self.employee_id = employee_id 

    def update_employee_info(self, new_name, new_email, new_password): 
        """Update the employee's name, email, and/or password.""" 
        self.name = new_name 
        self.email = new_email 
        self.change_password(new_password) 

# Create a new user account 
user = User('John Doe', 'john.doe@example.com', 'password123') 

# Change the user's password 
user.change_password('new_password456') 

# Create a new employee account 
employee = Employee('Jane Doe', 'jane.doe@example.com', 'password789', 'employee_123') 

# Update the employee's info 
employee.update_employee_info('Jane Smith', 'jane.smith@example.com', 'new_password012') 

# Attempt to log in
user.login('john.doe@example.com', 'new_password456')  # This should succeed
employee.login('jane.doe@example.com', 'new_password012')  # This should also succeed

