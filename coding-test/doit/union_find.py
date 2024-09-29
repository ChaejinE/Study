nodes = [1, 2, 3, 4, 5, 6]
nodes = [0] + nodes
union_list = [i for i in nodes]


def find(a):
    root_node = union_list[a]
    if a != root_node:
        root_node = find(root_node)

    return root_node


def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        union_list[root_b] = root_a

    print(union_list)


union(1, 4)
union(5, 6)
union(4, 6)
