
class Underwriter:
    def identify_invalid_transactions(transactions):
        res = set()
        records = []
        for t in transactions:
            rec = t.split(',')
            rec[1] = int(rec[1])
            rec[2] = int(rec[2])
            records.append(rec)
        for rec in records:
            if rec[2] > 2000:
                rec[1] = str(rec[1])
                rec[2] = str(rec[2])
                res.add(','.join(rec))
                continue
            for x in records:
                if (rec[0] == x[0] and abs(rec[1]-int(x[1])) <= 60 and rec[2] == x[2]) or (rec[0] == x[0] and rec[3] != x[3] and abs(rec[1]-int(x[1]))) or (rec[1] == x[1] and rec[0] == x[0]):
                    rec[1] = str(rec[1])
                    rec[2] = str(rec[2])
                    res.add(','.join(rec))
                    break

        return list(res)
