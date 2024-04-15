from item import Item, Weapon, SpecialWeapon, Potion


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

healingPotion = Potion(name='Healing Potion',
                     value=5,
                     effect="healing",
                     potency=1)

excaliber = SpecialWeapon("Excaliber",
                          "Sword",
                          999,
                          9999999,
                          "UBBRAKABLE",
                          "HOLY")

iron = Item(name="Iron",
            value=2,
            type="ingot")

stick = Item(name="stick",
             value=1,
             type='item')
