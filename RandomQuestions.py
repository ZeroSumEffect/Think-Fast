#
#    Random Question Generator for Think Fast!
#    Python 3.4
#
#    5 Dev 2017
#    by Zero Sum Effect
#

from random import randrange
import time

#saveQuestions = False  # Save questions to file or not
saveQuestions = True  # Save questions to file or not
pathtoFile = "" # (depending on OS) eg C:\directory\savehere\
numQuests = 100  # Number of Questions
linebreak = 5 # Line break every x

storeQ = [] 
storeItems = []
allQuestions = ""

# WARNING: Lists should contain more than 4 items

JKcrew = ["Bart", "Casey", "David", "Geo", "Gina", "Hoolia", "Jessica", 
            "Joe", "Josh", "Juila", "Nikki", "Steve", "Tiff"]

pronouns = ["you", "they", "we", "he", "she"]

beverages = ["coffee", "juice", "tea", "beer", "soda", "water", "cocktails", 
            "wine", "Sake", "Champagne", "hot chocolate", "milk", "milk shake",
            "tomato juice", "Bobo tea", "Capri Sun" , "Chamomile tea", "coconut milk", 
            "fruit punch", "green tea", "Kombucha tea", "Kool-aid", "lemonade", 
            "almond milk", "pomegranate juice", "prune juice", "Cola", "Root beer", 
            "Tang", "wheat grass", "Cappuccino"]
            
food = ["apples", "pies", "spaghetti", "McDees", "spring rolls", "doughnuts", 
        "pancakes", "carrot cake", "bagels", "fairy cakes", "muffins", "eggs",
        "birthday cake", "cup cakes", "strawberries", "pop tarts",
        "asparagus", "avocados", "almonds", "Bruscetta", "bacon", "baked beans", "BBQ",
        "bread", "broccoli", "buritto", "babaganoosh", "cheese", "chicken", "chips",
        "crisps", "french fries", "chocolate", "chowder", "cookies", "corn", "crab",
        "curry", "cereal", "chimichanga", "dates", "duck", "dumplings", "donuts",
        "dim sum", "enchilada", "eggrolls", "garlic", "ginger", "granola", "grapes",
        "green beans", "guancamole", "Graham crackers", "ham", "hamburger", "honey",
        "huenos rancheros", "hash browns", "hot dogs", "haiku roll", "hummus", "ice cream",
        "Irish stew", "jambalaya", "jelly", "jerky", "jalapeño", "kale", "ketchup", "kiwi",
        "kidney beans", "lobster", "lamb", "lasagna", "meatballs", "noodles", "pizza",
        "pepperoni", "quesadillas", "quiche", "Reuben", "ramen", "spinach", "tater tots",
        "toast", "waffles", "walnuts", "yogurt", "Zucchini"]
        
dVerbs = ["hate", "kill", "slap", "kiss", "tickle", "punch", "sue", "runover", "date", "attack",
            "tackle", "hug"]

uVerbs = ["hate", "love", "loathe", "detest", "dislike", "adore", "worship", "idolize",
            "admire", "revere", "cherish", "applaud", "honour", "dishonour", "fancy",
            "defend", "attack", "accuse" ]

objects = ["bike", "car", "table", "chair", "helmet", "glove", "laptop", 
            "mug", "bag", "hat", "camera", "shoe", "phone", "book", "lipstick",
            "t-shirt", "wig", "wrench", "hammer", "pen", "pencil", "stapler",
            "toothbrush", "parachute"]

