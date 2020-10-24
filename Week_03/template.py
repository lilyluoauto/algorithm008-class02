# coding:utf-8
#!/usr/bin/python
# ========================================================
# Project: project
# Creator: lilyluo
# Create time: 2020-04-28 10:17
# IDE: PyCharm
# =========================================================

def recursion(level, param1,param2):
    # terminator
    if level > max_level:
        process_result
        return

    # current logic dealing
    process(level, param1,param2)
    #drill down
    recursion(level+1,param1,param2)
    # reverse current state if needed
    pass

def divid_conquer(problem,param1,param2):
    #recursive terminator
    if problem is None:
        print_result
        return
    #prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem,data)
    #conquer subproblems
    subresult1 = divid_conquer(subproblems[0],p1,p1,……)
    subresult2 = divid_conquer(subproblems[1],p1,p2,……)
    subresult3 = divid_conquer(subproblems[2],p1,p2,……)

    #process and generate the final result
    result = process_result(subresult1,subresult2,subresult3,……)