import heapq
from collections import defaultdict


# FlightProcessor class to handle the graph and Dijkstra's Algorithm
class FlightProcessor:
    def __init__(self, flight_data):
        self.flight_data = flight_data
        self.flights_store = defaultdict(list)

    # Adding a route to the graph
    def add_routes(self, route):
        self.flights_store[route.origin.name].append(route.destination.name)

    # Dijkstra's Algorithm to find the shortest number of routes (edges)
    def dijkstra(self, start):
        # Priority queue to store (number of routes, airport)
        pq = [(0, start)]  # (0 routes initially, starting airport)
        # Dictionary to track the minimum number of routes to each airport
        min_routes = {airport_name: float('inf') for airport_name in self.flight_data}
        min_routes[start] = 0

        while pq:
            current_routes, current_airport = heapq.heappop(pq)

            # Explore all neighbors (connected airports)
            for neighbor in self.flights_store[current_airport]:
                new_route_count = current_routes + 1  # Each neighbor is one more route away
                if new_route_count < min_routes[neighbor]:
                    min_routes[neighbor] = new_route_count
                    heapq.heappush(pq, (new_route_count, neighbor))

        return min_routes