animals = ["baboon", "badger", "bald eagle", "bandicoot", "bat", "bear", "beaver", 
            "blue jay", "bonobo", "camel", "caribou", "carp", "chameleon", "cheetah",
            "chicken", "chimpanzee", "chinchilla", "chipmunk", "clownfish", "cobra",
            "condor", "boa constrictor", "cougar", "cow", "coyote", "crab", "crane",
            "crocodile", "crow", "cuckoo", "deer", "dingo", "dodo", "dog", "dolphin",
            "donkey", "dormouse", "dove", "dragonfly", "duck", "falcon", "ferret", 
            "finch", "fish", "flamingo", "fox", "frog", "flying squirrel", "gazelle",
            "gecko", "gerbil", "giant panda", "gibbon", "giraffe", "goat", "golden eagle",
            "goldfish", "gopher", "gorilla", "grasshopper", "great white shark",
            "grizzly bear", "guinea pig", "guppy", "haddock", "halibut", "hammerhead shark",
            "hamster", "hare", "hawk", "hedgehog", "hermit crab", "heron", "herring",
            "hippo", "hornet", "horse", "hummingbird", "humpback whale", "hyena", "kangaroo",
            "kingfisher", "koala", "lark", "lemming", "lemur", "leopard", "lion", "lionfish",
            "lizard", "llama", "macaw", "mackerel", "magpie", "mallard", "manatee",
            "manta ray", "marmoset", "meerkat","mink", "minnow", "mockingbird", "mole",
            "mongoose", "monkey", "moose", "mosquito", "mule", "narwhal", "newt", 
            "nightingale", "panda", "panther", "parakeet", "parrot", "parrotfish", "partridge",
            "peacock", "pelican", "penguin", "pheasant", "pig", "pigeon", "piranha","platypus",
            "polar bear", "pony", "porcupine", "possum", "prairie dog", "prawn", 
            "praying mantis", "puffin", "puma", "python", "rabbit", "raccoon", "rat",
            "rattlesnake", "raven", "red panda", "red squirrel", "reindeer", "rhino",
            "roadrunner", "rooster", "salamander", "salmon", "scorpion", "seahorse",
            "sea lion", "shark", "sheep", "shrew", "shrimp", "skunk", "sloth", "slug",
            "snail", "snake", "snow leopard", "sparrow", "sperm whale", "spider monkey",
            "tapir", "tarantula", "tasmanian devil", "tiger", "tiger shark", "toad",
            "tortoise", "toucan", "tree frog", "trout", "tuna", "turkey", "turtle",
            "wallaby", "walrus", "wasp", "warbler", "water buffalo", "weasel", "whale",
            "whippet", "whooping crane", "wild boar", "wildcat", "wildebeest", "wolf",
            "wolverine", "wombat", "woodchuck", "woodpecker", "swan", "zebra", "camel", "cat"]

favPeople = ["cartoon character", "superhero", "actor", "actress", "comedian", 
                "youTuber", "instagrammer", "artist", "singer", "teacher",
                "babysitter", "painter", "plumber", "Doctor", "Jedi", "robot",
                "Pokémon", "dentist", "clown", "friend"]

jobs = ["animator", "architect", "astronomer", "baker", "beekeeper", "butler", 
            "car mechanic", "carpenter", "ballerina", "cheese maker", "chimney sweep",
            "cook", "disc jockey", "electrician", "fashion designer", "film critic",
            "flying instructor", "fortune teller", "gardener", "historian", 
            "interior designer", "judge", "lift attendant", "master of ceremonies",
            "midwife", "mountain guide", "musician", "pharmacist", "philosopher",
            "photographer", "physicist", "physiotherapist", "sculptor", "editor",
            "captain", "songwriter", "zookeeper"]

adjectives = ["late", "great", "wet", "funny", "happy", "sad", "early", "mad", "loco", 
                "brazen", "adorable", "cute", "thirsty", "salty", "sour", "tangy", "cold",
                "chilly", "prickly", "filthy", "flaky", "warm", "charming", "chatty", 
                "quiet", "loud", "nosy", "grumpy", "manic", "excited", "exhausted", 
                "fierce", "fine", "angry", "annoyed", "brave", "afraid", "embarrassed",
                "nervous", "rundown", "scary", "quirky", "mysterious", "fantastic",
                "frantic", "grateful", "good", "creepy", "hungry", "thoughtful",
                "defiant", "tired", "zany", "enchanting", "delightful", "boring", "bad",
                "amused", "lucky", "enthusiastic", "foolish", "glorious", "smart",
                "helpful", "sassy", "shy", "inquisitive", "interesting", "insane", "sleepy",
                "swanky", "macho", "clever", "fragile", "brainy", "angelic", "calm", "busy",
                "cautious", "innocent", "chilish", "gifted", "mushy", "testy", "terrific",
                "uninterested", "perky", "wild", "womanly", "manly", "powerful", "puzzled",
                "erratic", "evil", "wrong", "tacky", "crushed", "clumsy", "cracked", "cute",
                "wild", "becoming", "bloody", "average", "dull", "gabby", "jolly", "itchy"]
                
pParticiples = ["arrested", "stuffed", "injured", "wrecked", "dancing", 
                        "crying", "hiding", "lying", "fidgeting", "cooking", "driving",
                        "sleeping", "waving", "baking", "shrinking", "vloging", "trespassing"]

toName = ["mean", "kind", "nice", "cold", "talking", "friendly"]

languages = ["Cantonese", "Mandarin", "Czech", "Croatian", "Danish", "Dutch", "Finnish", "French",
                "German", "Greek", "Hungarian", "Indonesian", "Irish", "Italian", "Japanese", "Latin",
                "Persian", "Polish", "Portuguese", "Russian", "Spanish", "Swedish", "Thai", "Turkish",
                "Vietnamese"]

