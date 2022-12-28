from ete3 import Tree

f = open("tree_file.txt", "r")

t = Tree(f.read())
# ancestor = t.get_common_ancestor("lcl|Query_22345")
ancestor = ("MN514967.1")

t.set_outgroup(t&ancestor)

f = open("tree.txt", "w")
f.write(str(t))
f.close()
