from airport_node import Airport
from flight_processor import FlightProcessor
from route_edge import RouteEdge

# Main execution method to find the minimum routes
def get_minimum_routes(airports, routes, start):
# Create a dictionary of Airport objects, with airport names as keys
    flight_data = {name: Airport(name) for name in airports}
    # Create the FlightProcessor object
    processor = FlightProcessor(flight_data)

    # Add routes (edges) to the graph
    for start_airport, destination_airport in routes:
        route_edge = RouteEdge(flight_data[start_airport], flight_data[destination_airport])
        processor.add_routes(route_edge)

    # Use Dijkstra's algorithm to find the minimum routes from the start airport
    return processor.dijkstra(start)


# List of airports
airports = [
    'DSM', 'ORD', 'BGI', 'LGA', 'JFK', 'TLV', 'DEL', 'DOH', 'CDG', 'SIN',
    'BUD', 'EWR', 'HND', 'ICN', 'SFO', 'SAN', 'EYW', 'LHR'
]

# List of routes (directed edges)
routes = [
    ('DSM', 'ORD'), ('ORD', 'BGI'), ('BGI', 'LGA'), ('LGA', 'JFK'),
    ('JFK', 'HND'), ('HND', 'ICN'), ('ICN', 'JFK'), ('SFO', 'SAN'),
    ('SAN', 'EYW'), ('EYW', 'LHR'), ('LHR', 'SFO'), ('DEL', 'CDG'),
    ('CDG', 'SIN'), ('CDG', 'BUD'), ('TLV', 'DEL'), ('DEL', 'DOH'),
    ('DOH', 'CDG')
]

# Display the available airports
print("Available airports to choose from: ")
print(', '.join(airports))

# Get starting airport input from the user
while True:
    start_airport = input("Enter the starting airport (three-letter code): ").upper()
    
    if start_airport in airports:
        break
    else:
        print(f"Error: '{start_airport}' is not a valid airport code. Please enter a valid one from the list: {', '.join(airports)}")

# Find the minimum number of additional routes to make all airports reachable
min_routes = get_minimum_routes(airports, routes, start_airport)


# Display the results
count = 0
print(f"\nMinimum number of one-way routes from {start_airport}:")
for airport, route_count in min_routes.items():
    if route_count == float('inf'):
       continue
    else:
        count += 1
       

print(f"\nMinimum number of additional one-way routes required: {count}")
        
