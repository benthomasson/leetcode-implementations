class Solution:
    def merge_nodes_between_zeros(self, password: str) -> bool:
        """Check if a password is strong based on 6 criteria.

        Args:
            password: The password string to validate.

        Returns:
            True if the password is strong, False otherwise.
        """
        if len(password) < 8:
            return False

        has_lower = has_upper = has_digit = has_special = False
        specials = set("!@#$%^&*()-+ ")

        for i, ch in enumerate(password):
            if i > 0 and ch == password[i - 1]:
                return False
            if ch.islower():
                has_lower = True
            elif ch.isupper():
                has_upper = True
            elif ch.isdigit():
                has_digit = True
            if ch in specials:
                has_special = True

        return has_lower and has_upper and has_digit and has_special
