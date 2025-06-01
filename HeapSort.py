import random
def generate_random_numbers():
    numbers = []
    for i in range(100):
        data = random.randint(0, 9)
        numbers.append(data)
    return numbers
def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[smallest]:
        smallest = left
    if right < n and arr[right] > arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    result = []
    for i in range(n):
        result.insert(0, arr[0])
        arr[0] = arr[n - 1 - i]
        heapify(arr, n - 1 - i, 0)
    return result

if __name__ == "__main__":
    random_numbers = generate_random_numbers()
    print("Data:")
    print(', '.join(map(str, random_numbers)))
    numbers_to_sort = random_numbers.copy()
    sorted_numbers = heap_sort(numbers_to_sort)
    print("\nData setelah diurutkan:")
    print(', '.join(map(str, sorted_numbers)))
    print(f"\nJumlah elemen: {len(sorted_numbers)}")

"""
Alasan memilih algoritma Heap Sort:
1. Heap memiliki kompleksitas waktu rata-rata O(log n) untuk memasukkan dan menghapus elemen, sehingga efisien untuk kumpulan data besar. 
Kita dapat mengubah array apa pun menjadi heap dalam waktu O(n). Yang terpenting adalah, kita dapat memperoleh nilai minimum atau maksimum dalam waktu O(1)
2. Pohon Heap merupakan pohon biner lengkap, oleh karena itu dapat disimpan dalam array tanpa pemborosan ruang.
3. Tumpukan dapat diubah ukurannya secara dinamis saat elemen dimasukkan atau dihapus, membuatnya cocok untuk aplikasi dinamis yang memerlukan penambahan atau penghapusan elemen secara real-time.
4. Heaps memungkinkan elemen diproses berdasarkan prioritas, membuatnya cocok untuk aplikasi waktu nyata, seperti penyeimbangan beban, aplikasi medis, dan analisis pasar saham.
5. Sebagian besar aplikasi heap memerlukan penataan ulang elemen di tempat. Misalnya HeapSort.
"""