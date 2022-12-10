"""
-Chef has finally got the chance of his lifetime to drive in the F1F1 tournament. But, there is one problem. 
-Chef did not know about the 107% rule and now he is worried whether he will be allowed to race in the main event or not.
-Given the fastest finish time as X seconds and Chef's finish time as Y seconds, determine whether Chef will be allowed to race in the main event or not.
-Note that, Chef will only be allowed to race if his finish time is within 107% of the fastest finish time.

Input Format:
-First line will contain TT, number of testcases. Then the testcases follow.
-Each testcase contains of a single line of input, two space separated integers XX and YY denoting the fastest finish time and Chef's finish time respectively.
Output Format:
-For each test case, output \texttt{YES}YES if Chef will be allowed to race in the main event, else output \texttt{NO}NO.

"""

T = int(input())
for t in range(T):
    x, y = input().split()
    if 1.07 * int(x) >= int(y):
        print("YES")
    else:
        print("NO")
