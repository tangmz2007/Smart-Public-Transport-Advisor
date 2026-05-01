# Smart-Public-Transport-Advisor
this is a smart public transport advisor for the group project of COMP1110. It is completely coded in python. Execution: download files and run main.py in pycharm or any other python IDE

```
│
├── main.py              # The "Master" script that handles the loop
├── metro_data.py        # The "Database" (contains stations, times, schedules)
├── metro_input.py       # The "Interpreter" (parses data and handles user input)
├── metro_router.py      # The "Engine" (contains Dijkstra/A* logic and fare fitting)
└── metro_output.py      # The "UI" (formats the final route report)
```
Here is a sample test case with outputs:
```
Please enter the origin station or a nearby landmark: "Prince Edward"
Recognized as station: Prince Edward.
Please enter the destination station or a nearby landmark: "Causeway Bay"
Recognized as station: Causeway Bay.
Please enter your preference (time/cost/balanced/transfer/comfort/walk/accessible): "cost"
Please enter the departure time (HH:MM): 09:00
Please enter the preferred entrance (optional, e.g. Gate A):
Please enter the destination landmark (optional):
Please enter the maximum budget (optional):
Please choose the departure mode (accurate/estimate, default: accurate):
Prioritize fewer stairs / accessibility? (y/n, default: n):
---outputs---
Arrival time: 09:39
Total travel time: 20.2 min
Total fare: HK$6.0
Transfers: 3
Walking time: 9.0 min
Pure in-vehicle time: 11.2 min
Average crowding: 2.38
High-crowding minutes: 0 min
Stair burden (transfers): 3
Estimated carbon saved: 0.719 kg
Entry recommendation: Defaulted to entrance Gate B, which is closer to the Line 2 platform and has better overall walking time; about 2 minutes.
Exit recommendation: Default recommended exit: Gate A. Estimated average walking time around that exit is about 2 minutes.
Path: Prince Edward -> Mong Kok -> Yau Ma Tei -> Jordan -> Tsim Sha Tsui -> Admiralty -> Wan Chai -> Causeway Bay
Instructions:
  1. Enter the station via Gate B at Prince Edward. Estimated walk to the platform: 2 minutes.
  2. Take Line 2 (Toward Central) from Prince Edward to Admiralty.
  3. Transfer at Admiralty to Line 1 (Toward Chai Wan), then continue to Causeway Bay.
  4. After arriving at Causeway Bay, leave via Gate A. Estimated walk after exit: 2 minutes.
  Default recommended exit: Gate A. Estimated average walking time around that exit is about 2 minutes.
```
