#!/usr/bin/python
# -*- coding: utf-8 -*-

# 어떤 노드에 연결되어 있는 노드 중에 색칠이 칠해져있는지 확인해주고, 무슨 색이 칠해져있는지 확인해주는 함수
def IsThereColoredNode ( node, edges, solution ):
    trueorfalse = False
    ColoredConnected = []
    
    # edge 리스트를 죽 흝어본다.
    for edge in edges:
        # edge 리스트 중에 찾고자 하는 노드가 있으면
        if node in edge:
            # edge에서 찾고자 하는 노드를 빼고 다른 노드에 색깔이 칠해져있는지, 이 경우에는 0 이외의 숫자, 확인
            temp = list(edge)
            temp.remove(node)
            if solution[temp[0]] is not 0:
                # 일단은 칠해져있는 모든 노드를 리턴해본다. temp는 칠해져있는 노드의 인덱스, solution[temp]는 칠해져있는 값 
                ColoredConnected = [ temp, solution[temp] ]
                trueorfalse = True
    return trueorfalse, ColoredConnected

def ConnectedNodes( SelectedNode, edges ):
    # 연결되어 있는 노드를 담을 리스트
    ConnectedNodes = []
    
    # edge를 죽 훑어본다.
    for edge in edges:
        if SelectedNode in edge:
            temp = list(edge)
            temp.remove(SelectedNode)
            tempint = int(temp[0])
            ConnectedNodes.append(tempint)
            
    return ConnectedNodes

# 연결되어 있는 node중에 색이 칠해져있는게 있는지 확인해서, 안 칠해져있으면 True, 칠해져있으면 False와 칠해져있는 값 리턴
def IsNotThereColoredNode(checknode, nodes, solution, edges):
    for edge in edges:
        if checknode in edge:
            temp = list(edge)
            temp.remove(checknode)
            #print solution[temp[0]]

def Coloring( nodes, solution, Color, edges ):
    for node in nodes:
        if IsNotThereColoredNode(node, nodes, solution, edges):
            solution[node] = Color
    return

def ColoringNode( index, edges, solution, node_count, Color ):
    #연결되어있는 node의 리스트 생성
    CNodes = ConnectedNodes( index, edges )
    
    #연결되어 있는 node의 색깔을 받는다.
    CNColors = []
    for cn in CNodes:
        CNColors.append(solution[cn])
    
    #print "index: ", index, " CNodes: ",  CNodes, "CNColors: ", CNColors
    
    #0부터 node의 숫자만큼의 색깔 중에서 가장 낮은 숫자를 칠한다. 
    for i in range(0, node_count):
        if not i in CNColors:
            #print "ith solution color: ", i
            solution[index] = i
            return
    
    solution[index] = Color
    return 

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
        
    solution = [-1]*node_count
    
    # 각 node별로 edge들의 갯수를 구한다.
    NodesHaveEdgenum = [0]*node_count
    
    for edge in edges:
        NodesHaveEdgenum[edge[0]] += 1
        NodesHaveEdgenum[edge[1]] += 1
        
    # 각 node별로 edge의 수가 많은 순으로 사전 정렬
    WeightedIndex = []
 
       
    for i in range(0, node_count):
        WeightedIndex.append( [i,NodesHaveEdgenum[i]] )
        
    WeightedIndex = sorted( WeightedIndex, key=lambda WeightedIndex:WeightedIndex[1], reverse=True )
    #사전 정렬 끝.
    
    #계산이 끝난 후 solution에서 각각 1을 빼야됨
    
    #많아봐야 노드 갯수 이상의 색을 칠할 필요는 없으므로 loop의 한계는 node수로 한계지어놓는다.
    for i, index in enumerate(WeightedIndex):
        #node의 index를 주면 해당 node에 가장 작은 색을 칠한다.
        #print "index[0]: ", index[0], " ,edges: ", edges, " ,solution: ", solution, " ,i: ", i
        ColoringNode( index[0], edges, solution, node_count, i )
        
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
