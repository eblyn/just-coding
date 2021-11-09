# http://algorithms-live.blogspot.com/
# It is not clear how to manage the position zero in the BIT

class FenwickTree:

    def __init__(self, init_values):
        self.value = [0 for _ in range(len(init_values))]
        self.indexed_sum = [0 for _ in range(len(init_values))]
        for index in range(len(init_values)):
            self.update(index, init_values[index])

    def update(self, index, new_value):
        old = self.value[index]
        dif = new_value - old
        self.value[index] += dif
        index += 1 
        while(index <= len(self.value)):           
            self.indexed_sum[index - 1] += dif
            index = index + first_signif_bit(index)

    def sum(self, index):
        index += 1 
        sum = 0
        while(index > 0):           
            sum += self.indexed_sum[index - 1]
            index = index - first_signif_bit(index)
        return sum
        
def first_signif_bit(x):
    return x&-x


if __name__ == "__main__":
    v = [2, 7, 1, 9, 7, 0, 3, 5, 8, 3, 8, 4, 1, 6, 6, 9]
    bit = FenwickTree(v)
    print(bit.indexed_sum)
    print(bit.sum(9), bit.sum(12))

