"""
You want to buy a laptop. Each laptop has two parameters: Rating & Price. Your task is to buy a laptop with the highest rating within a given price range. Given Q tasks, each query consisting of price range required, you have to print the highest rated laptop that can be bought within that price range.

Input format:

The first line contains N denoting the number of inputs.
The following N lines contain P & R denoting price and range of a laptop.
Next line contains Q denoting the number of queries.
The following Q lines contain two integers X & Y denoting the price range (inclusive).
Output format:
For each task Q, print the highest rating that can be bought within the range.
If you cannot get any laptop within the range, print -1.

Constraints:
image

Sample Input:
5
1000 300
1100 400
1300 200
1700 500
2000 600
3
1000 1400
1700 1900
0 2000

Sample Output:
400
500
600

length of prices>1

"""

def bs(max_price, prices, start, end):
    found=False
    while (start<=end and not found):
        mid=(start+end)//2
        if prices[mid]==max_price:
            return max_price
        elif prices[mid]>max_price:
            pass
             



    return None

prices=[1000, 1100, 1300, 1700, 2000]
rating=[300, 400, 200, 500, 600]
query=[(1000,1400),(1700,1900),(0,2000)]
""" code """ 

for q in query:
    best_price = bs(q[1],prices, 0, len(prices)-1)