"""Employee pay calculator."""
from contract_type import ContractType
from commission_type import CommissionType

class Contract:
    contract_type: ContractType
    pay: int
    hourly_rate: int
    number_of_hours: int

    def __init__(self, contract_type, pay=None, hourly_rate=None, number_of_hours=None):
        if (contract_type == ContractType.SALARY):
            self.pay = pay
            self.contract_type = contract_type
        if (contract_type == ContractType.HOURLY):
            self.hourly_rate = hourly_rate
            self.number_of_hours = number_of_hours
            self.pay = hourly_rate * number_of_hours
            self.contract_type = contract_type

class Commission:
    commission_type: CommissionType
    bonus: int
    rate: int
    number_of_contracts: int

    def __init__(self, commission_type, bonus=None, rate=None, number_of_contracts=None):
        if (commission_type == CommissionType.FIXED):
            self.bonus = bonus
            self.commission_type = commission_type
        if (commission_type == CommissionType.LINEAR):
            self.rate = rate
            self.number_of_contracts = number_of_contracts
            self.bonus = rate * number_of_contracts
            self.commission_type = commission_type

class Employee:
    name: str
    contract: Contract
    commission: Commission

    def __init__(self, name, contract=None, commission=None):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        return self.contract.pay + self.commission.bonus

    def __str__(self):
        if (self.contract.contract_type == ContractType.SALARY):
            if (self.commission.commission_type == CommissionType.FIXED):
                if (self.commission.bonus == 0):
                    return f"{self.name} works on a monthly salary of {self.contract.pay}. Their total pay is {self.get_pay()}."    
                return f"{self.name} works on a monthly salary of {self.contract.pay} and receives a bonus commission of {self.commission.bonus}. Their total pay is {self.get_pay()}."
            if (self.commission.commission_type == CommissionType.LINEAR):
                return f"{self.name} works on a monthly salary of {self.contract.pay} and receives a commission for {self.commission.number_of_contracts} contract(s) at {self.commission.rate}/contract.  Their total pay is {self.get_pay()}."
        if (self.contract.contract_type == ContractType.HOURLY):
            if (self.commission.commission_type == CommissionType.FIXED):
                if (self.commission.bonus == 0):
                    return f"{self.name} works on a contract of {self.contract.number_of_hours} hours at {self.contract.hourly_rate}/hour. Their total pay is {self.get_pay()}."    
                return f"{self.name} works on a contract of {self.contract.number_of_hours} hours at {self.contract.hourly_rate}/hour and receives a bonus commission of {self.commission.bonus}. Their total pay is {self.get_pay()}."
            if (self.commission.commission_type == CommissionType.LINEAR):
                return f"{self.name} works on a contract of {self.contract.number_of_hours} hours at {self.contract.hourly_rate}/hour and receives a commission for {self.commission.number_of_contracts} contract(s) at {self.commission.rate}/contract.  Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
contract_billie = Contract(ContractType.SALARY, pay = 4000)
commission_billie = Commission(CommissionType.FIXED, bonus = 0)
billie = Employee('Billie', contract_billie, commission_billie)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
contract_charlie = Contract(ContractType.HOURLY, hourly_rate = 25, number_of_hours = 100)
commission_billie = Commission(CommissionType.FIXED, bonus = 0)
charlie = Employee('Charlie', contract_charlie, commission_billie)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
contract_renee = Contract(ContractType.SALARY, pay = 3000)
commission_renee = Commission(CommissionType.LINEAR, rate = 200, number_of_contracts = 4)
renee = Employee('Renee', contract_renee, commission_renee)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
contract_jan = Contract(ContractType.HOURLY, hourly_rate = 25, number_of_hours = 150)
commission_jan = Commission(CommissionType.LINEAR, rate = 220, number_of_contracts = 3)
jan = Employee('Jan', contract_jan, commission_jan)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
contract_robbie = Contract(ContractType.SALARY, pay = 2000)
commission_robbie = Commission(CommissionType.FIXED, bonus = 1500)
robbie = Employee('Robbie', contract_robbie, commission_robbie)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
contract_ariel = Contract(ContractType.HOURLY, hourly_rate = 30, number_of_hours = 120)
commission_ariel = Commission(CommissionType.FIXED, bonus = 600)
ariel = Employee('Ariel', contract_ariel, commission_ariel)
