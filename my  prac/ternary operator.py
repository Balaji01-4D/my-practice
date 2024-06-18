age=19
voterid=True
if age>18 and voterid:
    print("adult: go and vote")
if age<18:
    print('child')
if age>18:
    if not(voterid):
        print("go and apply asap")