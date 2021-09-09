import hashlib
import time

number_range = 1000000000
difficulty = 6
def mine_bitcoin(block_number, transactions, previous_hash, difficulty):
    for nonce in range(number_range):
        raw_text = str(block_number) + transactions + previous_hash + str(nonce)
        find_hash = hashlib.sha256(raw_text.encode()).hexdigest()
        if find_hash.startswith("0"*difficulty):
            print(f"We found a new block hash! With Nonce ==> {nonce}")
            return find_hash


# hash = "45677" + "343512" + "asd3asdhv34324nv23hbc43" + "1"
# print(hashlib.sha256(hash.encode()).hexdigest())

if __name__ == "__main__":

    begin = time.time()
    print("Start Minning")

    new_hash = mine_bitcoin(80,"43","asdas4d5asf54xzc454asqw54",difficulty)
    # print(hashlib.sha256("8043asdas4d5asf54xzc454asqw5416221".encode()).hexdigest())
    full_time = str((time.time()) - begin)
    print(f"zamani ke baraye mine kardane bitcoin sarf shod ==> {full_time}")
    print(new_hash)

