
class Item:
    def __init__(self, 
                 name: str, 
                 value: float, 
                 type: str, 
                 ) -> None:
        self.name = name
        self.value = value
        self.type = type

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

class Weapon(Item):
    def __init__(self,
                 name: str,
                 weaponType: str,
                 damage: int,
                 value: int
                 ) -> None:
        super().__init__(name, 
                         value, 
                         "weapon")
        self.weaponType = weaponType
        self.damage = damage

class SpecialWeapon(Weapon):
    def __init__(self, 
                 name: str, 
                 weaponType: str, 
                 damage: int, 
                 value: int,
                 *attributes) -> None:
        super().__init__(name, 
                         weaponType, 
                         damage, 
                         value)
        self.attributes = attributes

class Potion(Item):
    def __init__(self, name: str, value: float, effect: str, potency: int) -> None:
        super().__init__(name, value, "Potion")
        self.effect = effect
        self.potency = potency
