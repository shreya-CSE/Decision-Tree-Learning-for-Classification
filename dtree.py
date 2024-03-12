import sys
import math
import random

glabel_array = []
glabel_num = 0 
example_idx= 0

#Declaration of global variables

def LabelArray(label_array,attributes):
    global glabel_array 
    global glabel_num
    global example_idx
    glabel_array = sorted(set(label_array))
    glabel_num = len(glabel_array)
    example_idx = attributes
    print("GlobalArray", glabel_array, "array_len =",  glabel_num,"example_idx=",example_idx)            

#Reading input file
def read_file(file_path):
    lines_list = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            values_list_1 = line.split()
            values_list = [float(value) for value in values_list_1]
            lines_list.append(values_list)
    return lines_list            

#Declaration of class Node
class Node:
    def __init__(self, LeftSubTree = None, RightSubTree = None, leaf = False,attribute = None,threshold= None,distribution = None):
        self.left_child = LeftSubTree
        self.right_child= RightSubTree
        self.leaf = leaf
        self.attribute = attribute
        self.threshold = threshold
        self.distribution = distribution

#Assigning Node to tree as subtree
def DecisionTreeRoot(best_attribute,best_threshold):
    test = Node(attribute = best_attribute, threshold = best_threshold)
    return test

#Assigning Node to tree as a Leaf node
def DecisionTreeLeaf(leaf,distribution):
    leaf_node= Node(leaf = leaf, distribution= distribution)
    return leaf_node

#Fuction to select best_threshold ,best_attribute for optimized version
def ChooseAttribute(examples,attributes):
    max_gain = -1
    best_attribute = -1
    best_threshold = -1
    for attribute in range(attributes):
        attribute_values = SelectColumn(examples,attribute)
        L = min(attribute_values)
        M = max(attribute_values)
        cnt =len(examples)
        for K in range(1,50):
            threshold = L + (K*((M-L)/51))
            gain = InfoGain(examples,attribute,threshold)
            if gain > max_gain:
                max_gain = gain
                best_attribute = attribute
                best_threshold = threshold
    return(best_attribute,best_threshold)

#Function to select best threshold and random selection of attribute for random version
def ChooseAttributeRandom(examples,attributes):
    max_gain = -1
    best_attribute = -1
    best_threshold = -1
    attribute = random.randint(0,attributes)
    attribute_values = SelectColumn(examples,attribute)
    L = min(attribute_values)
    M = max(attribute_values)
    cnt =len(examples)
    for K in range(1,50):
        threshold = L + (K*((M-L)/51))
        gain = InfoGain(examples,attribute,threshold)
        if gain > max_gain:
            max_gain = gain
            best_attribute = attribute
            best_threshold = threshold
    return(best_attribute,best_threshold)


#Function to select attribute
def SelectColumn(examples,attribute):
    attribute_values = []
    examples_1 = list(map(list,zip(*examples)))
    attribute_values = examples_1[attribute]
    return attribute_values

#Function for Entropy calculation(part)
def EntropyCalc(examples,attributes):
    class_label = {}
    entropy = 0
    for example in examples:
        label = example[attributes]
        if label in class_label:
            class_label[label] += 1
        else:
            class_label[label] = 1
    total_samples = len(examples)
    for count in class_label.values():
        label_prob = count/total_samples
        entropy  += label_prob *math.log2(label_prob)
    return(-entropy)

#Function for entropy calculation
def EntropyCalcThreshold(examples,attribute,attributes,threshold):
    entropy = 0
    example_bin_1 = []
    example_bin_2 = []
    for example in examples:
        attribute_val = example[attribute]
        if(attribute_val < threshold):
            example_bin_1.append(example)
        else:
            example_bin_2.append(example)
    
    entropy_1 = EntropyCalc(example_bin_1,attributes)
    entropy_2 = EntropyCalc(example_bin_2,attributes)
    
    k34 = len(example_bin_1)
    k56 = len(example_bin_2)
    k = len(examples)
    gain = (((k34/k)*entropy_1) +((k56/k)*entropy_2))
    return(gain)

