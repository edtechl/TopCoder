class A0Paper:
    def canBuild(self, A):
        A_count = len(A)
        A_size_list = [0]*A_count
        A_end = A_count-1
        
        if A_end == 0 and A[A_end] > 0:
            print("Possible")
        else:
            A_count_list = [0]*A_count
            i = A_end
            while i > 0:
                if A[i] > 0:
                    A_count_list[i] += 1
                i -= 1
            a_size_pos = len(A_count_list)-1
            while a_size_pos > 0:
                a_add_pos = a_size_pos
                number_of_larger_sizes_made = 0
                while A_count_list[a_size_pos] > 1:
                    A_count_list[a_size_pos] /= 2
                    a_add_pos -= 1
                    number_of_larger_sizes_made += 1
                A_count_list[a_add_pos] += number_of_larger_sizes_made
                if A_count_list[0] > 0:
                    print("Possible")
                    break
                a_size_pos -=1

if __name__ == "__main__":
    A0PaperBoi = A0Paper()
    A0PaperBoi.canBuild((0,3))