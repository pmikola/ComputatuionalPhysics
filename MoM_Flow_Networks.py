# MOM_FLOW_NETWORSK
from __future__ import print_function
from ortools.graph import pywrapgraph

# Instantiate a SimpleMinCostFlow solver.

array_solution_min_cost = []
array_solution_max_flow = []
maximum_flow = []
final_cost = []
# Zdolności wydobywcze kopalń
Wa = 10  # [kton]
Wb = 13  # [kton]
Wc = 17  # [kton]

# Średnie zużycie dobowe węgla przez elektrownie
Zf = -15  # [kton]
Zg = -12  # [kton]
Zh = -8  # [kton]


def main(WA, WB, WC, k):
    start_nodes = [0, 0, 1, 1, 2, 2, 3, 4, 3, 3, 3, 4, 4, 4 ]
    end_nodes =   [3, 4, 3, 4, 3, 4, 4, 3, 5, 6, 7, 5, 6, 7 ]
    capacities =  [8,10,10,13, 10,5, 20,20,16,5, 10,7, 11,10]
    unit_costs =  [3, 6, 6, 3, 4, 6, 2, 2, 5, 7, 3, 5, 4, 2 ]
    supplies =    [Wa - WA, Wb - WB, Wc - WC, 0, 0, Zf, Zg, Zh]

    # Instantiate a SimpleMaxFlow solver.
    if k == 0:
        max_flow = pywrapgraph.SimpleMaxFlow()
        # Add each arc.
        for i in range(0, len(start_nodes)):
            max_flow.AddArcWithCapacity(start_nodes[i], end_nodes[i], capacities[i])

        for ix in range(0, 8):
            for iy in range(0, 8):
                if max_flow.Solve(0 + ix, 0 + iy) == 0:

                    print('')
                    print('  Arc    Flow / Capacity')
                    for i in range(max_flow.NumArcs()):
                        print('%1s -> %1s   %3s  / %3s' % (
                            max_flow.Tail(i),
                            max_flow.Head(i),
                            max_flow.Flow(i),
                            max_flow.Capacity(i)))
                        maximum_flow.append(max_flow.Flow(i))
                    print('Source side min-cut:', max_flow.GetSourceSideMinCut())
                    print('Sink side min-cut:', max_flow.GetSinkSideMinCut())
                    print('Max flow:', sum(maximum_flow))
                    array_solution_max_flow.append("{}  {} and {} is: {} ".format("Max Flow Between Nodes",0+ix,0+iy,sum(maximum_flow)))
                    maximum_flow.clear()
                else:
                    print('There was an issue with the max flow input.')
    else:
        # Add node supplies.
        min_cost_flow = pywrapgraph.SimpleMinCostFlow()
        for i in range(0, len(supplies)):
            min_cost_flow.SetNodeSupply(i, supplies[i])

        # Add each arc.
        for i in range(0, len(start_nodes)):
            min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i],
                                                        capacities[i], unit_costs[i])

        # print(min_cost_flow.NumArcs())
        # Find the minimum cost flow between node 0 and node 4.
        if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
            # print('Minimum cost:', min_cost_flow.OptimalCost())
            print('')
            print('  Arc    Flow / Capacity  Cost')
            for i in range(min_cost_flow.NumArcs()):
                cost = min_cost_flow.UnitCost(i)
                print('%1s -> %1s   %3s  / %3s       %3s' % (
                    min_cost_flow.Tail(i),
                    min_cost_flow.Head(i),
                    min_cost_flow.Flow(i),
                    min_cost_flow.Capacity(i),
                    cost))
                if min_cost_flow.Flow(i) > 0:
                    final_cost.append(cost)
                else:
                    pass
            array_solution_min_cost.append(sum(final_cost))
        else:
            print('There was an issue with the min cost flow input.')


k = 0
if k == 0:
    a = 0
    b = 0
    c = 0
    main(a, b, c, k)
    print(array_solution_max_flow)
else:
    for a in range(0, 5):
        for b in range(0, 5):
            for c in range(0, 5):
                if a + b + c == 5 or a + b + c == 0:
                    main(a, b, c, k)
                    print("{} of (A) {} kton + (B) {} kton + (C) {} kton setup is: {}".format("Minimum cost", Wa - b, Wb - b,Wc - c,min(array_solution_min_cost,default=0)))
                else:
                    pass
