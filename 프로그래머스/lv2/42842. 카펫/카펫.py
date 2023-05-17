def solution(brown, yellow):
    # bh, bw = yh+2, yw+2
    # brown+yellow = bh*bw = (yh+2) + (yw+2)
    # yellow = yh*yw = (bh-2) + (bw-2)
    # brown = 2bh+2bw-4
    for bh in range(1, brown//2 + 1):
        bw = (brown - 2*bh + 4) // 2
        yh, yw = bh-2, bw-2
        if yellow == yh*yw and brown+yellow == bh*bw:
            return [bw,bh]