#Function for Information gain
def InfoGain(examples, attribute, threshold):
    for example in examples :
        attributes = len(example)-1
    entropy = EntropyCalc(examples, attributes)
    gain_1 = EntropyCalcThreshold(examples,attribute,attributes,threshold)
    gain = entropy - gain_1
    return(gain)

#Decision tree learning  for optimised version
def DTL(examples,attributes,default):
    best_attribute= -1
    best_threshold = -1
    class_label = {}
    for example in examples:
        label = example[attributes]
        if label in class_label:
            class_label[label] +=1
        else:
            class_label[label] = 1
    if len(examples) == 0:
        print("EMPTY ")
        leaf = True
        default = {}
        leaf_node = DecisionTreeLeaf(leaf,Default)
        return leaf_node
    elif (len(class_label) == 1):
        leaf = True
        temp = Distribution(examples)
        leaf_node = DecisionTreeLeaf(leaf,temp)
        return leaf_node
    else:
        best_attribute , best_threshold = ChooseAttribute(examples,attributes)
        examples_left = []
        examples_right = []
        examples_left = [example for example in examples if example[best_attribute] < best_threshold]
        examples_right = [example for example in examples if example[best_attribute] >= best_threshold]
        if (len(examples_left) < 50 or len(examples_right) <50) :
            leaf = True
            temp = Distribution(examples)
            leaf_node = DecisionTreeLeaf(leaf,temp)
            return leaf_node
        else:
            tree = DecisionTreeRoot(best_attribute,best_threshold)
            tree.left_child = DTL(examples_left,attributes,Distribution(examples))
            tree.right_child = DTL(examples_right,attributes,Distribution(examples))
            return tree

#Decision tree learning for randomised verion
def DTLRandom(examples,attributes,default):
    best_attribute= -1
    best_threshold = -1
    class_label = {}
    for example in examples:
        label = example[attributes]
        if label in class_label:
            class_label[label] +=1
        else:
            class_label[label] = 1
    if len(examples) == 0:
        leaf = True
        default = {}
        leaf_node = DecisionTreeLeaf(leaf,Default)
        return leaf_node
    elif (len(class_label) == 1):
        leaf = True
        temp = Distribution(examples)
        leaf_node = DecisionTreeLeaf(leaf,temp)
        return leaf_node
    else:
        best_attribute , best_threshold = ChooseAttributeRandom(examples,attributes)
        examples_left = []
        examples_right = []
        examples_left = [example for example in examples if example[best_attribute] < best_threshold]
        examples_right = [example for example in examples if example[best_attribute] >= best_threshold]
        if (len(examples_left) < 50 or len(examples_right) <50) :
            leaf = True
            temp = Distribution(examples)
            leaf_node = DecisionTreeLeaf(leaf,temp)
            return leaf_node
        else:
            tree = DecisionTreeRoot(best_attribute,best_threshold)
            tree.left_child = DTLRandom(examples_left,attributes,Distribution(examples))
            tree.right_child = DTLRandom(examples_right,attributes,Distribution(examples))
            return tree

#Calculation of Distribution
def Distribution(examples):
    dist_label= {}
    class_label = {}
    for example in examples:
        label = int(example[example_idx])
        if label in class_label:
            class_label[label] += 1
        else:
            class_label[label] =1
    example_cnt = len(examples)
    for idx in glabel_array:
        if idx in class_label:
            val = class_label[idx]/example_cnt
            dist_label[idx] = val
        else:
            dist_label[idx] =0
    return dist_label

def TestingTree(Node,test_data):
    if Node.leaf == False:
        attribute = Node.attribute
        if test_data[attribute] < Node.threshold :
            TestingTree(Node.left_child,test_data)
        else:
            TestingTree(Node.right_child,test_data)
    else:
        max_label = max(Node.distribution, key=lambda k: Node.distribution[k])
        if max_label == test_data[example_idx]:
            print("PASS:node_data =", max_label,"test_data=",test_data[example_idx])
        else:
            print("FAIL: node_data = ",max_label, "Test_data= ", test_data[example_idx])

