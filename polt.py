import pandas as pd
import plotly.express as pe

m = pd.read_csv("data - data.csv")
f = pe.scatter(m, x="Date", y="Cases",
	          size="Cases",color="Country",
                   size_max=15)
f.show()
