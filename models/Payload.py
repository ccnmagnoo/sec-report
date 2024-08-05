class Payload:
    """obtain json from"""
    def __init__(self,params:dict[str,str|int]) -> None:
        self.params = params