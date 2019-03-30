import itertools
from multiprocessing.pool import Pool as ProcPool


class Grammar:
    """Apply production rules to strings."""

    def __init__(self, productions):
        """Initialize a Grammar with the given production rules.

        :param productions: The production rules for the Grammar.
        :type productions: dict
        """
        self.productions = productions
        self.symbols = frozenset(filter(str.isalpha, productions.keys()))
        self.pool = ProcPool()

    def __check_text_symbols(self, text):
        """Ensure the given text contains only known symbols."""
        for symbol in filter(str.isalpha, text):
            if symbol not in self.symbols:
                raise ValueError(f"Unknown symbol '{symbol}'")

    @staticmethod
    def _apply_symbol(args):
        symbol, rules = args
        return rules.get(symbol, symbol)

    def apply(self, text):
        """Apply the production rules to the given text."""
        self.__check_text_symbols(text)

        # Use a chunk size for efficiency with smaller text.
        return "".join(
            self.pool.imap(
                self._apply_symbol, zip(text, itertools.repeat(self.productions)), chunksize=64
            )
        )

    def iapply(self, axiom):
        """Return an infinite iterator to apply the production rules to the given axiom."""
        while True:
            axiom = self.apply(axiom)
            yield axiom
