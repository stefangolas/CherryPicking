# CherryPicking

## 96 to 384 Cherry Picking 


### Motivation
We want to compile a worklist into a set of time-efficient aspiration and dispense commands. To do this we have to identify sets of aspiration and dispense pairs where the wells for each aspiration and dispense (a.d.) pair lie in the same column. This way we can execute a list of multiple a.d. pairs simultaneously using the 8-channel pipetting arm.

An a.d. list is a 2-d list containing an aspiration list and a dispense list. Each a.d. list is composed of wells e.g. (TargetPlate1, 4) where each aspiration well is matched to its dispense well counterpart by position. An a.d. list can not exceed length n=8 for our purposes. 

**a.d. list := [ [ (TargetPlate, x), …]n, [ (SourcePlate, y), …]n ]**

**a.d. pair :=  (TargetPlate, x), (SourcePlate, y)**

[Contribution guidelines for this project](/Time-Efficient%20Cherry%20Picking.pdf)


The list is extended when we add an additional pair. Every additional pair has to belong to the worklist map, an adjacency list of well-to-well transfers. We also remove the pair’s source well from the worklist map for that target well when we add a pair.

https://en.wikipedia.org/wiki/Adjacency_list
This is the data type we are using to represent the worklist map.

**wl = worklist_96('061322_32Seqs.csv')**

wl is the worklist map, a dictionary mapping each target well to a set of source wells, e.g. x1→[y1, y2, ..] or in Python notation {target_well1: [source_well1, source_well2, ..], ...}

x1→[y1, y2, ..] <br>
Add pair (x1, y1) to a.d. list <br>
x1→[y2, ..] <br>

When x1→[ ] we delete x1 as a key from the worklist map.


**target_cols = get_96wp_columns([target_plate], 0, 1)**
**source_cols = get_columns_from_deck(source_plates, carrier_max_plates = 4)**

source_cols and target_cols are 2-dimensional lists where each element is a list representing a column of wells, for every column from source or target plates. We treat all in-line columns from separate plates on the same carrier (e.g., the first column of every plate on the same carrier) as one column. This reflects the ability of the pipetting arm to pipette from these positions simultaneously.

For target columns of length n and quantity m: 
target_cols := [ [ (TargetPlate, 0)0, ... (TargetPlate, n)]n, … ]m

For every combination of source_col and target_col, we expose only the links in the worklist map where each well belongs to its respective set in the intersection of wl & (source_col | target_col), i.e., either source_col or target_col. 
