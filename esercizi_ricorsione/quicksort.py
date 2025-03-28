# import
import quicksort


class QuickSort:

    def sort(self,sequenza):

        if len(sequenza)<=1:
            return sequenza
        else:
            pivot = sequenza[0]

            sequenza_smaller= []
            for i in range(1,len(sequenza)):
                if sequenza[i]<pivot:
                    sequenza_smaller.append(sequenza[i])

            sequenza_pivot=[n for n in sequenza if n==pivot]
            sequenza_larger = [n for n in sequenza if n > pivot]

            return (self.sort(sequenza_smaller)+(sequenza_pivot)+self.sort(sequenza_larger))

if __name__=="__main__":
    sequenza=[3,5,0,2,11,31,4,7]

    print(f"Sequenza non ordinata: {sequenza}")
    print()
    print(f"Sequenza ordinata: {quicksort.QuickSort().sort(sequenza)}")

