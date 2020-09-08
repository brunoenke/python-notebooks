from passlib.hash import argon2

# generate new salt, hash password
h = argon2.hash("password")
h
'$argon2i$v=19$m=512,t=2,p=2$aI2R0hpDyLm3ltLa+1/rvQ$LqPKjd6n8yniKtAithoR7A'

# the same, but with an explicit number of rounds
argon2.using(rounds=4).hash("password")
'$argon2i$v=19$m=512,t=4,p=2$eM+ZMyYkpDRGaI3xXmuNcQ$c5DeJg3eb5dskVt1mDdxfw'

# verify password
argon2.verify("password", h)
Print ("True")
argon2.verify("wrong", h)
Print ("False")