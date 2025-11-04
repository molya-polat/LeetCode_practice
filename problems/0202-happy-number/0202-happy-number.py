class Solution:
    def isHappy(self, n: int) -> bool:
        setCollect = set()
        while True:
            sm = 0
            for ch in str(n):
                sm += (int(ch))**2

            if sm in setCollect:
                return False
            elif sm == 1:
                return True
            setCollect.add(sm)
            n = sm

        return False

        # O() - time ?
        # O() - memory = time cimpl