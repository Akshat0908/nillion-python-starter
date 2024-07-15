from nada_dsl import *

def initialize_parties():
    return [
        Party(name="Auctioneer"),
        Party(name="Bidder1"),
        Party(name="Bidder2"),
        Party(name="Bidder3")
    ]

def initialize_items(nr_items):
    items = []
    for i in range(nr_items):
        items.append(Party(name="Item" + str(i)))
    return items

def initialize_bids(nr_bidders, nr_items, bidders, items):
    bids_per_item = []
    for item in items:
        bids_per_item.append([])
        for bidder in bidders:
            bids_per_item[-1].append(
                SecretUnsignedInteger(
                    Input(name="bid_" + bidder.name + "_" + item.name, party=bidder)
                )
            )
    return bids_per_item

def record_bids_on_blockchain(bids_per_item, items):
    blockchain_records = []
    for item_idx, item in enumerate(items):
        for bidder_idx, bidder_bids in enumerate(bids_per_item[item_idx]):
            blockchain_records.append(
                Output(bidder_bids, "bid_" + item.name + "_by_" + str(bidder_idx), item)
            )
    return blockchain_records

def determine_winner(nr_bidders, nr_items, bids_per_item, bidders, items):
    winners = []
    for item_idx in range(nr_items):
        highest_bid = bids_per_item[item_idx][0]
        winner = bidders[0]
        for bidder_idx in range(1, nr_bidders):
            if bids_per_item[item_idx][bidder_idx] > highest_bid:
                highest_bid = bids_per_item[item_idx][bidder_idx]
                winner = bidders[bidder_idx]
        winners.append(Output(highest_bid, "winning_bid_" + items[item_idx].name, winner))
    return winners

def nada_main():
    nr_bidders = 3
    nr_items = 2

    parties = initialize_parties()
    auctioneer = parties[0]
    bidders = parties[1:]

    items = initialize_items(nr_items)

    bids_per_item = initialize_bids(nr_bidders, nr_items, bidders, items)

    blockchain_records = record_bids_on_blockchain(bids_per_item, items)

    winners = determine_winner(nr_bidders, nr_items, bids_per_item, bidders, items)

    return winners + blockchain_records

if __name__ == "__main__":
    nada_main()
