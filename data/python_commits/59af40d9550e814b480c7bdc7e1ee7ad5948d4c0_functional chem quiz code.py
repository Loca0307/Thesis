import random

names = [
    'hydrogen', 'helium', 'lithium', 'beryllium', 'boron', 'carbon', 'nitrogen', 'oxygen', 'fluorine', 'neon', 'sodium', 'magnesium', 'aluminium', 'silicon', 
    'phosphorus', 'sulfur', 'chlorine', 'argon', 'potassium', 'calcium', 'scandium', 'titanium', 'vanadium', 'chromium', 'manganese', 'iron', 'cobalt', 'nickel', 
    'copper', 'zinc', 'gallium', 'germanium', 'arsenic', 'selenium', 'bromine', 'krypton', 'rubidium', 'strontium', 'yttrium', 'zirconium', 'niobium', 
    'molybdenum', 'technetium', 'ruthenium', 'rhodium', 'palladium', 'silver', 'cadmium', 'indium', 'tin', 'antimony', 'tellurium', 'iodine', 'xenon', 
    'cesium', 'barium', 'lanthanum', 'cerium', 'praseodymium', 'neodymium', 'promethium', 'samarium', 'europium', 'gadolinium', 'terbium', 'dysprosium', 
    'holmium', 'erbium', 'thulium', 'ytterbium', 'lutetium', 'hafnium', 'tantalum', 'tungsten', 'rhenium', 'osmium', 'iridium', 'platinum', 'gold', 'mercury', 
    'thallium', 'lead', 'bismuth', 'polonium', 'astatine', 'radon', 'francium', 'radium', 'actinium', 'thorium', 'protactinium', 'uranium', 'neptunium', 
    'plutonium', 'americium', 'curium', 'berkelium', 'californium', 'einsteinium', 'fermium', 'mendelevium', 'nobelium', 'lawrencium', 'rutherfordium', 
    'dubnium', 'seaborgium', 'bohrium', 'hassium', 'meitnerium', 'darmstadtium', 'roentgenium', 'copernicium', 'nihonium', 'flerovium', 'moscovium', 
    'livermorium', 'tennessine', 'oganesson'
]
symbols = [
    'h', 'he', 'li', 'be', 'b', 'c', 'n', 'o', 'f', 'ne', 'na', 'mg', 'al', 'si','p', 's', 'cl', 'ar', 'k', 'ca', 'sc', 'ti', 'v', 'cr', 'mn', 'fe', 'co', 'ni', 
    'cu', 'zn', 'ga', 'ge', 'as', 'se', 'br', 'kr', 'rb', 'sr', 'y', 'zr', 'nb','mo', 'tc', 'ru', 'rh', 'pd', 'ag', 'cd', 'in', 'sn', 'sb', 'te', 'i', 'xe', 
    'cs', 'ba', 'la', 'ce', 'pr', 'nd', 'pm', 'sm', 'eu', 'gd', 'tb', 'dy', 'ho','er', 'tm', 'yb', 'lu', 'hf', 'ta', 'w', 're', 'os', 'ir', 'pt', 'au', 'hg', 
    'tl', 'pb', 'bi', 'po', 'at', 'rn', 'fr', 'ra', 'ac', 'th', 'pa', 'u', 'np','pu', 'am', 'cm', 'bk', 'cf', 'es', 'fm', 'md', 'no', 'lr', 'rf', 'db', 'sg', 
    'bh', 'hs', 'mt', 'ds', 'rg', 'cn', 'nh', 'fl', 'mc', 'lv', 'ts', 'og'
]
ato_num = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 
    43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 
    83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 
    118
]
groups = [
    1, 18, 1, 2, 13, 14, 15, 16, 17, 18, 1, 2, 13, 14, 15, 16, 17, 18, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 1, 2, 3, 4, 5, 6, 
    7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 
    1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
]
periods = [
    1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 
    5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]
try:
    print('This is a chem quiz')
    print('Input range of the quiz, in atomic number (e.g helium-boron is min=2, max=5)')
    min = int(input('Minimum atomic number is: '))
    max = int(input('Maximum atomic number is: '))
    num_questions = int(input('How long should the quiz be: '))
    print('Choose your quiz question (symbol, atomic number, name, group, period, random):')
    print('If chosen symbol, then name is shown and the symbol is the question')
    print('If chosen atomic number, then name is shown and the atomic numbers is the question')
    print('If chosen group, then name is shown and the group is the question')
    print('If chosen period, then name is shown and the period is the question')
    print('If chosen name, then symbol is shown and the name is the question')
    print('If chosen random, each question will have the aforemensioned parts randomised')
    question = str(input('What is your choice:'))
    i=0
    for i in range(0,num_questions):
        ranint = random.randint(min,max)
        ranint = ranint-1 #for list as list begins at zero
        if question.lower() == 'name':
            print(symbols[ranint])
            answer1 = str(input('The name is? '))
            if answer1.lower() == names[ranint]:
                print('Correct!')
            else:
                print('Incorrect')
                print(names[ranint])
        elif question.lower() == 'symbol':
            print(names[ranint])
            answer1 = str(input('The symbols is? '))
            if answer1.lower() == symbols[ranint]:
                print('Correct!')
            else:
                print('Incorrect')
                print(symbols[ranint]) 
        elif question.lower() == 'atomic number':
            print(names[ranint])
            answer1 = int(input('The atomic number is? '))
            if answer1 == ato_num[ranint]:
                print('Correct!')
            else:
                print('Incorrect')
                print(ato_num[ranint]) 
        elif question.lower() == 'group':
            print(names[ranint])
            answer1 = int(input('The group is? '))
            if answer1 == groups[ranint]:
                print('Correct!')
            else:
                print('Incorrect')
                print(groups[ranint]) 
        elif question.lower() == 'period':
            print(names[ranint])
            answer1 = int(input('The period is? '))
            if answer1 == periods[ranint]:
                print('Correct!')
            else:
                print('Incorrect')
                print(periods[ranint])
        elif question.lower() == 'random':
            ranrand = random.randint(1,5) #1 = names, 2=symbols,3=atomic num, 4=groups, 5=periods,
            if ranrand > 1 or ranrand <= 5:
                print(names[ranint])
                if ranrand == 2:
                    answer1 = str(input('The symbols is? '))
                    if answer1.lower() == symbols[ranint]:
                        print('Correct!')
                    else:
                        print('Incorrect')
                        print(symbols[ranint]) 
                elif ranrand == 3:
                    answer1 = int(input('The atomic number is? '))
                    if answer1 == ato_num[ranint]:
                        print('Correct!')
                    else:
                        print('Incorrect')
                        print(ato_num[ranint]) 
                elif ranrand == 4:
                    answer1 = str(input('The group is? '))
                    if answer1 == groups[ranint]:
                        print('Correct!')
                    else:
                        print('Incorrect')
                        print(groups[ranint])
                elif ranrand == 5:
                    answer1 = int(input('The period is? '))
                    if answer1 == periods[ranint]:
                        print('Correct!')
                    else:
                        print('Incorrect')
                        print(periods[ranint])
            elif ranrand == 1:
                print(symbols[ranint])
                answer1 = int(input('The name is? '))
                if answer1.lower() == names[ranint]:
                    print('Correct!')
                else:
                    print('Incorrect')
                    print(names[ranint])

        else:
            print('Incorrect input') 
            break

except ValueError:
    print('There has been a value error')







