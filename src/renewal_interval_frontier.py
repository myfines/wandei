#!/usr/bin/env python3
"""Exact finite frontier of consecutive *expanding* Collatz renewal gates.

This is not a test that the entire Collatz orbit reaches 1.
"""
import argparse
from renewal_gate_fractal import gate


def scan(limit):
    assert limit>=3
    first={}
    maxrun=0
    maxseed=None
    histogram={}
    for n in range(3,limit+1,4):
        x=n
        r=0
        while True:
            kind,x,_,_=gate(x)
            if kind not in ('B1','B3'):
                break
            r+=1
            if r not in first:
                first[r]=n
        histogram[r]=histogram.get(r,0)+1
        if r>maxrun:
            maxrun,maxseed=r,n
    return maxrun,maxseed,first,histogram


def export(limit,output):
    import csv
    rmax,witness,first,hist=scan(limit)
    total=sum(hist.values())
    survivors=total
    with open(output,'w',newline='',encoding='utf-8') as file:
        writer=csv.writer(file)
        writer.writerow(['depth','first_positive_seed_le_limit','survivors_le_limit','tested_seeds','modular_haar_ratio'])
        writer.writerow([0,3,total,total,'1'])
        for depth in range(1,rmax+2):
            survivors-=hist.get(depth-1,0)
            writer.writerow([depth,first.get(depth,''),survivors,total,f'(5/8)^{depth}'])
    return rmax,witness


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--limit',type=int,default=1_000_000)
    p.add_argument('--csv')
    args=p.parse_args()
    if args.csv:
        m,n=export(args.limit,args.csv)
    else:
        m,n,first,hist=scan(args.limit)
        for i in sorted(first):
            print(i,first[i],sep=',')
    print('max consecutive expanding gates:',m,'at positive seed',n)
