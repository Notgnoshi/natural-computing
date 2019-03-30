class Grammar:
    """Apply production rules to strings."""

    def __init__(self, productions):
        """Initialize a Grammar with the given production rules.

        :param productions: The production rules for the Grammar.
        :type productions: dict
        """
        self.productions = productions
        self.symbols = frozenset(filter(str.isalpha, productions.keys()))

    def apply(self, text):
        """Apply the production rules to the given text."""
        return text

    def iapply(self, axiom):
        """Return an infinite iterator to apply the production rules to the given axiom."""
        while True:
            yield axiom
