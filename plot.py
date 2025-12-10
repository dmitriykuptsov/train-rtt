import plotly.express as px
import pandas as pd
from sys import argv

df = pd.read_csv(argv[1])

color_scale = [(0, 'orange'), (1,'red')]

fig = px.scatter_mapbox(df,
                        lat="lat",
                        lon="lng",
                        color="mean",
                        color_continuous_scale=color_scale,
                        size="mean",
                        zoom=8,
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
