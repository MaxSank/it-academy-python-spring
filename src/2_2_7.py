"""
House Password: Simple

Stephan and Sophia forget about security and
use simple passwords for everything. Help
Nikola develop a password security check module.
The password will be considered strong enough if
its length is greater than or equal to 10 symbols,
it has at least one digit, as well as containing
one uppercase letter and one lowercase letter in
it. The password contains only ASCII latin letters
or digits.

Input: A password as a string.

Output: Is the password safe or not as a boolean
or any data type that can be converted and
processed as a boolean. In the results you
will see the converted results.

Precondition:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64
"""


def checkio(data: str) -> bool:
    if 10 <= len(data) <= 64:

        for symbol in data:
            if "0" <= str(symbol) <= "9":
                for symbol in data:
                    if "a" <= str(symbol) <= "z":
                        for symbol in data:
                            if "A" <= str(symbol) <= "Z":
                                return True
                            else:
                                pass
                    else:
                        pass
            else:
                pass
    if None:
        pass
    else:
        return False


print(checkio("!@aaaaaaaaaaaaaaaaaaaA"))
