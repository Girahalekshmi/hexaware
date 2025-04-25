class OverDraftLimitExceededException(Exception):
    def __init__(self, message="Overdraft limit exceeded."):
        super().__init__(message)
