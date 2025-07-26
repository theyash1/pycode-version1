from flask import Flask, request, jsonify
import secrets
import string
import re

app = Flask(__name__)

class PasswordManager:
    
    def __init__(self):
        self.minimum_length = 12
        self.password_blacklist = set(self.load_blacklist())
    
    def load_blacklist(self):
        return {"password", "123456", "123456789", "qwerty", "abc123", "password123"}
    
    def check_password_strength(self, password):
        missing_criteria = []

        if len(password) < self.minimum_length:
            missing_criteria.append("> Minimum password length is 12 characters.")
        
        if not re.search(r'[A-Z]', password):
            missing_criteria.append("> At least one uppercase letter required.")
        
        if not re.search(r'[a-z]', password):
            missing_criteria.append("> At least one lowercase letter required.")
        
        if not re.search(r'\d', password):
            missing_criteria.append("> At least one digit required.")
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            missing_criteria.append("> At least one special character required.")
        
        if password.lower() in self.password_blacklist:
            missing_criteria.append("> Password is too common or weak.")

        # Entropy check (basic)
        if self.calculate_entropy(password) < 40:
            missing_criteria.append("> Password lacks sufficient entropy (complexity).")
        
        return missing_criteria

    def calculate_entropy(self, password):
        
        char_set_size = len(set(password))
        entropy = len(password) * (char_set_size).bit_length()
        return entropy
    
    def generate_random_password(self):
        
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(self.minimum_length))
        
        
        while not any(c.isupper() for c in password) or not any(c.islower() for c in password) or \
              not any(c.isdigit() for c in password) or not any(c in string.punctuation for c in password):
            password = ''.join(secrets.choice(alphabet) for _ in range(self.minimum_length))
        
        return password

password_manager = PasswordManager()

@app.route('/check-password', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password')
    
    if not password:
        return jsonify({'error': 'Password is required.'}), 400
    
    missing_criteria = password_manager.check_password_strength(password)
    if missing_criteria:
        return jsonify({'isValid': False, 'missingCriteria': missing_criteria})
    else:
        return jsonify({'isValid': True, 'missingCriteria': []})

@app.route('/generate-password', methods=['GET'])
def generate_password():
    password = password_manager.generate_random_password()
    return jsonify({'password': password})

if __name__ == "__main__":
    app.run(debug=True)
