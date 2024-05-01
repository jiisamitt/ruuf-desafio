
# Function to calculate the number of pannels that fit in the roof
def pannels_fitting(pannel_x, pannel_y, roof_x, roof_y):
  # X will be the bigger dimension of the pannel and roof
  
  # Get the bigger dimension of the pannel
  p_x = max(pannel_x, pannel_y)
  p_y = min(pannel_x, pannel_y)
  
  # Get the bigger dimension of the roof
  r_x = max(roof_x, roof_y)
  r_y = min(roof_x, roof_y)
  
  # Calculate the number of pannels that fit in the roof
  r_x_with_p_x = int((r_x/p_x))*int((r_y/p_y))
  
  # If the pannel from the small side fits in the rest of the roof
  rest = 0
  if r_x%p_x >= p_y:
    rest = (int((r_x%p_x)/(p_y)))*int(r_y/p_x)
  
  return r_x_with_p_x + rest

  


# Pannel dimensions
pannel_x = int(input("Ingrese la dimensión x del panel: "))
pannel_y = int(input("Ingrese la dimensión y del panel: "))

# Roof dimensions
roof_x = int(input("Ingrese la dimensión x del techo: "))
roof_y = int(input("Ingrese la dimensión y del techo: "))

print(pannels_fitting(pannel_x, pannel_y, roof_x, roof_y))