import json


def new_game():
    return {'balance': 10, 'events': {}, 'paused': False, 'clock': 0, 'next_id': 1, 'audit': [('a', 1), ('b', 2)], 'used': 1, 'cap': 2, 'count': 0, 'accounts': {}, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_11(state):
    amount = 20
    if state["balance"] < amount:
        return False
    state["balance"] -= amount
    return True

def bug_18(state):
    event_id = 1
    if event_id in state["events"]:
        return False
    state["events"][event_id] = True
    return True

def bug_25(state):
    if state["paused"]:
        return state["clock"]
    state["clock"] += 1
    return state["clock"]

def bug_2(state):
    return None

def bug_9(state):
    return state["next_id"]

def bug_16(state):
    owner = "a"
    return [row for row in state["audit"] if row[0] == owner]

def bug_23(state):
    return state["cap"] - state["used"]

def bug_0(state):
    element = "x"
    processed = state.setdefault("processed", set())
    if element in processed:
        return False
    processed.add(element)
    return True

def bug_7(state):
    state["count"] += 1
    return state["count"]

def bug_14(state):
    return state["accounts"].get("missing", 0)

def bug_30(state):
    failed = any(status == "failed" for _, status in state["log"])
    if failed:
        state["value"] = state["snapshot"]
        return False
    state["value"] = state["snapshot"]
    return True

def bug_31(state):
    if state["settled"]:
        return False
    return True

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
