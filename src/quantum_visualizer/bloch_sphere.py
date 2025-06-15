import numpy as np
import plotly.graph_objects as go

# Define a qubit
qubit = np.array([1/np.sqrt(3), np.sqrt(2j/3)], dtype=complex)
theta = float(np.arccos(qubit[0]) * 2)
phi = float(qubit[0] / np.sin(theta/2))

print(theta)
print(phi)

# Define axis line length
axis_range = [-1.5, 1.5]

# x-axis
x_axis = go.Scatter3d(
    x=axis_range,
    y=[0, 0],
    z=[0, 0],
    mode='lines',
    line=dict(color='red', width=1),
    name='x-axis'
)

# y-axis
y_axis = go.Scatter3d(
    x=[0, 0],
    y=axis_range,
    z=[0, 0],
    mode='lines',
    line=dict(color='green', width=1),
    name='y-axis'
)

# z-axis
z_axis = go.Scatter3d(
    x=[0, 0],
    y=[0, 0],
    z=axis_range,
    mode='lines',
    line=dict(color='blue', width=1),
    name='z-axis'
)

# Label the six important states
labeled_points = go.Scatter3d(
    x=[1, -1, 0, 0, 0, 0],
    y=[0, 0, 1, -1, 0, 0],
    z=[0, 0, 0, 0, 1, -1],  
    mode='markers+text',
    marker=dict(size=2, color='black'),
    text=['|+>', '|->', '|+i>', '|-i>', '|0>', '|1>'],  # Labels
    textposition='top center',
    name='Important States'
)

# Create sphere surface
u, v = np.mgrid[0:2*np.pi:20*2j, 0:np.pi:20*1j]
X = np.cos(u)*np.sin(v)
Y = np.sin(u)*np.sin(v)
Z = np.cos(v)
surface = go.Surface(x=X, y=Y, z=Z, opacity=0.4, colorscale=[[0, 'white'], [1, 'white']])

# Create qubit vector
X = np.cos(phi)*np.sin(theta)
Y = np.sin(phi)*np.sin(theta)
Z = np.cos(theta)
vector = go.Scatter3d(
    x=[0, X*0.8],
    y=[0, Y*0.8],
    z=[0, Z*0.8],
    mode='lines+markers',
    line=dict(color='purple', width=6),
    marker=dict(size=2, color='purple'),
    name='qubit state'
)
cone = go.Cone(
    x=[X],
    y=[Y],
    z=[Z],
    u=[X],
    v=[Y],
    w=[Z],
    sizemode='absolute',
    sizeref=0.2,
    anchor='tip',
    showscale=False,
    colorscale=[[0, 'purple'], [1, 'purple']]
)
print(X)


# Display the sphere and the points
fig = go.Figure(data=[surface, x_axis, y_axis, z_axis, labeled_points, vector, cone])
fig.update_xaxes(showline=True, linewidth=2, linecolor="black")
fig.show()

