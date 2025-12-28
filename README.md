BANKING MANAGEMENT SYSTEM 
CSE-101 lab project_1
Diğdem Edinç
    This project is a terminal-based banking management system developed using Phyton. It simulates a simple banking platform that features:
    -> Register an log in
    -> Deposit money
    -> Withdraw money
    -> Transfer money between accounts (provided that both accounts are registered.)
    -> View balance
    -> View transaction history
    -> Apply interest and monthly fees
    -> Simple admin functions
    -> Data storage with JSON 

File Structure
main.py – Menu loop and program entry point
user.py – User registration, login, and account management
bank_operations.py – Deposit, withdrawal, transfer, balance functions
file_manager.py – Load and save data using JSON files
report.py – Transaction history and basic reports
data/ – Stores users.json and transaction data
tests/ – Basic unit tests
