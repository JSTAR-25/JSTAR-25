#CodeCademy Project

#Ground Shipping
weight = 41.5
g_cost = "" 
g_flat_charge = 20.00

if weight <= 2.00:
  g_cost = weight * 1.50
elif weight <= 6:
  g_cost = weight * 3.00
elif weight <= 10:
  g_cost = weight * 4
elif weight >= 10.1:
  g_cost = weight * 4.75
else:
  g_cost = ""

g_cost += g_flat_charge

print("Package Weight: ", weight, "lbs")
print("Ground Shipping Cost: £", g_cost)

#Ground Shipping Premium
gp_cost = ""
gp_flat_charge = 125.00

print("Ground Shipping Premium Cost: £", gp_flat_charge)

#Drone Shipping
d_cost = ""
d_flat_charge = 0

if weight <= 2:
  d_cost = weight * 4.50
elif weight <= 6:
  d_cost = weight * 9.00
elif weight <= 10:
  d_cost = weight * 12
elif weight >= 10.1:
  d_cost = weight * 14.25
else:
  d_cost = ""

print("Drone Shipping Cost: £", d_cost) 


