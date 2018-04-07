from random import *

for i in range(0, 50):
    numEnemies = randint(1, 5);
    distanceToClosestEnemy = randint(0, 14);
    distanceToBigBad = randint(0, 14);
    if (randint(0, 3) < 3):
        distanceToBigBad = distanceToClosestEnemy;
    flankingStatus = randint(-1, 1);
    if flankingStatus is 0:
        flankingStatus = -1;
    abilityToFlank = randint(-1, 1);
    if abilityToFlank is 0:
        abilityToFlank = 1;
    if flankingStatus is 1:
        abilitytoFlank = 1;
    sizes = [-2, -1, 0, 1, 2, 4]
    closestEnemySize = sample(sizes, 1)[0];
    bigBadSize = closestEnemySize;
    if (numEnemies == 1):
        bigBadSize = closestEnemySize;
    if randint(0, 3) is 0:
        bigBadSize = sample(sizes, 1)[0];
    canReachBad = -1;
    if (bigBadSize <= 1):
        canReachBad = 1;
    if (distanceToBigBad <= 1):
        canReachBad = 1;
    health = randint(1, 12);
    enemyHitRate = randint(0, 101)/100.0;
    if (randint(0, 3) is 0):
        enemyHitRate = 1;
    yourHitRate = randint(0, 101)/100.0;
    if (randint(0, 3) is 0):
        yourHitRate = 1;
    maxDamage = randint(0, 20);
    
    print(numEnemies, distanceToClosestEnemy, distanceToBigBad, flankingStatus, abilityToFlank, closestEnemySize, 
          bigBadSize, canReachBad, health, enemyHitRate, yourHitRate, maxDamage, sep="\t");