illness = ["pink eye", "a sore throat", "the flu", "asthma", "chickenpox", "a cold sore", "a cold",
            "constipation", "a cough", "diabetes", "diarrhoea", "dizziness", "dry mouth",
            "earache", "erectile dysfunction", "a fever", "food poisoning", "gallstones",
            "genital warts", "glandular fever", "gout", "haemorrhoids", "hay fever",
            "headaches", "hearing loss", "head lice", "insomnia", "an irritable hip", "an itchy bottom",
            "kidney stones", "leg cramps", "malaria", "measles", "meningitis", "menopause",
            "mumps", "a nosebleed", "pneumonia", "shingles", "stress", "sunburn", "swollen glands",
            "tonsillitis", "a toothache", "vaginal thrush", "vertigo", "eczema", "warts",
            "yellow fever"]

countries =["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia",
            "Aruba", "Australia", "Austria", "Azerbaijan", "The Bahamas", "Bahrain",
            "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Bhutan", "Bolivia",
            "Botswana", "Brazil", "Brunei", "Bulgaria", "Burma", "Burundi", "Cambodia",
            "Cameroon", "Canada", "Cabo Verde", "Chad", "Chile", "China", "Colombia", 
            "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Denmark", "Djibouti",
            "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Estonia", "Ethiopia",
            "Fiji", "Finland", "France", "The Gambia", "Germany", "Ghana", "Greece", "Grenada",
            "Guatemala", "Guinea", "Haiti", "Honduras", "Hong Kong", "Hungary", "Iceland",
            "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica",
            "Japan", "Jordan", "Laos", "Latvia", "Lebanon", "Liberia", "Libya", "Liechtenstein",
            "Lithuania", "Luxembourg", "London", "Macau", "Macedonia", "Madagascar", "Malaysia", 
            "the Maldives", "Malta", "Marshall Islands", "Mauritius", "Mexico", "Moldova", "Monaco",
            "Mongolia", "Montenegro", "Morocco", "Mozambique", "Namibia", "Nepal", "Netherlands",
            "New Zealand", "Nicaragua", "Nigeria", "North Korea", "Norway", "Oman", "Pakistan",
            "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal",
            "Qatar", "Romania", "Russia", "Rwanda", "Saint Lucia", "Samoa", "San Marino",
            "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", 
            "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "Spain",
            "Sri Lanka", "Sudan", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan",
            "Tanzania", "Thailand", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey",
            "Ukraine", "United Kingdom", "Uruguay", "Venezuela", "Vietnam", "Yemen", "Joemalia",
            "Zimbabwe"]
            
colours = ["red", "orange", "yellow", "green", "cyan", "blue", "indigo", "violet", "purple",
            "magenta", "pink", "brown", "white", "gray", "black", "teal"]

numbers = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
            "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
            "nineteen", "twenty"]

