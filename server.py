import json
import asyncio
from replit import websockets

# Create a set to store all connected clients
clients = set()

# Define the WebSocket handler
async def handle_websocket(websocket):
    # Add the client to the set of connected clients
    clients.add(websocket)
    print(f"New client connected (Total clients: {len(clients)})")

    try:
        while True:
            # Receive message from the client
            message = await websocket.recv()
            data = json.loads(message)
            output = data['output']
            print(output)  # Optional: print the output to the server console

            # Send the output to all connected clients
            for client in clients:
                await client.send(output)
    except websockets.exceptions.ConnectionClosedError:
        # Remove the client from the set of connected clients when the connection is closed
        clients.remove(websocket)
        print(f"Client disconnected (Total clients: {len(clients)})")

# Start the WebSocket server
async def main():
    server = await websockets.serve(handle_websocket, '0.0.0.0', 8000)
    await server.wait_closed()

asyncio.run(main())
