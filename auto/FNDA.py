class FNDA:
    ERROR = 'ERROR'

    def __init__(self, V, Q, q0, F, func):
        self.V = set(V)
        self.Q = set(Q)
        self.q0 = set(q0)
        self.F = set(F)
        self.func = func

    def run(self, string):
        sym_cnt = 0
        last_allowed = 0
        success = False

        q = self.q0
        for x in string:
            q_next = set()
            for state in q:
                if state == self.ERROR:
                    continue
                for transition in self._transit(state, x):
                    q_next.add(transition)

            q = q_next
            #print(x, q)
            sym_cnt += 1

            for state in q:
                if state in self.F:
                    last_allowed = sym_cnt
                    success = True

            if q == {self.ERROR}:
                break

        for state in q:
            if state in self.F:
                last_allowed = sym_cnt
                success = True

        return (success, last_allowed)

    def _transit(self, q, x):
        if x not in self.V:
            return [self.ERROR]
        if self.func.get(q).get(x):
            return self.func.get(q).get(x)
        return [self.ERROR]
