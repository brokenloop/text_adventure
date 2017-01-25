class Enemy:
    """Basic class for an enemy"""

    def __init__(self, hp, attack_power):
        self.hp = hp
        self.attack_power = attack_power

    def reduce_health(self, damage):
        self.hp -= damage

enemy_list = [Enemy(10, 2), Enemy(20, 4)] #This shows how to initialize multiple instance objects in a list

print ("The hp of the first enemy is:", enemy_list[0].hp) #this shows how to access those instance objects,
print ("The hp of the second enemy is:", enemy_list[1].hp)



enemy_library = {(0, 0): Enemy(10, 2), }

print(enemy_library[(0, 0)].hp)