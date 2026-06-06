class Solution:
    def defangIPaddr(self, address: str) -> str:
        """Replace every '.' in an IPv4 address with '[.]'.

        Args:
            address: A valid IPv4 address string.

        Returns:
            The defanged IP address string.
        """
        return address.replace(".", "[.]")