#Function for retreiving the leaf data with the tree generated with training data
def TestingTreeForest(TNode,test_data):
    #distribution = {}
    myValue = "abc"
    if TNode.leaf == False:
        attribute = TNode.attribute
        if test_data[attribute] < TNode.threshold :
            distribution = TestingTreeForest(TNode.left_child,test_data)
            return distribution
        else:
            distribution = TestingTreeForest(TNode.right_child,test_data)
            return distribution
    elif TNode.leaf == True:
        distribution = TNode.distribution
        return distribution
    else:
        print("ERROR")
    #return distribution


def Testing(testing_list,decision_tree):
    testing_list_len = len(testing_list)
    for i in range(0, testing_list_len):
        test_data = testing_list[i]
        TestingTree(decision_tree,test_data)
    return

#Function for testing data with the tree generated from the training data
def Forest(tree_num,examples,attributes,testing_list):
    forest = []
    decision_tree = Node()
    forest_distribution = {}
    final_distribution = {}
    total_accuracy= 0
    if tree_num == 0:
        decision_tree = DTL(examples,attributes,Distribution(examples))
        forest.append(decision_tree)
        tree_num = 1
    else:
        for i in range(0,tree_num) :
            decision_tree = DTLRandom(examples,attributes,Distribution(examples))
            forest.append(decision_tree)
    for i in range(0, len(testing_list)):
        test_data = testing_list[i]
        final_distribution.clear()
        for j in range(0, tree_num):
            decision_tree = forest[j]
            forest_distribution = TestingTreeForest(decision_tree,test_data)
            for key in set(forest_distribution.keys()):
                value1 = forest_distribution.get(key, 0)
                value2 = final_distribution.get(key, 0)
                value = value1+value2
                final_distribution[key] = value
        for key in set(final_distribution.keys()):
            forest_distribution[key] = final_distribution.get(key,0)/3
        max_label = max(forest_distribution, key=lambda k: forest_distribution[k])
        max_value = forest_distribution[max_label]
        if max_label == test_data[example_idx]:
            max_keys = [key for key, value in forest_distribution.items() if value == max_value]
            if (len(max_keys)>0):
                accuracy = 1/len(max_keys)
        else:
            accuracy = 0
        print("Index:", i ,max_label, int(test_data[example_idx]),accuracy)
        total_accuracy += accuracy
    print("total_accuracy:",total_accuracy/len(testing_list)) 
    return

if __name__ =='__main__':
    training_file = sys.argv[1]
    testing_file = sys.argv[2]
    option = sys.argv[3]

    examples = []
    training_list = read_file(training_file)
    label_array = []
    for line in training_list:
        attributes = len(line)-1
        examples.append(line)
        label_array.append(int(line[attributes]))
    LabelArray(label_array,attributes)
    training_cases = len(training_list)   
    testing_list = read_file(testing_file)
    testing_list_len = len(testing_list)
    
    if option =='optimized': 
        #decision_tree = DTL(examples,attributes,Distribution(examples))
        #Testing(testing_list,decision_tree)
        tree_num = 0
        Forest(tree_num,examples,attributes,testing_list) 
    elif option == 'randomized':
        #decision_tree = DTLRandom(examples,attributes,Distribution(examples))
        #Testing(testing_list,decision_tree)
        tree_num = 1
        Forest(tree_num,examples,attributes,testing_list) 
    elif option == 'forest3':
        tree_num = 3
        Forest(tree_num,examples,attributes,testing_list) 
    elif option == 'forest15':    
        tree_num = 15
        Forest(tree_num,examples,attributes,testing_list) 
    else:
        print("Incorrect input")
        print("Filename trainingfile.txt testingfile.txt option(optimized,randomized,forest3,forest15)")


