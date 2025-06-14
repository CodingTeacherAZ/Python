### dictionary mapping with immediate function calls using get method ###
import math
def calculate_tip(amount, rating):
    return {"terrible":0*amount,
            "poor":math.ceil(0.05*amount),
            "good":math.ceil(0.1*amount),
            "great":math.ceil(0.15*amount),
            "excellent":math.ceil(0.2*amount)}.get(rating.lower(), "Rating not recognised")

print(calculate_tip(30, "poor"))  # returns 2
print(calculate_tip(20, "Excellent")) # returns 4
print(calculate_tip(20, "hi")) # returns 'Rating not recognised'
print(calculate_tip(107.65, "GReat")) # returns 17)
print(calculate_tip(20, "great!")) # returns 'Rating not recognised'

        
