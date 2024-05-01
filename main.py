
# Function to calculate the number of pannels that fit in the roof
def pannels_fitting(pannel_x, pannel_y, roof_x, roof_y):
  
  # Amount of pannels that fit in the roof, without considering the "remainder" of the roof
  r_x_with_p_x = int((roof_x/pannel_x))*int((roof_y/pannel_y))
  
  # If the pannel from one sides fits in the rest of the roof, we add it
  rest = 0
  if roof_x%pannel_x >= pannel_y:
    rest += (int((roof_x%pannel_x)/(pannel_y)))*int(roof_y/pannel_x)
  
  if roof_y%pannel_y >= pannel_x:
    rest += (int((roof_y%pannel_y)/(pannel_x)))*int(roof_x/pannel_y)
  
  first_option =  r_x_with_p_x + rest
  
  # Now we do the same, but with the other side of the roof
  r_y_with_p_x = int((roof_x/pannel_y))*int((roof_y/pannel_x))
  
  # If the pannel from one sides fits in the rest of the roof, we add it
  rest = 0
  if roof_x%pannel_y >= pannel_x:
    rest += (int((roof_x%pannel_y)/(pannel_x)))*int(roof_y/pannel_y)
  
  if roof_y%pannel_x >= pannel_y:
    rest += (int((roof_y%pannel_x)/(pannel_y)))*int(roof_x/pannel_x)
  
  second_option = r_y_with_p_x + rest
  
  return max(first_option, second_option)

  


# Pannel dimensions
pannel_x = int(input("Ingrese la dimensión x del panel: "))
pannel_y = int(input("Ingrese la dimensión y del panel: "))

# Roof dimensions
roof_x = int(input("Ingrese la dimensión x del techo: "))
roof_y = int(input("Ingrese la dimensión y del techo: "))

print(pannels_fitting(pannel_x, pannel_y, roof_x, roof_y))