# pwd_gen_with.py

# Simple Password Generator

This Python script generates random passwords based on user-defined criteria. You can specify the minimum length of the password and whether you want to include numbers and special characters in the generated password.

## How It Works

1. The script first defines three character sets:
   - `letters`: Lowercase and uppercase letters
   - `digits`: Numerical digits (0-9)
   - `special`: Special characters (e.g., !@#$%^&*)

2. It combines these character sets based on user preferences to create the `characters` string.

3. The script initializes an empty string called `pwd` to store the generated password.

4. It also sets `meets_criteria`, `has_number`, and `has_special` flags to False to ensure that the generated password meets the specified criteria.

5. The script enters a loop to generate the password:
   - It randomly selects characters from the `characters` string and appends them to `pwd`.
   - It checks whether the selected character is a digit and updates the `has_number` flag accordingly.
   - It checks whether the selected character is a special character and updates the `has_special` flag accordingly.
   - It evaluates whether the generated password meets the criteria:
     - If numbers are required, it checks if `has_number` is True.
     - If special characters are required, it checks if `has_special` is True.

6. The loop continues until the password meets the criteria and has reached the specified minimum length.

7. Finally, the generated password is displayed to the user.

## Usage

To use the password generator, follow these steps:

1. Run the `password_gen.py` script. 
  (If you prefer using Jupyter Notebook, you can do so as well.)

2. Enter the minimum length for the password when prompted.

3. Respond to the following prompts:
   - "Include numbers? (y/n):" - Enter 'y' for yes or 'n' for no.
   - "Include special characters? (y/n):" - Enter 'y' for yes or 'n' for no.

4. The script will generate a password based on your criteria and display it.

## Example

Here's an example of running the script:

```python
Enter minimum length: 12
Include numbers? (y/n): y
Include special characters? (y/n): n
The generated password is: 9LwT9tF3nEuk
