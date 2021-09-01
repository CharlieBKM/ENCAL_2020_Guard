# Improtant note: This data file would ordinarily be used to connect with a proper database server
# more likely PostgreSQL, but thats me. I do plan on rewritting this in the future for such implementations.
# With that said, this file will be be very slow to run and only to demonstrate data processing using
# functions and pandas along with providing a central file for data references
#
# Import Pandas
import pandas as pd



##Base de datos

eni_complete = pd.read_csv("data//guard_complete_T_secc.csv")
eni_complete = eni_complete.round(0)

preguntas=pd.read_csv("data//variablespreguntasG.csv")

