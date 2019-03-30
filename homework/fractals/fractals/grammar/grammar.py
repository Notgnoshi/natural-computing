class Grammar:
    """Apply production rules to strings."""

    def __init__(self, productions):
        """Initialize a Grammar with the given production rules.

        :param productions: The production rules for the Grammar.
        :type productions: dict
        """
        self.productions = productions
        self.symbols = frozenset(filter(str.isalpha, productions.keys()))

    def __check_text_symbols(self, text):
        """Ensure the given text contains only known symbols."""
        for symbol in filter(str.isalpha, text):
            if symbol not in self.symbols:
                raise ValueError(f"Unknown symbol '{symbol}'")

    def apply(self, text):
        """Apply the production rules to the given text."""
        self.__check_text_symbols(text)
        return text

    def iapply(self, axiom):
        """Return an infinite iterator to apply the production rules to the given axiom."""
        while True:
            yield axiom
