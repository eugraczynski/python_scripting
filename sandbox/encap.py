class _A:
    def _method(self):
        return 42

    def method(self):
        return self._method()
