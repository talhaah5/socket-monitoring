#\install the `websocket-client`, `websockets` library beforehand: `# pip install websocket-client==1.5.1 websockets==9.1`
import websocket
import json

from dotenv import load_dotenv
import os

# load the environment variables from the .env file
load_dotenv()
# get the value of the PATH environment variable
rt = os.environ['READ_ONLY_TOKEN']
print(rt)
def subscribe_to_global_updates(ws):
  subscriptionMessage = [
    "SUBSCRIBE",
    [
      {
        "e": "globalUpdates",
        "p": "ETH-PERP", # You can replace "ETH-PERP" with any other valid market symbol
      },
      {
        "e": "globalUpdates",
        "p": "BTC-PERP", # You can replace "ETH-PERP" with any other valid market symbol
      }
   
    ]
  
  ]
  ws.send(json.dumps(subscriptionMessage))

def subscribe_to_user_updates(ws):
  subscriptionMessage = [
    "SUBSCRIBE",
    [
      {
        "e": "userUpdates",
        "rt": rt, # Replace with your actual token
      }
    ]
  ]
  ws.send(json.dumps(subscriptionMessage))

def on_message(ws, message):
  
    data = json.loads(message)
    print(message)
    event_name = data["eventName"]
    
    if event_name == 'MarketDataUpdate':
        # Handle RecentTrades event
        pass
      
    elif event_name == 'RecentTrades':
        # Handle RecentTrades event
        pass
      
    elif event_name == 'OrderbookUpdate':
        # Handle OrderbookUpdate event
        pass
      
    else:
        # Add cases for other events like OrderbookUpdate, MarketHealth, etc.
        pass
      
      
websocket_url = "wss://notifications.api.sui-prod.bluefin.io/"

ws = websocket.create_connection(websocket_url)

print("WebSocket connection has been established: ", websocket_url)

# subscribe_to_global_updates(ws)
subscribe_to_user_updates(ws)
while True:
  
    op_code, frame = ws.recv_data_frame(True)
    
    if op_code == websocket.ABNF.OPCODE_CLOSE:
        print("CLOSE frame received, closing websocket connection")
        
    elif op_code == websocket.ABNF.OPCODE_PING:
        ws.pong("")
        print("Received Ping; PONG frame sent back")
        
    elif op_code == websocket.ABNF.OPCODE_PONG:
        print("Received PONG frame")
        
    else:
        data = frame.data
        
        if op_code == websocket.ABNF.OPCODE_TEXT:
            data = data.decode("utf-8")
            
        on_message(ws, data)
