class MultiplicationTable:
    @classmethod
    def print_table(cls, size=12):
        for i in range(1, size+1):
            for j in range(1, size+1):
                print(f"{i*j}\t", end='')
            print()
MultiplicationTable.print_table()