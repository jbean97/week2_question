class PriorityQueue:
  def __init__(self):
    self.heap = []

  def push(self, item, priority):
    entry = (priority, item)
    self.heap.append(entry)
    self._sift_up(len(self.heap) - 1)

  def pop(self):
    if len(self.heap) > 1:
      self._swap(0, len(self.heap) - 1)
      _, item = self.heap.pop() #priority 변수를 사용하지 않아 _로 전환하였음. 필요시 수정
      self._sift_down(0)
      return item
    elif len(self.heap) == 1:
      _, item = self.heap.pop()
      return item
    else:
      return None

  def _sift_up(self, index):
    # 인덱스가 0보다 클 때,
    # 부모 인덱스로 전환
    # 부모가 지금보다 크다면?
    # 테스크가 크다면? ㄴㄴ -> priority를 기준으로 설정해야함.

    while index > 0:
      parent_index = (index - 1) // 2
      if self.heap[parent_index][0] > self.heap[index][0]: # idx 0 이 priority
        self._swap(parent_index, index)
        index = parent_index
      else:
        break

  def _sift_down(self, index):
    while True:
      left_child_index = 2 * index + 1
      right_child_index = 2 * index + 2
      smallest = index

      if left_child_index < len(self.heap) and \
        self.heap[left_child_index][0] < self.heap[smallest][0]:
        smallest = left_child_index

      if right_child_index < len(self.heap) and \
        self.heap[right_child_index][0] < self.heap[smallest][0]:
        smallest = right_child_index

      if smallest != index:
        self._swap(index, smallest)
        index = smallest
      else:
        break

  def _swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
