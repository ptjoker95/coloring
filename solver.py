#!/usr/bin/python
# -*- coding: utf-8 -*-

def coloring( edges, solution, node_count, ith ):
    if min(solution) != 0 or ith > 2:
        return
    #nodes는 node들의 edge수를 넣는 리스트
    nodes = [0]*node_count
    #nodes에 각 node별 edge의 갯수를 더한다.
    for edge in edges:
        nodes[edge[0]] += 1
        nodes[edge[1]] += 1
    print"nodes: ", nodes
    
    #가장 많은 edge를 가지고 있는 node의 index를 찾아낸다.
    index = nodes.index(max(nodes))
    print"index: ", index
    #ith는 i번째 색깔이라는 의미임
    solution[index] = ith
    print "solution: ", solution
    print "before edges: ", edges
    #선택된 node에 연결되어 있는 edge를 다 찾아다니며 색칠을 한다. 다만, 이미 색칠이 칠해져있는 경우에는 패스한다.
    for edge in edges:
        #print "edge[0]: ", edge[0], " ,edge[1]: ", edge[1]
        if edge[0] == index:
            if solution[edge[1]] is 0:
                #print"here 1"
                solution[edge[1]] = ith+1
                edges.remove(edge)
                #printedges
        if edge[1] == index:
            if solution[edge[0]] is 0:
                #print"here 2"
                solution[edge[0]] = ith+1
                edges.remove(edge)
                #printedges
    
    print "after edges: ", edges
    
    coloring( edges, solution, node_count, ith+1 )
    
def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
    
    solution = [0] * node_count
    #edge의 갯수가 많은 node를 찾는다
    
    coloring( edges, solution, node_count, 1 )
    '''
    index = nodes.index(max(nodes))
        print "index: ", index 
        solution[index] = i
        print "solution: ", solution
        nodes[index] = 0
        for edge in edges:
            if edge[0] is index or edge[1] is index:
                print "this node"
    '''
    # build a trivial solution
    # every node has its own color
    
    #애초에 색칠을 1부터 시작해서, solution의 값들에서 1을 빼준다.
    solution[:] = [x - 1 for x in solution]

    # prepare the solution in the specified output format
    output_data = str(node_count) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'
