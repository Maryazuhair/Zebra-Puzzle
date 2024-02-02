from aima.logic import PropKB, dpll_satisfiable
from aima.utils import expr, Expr

# Initialize an empty list to store logical rules
rules_list = []

# Define categories for the puzzle
nationalities = ['Norwegian', 'Spaniard', 'Ukrainian']
pets = ['Dog', 'Fox', 'Zebra']
drinks = ['Milk', 'Tea', 'Juice']
houses = ['1', '2', '3']

# Generate rules for pets not being in the same house
for i in range(len(pets)):
    for j in range(len(houses)):
        for k in range(len(houses)):
            if j != k:
                rule = "~(" + pets[i] + houses[j] + " & " + pets[i] + houses[k] + ")"
                rules_list.append(rule)

# Generate rules for drinks not being in the same house
for i in range(len(drinks)):
    for j in range(len(houses)):
        for k in range(len(houses)):
            if j != k:
                rule = "~(" + drinks[i] + houses[j] + " & " + drinks[i] + houses[k] + ")"
                rules_list.append(rule)

# Generate rules for nationalities not being in the same house
for i in range(len(nationalities)):
    for j in range(len(houses)):
        for k in range(len(houses)):
            if j != k:
                rule = "~(" + nationalities[i] + houses[j] + " & " + nationalities[i] + houses[k] + ")"
                rules_list.append(rule)


# Generate rules for unique drinks in each house
for house in houses:
    statement = ""
    for i in range(len(drinks)):
        statement = statement + '(' + drinks[i] + house
        for j in range(len(drinks)):
            if i != j:
                statement = statement + ' & ~' + drinks[j] + house
        statement = statement + ') | '
    rules_list.append(statement[:-2])

# Generate rules for unique pets in each house
for house in houses:
    statement = ""
    for i in range(len(pets)):
        statement = statement + '(' + pets[i] + house
        for j in range(len(pets)):
            if i != j:
                statement = statement + ' & ~' + pets[j] + house
        statement = statement + ') | '
    rules_list.append(statement[:-2])

# Generate rules for unique nationalities in each house
for house in houses:
    statement = ""
    for i in range(len(nationalities)):
        statement = statement + '(' + nationalities[i] + house
        for j in range(len(nationalities)):
            if i != j:
                statement = statement + ' & ~' + nationalities[j] + house
        statement = statement + ') | '
    rules_list.append(statement[:-2])

# Additional rules
rules_list.extend(['Milk3',
                  '(Spaniard1 & Dog1) | (Spaniard2 & Dog2) | (Spaniard3 & Dog3)',
                  '(Ukrainian1 & Tea1) | (Ukrainian2 & Tea2) | (Ukrainian3 & Tea3)',
                  'Norwegian1',
                  '(Norwegian1 & Tea2) | (Norwegian2 & (Tea1 | Tea3)) | (Norwegian3 & Tea2)',
                  '(Juice1 & Fox1) | (Juice2 & Fox2) | (Juice3 & Fox3)'
                   ])

# Print the generated rules
print(rules_list)



# Create a Propositional Knowledge Base
prop_KB = PropKB()

# Add each rule to the knowledge base
for rule in rules_list:
    prop_KB.tell(expr(rule))

# Perform model checking using DPLL algorithm
print(dpll_satisfiable(Expr('&', *prop_KB.clauses)))