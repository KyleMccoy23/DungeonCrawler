from item import Item

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

ironSword = Weapon(name="Iron Sword",
                    weaponType="sharp",
                    damage=5,
                    value=10)

shortBow = Weapon(name="Short Bow",
                   weaponType="ranged",
                   damage=4,
                   value=8)

fists = Weapon(name="Fists",
               weaponType="blunt",
               damage=2,
               value=0)

class SpecialWeapon(Weapon):
    def __init__(self, 
                 name: str, 
                 weaponType: str, 
                 damage: int, 
                 value: int,
                 *atributes) -> None:
        super().__init__(name, 
                         weaponType, 
                         damage, 
                         value)
        self.atributes = atributes