qList = {   0: (("Who ate all the ", food, "?")), 
            1: (("Who drank all the ", beverages, "?")), 
            2: (("Who did ", JKcrew + pronouns," ", dVerbs, "?")), 
            3: (("Who stole the ", objects, "?")),
            4: (("Who took ", JKcrew,"'s ", objects + food + beverages, "?")),
            5: (("Who is ", JKcrew, "'s favourite ", favPeople, "?")),
            6: (("Who is your favourite ", favPeople, "?")),
            7: (("Why were you ", pParticiples, "?")),
            8: (("Why was ", JKcrew, " ", pParticiples, "?")),
            9: (("Why did ", JKcrew, " take ", JKcrew,"'s ", objects + food + beverages, "?")),
            10: (("Why are you so ", adjectives, "?")),
            11: (("Why is ", JKcrew, " so ", adjectives, "?")),
            12: (("Why are you so ", toName, " to ", JKcrew,"?")),
            13: (("How do you make ", beverages + food,"?")),
            14: (("How do you say ", food + objects + beverages + animals, " in ", languages, "?")),
            15: (("Why do you ", uVerbs, " me?")),
            16: (("Why does ", JKcrew, " ", uVerbs, " ", JKcrew, "?")),
            17: (("How much does a ", objects + animals, " weigh?")),
            18: (("How heavy is a ", animals, "?")),
            19: (("How big is a ", objects + animals, "?")),
            20: (("What's the deal with ", objects + animals, "s?")),
            21: (("What's a combination of a ", objects + animals, " and ", objects + animals, " called?")),
            22: (("What's it called when two ", animals, "s kiss?")),
            22: (("How does ", JKcrew, " look today?")),
            23: (("How young is ", JKcrew, "?")),
            24: (("How did you get ", illness, "?")),
            25: (("How did ", JKcrew, " get ", illness, "?")),
            26: (("How many people are there in ", countries, "?")),
            27: (("What's the favourite activity in ", countries, "?")),
            28: (("What was ", JKcrew, " doing in ", countries, "?")),
            29: (("What is your ", favPeople + animals + objects," doing right now?")),
            30: (("Where is your ", favPeople + animals + objects," right now?")),
            31: (("What would be a good name for a ", jobs + favPeople + objects, " for ", animals,"s?")),
            32: (("What would be a better name for ", jobs + favPeople + animals + objects,"s?")),
            33: (("What are ", animals + objects,"s made out of?")),
            34: (("What are the names of the two ", jobs+favPeople, "s?")),
            35: (("What are ", favPeople + animals + objects,"s?")),
            36: (("What are ", jobs+favPeople + animals + objects,"s good for?")),
            37: (("What colour is your ", objects + animals,"?")),
            38: (("What's a cool greeting in ", countries, "?")),
            39: (("What would a ", animals, " call a ", jobs+ favPeople + objects, "?")),
            40: (("Where would ", JKcrew+ pronouns, " be ", pParticiples, " in ", countries, "?")),
            41: (("How would ", JKcrew+ pronouns, " find a ", jobs+favPeople + animals + objects, " in ", countries, "?")),
            42: (("How would ", JKcrew+ pronouns, " give ", illness, " to a ", animals + objects, "?")),
            43: (("Why would ", animals + objects, "s have ", illness, "?")),
            44: (("Why would ", animals, "s like videos of ", animals + objects, "s?")),
            45: (("Why do the ", languages, " ", jobs, "s like memes of ", JKcrew + animals + objects, "s?")),
            46: (("Why would ", JKcrew, " carry a ", animals + objects, " in ", countries, "?")),
            47: (("Why would ", JKcrew, " be feeding ", food+ objects, " to a ", animals, "?")),
            48: (("What's the law in ", countries, " about ", food+ objects, "s and ", animals, "s?")),
            49: (("Why would the ", jobs+favPeople, " paint a ", animals + objects, " ", colours, "?")),
            50: (("Why does ", JKcrew, " have a ", colours, " ", animals + objects, "?")),
            51: (("What happened after ", JKcrew, " and a ", jobs+favPeople+animals, " walked into a bar?")),
            52: (("How would you fit a ", animals, " into a ", objects, "?")),
            53: (("What did ", JKcrew+ pronouns, " leave in ", countries, "?")),
            54: (("Why would ", JKcrew+ pronouns, " have ", numbers, " ", animals + objects, "s?")),
            55: (("Why does the ", animals, " like eating ", food, "?")),
            56: (("Where in ", countries, " would you find ", numbers, " ", animals + objects, "s?")),
            57: (("How many ", jobs+ animals + objects, "s are there in ", countries, "?")),
            58: (("What would a ", languages, " ", jobs + animals, " sound like?")),
            59: (("Who would like a ", colours, " ", animals + objects, "?")),
            60: (("Why did the ", jobs+favPeople+animals, " cross the road?")),
            61: (("Why did the ", jobs," ", dVerbs, " a ", animals,"?")),
            62: (("What's the capital of ", countries, "?")),
            63: (("How old is the ", jobs+favPeople+animals, "?")),
            }
            
            
def countList(myList):
    return len(myList)

def randNum(numrange):
    num = randrange(0, numrange)
    return num

def pickItem(itemList, storedList):
    itemRange = countList(itemList)
    numStored = len(storedList)
    if (numStored > 20):
        if (itemRange > 8):
            itemCap = 8
        else:
            itemCap = itemRange - 3
    else:
        itemCap = itemRange - 3
    lastItems = storedList[-itemCap:] # Last X stored items
    # Set upper limit of tries, to stop infinite looping
    tryLimit = itemRange * 4
    # Keep randomly picking items if it has been chosen before
    for i in range(tryLimit):
        newItem = itemList[randNum(itemRange)]
        # Check if item has already been chosen
        if not(newItem in storedList):
            storedList.append(newItem)
            break
    if ((i+1) == tryLimit):
        while (newItem in lastItems):
            newItem = itemList[randNum(itemRange)]
        storedList.append(newItem)
    
    return newItem
    
def makeQuestion(Q_args):
    tempStr = ""
    
    for Q_items in Q_args:
        if type(Q_items) is list:
            tempStr += pickItem(Q_items, storeItems)
        elif type(Q_items) is str:
            # Remove 's' if there's already a 's' in the item
            if (len(tempStr) > 0):
                if (tempStr[-1] == "s"):
                    tempItem = Q_items[0:2]
                    if ((tempItem == "s ") or (tempItem == "s?")):
                        Q_items = Q_items[1:]
            tempStr += Q_items
    return tempStr

tmplist = list(qList.keys())

lb = 0
for i in range(numQuests):
    tmpNum = pickItem(tmplist,storeQ)
    if (lb % linebreak == 0):
        allQuestions += "\n"
    allQuestions += makeQuestion(qList[tmpNum]) + "\n"

    lb += 1
print(allQuestions)

# Save questions to file
# Open new data file
if (saveQuestions):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    f = open(pathtoFile+"Questions" + timestr + ".txt", "w")
    f.write(allQuestions)
    f.close()
