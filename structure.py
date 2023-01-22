# File includes structure used in the task in the form of class
class Detail:
    id: str
    name: str
    amount: int

    # base constructor with required parameters
    def __init__(self, id: str = None, name: str = None, amount: int = None) -> None:
        self.id=id
        self.name=name
        self.amount=amount
    # override of to_string method for the puspose of writing detail's data into the output file
    def __str__(self):
        return self.id+";"+self.name+";"+self.amount+";\n"

    def getFieldValue(self,field):
        if field==Field.id:
            return self.id
        elif field==Field.name:
            return self.name.lower()
        elif field==Field.amount:
            return int(self.amount)

# class to allow extraction of the values from Detail field
class Field:
    id = "id"
    name = "name"
    amount = "amount"